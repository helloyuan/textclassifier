#!/usr/bin/python

"""
This file generates X, y from raw files

please use 
from load_data import load_data

sorry for the bad names :-)

"""
import os
import numpy as np

def non_hash(values, length=44):
    """
    params:
        values: a feature array
        length: the length of hash value
    return: boolean, indicate whether the feature is non-hash_value or not
    """
    return not any(len(value) == length for value in values)

def convert_categories(values):
    """
    params:
        values: a feature array
    return: integer, within range(len(categories))
    """
    categories, values = np.unique(values, return_inverse=True)
    return values

def load_data(f_train='train.csv', f_label='trainLabels', f_X='X.npy', f_y='y.npy'):
    """
    params:
        f_train: feature values file
        f_label: label or class file
        f_x: object file storing X
        f_y: object file storing y

    return: 
        X: array-like matrix, shape = [n_samples, n_features]
        y: array-like matrix, shape = [n_samples, n_classes]
    """
    if os.path.exists(f_X):
        X = np.load(f_X)
    else:
        # load file, remove feature names
        train_set = np.genfromtxt(f_train, delimiter=',', dtype='str')[1:]
        # remove instance numbers
        features = train_set.T[1:]
        # remove all the hash values with length of 44 
        features = filter(non_hash, features)
        # change categorical features as float representation
        X = np.array(map(convert_categories, features)).T
        np.save(f_X, X)
    if os.path.exists(f_y):
        y = np.load(f_y)
    else:
        # one array for each class, not for each instance
        y = np.genfromtxt(f_label, delimiter=',')[1:].T[1:].T
        np.save(f_y, y)

    return X, y
	
if __name__ == '__main__':
    load_data()
