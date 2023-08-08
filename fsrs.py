from models import *

class FSRS:
    params: Parameters

    def __init__(self) -> None:
        self.params = Parameters()

    def review(self, card: Card, rating: Rating):
        now = datetime.utcnow()
        card.last_review = now
        card.reps += 1

        if card.state == State.New:
            card.elapsed_days = 0
        else:
            card.elapsed_days = (now - card.last_review).days

        match (card.state):
            case State.New:
                card.stability = self.init_stability(rating)
                card.difficulty = self.init_difficulty(rating)

                match (rating):
                    case Rating.Again:
                        card.due = now + timedelta(minutes=1)
                    case Rating.Hard:
                        card.due = now + timedelta(minutes=5)
                    case Rating.Good:
                        card.due = now + timedelta(minutes=10)
                
                easy_interval = self.next_interval(card.stability)
                




    def init_stability(self, r: int) -> float:
        return max(self.p.w[r-1], 0.1)

    def init_difficulty(self, r: int) -> float:
        return min(max(self.p.w[4] - self.p.w[5] * (r - 3), 1), 10)

    def next_interval(self, s: float) -> int:
        new_interval = s * 9 * (1 / self.p.request_retention - 1)
        return min(max(round(new_interval), 1), self.p.maximum_interval)

    def next_difficulty(self, d: float, r: int) -> float:
        next_d = d - self.p.w[6] * (r - 3)
        return min(max(self.mean_reversion(self.p.w[4], next_d), 1), 10)