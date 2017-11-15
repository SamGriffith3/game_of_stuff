from random import shuffle
from local_db import *


def flip_switch():
    switch = 1
    if switch == 1:
        switch -= 1
    else:
        switch += 1
        

def choose_ratings():
    g = 0
    t = 0
    r = 0
    rating = input("Choose Rating: G, T, or R").lower().strip()
    if rating in ["g", "t", "r"]:
        return rating
    else:
        return choose_ratings()


def choose_card():
    switch = flip_switch()
    rating = choose_ratings()
    card_ids = [session.query(Cards).filter(Cards.rating == rating).all()]
    shuffle(card_ids)
    while switch == 0:
        c = card_ids.pop(0)
        print(c.card)
        switch = flip_switch()
        GameData.flip_card(True)
        return c
                

def write_response():
    choose_card()
    response = input(c + " : ")
  	return response
    
    
if __name__ == '__main__':
    write_response()
        
    
    


