# -*- coding: utf-8 -*-
"""
Created on Sun May  2 09:40:49 2021

@author: 1002245
"""

import os
import re
import numpy as np

    
class Document:
    def __init__(self):
        self._bow = None
        self._file_name = None
        self._text = []
        self._label = None

    @property
    def label(self):
        return self._label
    @label.setter
    def label(self, label):
        self._label = label
        
    def load(self, file_name):
        self._file_name = file_name
        with open(file_name, "r") as file:
            for line in file:
                words = re.sub("[^a-zA-Z0-9]", " ", line).split()
                self._text.extend(words)
    
    def get_representation(self, vocabulary):
        self._bow = np.zeros(len(vocabulary))
        for word in self._text:
            word = word.lower()
            if word in vocabulary:
                i = vocabulary.index(word)
                self._bow[i] = self._bow[i] + 1
                
    def __sub__(self, doc):
        distance = np.sum(np.minimum(self._bow, doc._bow)) 
        distance /= min(np.sum(self._bow), np.sum(doc._bow))
        return 1 - distance

class Classification:
    def __init__(self):
        self._training = []
        self._vocabulary = []
        self._labels = ['atheism', 'autos', 'baseball', 'crypt', 'electronics', 'forsale', 'graphics', 'hardware-mac', 'hardware-pc', 'hockey', 'med', 'motorcycles', 'ms-windows', 'polítics-guns', 'polítics-mideast', 'religion-christian', 'religion-misc', 'space', 'windows-x', 'polítics-misc']
        
    def load_vocabulary(self, file_vocabulary):
        with open(file_vocabulary, 'r') as file:
            for line in file:
                self._vocabulary.append(line[:-1])
    
    def load_training(self, train):
        file_list = os.listdir(train)
        for file in file_list:
            doc = Document()
            doc.load(train + file)
            doc.get_representation(self._vocabulary)
            for l in self._labels:
                if (re.search(l,file)) != None:
                    doc.label = l
            self._training.append(doc)
    
    def classify_document(self, file, k):
        doc_test = Document()
        doc_test.load(file)
        doc_test.get_representation(self._vocabulary)
        rank = [(doc_training, doc_test - doc_training) for doc_training in self._training]
        rank.sort(key = lambda document:document[1])
        ranked_labels = [document[0].label for document in rank[0:k]]
        count_labels = [ranked_labels.count(l) for l in self._labels]
        doc_test.label = self._labels[count_labels.index(max(count_labels))]
        return (doc_test, rank[0:k])

  
def classificacio_newsgroups(train, test, vocabulary_file, k):
    c = Classification()
    c.load_vocabulary(vocabulary_file)
    c.load_training(train)
    files_test = os.listdir(test)
    labels = []
    for file in files_test:
        if (file.find('.txt') != -1):
            doc_test, list_evidence = c.classify_document(test + file, k)
            if (re.search(doc_test.label,file)) != None:
                correct = True
            else:
                correct = False
            labels.append((file, doc_test.label, correct, [e[1] for e in list_evidence]))
    return labels

labels = classificacio_newsgroups('newsgroups/train/', 'newsgroups/test/', 'newsgroups/vocabulary.txt', 5)