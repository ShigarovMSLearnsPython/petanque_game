import logging
import math
import input
import physics as p
from setup import *


logging.basicConfig(level=logging.INFO)


# returns str with team from the top of score_board, if it beats second one
def get_winner(first_line: tuple, second_line: tuple) -> str:
    if first_line[1] > second_line[1]:
        return f'{first_line[0]}'
    else:
        return f'equality'


class Ball:
    def __init__(self, team=0, is_cochonnet=False, start_pos=START_POSITION, scale=BALL_RADIUS, id=0):
        self.id = id
        self.place = (start_pos[0], start_pos[1], start_pos[2])
        self.team = team
        self.scale = scale
        self.is_cochonnet = is_cochonnet
        if is_cochonnet:
            self.scale = COCHONNET_RADIUS


class Round:
    def __init__(self, number: int):
        self.number= number

        self.score: dict[int: int] = {key: 0 for key in range(1, NUMBER_OF_PLAYERS+1)}

        self.field: dict[int: tuple[float, float, float]] = {}

        self.balls: list[Ball] = [Ball(is_cochonnet=True)]

    # mesures distances sum of teams balls to cocho and writes them down
    def distance_to_cocho_measurements(self) -> dict[int, int]:
        for ball in self.balls[1:]:
            distance = math.dist(self.field[ball.id], self.field[1])
            self.score[ball.team] += distance

        logging.info(f'Summed distances are {self.score}')
        return self.score

    # takes fling direction in dependency of ball scale and input type
    def get_fling_direction(self, ball: Ball):
        if not ball.is_cochonnet:
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
            direction = self.get_fling_direction(ball)

            # fling this ball and get after fling round field
            self.field = p.fling_ball_simulation(ball.id, direction, self.number)  # simulation
            logging.info('Balls on field coordinates = ' + f'{self.field}')

            logging.info(f'Team {ball.team} has flunged ball {ball.id}')

        return self.distance_to_cocho_measurements()


class Game:
    def __init__(self, number_of_players=NUMBER_OF_PLAYERS, rounds_in_game=ROUNDS_IN_GAME):
        self.score = {i+1: 0 for i in range(number_of_players)}
        self.rounds = [Round(i+1) for i in range(rounds_in_game)]
        self.in_progress = True

    # writes down to GAME score according to round score
    def record_game_score(self, round_score: dict[int, int]) -> dict[int, int]:
        round_winner = sorted(round_score, key=round_score.get)[0]
        self.score[round_winner] += 1
        return self.score

    # charges all balls for round according to current game leader
    def append_teams_balls_in_round_by_order(self, round: Round):
        order = sorted(self.score, key=self.score.get, reverse=True)
        logging.info(f'The score is {self.score}')
        for team_number in order * BALLS_IN_ROUND:
            round.balls.append(Ball(team_number))

    # returns ordered by score game board
    def get_score_board(self) -> dict[str: int]:
        board = []
        for key in sorted(self.score, key=self.score.get, reverse=True):
            board.append((f'team {key}', self.score[key]))
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
        winner = f'{get_winner(board[0], board[1])}'

        for rec in board:
            logging.info(f'{rec[0]}: {rec[1]}')
        logging.info(f'\nAaand {winner} is the winner!')

        self.in_progress = False
        # return board, f'{winner} is the winner'


game = Game()

game.play()
