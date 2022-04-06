import math
import input
import physics as p
from setup import *


class Ball:
    def __init__(self, team, start_pos=START_POSITION, scale=BALL_RADIUS, id=0):
        self.id = id
        self.place = (start_pos[0], start_pos[1], start_pos[2])
        self.team = team
        self.scale = scale


class Round:
    def __init__(self, number, leader=1, balls=BALLS_IN_ROUND):
        self.number = number
        self.leader = leader
        self.score = {'team_1': 0, 'team_2': 0}
        self.field = {}
        ball_cochonnet = Ball(leader, scale=COCHONNET_RADIUS)
        self.balls = [ball_cochonnet]
        order = [1,2] if not bool(leader - 1) else [2,1]
        for ball in range(balls):
            self.balls.append(Ball(order[0]))
            self.balls.append(Ball(order[1]))

    def ball_measurements(self):
        for ball in self.balls[1:]:
            distance = math.dist(self.field[ball.id], self.field[1])
            if ball.team == 1:
                self.score['team_1'] += distance
            if ball.team == 2:
                self.score['team_2'] += distance

        return self.score

    def balls_flinging(self):
        for ball in self.balls:
            # Load before fling round field
            p.load_world(self.field)  # simulation

            # Create ball and get ball.id
            ball.id = p.load_object(ball.place, ball.scale)  # simulation
            print(f'ball.id = {ball.id}')

            # Take fling direction
            if ball.id != 1:
                direction = input.get_deviation_from_cachonnet(INPUT_MODE, self.field[1])
            else:
                direction = input.random_cochonnete_vector()

            # fling this ball and get after fling round field
            self.field, disconnect = p.fling_ball_simulation(ball.id, direction)  # simulation

        return self.ball_measurements()


class Game:
    def __init__(self, rounds_in_game=ROUNDS_IN_GAME):
        self.score = {'team_1': 0, 'team_2': 0}
        self.rounds = []
        for i in range(rounds_in_game):
            self.rounds.append(Round(i))

    def get_game_score(self, round: Round):
        self.score['team_1'] += 1 if round.score['team_1'] < round.score['team_2'] else 0
        self.score['team_2'] += 1 if round.score['team_1'] > round.score['team_2'] else 0
        return self.score

    def get_current_game_leader(self):
        return 1 if self.score['team_1'] < self.score['team_2'] else 2

    def get_winner(self):
        t_1_score = self.score['team_1']
        t_2_score = self.score['team_2']
        if t_1_score > t_2_score:
            return 'team_1'
        elif t_1_score < t_2_score:
            return 'team_2'
        else:
            return 'equal'

    def play(self):
        for this_round in self.rounds:
            this_round.leader = self.get_current_game_leader()
            this_round.score = this_round.balls_flinging()
            self.score = self.get_game_score(this_round)

        return self.get_winner(), self.score


game = Game()

print(game.play())
