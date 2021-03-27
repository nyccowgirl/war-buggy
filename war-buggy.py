#!/usr/local/bin/python3
import random

# war, the card game of chance where 26 battles take place between rival armies.
# the higher card wins each battle. ties accumulate a bonus to be won at the next battle.
# for each battle, outputs the number of cards left, the two cards drawn, and the win totals.
# if a battle is a tie, its value is accrued towards the next one that is won.

# build deck list, containing tuples of the names and values of each card
# the order of the names list determines the cards' values
# the deck is 52 tuples like this:  ('Jack of Diamonds', 11)
names = [ 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace' ]
suits = [ 'Hearts', 'Diamonds', 'Spades', 'Clubs' ]
# EDIT: To get 'Jack of Diamonds' to reflect value of 11, index should be from names list plus 2.
deck = [ (name + ' of ' + suit, (names.index(name) + 2) ) for name in names for suit in suits ]
bonus, scoreA, scoreB = 0, 0, 0

# as long as there are cards left in the deck, draw pairs for each battle
# while loop is safe as long as the only thing that happens to deck is .pop()
while deck:

 # compare a pair of cards' values, tally scores and adjust bonus
 # there are three possible cases; in case of a win the bonus is paid out, otherwise it rises
 # EDIT: pop() removes the last items in list. Given the order that they were created, the cards will always
 # be tied so changed to get random element based on range of remaining size of deck -> instead of
 # cardA, cardB = deck.pop(), deck.pop()
 cardA, cardB = deck.pop(random.randrange(len(deck))), deck.pop(random.randrange(len(deck)))
 if cardA[1] == cardB[1]:
  # EDIT: If tie, 1 is added to bonus to carry over to next round (instead of bonus += scoreA).
  bonus += 1
  outcome = 'ties'
 elif cardA[1] > cardB[1]:
  scoreA += 1 + bonus
  bonus = 0
  outcome = 'beats'
 else:
  # EDIT: If cardB[1] > cardA[1], scoreB should win 1 plus any carryover bonus (instead of scoreA += 1 + bonus).
  scoreB += 1 + bonus
  bonus = 0
  # EDIT: this line should be indented under the else statement
  outcome = 'is beaten by'

 # display the outcome of each battle, current winnings, and how much left to be won
 event = "The {} {} the {}!".format ( cardA[0], outcome, cardB[0] )
 print ( '{:55.55}  ${} to ${}, ${} left.'.format ( event, scoreA, scoreB, int(len(deck)/2) ) )

