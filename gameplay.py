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
    c = choose_card()
    response = input(c + " : ")
    return response, c


def turn(user_id):
    response, c = write_response()
    card_responses = {}
    user = session.query(User).filter(User.user_id == user_id).one()
    card_responses[user.name] = {"responses": card_responses, "c": c, "user": user}
    return card_responses


def get_user():
    users = session.query()



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
