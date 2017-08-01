#!/usr/bin/python env
#encoding:utf-8
"""
@version: python2.7
@author: ‘whyc'
@license: Apache Licence 
@contact: 8720whyc@gmail.com
@site: 
@software: PyCharm
@file: Demo2.py
@time: 17-7-28 下午9:41
"""

import  collections
from random import choice
# 创建一个纸牌的集合
Card = collections.namedtuple('Card',['rank','suit'])

class FrenchDeck():
    #生成十三张拍　
    ranks = [str(n) for n in range(2,11)] + list("JQKA")
    #四种不同的花色
    suits = 'spades diamonds clubs hearts'.split()
    kings = 'Litte Big'.split()
    def __init__(self):
        self._cards = [Card(rank=rank,suit=suit) for suit in self.suits
                                                  for rank in self.ranks]+\
                       [Card(rank=king,suit='king') for king in self.kings]
    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

    def __setitem__(self, key, value):
        self._cards[key]=value


suit_values = dict(spades=3,hearts=2,clubs=1,diamonds=0)
def spades_high(card):
    if card.rank==FrenchDeck.kings[0]:
        return 52
    if card.rank==FrenchDeck.kings[1]:
        return 53
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

def wash_cards():
    pass



if __name__ == '__main__':
    deck = FrenchDeck()
    print len(deck),deck[1]
    beer_card = Card('7','diamonds')
    print beer_card.__getitem__(0)
    lens = len(deck)
    #for i in range(0,lens+1):
        #print choice(deck)
    for card in sorted(deck,key=spades_high):
        print card
    #print deck[12:13]
    print "deck len %s"%len(deck)