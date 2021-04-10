# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:02:40 2019

@author: ernest
"""

#Distances among histograms
#https://stats.stackexchange.com/questions/7400/how-to-assess-the-similarity-of-two-histograms


import os
import re
import numpy as np
import time

def create_vocabulary():
    for root, dirs, files in os.walk('test/vocabulary'):
        file_list = [os.path.join(root, file) for file in files]
    dictionary = []
    for file in file_list:
        with open(file, "r") as fitxer:
            for linia in fitxer:
                paraules = re.sub("[^a-zA-Z0-9]", " ", linia).split()
                for paraula in paraules:
                    if paraula.lower() not in dictionary and re.search("[0-9]",paraula)==None and len(paraula)>=3:
                        dictionary.append(paraula.lower())
    with open('test/vocabulary.txt', 'w') as f:
        for item in dictionary:
            f.write("%s\n" % item)
    return dictionary
                

class Document:
    def __init__(self):
        self.bow = {}
        self.file_name = None
        self.text = []
        self.spam = None
    
    def load(self, file_name):
        self.file_name = file_name
        with open(file_name, "r") as file:
            for line in file:
                words = re.sub("[^a-zA-Z0-9]", " ", line).split()
                self.text.extend(words)
    
    def get_representation(self, vocabulary):
        for word in vocabulary:
            self.bow[word] = 0
        for word in self.text:
            word = word.lower()
            if word in vocabulary:
                if word in self.bow:
                    self.bow[word] = self.bow[word] + 1

    def distance(self, doc):
        distance = 0.0
        for word in self.bow:
            distance = distance + min(self.bow[word], doc.bow[word])
        distance /= min(sum(self.bow.values()), sum(doc.bow.values()))
        return 1 - distance

class Document_np:
    def __init__(self):
        self.bow = None
        self.file_name = None
        self.text = []
        self.spam = None
    
    def load(self, file_name):
        self.file_name = file_name
        with open(file_name, "r") as file:
            for line in file:
                words = re.sub("[^a-zA-Z0-9]", " ", line).split()
                self.text.extend(words)
    
    def get_representation(self, vocabulary):
        self.bow = np.zeros(len(vocabulary))
        for word in self.text:
            word = word.lower()
            if word in vocabulary:
                i = vocabulary.index(word)
                self.bow[i] = self.bow[i] + 1
                
    def distance(self, doc):
        distance = np.sum(np.minimum(self.bow, doc.bow)) 
        distance /= min(np.sum(self.bow), np.sum(doc.bow))
        return 1 - distance

class Document_list:
    def __init__(self):
        self.bow = []
        self.file_name = None
        self.text = []
        self.spam = None
    
    def load(self, file_name):
        self.file_name = file_name
        with open(file_name, "r") as file:
            for line in file:
                words = re.sub("[^a-zA-Z0-9]", " ", line).split()
                self.text.extend(words)
    
    def get_representation(self, vocabulary):
        self.bow = [0]*(len(vocabulary))
        for word in self.text:
            word = word.lower()
            if word in vocabulary:
                i = vocabulary.index(word)
                self.bow[i] = self.bow[i] + 1

    def distance(self, doc):
        minimum = [min(i,j) for i,j in zip(self.bow, doc.bow)]
        distance = sum(minimum)
        distance /= min(sum(self.bow), sum(doc.bow))
        return 1 - distance
    
class Classification:
    def __init__(self):
        self.training = []
        self.vocabulary = []
        
    def load_vocabulary(self, file_vocabulary):
        with open(file_vocabulary, 'r') as file:
            for line in file:
                self.vocabulary.append(line[:-1])
    
    def load_training(self, train):
        file_list = os.listdir(train)
        for file in file_list:
            doc = Document()
            doc.load(train + file)
            doc.get_representation(self.vocabulary)
            if (re.search("spm",file)) == None:
                doc.spam = False
            else:
                doc.spam = True
            self.training.append(doc)
    
    def classify_document(self, file, k):
        doc_test = Document()
        doc_test.load(file)
        doc_test.get_representation(self.vocabulary)
        rank = [(doc_training, doc_test - doc_training) for doc_training in self.training]
        rank.sort(key = lambda document:document[1])
        ranked_labels = [document[0].spam for document in rank[0:k]]
        doc_test.spam = ranked_labels.count(True) > ranked_labels.count(False)
        return (doc_test, rank[0:k])

  
def deteccio_spam(train, test, vocabulary_file, k):
    c = Classification()
    c.load_vocabulary(vocabulary_file)
    c.load_training(train)
    files_test = os.listdir(test)
    labels = []
    for file in files_test:
        if (file.find('.txt') != -1):
            doc_test, list_evidence = c.classify_document("test/" + file, k)
            labels.append((file, doc_test.spam, [e[1] for e in list_evidence]))
    return labels

vocabulary = []
with open('vocabulary.txt', 'r') as file:
    for line in file:
        vocabulary.append(line[:-1])

doc1 = Document()
doc1.load('3-1msg1.txt')
doc1.get_representation(vocabulary)
doc2 = Document()
doc2.load('3-1msg2.txt')
doc2.get_representation(vocabulary)
start = time.time()
for i in range(1000):
    d = doc1.distance(doc2)
end = time.time()
print("dictionary")
print(d)
print(end - start)

doc1 = Document_np()
doc1.load('3-1msg1.txt')
doc1.get_representation(vocabulary)
doc2 = Document_np()
doc2.load('3-1msg2.txt')
doc2.get_representation(vocabulary)
start = time.time()
for i in range(1000):
    d = doc1.distance(doc2)
end = time.time()
print("numpy")
print(d)
print(end - start)

doc1 = Document_list()
doc1.load('3-1msg1.txt')
doc1.get_representation(vocabulary)
doc2 = Document_list()
doc2.load('3-1msg2.txt')
doc2.get_representation(vocabulary)
start = time.time()
for i in range(1000):
    d = doc1.distance(doc2)
end = time.time()
print("list")
print(d)
print(end - start)