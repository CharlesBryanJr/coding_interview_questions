'''
CS 5/7322
Introduction to Natural Language Processing 
Spring 2025
Homework 1

Logical Flow: Initialization -> Expectation -> Maximization -> Document Probability Calculation

'''

import numpy as np
import pandas as pd


corpus = ['ABAAC', 'CABBC', 'BABCBABC']
unique_words = list(set(''.join(corpus)))
num_topics = 2


initial_assignment = {
    'A': 0,
    'B': 1,
    'C': 0
}


def initialize_topic_word_vector(unique_words, num_topics, initial_assignment):
    """Initialize P(w|z) - Topic-Word Probabilities."""
    topic_word_vector = np.zeros((num_topics, len(unique_words)))
    
    for word in unique_words:
        topic = initial_assignment[word]
        word_index = unique_words.index(word)
        topic_word_vector[topic, word_index] += 1
    
    return topic_word_vector / topic_word_vector.sum(axis=1, keepdims=True)


def initialize_document_topic_vector(corpus, num_topics, initial_assignment, unique_words):
    """Initialize P(z|d) - Document-Topic Probabilities."""
    document_topic_vector = np.zeros((len(corpus), num_topics))
    
    for doc_idx, doc in enumerate(corpus):
        for word in doc:
            topic = initial_assignment[word]
            document_topic_vector[doc_idx, topic] += 1
    
    return document_topic_vector / document_topic_vector.sum(axis=1, keepdims=True)


topic_word_vectors = initialize_topic_word_vector(unique_words, num_topics, initial_assignment)
document_topic_vectors = initialize_document_topic_vector(corpus, num_topics, initial_assignment, unique_words)
print("Initial Topic-Word Probabilities:\n", topic_word_vectors)
print("\nInitial Document-Topic Probabilities:\n", document_topic_vectors)


def compute_topic_probability_for_word(word, doc_idx, topic_word_vector, document_topic_vector, unique_words, num_topics):
    """Compute P(z | w, d) for a given word."""
    word_index = unique_words.index(word)
    topic_probs = [
        topic_word_vector[topic, word_index] * document_topic_vector[doc_idx, topic]
        for topic in range(num_topics)
    ]
    
    total_prob = sum(topic_probs)
    return [p / total_prob for p in topic_probs]


def calculate_word_topic_probabilities(topic_word_vector, document_topic_vector, corpus, unique_words):
    """Compute P(z | w, d) for all words in all documents."""
    word_topic_probabilities = {}

    for doc_idx, doc in enumerate(corpus):
        word_topic_probabilities[doc_idx] = {
            word: compute_topic_probability_for_word(word, doc_idx, topic_word_vector, document_topic_vector, unique_words, num_topics)
            for word in doc
        }
    
    return word_topic_probabilities


word_topic_probabilities = calculate_word_topic_probabilities(topic_word_vectors, document_topic_vectors, corpus, unique_words)
for doc_idx, doc_probs in word_topic_probabilities.items():
    print(f"\nDocument {doc_idx} - Word-Topic Probabilities:")
    for word, probs in doc_probs.items():
        print(f"  {word}: Topic 1 = {probs[0]:.4f}, Topic 2 = {probs[1]:.4f}")


def expectation_step(topic_word_vector, document_topic_vector, corpus, unique_words):
    """Perform the Expectation step (E-Step) in the EM Algorithm."""
    return calculate_word_topic_probabilities(topic_word_vector, document_topic_vector, corpus, unique_words)


def maximization_step(word_topic_probabilities, corpus, unique_words, num_topics):
    """Perform the Maximization step (M-Step) in the EM Algorithm."""
    new_topic_word_vector = np.zeros((num_topics, len(unique_words)))
    new_document_topic_vector = np.zeros((len(corpus), num_topics))

    for doc_idx, doc in enumerate(corpus):
        for word in doc:
            word_idx = unique_words.index(word)
            topic_probs = word_topic_probabilities[doc_idx][word]

            for topic in range(num_topics):
                new_topic_word_vector[topic, word_idx] += topic_probs[topic]
                new_document_topic_vector[doc_idx, topic] += topic_probs[topic]

    new_topic_word_vector /= new_topic_word_vector.sum(axis=1, keepdims=True)
    new_document_topic_vector /= new_document_topic_vector.sum(axis=1, keepdims=True)

    return new_topic_word_vector, new_document_topic_vector


def em_algorithm(corpus, unique_words, num_topics, initial_assignment, num_iterations=10):
    """Run the full EM algorithm with E-Step and M-Step iterations."""
    topic_word_vector = initialize_topic_word_vector(unique_words, num_topics, initial_assignment)
    document_topic_vector = initialize_document_topic_vector(corpus, num_topics, initial_assignment, unique_words)

    for iteration in range(num_iterations):
        word_topic_probabilities = expectation_step(topic_word_vector, document_topic_vector, corpus, unique_words)
        topic_word_vector, document_topic_vector = maximization_step(word_topic_probabilities, corpus, unique_words, num_topics)

    return topic_word_vector, document_topic_vector


final_topic_word_vectors, final_document_topic_vectors = em_algorithm(corpus, unique_words, num_topics, initial_assignment, num_iterations=10)
print("\nFinal Topic-Word Probabilities:\n", final_topic_word_vectors)
print("\nFinal Document-Topic Probabilities:\n", final_document_topic_vectors)


def compute_word_probability(word, doc_idx, topic_word_vector, document_topic_vector, unique_words, num_topics):
    """Compute P(w) using topic-word and document-topic probabilities."""
    word_index = unique_words.index(word)
    return sum(
        topic_word_vector[topic, word_index] * document_topic_vector[doc_idx, topic]
        for topic in range(num_topics)
    )


def compute_document_probability(doc, doc_idx, topic_word_vector, document_topic_vector, unique_words, num_topics):
    """Compute the probability of an entire document being generated."""
    doc_prob = 1.0
    for word in doc:
        doc_prob *= compute_word_probability(word, doc_idx, topic_word_vector, document_topic_vector, unique_words, num_topics)
    return doc_prob


def compute_document_generation_probabilities(corpus, topic_word_vector, document_topic_vector, unique_words, num_topics):
    """Compute P(d) for each document."""
    return [compute_document_probability(doc, doc_idx, topic_word_vector, document_topic_vector, unique_words, num_topics)
            for doc_idx, doc in enumerate(corpus)]


document_generation_probabilities = compute_document_generation_probabilities(corpus, final_topic_word_vectors, final_document_topic_vectors, unique_words, num_topics)
print("\nDocument Generation Probabilities:")
for doc_idx, prob in enumerate(document_generation_probabilities):
    print(f"Document {doc_idx}: {prob:.6f}")