from models import *

class FSRS:
    params: Parameters

    def __init__(self) -> None:
        self.params = Parameters()

    def repeat(self, card: Card):
        now = datetime.utcnow()
        if card.state == State.New:
            card.elapsed_days = 0
        else:
            card.elapsed_days = (now - card.last_review).days
        card.last_review = now
        card.reps += 1
        