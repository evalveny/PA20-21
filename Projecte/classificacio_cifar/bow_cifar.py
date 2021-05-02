# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 19:03:42 2021

@author: 1002245
"""

import os
import re
import numpy as np
import cv2
import pickle

def compute_bow_images(img, bow_extractor):
    sift = cv2.SIFT_create()
    keypoints = sift.detect(img)
    if keypoints != []:
        bow = bow_extractor.compute(img, keypoints)
    else:
        bow = np.zeros((1, bow_extractor.descriptorSize()))
    return bow

def init_bow_images(file_vocabulary):
    sift = cv2.SIFT_create()
    matcher = cv2.FlannBasedMatcher() 
    with open(file_vocabulary, 'rb') as fitxer:
        vocabulary = pickle.load(fitxer)
    bow_extractor = cv2.BOWImgDescriptorExtractor(sift, matcher)
    bow_extractor.setVocabulary(vocabulary)
    return bow_extractor
    
class Document:
    def __init__(self):
        self._bow = None
        self._file_name = None
        self._img = None
        self._label = None
    
    @property
    def label(self):
        return self._label
    @label.setter
    def label(self, label):
        self._label = label
    
    def load(self, file_name):
        self._file_name = file_name
        self._img = cv2.imread(file_name)

    
    def get_representation(self, bow_extractor):
        img_gray = cv2.cvtColor(self._img,cv2.COLOR_BGR2GRAY)
        self._bow = compute_bow_images(img_gray, bow_extractor)

    
    def __sub__(self, doc):
        distance = np.sum(np.minimum(self._bow, doc._bow)) 
        distance /= min(np.sum(self._bow), np.sum(doc._bow))
        return 1 - distance

class Classification:
    def __init__(self):
        self._training = []
        self._bow_extractor = None
        self._labels = ['airplane', 'horse']
        
    def load_vocabulary(self, file_vocabulary):
        self._bow_extractor = init_bow_images(file_vocabulary)
    
    def load_training(self, train):
        file_list = os.listdir(train)
        for file in file_list:
            doc = Document()
            doc.load(train + file)
            doc.get_representation(self._bow_extractor)
            for l in self._labels:
                if (re.search(l,file)) != None:
                    doc.label = l
            self._training.append(doc)
    
    def classify_document(self, file, k):
        doc_test = Document()
        doc_test.load(file)
        doc_test.get_representation(self._bow_extractor)
        rank = [(doc_training, doc_test - doc_training) for doc_training in self._training]
        rank.sort(key = lambda document:document[1])
        ranked_labels = [document[0].label for document in rank[0:k]]
        count_labels = [ranked_labels.count(l) for l in self._labels]
        doc_test.label = self._labels[count_labels.index(max(count_labels))]
        return (doc_test, rank[0:k])

  
def classificacio_cifar(train, test, vocabulary_file, k):
    c = Classification()
    c.load_vocabulary(vocabulary_file)
    c.load_training(train)
    files_test = os.listdir(test)
    labels = []
    for file in files_test:
        if (file.find('.jpg') != -1):
            doc_test, list_evidence = c.classify_document("test/" + file, k)
            if (re.search(doc_test.label,file)) != None:
                correct = True
            else:
                correct = False
            labels.append((file, doc_test.label, correct, [e[1] for e in list_evidence]))
    return labels

labels = classificacio_cifar('train/', 'test/', 'vocabulary.dat', 5)