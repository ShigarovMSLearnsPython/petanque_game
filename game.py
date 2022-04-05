import math
import random

import physics as p

cochonnet_radius = 0.2
ball_radius = 0.4
dirrections = [(-1, 0.3, 1.6), (-0.8, 0, 1.6), (-1, 2, 1)]
power = 200
start_position = (0, 0, 1)
balls_in_round = 1
rounds_in_game = 3


class Round:
    def __init__(self, number, leader, balls=balls_in_round):
        self.number = number
        self.leader = leader
        self.score = {'team_1': 0, 'team_2': 0}
        self.field = {}
        self.balls = []
        for ball in range(balls):
            self.balls.append(Ball(1))
            self.balls.append(Ball(2))

    def get_score(self):
        for ball in self.balls:
            distance = math.dist(ball.place, ball_cochonnet.place)
            if ball.team == 1:
                print('ok')
                self.score['team_1'] += distance
            if ball.team == 2:
                self.score['team_2'] += distance

            return self.score


    def clean_field(self):

        for ball in self.balls:
            p.p.removeBody(ball.id)
        return True


class Ball:
    def __init__(self, team, start_pos=start_position, scale=ball_radius, id=0):
        self.id = id
        self.place = (start_pos[0], start_pos[1], start_pos[2])
        self.team = team
        self.scale = scale


def ran_dir(x,y,z):
    dir = (x * random.uniform(0.98, 1.2), y * random.uniform(0.98, 1.2), z * random.uniform(0.98, 1.2))
    return dir


def get_winner():
    return 'team_1' if game_score['team_1'] > game_score['team_2'] else 'team_2'

all_game = []
game_score = {'team_1': 0, 'team_2': 0}
for n in range(rounds_in_game):
    round = Round(n, 1)
    dirrection = ran_dir(-0.8, 0.6, 1.6)
    ball_cochonnet = Ball(1, scale=cochonnet_radius)
    ball_cochonnet.place = p.fling_ball_simulation(ball_cochonnet, dirrection, power)
    round.field.update({ball_cochonnet.id: ball_cochonnet.place})

    for ball in round.balls:
        dirrection = ran_dir(-0.8, 0.6, 1.6)
        ball.place = p.fling_ball_simulation(ball, dirrection, power)
        round.field.update({ball.id: ball.place})

        distance = math.dist(ball.place, ball_cochonnet.place)
        print(distance)
        if ball.team == 1:
            round.score['team_1'] += distance
        if ball.team == 2:
            round.score['team_2'] += distance

    game_score['team_1'] += round.score['team_1']
    game_score['team_2'] += round.score['team_2']
    all_game.append(round)
    round.clean_field()
    p.p.removeBody(ball_cochonnet.id)

    # print(ball.place)
    # print(ball.team)

print(f'winner is {get_winner()}')





# ball_1.fling_ball(dirrection, power)
# round_1.ball_flings()
# round_1.get_score()


# def input(player_id: int, x, y, z, power):
#     pass
#
# def get_score():
#     pass
#
# def load_fling():
#     pass

# def simulate_fling(pointer, power):
#     return location_data
