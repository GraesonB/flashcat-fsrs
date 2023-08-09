import random
from datetime import datetime
from fsrs import FSRS
from models import Card as NewCard, Rating
from real_fsrs.real_models import Card
from rich import print
from real_fsrs.real import FSRS as RFSRS

fsrs = FSRS()
real_fsrs = RFSRS()

real_card = Card()
new_card = NewCard()

for i in range(200):
    rating = random.randint(1,4)
    # rating = Rating.Easy
    fsrs.review(new_card, rating)
    now = datetime.utcnow()
    scheduling_cards = real_fsrs.repeat(real_card, now)

    real_card = scheduling_cards[rating].card




print(vars(new_card))
print(vars(real_card))