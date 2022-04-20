#!/bin/zsh
echo registering new user
curl 'http://127.0.0.1:5000/signup?id=666&nickname=Devil'

echo registering another new user
curl 'http://127.0.0.1:5000/signup?id=606&nickname=Bob'

echo get list of all users
curl 'http://127.0.0.1:5000/all_users'

echo player 1 is ready
curl 'http://127.0.0.1:5000/ready_for_the_game?game_id=111&id=666'

echo player 2 is ready
curl 'http://127.0.0.1:5000/ready_for_the_game?game_id=111&id=606'

echo start the game
curl 'http://127.0.0.1:5000/game?game_id=111&p1=606&p2=666'
