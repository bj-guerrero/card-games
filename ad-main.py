# Shuffle deck
# Draw two, pop two cards out of deck
# Calculate probability
# Bet, Y or N
    # if Y: draw one, pop card out of deck
    # if N: continue
# Draw two, pop two cards out of deck
# Calcualte probability
# Bet, Y or N
    # if Y: draw one, pop card out of deck
    # if N: continue
# Draw two, pop two cards out of deck
# ...
# ...

import random

suits = ['H','D','C','S']
values = ['02','03','04','05','06','07','08','09','10','11','12','13','14']

cards = []
for suit in suits:
    for value in values:
        cards.append(value + suit)

del suit
del value

shuffle = random.sample(cards, len(cards))
while True:
    
    while True:
       d1 = input("\nDraw 1: ").upper()
       d2 = input("Draw 2: ").upper()
       if (d1 in shuffle) and (d2 in shuffle):
           shuffle.remove(d1)
           shuffle.remove(d2)
           break
       else:
            print("\nInvalid input. Try again.")
    
    ##### Can call Aces high or low #####
    if d1[:2] == '14' and d2[:2] != '14':
        d1l = list(d1)
        d1l[:2] = '02'
        d1_low = "".join(d1l)
        draws_low = [d1_low, d2]
        draws_low.sort()
    elif d1[:2] != '14' and d2[:2] == '14':
        d2l = list(d2)
        d2l[:2] = '02'
        d2_low = "".join(d2l)
        draws_low = [d1, d2_low]
        draws_low.sort()
    elif d1[:2] == '14' and d2[:2] == '14':
        d1l = list(d1)
        d1l[:2] = '02'
        d1_low = "".join(d1l)
        d2l = list(d2)
        d2l[:2] = '02'
        d2_low = "".join(d2l)
        draws_low = [d1, d2_low]
        draws_low.sort()
    else:
        pass
    ##########
    
    draws = [d1, d2]
    draws.sort()
    
    wins = []
    for card in shuffle:
        if int(card[0:2]) > int(draws[0][0:2]) and int(card[0:2]) < int(draws[1][0:2]):
            wins.append(1)
        else:
            wins.append(0)
        pct_win = (sum(wins) / len(wins))*100
    print("Probability of winning: " + str(round(pct_win, 2)) + "%")
    
    try:
        wins = []
        for card in shuffle:
            if int(card[0:2]) > int(draws_low[0][0:2]) and int(card[0:2]) < int(draws_low[1][0:2]):
                wins.append(1)
            else:
                wins.append(0)
                pct_win_low = (sum(wins) / len(wins))*100            
        print("Probability of winning (Ace low or Ace low/Ace high): " + str(round(pct_win_low, 2)) + "%\n")
        del draws_low
    except NameError:
        print("No Aces are drawn yet.\n")
    
    while True:
        decision = input("Bet: ")
        if decision.upper() == 'Y' or decision.upper() == 'N':    
            break
        else:
            print("Invalid input. Try again.\n")
            
    if decision.upper() == 'Y' and len(shuffle) != 0:
        while True:
            d3 = input("Bet draw: ").upper()
            if d3 in shuffle:
                shuffle.remove(d3)
                break
            else:
                print("Card not in deck. Try again.\n")
   
    elif decision.upper() == 'Y' and len(shuffle) == 0:
        print("No more cards to bet. End of game. Reshuffle cards.")
        break 
                
    elif decision.upper() == 'N':
        pass
            
    print("\nRemaining cards: " + str(len(shuffle)))
    
    if len(shuffle) in [0, 1, 2]:
        print("End of game. Reshuffle cards.")
        break