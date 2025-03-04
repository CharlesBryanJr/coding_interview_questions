'''
CS 5/7322
Introduction to Natural Language Processing 
Spring 2025
Homework 1

(24 points) Consider the following corpus (each line is a separate sentence):
AABD 
DABC 
CCBA 
BABD 
DABB 
ACCD

Suppose we want to build a bigram model based on the corpus above. Assume we have both a 
begin and end sentence symbol for each sentence.

Calculate the perplexity of each sentence (separately) for each of the two cases 
The base case (no smoothing)
Using Laplace (plus 1) smoothing. Note that the bigram <begin><end> will never occur so it’s probability does not need to be smoothed. (Hint: you should start the smoothing process by adding 1 to the frequency of all possible bigrams)
Also show the probabilities for each bigram (preferably in a 2-d matrix).

Implementation Flow: 
    Preprocessing -> 
    Frequency Count -> 
    Probability Computation -> 
    Perplexity Calculation ->
    Matrix Display ->
    Evaluation
'''

import numpy as np
import math

class BigramModel:
    def __init__(self, corpus):
        """Step 1: Preprocess Corpus - Add <begin> and <end> tokens and extract unique symbols."""
        self.corpus = [['<begin>'] + list(sentence) + ['<end>'] for sentence in corpus]
        self.unique_symbols = sorted(set(symbol for sentence in self.corpus for symbol in sentence))
        self.symbol_to_idx = {symbol: idx for idx, symbol in enumerate(self.unique_symbols)}
    
    
    def _count_frequencies(self, smoothing=False):
        """Step 2: Count Bigram Frequencies with optional Laplace smoothing."""
        n = len(self.unique_symbols)
        freq_matrix = np.zeros((n, n), dtype=int)
        
        for sentence in self.corpus:
            for i in range(len(sentence) - 1):
                from_idx = self.symbol_to_idx[sentence[i]]
                to_idx = self.symbol_to_idx[sentence[i+1]]
                freq_matrix[from_idx, to_idx] += 1
        
        if smoothing:
            freq_matrix += 1  # Apply Laplace smoothing
        
        return freq_matrix
    

    def calculate_probabilities(self, smoothing=False):
        """Step 3: Calculate the probability matrix from bigram counts."""
        freq_matrix = self._count_frequencies(smoothing)
        prob_matrix = np.zeros_like(freq_matrix, dtype=float)
        
        for i in range(len(self.unique_symbols)):
            row_total = np.sum(freq_matrix[i, :])
            if row_total > 0:
                prob_matrix[i, :] = freq_matrix[i, :] / row_total  # Normalize by row sum
        
        return prob_matrix
    

    def calculate_sentence_perplexity(self, sentence, prob_matrix):
        """Step 4: Compute Perplexity of a given sentence."""
        full_sentence = ['<begin>'] + list(sentence) + ['<end>']
        log_probs = []
        
        for i in range(len(full_sentence) - 1):
            from_idx = self.symbol_to_idx[full_sentence[i]]
            to_idx = self.symbol_to_idx[full_sentence[i+1]]
            prob = prob_matrix[from_idx, to_idx]
            log_probs.append(math.log(prob) if prob > 0 else float('-inf'))
        
        return math.exp(-sum(log_probs) / len(log_probs)) if log_probs else float('inf')
    

    def print_probability_matrix(self, prob_matrix):
        """Step 5: Print probability matrix for debugging."""
        print("Probability Matrix:")
        print("From\\To", end="\t")
        print("\t".join(self.unique_symbols))
        
        for i, from_symbol in enumerate(self.unique_symbols):
            row_values = "\t".join(f"{prob_matrix[i, j]:.3f}" for j in range(len(self.unique_symbols)))
            print(f"{from_symbol}\t{row_values}")


corpus = ["AABD", "DABC", "CCBA", "BABD", "DABB", "ACCD"]
model = BigramModel(corpus)

print("Base Case - No Smoothing:")
base_probs = model.calculate_probabilities(smoothing=False)
model.print_probability_matrix(base_probs)

print("\nPerplexity (Base Case):")
for sentence in corpus:
    perplexity = model.calculate_sentence_perplexity(sentence, base_probs)
    print(f"{sentence}: {perplexity:.3f}")

print("\n" + "="*50 + "\n")

print("Laplace Smoothing:")
smoothed_probs = model.calculate_probabilities(smoothing=True)
model.print_probability_matrix(smoothed_probs)

print("\nPerplexity (Laplace Smoothing):")
for sentence in corpus:
    perplexity = model.calculate_sentence_perplexity(sentence, smoothed_probs)
    print(f"{sentence}: {perplexity:.3f}")