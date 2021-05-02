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
import matplotlib.pyplot as plt   

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
    
   
    def load(self, file_name):
        raise NotImplementedError()
   
    def get_representation(self, bow_extractor):
        raise NotImplementedError()
    
    def __sub__(self, doc):
        distance = np.sum(np.minimum(self._bow, doc._bow)) 
        distance /= min(np.sum(self._bow), np.sum(doc._bow))
        return 1 - distance
    
    def visualize(self, axs):
        raise NotImplementedError()

class Image(Document):
    def __init__(self):
        super().__init__()
        self._img = None
        
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

    def visualize(self, axs):
        axs.axis('off')
        axs.imshow(self._img)

class Text(Document):
    def __init__(self):
        super().__init__()
        self._text = []
    
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
                
    def visualize(self, axs):
        with open(self._file_name) as file:
            text = file.read()
        axs.axis('off')
        axs.text(0, 1, text, va = 'top', clip_on = True, fontsize = 'xx-small')
                
class Retrieval:
    def __init__(self, tipus):
        self._training = []
        self._vocabulary = None
        self._tipus = tipus
        
    def load_vocabulary(self, file_vocabulary):
        if self._tipus =='txt':
            self._vocabulary = []
            with open(file_vocabulary, 'r') as file:
                for line in file:
                    self._vocabulary.append(line[:-1])
        else:
            self._vocabulary = init_bow_images(file_vocabulary)
    
    def load_training(self, train):
        file_list = os.listdir(train)
        for file in file_list:
            if self._tipus == 'txt':
                doc = Text()
            else:
                doc = Image()
            doc.load(train + file)
            doc.get_representation(self._vocabulary)
            self._training.append(doc)
    
    def retrieval(self, file, k):
        if self._tipus == 'txt':
            doc_test = Text()
        else:
            doc_test = Image()        
        doc_test.load(file)
        doc_test.get_representation(self._vocabulary)
        rank = [(doc_training, doc_test - doc_training) for doc_training in self._training]
        rank.sort(key = lambda document:document[1])
        retrieval_list = [document[0] for document in rank[0:k]]
        return retrieval_list
  
def retrieval(test, train, tipus, vocabulary_file, k):
    r = Retrieval(tipus)
    r.load_vocabulary(vocabulary_file)
    r.load_training(train)
    files_test = os.listdir(test)
    for file in files_test:
        if (file.find('.jpg') != -1) or (file.find('.txt') != -1):
            result = r.retrieval(test + file, k)
            fig, axs = plt.subplots(1,5)
            for i,d in enumerate(result):
                d.visualize(axs[i])

retrieval('cifar/test/', 'cifar/train/', 'img', 'cifar/vocabulary.dat', 5)
