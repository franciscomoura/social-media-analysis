# -*- coding: utf-8 -*-
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import twitter_credentials
import json


class TwitterStreamingListener(StreamListener):
    """docstring for TwitterStreamingListener"StreamListener""
    def __init__(self, arg):
        super(TwitterStreamingListener,StreamListener self).__init__()
        self.arg = arg
    """
    def on_data(self, data):
        try:
            with open('../data/doencas-tweets.json', 'a') as file:
                file.write(data)
                #print(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
            sleep(5)
        return True

    def on_error(self, status):
        print(status)
        return True

if __name__ == '__main__':
    auth = OAuthHandler(twitter_credentials.consumer_key, twitter_credentials.consumer_secret)
    auth.set_access_token(twitter_credentials.access_token, twitter_credentials.access_token_secret)
    api = tweepy.API(auth)

    """
    tracker_words = ['#AnistiaCaixa2NAO', 'anistia', 'caixa 2', 'dolar', 'alta', 'crise', 
                     'temer', 'governo', 'ladrões', 'partidos', 'políticos', 'câmara', 
                     'deputados', 'stf', 'gilmar mendes',  # segunda adição
                     'pec dos gastos', 'protestos', 'reclamações', 'black friday', # terceira adição
                     'black', 'fraude', # quarta adição
                     'corrupção', 'propina', '10 medidas contra corrupção' # quinta adicao
                     ] 
    """
    tracker_words = ['estupro', 'denúncia', 'vítima', 'abuso sexual', 'assédio sexual', 'violência sexual',
                     'dengue', 'gripe', 'resfriado', 'malária', 'febre', 'chikungunya', 'zika', 'vírus', 'mosquito',
                     'Aedes aegypti', 'depressão', 'ansiedade'
    ]
    twitter_stream = Stream(auth, TwitterStreamingListener())
    twitter_stream.filter(track=tracker_words)

