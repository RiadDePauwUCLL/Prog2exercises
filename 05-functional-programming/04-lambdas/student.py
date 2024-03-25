from itertools import count
import util

def group_by_suit(cards):
    return util.group_by(cards, lambda c1 : c1.suit == cards)