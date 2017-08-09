import numpy as np
import sys
import os

from util import *
# spec the path
train_ratio = .9
fname = 'text8_raw.txt'

data_dir = '/Users/Qihong/Dropbox/github/char_lstm/data/text8/'
input_file_path = os.path.join(data_dir, fname)

# 10^8 chars in the file
num_chars , _ , _  = get_doc_counts(input_file_path)
train_size = int(num_chars * train_ratio)
valid_size = int(num_chars * (1 - train_ratio))

# load the text file
file = open(input_file_path, 'r')

# split training and test set
# read the training seq
train = file.read(train_size)
# jump to where it was left
file.seek(file.tell())
# read the valid seq
valid = file.read(valid_size)

# save them as txt
write2txtfile(train, data_dir, 'train.txt')
write2txtfile(valid, data_dir, 'valid.txt')

# convert text to ascii values - NOT NEEDED FOR THE CHAR_LSTM
# train = string2list_of_ascii(train)
# valid = string2list_of_ascii(valid)

# write it to a .npz file
# np.savez(path+fname_out, train=train, valid=valid)

# # check file
# npzfile = np.load(path+fname_out)
# print npzfile.files
# temp = npzfile['train']
# print type(temp[1])