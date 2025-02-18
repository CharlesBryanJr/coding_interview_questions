import math
import nltk
import PyPDF2
import os
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from collections import Counter

class CorpusReader_TFIDF:
    def __init__(self, corpus_dir, tf="raw", idf="base", stopWord="none", toStem=False, stemFirst=False, ignoreCase=True):
        self.corpus_dir = corpus_dir
        self.tf_method = tf
        self.idf_method = idf
        self.stopWord = stopWord
        self.toStem = toStem
        self.stemFirst = stemFirst
        self.ignoreCase = ignoreCase
        self.stemmer = SnowballStemmer("english") if toStem else None
        
        if stopWord == "standard":
            self.stop_words = set(stopwords.words("english"))
        elif stopWord != "none":
            with open(stopWord, "r") as f:
                self.stop_words = set([line.strip().lower() for line in f])
        else:
            self.stop_words = set()
        
        self.doc_terms = self.load_documents()
        self.idf_values = self.compute_idf()
    
    def load_documents(self):
        doc_terms = {}
        for file in os.listdir(self.corpus_dir):
            if file.endswith(".pdf"):
                file_path = os.path.join(self.corpus_dir, file)
                text = self.extract_text_from_pdf(file_path)
                words = self.preprocess(word_tokenize(text))
                doc_terms[file] = words
        return doc_terms
    
    def extract_text_from_pdf(self, file_path):
        text = ""
        with open(file_path, "rb") as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() + " "
        return text
    
    def preprocess(self, words):
        if self.ignoreCase:
            words = [word.lower() for word in words]
        
        if self.toStem and self.stemFirst:
            words = [self.stemmer.stem(word) for word in words]
        
        words = [word for word in words if word.isalnum() and word not in self.stop_words]
        
        if self.toStem and not self.stemFirst:
            words = [self.stemmer.stem(word) for word in words]
        
        return words
    
    def compute_tf(self, words):
        counts = Counter(words)
        if self.tf_method == "raw":
            return counts
        elif self.tf_method == "log":
            return {term: 1 + math.log2(freq) if freq > 0 else 0 for term, freq in counts.items()}
        return counts
    
    def compute_idf(self):
        doc_count = len(self.doc_terms)
        term_doc_counts = Counter(term for doc in self.doc_terms.values() for term in set(doc))
        
        if self.idf_method == "base":
            return {term: math.log2(doc_count / term_doc_counts[term]) for term in term_doc_counts}
        elif self.idf_method == "smooth":
            return {term: math.log2(1 + (doc_count / term_doc_counts[term])) for term in term_doc_counts}
        return {}
    
    def compute_tfidf(self, words):
        tf_values = self.compute_tf(words)
        return {term: tf_values[term] * self.idf_values.get(term, 0) for term in tf_values}
    
    def tfidf(self, fileid, returnZero=False):
        tfidf_vector = self.compute_tfidf(self.doc_terms[fileid])
        return tfidf_vector if returnZero else {k: v for k, v in tfidf_vector.items() if v > 0}
    
    def tfidfAll(self, returnZero=False):
        return {fileid: self.tfidf(fileid, returnZero) for fileid in self.doc_terms}
    
    def tfidfNew(self, words):
        words = self.preprocess(words)
        return self.compute_tfidf(words)
    
    def listIDF(self):
        return self.idf_values
    
    def cosine_similarity(self, vec1, vec2):
        dot_product = sum(vec1.get(k, 0) * vec2.get(k, 0) for k in set(vec1.keys()).union(vec2.keys()))
        norm1 = math.sqrt(sum(v ** 2 for v in vec1.values()))
        norm2 = math.sqrt(sum(v ** 2 for v in vec2.values()))
        return dot_product / (norm1 * norm2) if norm1 and norm2 else 0.0
    
    def cosine_sim(self, fileid1, fileid2):
        return self.cosine_similarity(self.tfidf(fileid1), self.tfidf(fileid2))
    
    def cosine_sim_new(self, words, fileid):
        return self.cosine_similarity(self.tfidfNew(words), self.tfidf(fileid))
    
    def query(self, words):
        query_vector = self.tfidfNew(words)
        return sorted(((fileid, self.cosine_similarity(query_vector, self.tfidf(fileid))) for fileid in self.doc_terms), key=lambda x: x[1], reverse=True)
    
# --------------------------------------------
# For testing your own corpus
# --------------------------------------------

rootDir = '/Users/charlesbryan/Desktop/research_papers'  # Set to actual directory

tfidfCorpus = CorpusReader_TFIDF(rootDir)

q = tfidfCorpus.tfidfAll()
for x in q:
    print(x, q[x])

print("-----\n")