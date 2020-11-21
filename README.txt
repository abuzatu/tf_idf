Created by Adrian Buzatu on 21 Nov 2020.

# TF-IDF metric on text documents

A common task in analysing textual data is to evaluate how often each word appears in a document, but also in all the documents in the corpus studied. The best suited metric for such study is the Term Frequency - Inverse Document Frequency (TF-IDF). More information on [Wikipedia](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) and [tfidf.com](http://tfidf.com/). 

In this project we implement such a function to study a corpus of documents, given in the form of json strings. These are easily converted to python dictionaries, processed, and then converted back to json strings.

# How to run

To run the code, simply run
```
python tf_idf.py
```

or open the Jupyter Notebook and run the entire notebook.
```
python tf_idf.ipynb
```
