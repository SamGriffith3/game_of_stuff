from random import *

def flip_switch():
    switch = 1
    if switch == 1:
        switch -= 1
    else:
        switch += 1
        
        
def choose_card():
    used_cards = []
    rating_filter = []
    switch = flip_switch()
    if input("Include Rated G: y/n?") == "y" or "Y" rated_g = true 
    if input("Include Rated T: y/n?") == "y" or "Y" rated_t = true 
    if input("Include Rated R: y/n?") == "y" or "Y" rated_r = true 
    while switch == 0:
        query = session.query(cards).filter(cards.rated_g, cards.rated_t, cards.rated_r)
        card = random(len(query))
        #TODO make sure query results in list of ids
        if card in used_cards:
            continue
        else:
            flip_switch()
            used_cards.append(card)
            return card
        
                
def flip_card():
    card = choose_card()
    
    # This is where the code to access card database is stored
    #Needs to select a card that has not been played
    #print text


