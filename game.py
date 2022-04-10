
import math
import input
import physics as p
from setup import *


# returns str with team from the top of score_board, if it beats second one
def get_winner(board: dict[str, int]) -> str:
    if board[list(board)[0]] > board[list(board)[1]]:
        return f'{board[list(board)[0]]}'
    else:
        return f'equality'


class Ball:
    def __init__(self, team, start_pos=START_POSITION, scale=BALL_RADIUS, id=0):
        self.id = id
        self.place = (start_pos[0], start_pos[1], start_pos[2])
        self.team = team
        self.scale = scale


class Round:
    def __init__(self, number: int):
        self.number = number

        self.score = {}  # dict[int: int]
        for i in range(NUMBER_OF_PLAYERS):
            self.score.update({(i+1): 0})

        self.field = {}  # dict[int: tupple(float, float, float)]
        self.cochonnet = Ball(scale=COCHONNET_RADIUS)
        self.balls = [self.cochonnet]

    # mesures distances sum of teams balls to cocho and writes them down
    def distance_to_cocho_measurements(self) -> dict[int, int]:
        for ball in self.balls[1:]:
            distance = math.dist(self.field[ball.id], self.field[1])
            self.score[ball.team] += distance

        return self.score

    # takes fling direction in dependency of ball scale and input type
    def get_fling_direction(self, ball_scale):
        if ball_scale != COCHONNET_RADIUS:
            # for all balls. In this situation cochonnet is already flinged and we use its place to dirrect
            cochonnet_place = self.field[1]
            return input.get_fling_vector(INPUT_MODE, cochonnet_place)
        else:
            # for cochonnet. fling it with random vector
            return input.random_cochonnete_vector()

    # plays round and gets its score
    def play(self) -> dict[int, int]:
        for ball in self.balls:

            # create ball in physics and get unique ball.id
            ball.id = p.create_ball(ball.place, ball.scale)  # simulation

            # get direction of the fling
            direction = self.get_fling_direction(ball.scale)

            # fling this ball and get after fling round field
            self.field = p.fling_ball_simulation(ball.id, direction, self.number)  # simulation

        return self.distance_to_cocho_measurements()


class Game:
    def __init__(self, number_of_players=NUMBER_OF_PLAYERS, rounds_in_game=ROUNDS_IN_GAME):
        self.score = {}
        for i in range(number_of_players):
            self.score.update({i+1: 0})
        self.rounds = []
        for i in range(rounds_in_game):
            self.rounds.append(Round(i+1))

    # writes down to GAME score according to round score
    def record_game_score(self, round_score: dict[int, int]) -> dict[int, int]:
        round_winner = sorted(round_score, key=round_score.get, reverse=True)[0]
        self.score[round_winner] += 1
        return self.score

    # charges all balls for round according to current game leader
    def append_teams_balls_in_round_by_order(self, round: Round):
        order = sorted(self.score, key=self.score.get, reverse=True)
        for team_number in order * BALLS_IN_ROUND:
            round.balls.append(Ball(team_number))

    # returns ordered by score game board
    def get_score_board(self) -> dict[str: int]:
        board = {}
        for key in sorted(self.score, reverse=True):
            board.update({f'team {key}': self.score[key]})
        return board

    def play(self) -> dict[str: int]:
        p.load_world()

        for this_round in self.rounds:
            self.append_teams_balls_in_round_by_order(this_round)
            this_round.score = this_round.play()
            self.score = self.record_game_score(this_round.score)
            p.clean_balls()

        p.disconnect()

        board = self.get_score_board()
        winner = f'{get_winner(board)}'

        return board, f'{winner} is the winner'


game = Game()

print(game.play())
