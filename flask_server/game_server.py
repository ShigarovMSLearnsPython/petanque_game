from flask import Flask, request
from flask_server.game import Player, Game

app = Flask(__name__)

players_ever_played: dict[int: Player] = {}


@app.route('/')
def index():
    return 'Index Page'


@app.route('/signup')
def sign_up():
    id = request.args.get('id', type=int)
    # if there is such a player
    try:
        nickname = players_ever_played[id].nickname
        new = ''
    # if not, let's create one
    except KeyError:
        # ask player his nickname
        nickname = request.args.get('nickname', type=str)
        player = Player(id, nickname)
        players_ever_played.update({id: player})
        nickname = player.nickname
        new = 'new '

    app.logger.info(f'\n{new}player {nickname} with id {id} came to game.')
    return 'OK', 200


@app.route('/all_users')
def show_all_users():
    response = [f'{players_ever_played[id].nickname} - {players_ever_played[id].id}' for id in players_ever_played]
    app.logger.info(', '.join(response))
    return 'OK', 200


@app.route('/user/<user_id>')
def show_user_profile(user_id):
    # show the user profile for that user
    app.logger.info(players_ever_played[int(user_id)].nickname)
    return 'OK', 200


@app.route('/ready_for_the_game')
def player_is_ready_for_the_game():
    game_id = request.args.get('game_id', type=int)
    id = request.args.get('id', type=int)
    players_ever_played[id].ready_for_the_game = game_id
    app.logger.info(f'Player {players_ever_played[id].nickname} is ready for the game {game_id}')
    return 'OK', 200


@app.route('/game')
def play_game():
    game_id = request.args.get('game_id', type=int)
    id_1 = request.args.get('p1', type=int)
    id_2 = request.args.get('p2', type=int)

    if players_ever_played[id_1].ready_for_the_game == players_ever_played[id_2].ready_for_the_game == game_id:
        game = Game(game_id, [players_ever_played[id_1], players_ever_played[id_2]])
        app.logger.info(f'Created game {game_id} is to be started')
        game.play()
    return 'OK', 200
