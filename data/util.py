import os

def get_doc_counts(data_path):
  '''
  :return: the number of characters, words and lines of a document
  '''
  num_chars = num_words = num_lines = 0
  with open(data_path, 'r') as in_file:
    for line in in_file:
      num_lines += 1
      num_words += len(line.split())
      num_chars += len(line)
  print 'num_chars = %d, num_words = %d, num_lines = %d' \
        % (num_chars, num_words, num_lines)
  return num_chars, num_words, num_lines

# def string2list_of_ascii(string):
#   '''
#   preprocessing to a list of ascii values
#    - code space as 0
#    - code chars as ascii val - 96 (so range = 1-27)
#   '''
#   list_of_ascii = []
#   for i in range(len(string)):
#     if ord(string[i]) == 32:
#       list_of_ascii.append(0)
#     else:
#       list_of_ascii.append(ord(string[i]) - 96)
#   return list_of_ascii


def write2txtfile(my_text, datapath, filename):
  train_out_fname = os.path.join(datapath, filename)
  text_file = open(train_out_fname, "w")
  text_file.write(my_text)
  print 'write to <%s>' % train_out_fname
  text_file.close()