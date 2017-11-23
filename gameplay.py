from random import shuffle
from local_db import *
import time
from flask import session as ses


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


def countdown(t):
    while t:
        mins, secs = divmod(t, 30)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1
    print('Time Is Up!\n\n\n\n\n')
    
    
def write_response():
    c = choose_card()
    timer = countdown(1)
    if timer != 0:    
        response = input(c + " : ")
        return response, c
    else:
        print('You Missed Your Chance!')


def turn(user_id):
    response, c = write_response()
    card_responses = {}
    x = ses['user']
    card_responses[user.name] = {"responses": card_responses, "c": c, "user": user}


def reveal_answers():
    return "something"
    


    '''
 This section contains the code for creating and uploading a new card to the database
    Currently this is set to update the universal card database
    '''
    
    
def create_new_card():
    card = input(str("What's the STUFF?: "))
    return card


def select_card_rating():
    card = create_new_card()
    rating = input(str("Rated G, T, or R?: ")).lower().strip()
    if rating in ["g", "t", "r"]:
        card_gen = Cards(card=card, rating=rating)
        session.add(card_gen)
    else:
        print("Please choose a valid rating for the STUFF")
        select_card_rating()


if __name__ == '__main__':
    select_card_rating()
    turn(1)
