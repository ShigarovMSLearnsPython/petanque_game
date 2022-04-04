import physics as p

cochonnet_radius = 0.2
ball_radius = 0.6
dirrection = (1, -1, 0.6)
power = 1500

class Round:
    def __init__(self, number, leader, score):
        self.number = number
        self.leader = leader
        self.score = score
        self.field = {}


class Ball:
    def __init__(self, x, y, z, team, scale):
        self.place = (x, y, z)
        self.team = team
        self.scale = scale

    # def fling_ball(self, dirrection, power):
    #     p.fling_ball_simulation(self.scale, dirrection, power)

        # round.field = get_field()


round_1 = Round(1, None, (0, 0))
ball_1 = Ball(0, 0, 0.5, 1,ball_radius)
p.fling_ball_simulation(ball_1, dirrection, power)
# ball_1.fling_ball(dirrection, power)
# round_1.ball_flings()
# round_1.get_score()


def input(player_id: int, x, y, z, power):
    pass

def get_score():
    pass

def load_fling():
    pass

# def simulate_fling(pointer, power):
#     return location_data
