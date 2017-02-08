# -*- coding: utf-8 -*-
'''
Created on Dec 22, 2016

@author: Francisco Moura
'''

import pprint

from bson.code import Code
import pymongo


if __name__ == '__main__':
    mapper = Code("""
                function () {
                    emit(this.termo, 1);
                }
                """)
    
    reducer = Code("""
                function (key, value) {
                  return Array.sum(value);
                }
                """)
    
    client = pymongo.MongoClient('localhost', 27017)
    db = client.tweets_raw
    
    result = db.tweet_terms.map_reduce(mapper, reducer, "tf_results", 
                                       query={'$or': [
                                           {'termo': 'abuso'},
                                           {'termo': 'estupro'},
                                           {'termo': 'denuncia'},
                                           {'termo': 'vitima'},
                                           {'termo': 'assedio'},
                                           {'termo': 'violencia'}
                                           ]})
    for doc in result.find():
        pprint.pprint(doc)
        