import logging
import functools
import time
from string import punctuation
import json
import math

def timing(f):
    """Print the timing for the function"""
    # create a decorator as a wrapper so that before the function call we get the time
    # after the function call we get the new time, so compute the elapsed time, and print it
    # also print out the result if the permutation is possible or not and the two words
    @functools.wraps(f) # preserves information about the original function
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        logging.info(f"Result of {int(result)} for function { f.__name__}() in elapsed time {end - start:.3f} seconds.")
        return result
    # done inner function
    return wrapper
# done function

@timing
def process_corpus(corpus):
    logging.info("")
    logging.info("")
    logging.info(f"**** new corpus  ****")
    logging.info(f"{corpus}")
    # convert the json string of the corpus to a Python dictionary
    dict_sentence_name_sentence_text = json.loads(corpus)

    N = 0 # counter_document
    dict_sentence_name_dict_word_TF = {}
    dict_sentence_name_number_word = {}

    list_word = []
    for sentence_name in sorted(dict_sentence_name_sentence_text.keys()):       
        N += 1
        dict_word_TF = {}
     
        sentence_text = dict_sentence_name_sentence_text[sentence_name]
        # remove punctuation marks and set all characters to lower
        sentence_text = sentence_text.translate(str.maketrans('', '', punctuation)).lower()
        dict_sentence_name_number_word[sentence_name] = len(sentence_text.split(" "))
        # split into words and count
        for word in sentence_text.split(" "):
            list_word.append(word)
            if word not in dict_word_TF.keys():
                dict_word_TF[word] = 1
            else:
                dict_word_TF[word] += 1
        dict_sentence_name_dict_word_TF[sentence_name] = dict_word_TF
    list_word = sorted(set(list_word))

    dict_word_DF = {}
    for word in list_word:
        dict_word_DF[word] = 0
        for sentence_name in sorted(dict_sentence_name_sentence_text.keys()):
            dict_word_TF = dict_sentence_name_dict_word_TF[sentence_name]
            if word in dict_word_TF.keys():
                dict_word_DF[word] += 1

    dict_document_dict_word_w = {}
    for sentence_name in sorted(dict_sentence_name_dict_word_TF.keys()):
        # loop over documents
        dict_word_w = {}
        dict_word_TF = dict_sentence_name_dict_word_TF[sentence_name]
        logging.debug(f"dict_word_TF, len={len(dict_word_TF)}")
        L = dict_sentence_name_number_word[sentence_name]
        if L == 0:
            dict_document_dict_word_w[sentence_name] = None 
        else: 
            for word in sorted(dict_word_TF.keys()):
                C = dict_word_TF[word]
                TF = C / L
                DF = dict_word_DF[word]
                N_DF = N / DF
                w = TF * math.log(N_DF)
                logging.debug(f"word={word}, C={C}, L={L}, TF={TF}, DF={DF}, N={N}, N_DF={N_DF}, w = {w}")
                dict_word_w[word] = w
            dict_document_dict_word_w[sentence_name] = dict_word_w

    logging.info(json.dumps(dict_document_dict_word_w, indent = 2))

    return 0
