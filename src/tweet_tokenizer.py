# -*- coding: utf-8 -*-
'''
Created on Dec 22, 2016
Adaptado do Livro: Mastering social media mining with Python

@author: Francisco Moura

'''

import string

from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer 
import pymongo


# from https://github.com/davidmogar/normalizr
def remove_acentos(tokens=list()):
    """
    Remove acentos dos tokens
    Return: lista de tokens
    """
    import unicodedata
    from normalizr import Normalizr
    normalizr = Normalizr(language='pt')
    normalizations = [ 'remove_accent_marks' ]
    l = list()
    for token in tokens:
        l.append(normalizr.normalize(token, normalizations))
    return l

# extract from book Mastering social media mining with Python
def process(text, tokenizer=TweetTokenizer(), stopwords=[]): 
    """Process the text of a tweet: 
    - Lowercase 
    - Tokenize 
    - Stopword removal 
    - Digits removal 
 
    Return: list of strings 
    """ 
    text = text.replace('\n', ' ').replace('\t','').lower() 
    tokens = tokenizer.tokenize(text) 
    return [tok for tok in tokens if tok not in stopwords and not tok.isdigit()] 


if __name__ == '__main__':
    
    tweet_tokenizer = TweetTokenizer() 
    punctuation = list(string.punctuation) 
    
    stopword_pt = stopwords.words('portuguese') 
    stopword_es = stopwords.words('spanish')
    stopword_en = stopwords.words('english')
    stopword_all = stopword_pt + stopword_es + stopword_en
    stopword_all += punctuation + ['rt', 'via', '...', '…']
    print(stopword_all)
    
    client = pymongo.MongoClient('localhost', 27017)
    db = client.tweets_raw
    
    # tokenizar todos os texts dos tweets
    tweets = db.saude_coletiva.find({}, {"_id": 0, "text": 1})
    number_of_tweets = 0
    
    for text in tweets:
        number_of_tweets += 1
        print('number of tweets processed: {}'.format(number_of_tweets))
        if (text.get('text') != None):
            tokens = process(text.get('text'), tweet_tokenizer, stopword_all)
            print(tokens)
           
            for token in remove_acentos(tokens):
                db.tweet_terms.insert_one({"termo": token})

    print("Completed....!!!")
