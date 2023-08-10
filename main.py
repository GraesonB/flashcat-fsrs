from fsrs import FSRS
from models import *

fsrs = FSRS()
card = Card()

card = fsrs.review(card, Rating.Easy)
print(vars(card))