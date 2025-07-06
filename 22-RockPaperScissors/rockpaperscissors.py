"""
Write a rps_winner() function with parameters player1 and player2. These parameters are
passed one of the strings 'rock', 'paper', or 'scissors' representing that player’s move. If
this results in player 1 winning, the function returns 'player one'. If this results in player 2
winning, the function returns 'player two'. Otherwise, the function returns 'tie'.

Assume player move values are restricted to rock, paper, or scissors
"""

def rps_winner(p1_mov, p2_mov):
    movement = ["rock", "paper", "scissors"]
    win_to = ["scissors", "rock", "paper"]

    """checks player 1 winner"""
    ndx = movement.index(p1_mov)
    if win_to[ndx] == p2_mov:
        return "player one"

    """checks player 2 winner"""
    ndx = movement.index(p2_mov)
    if win_to[ndx] == p1_mov:
        return "player two"

    """tie"""
    return "tie"


assert rps_winner('rock', 'paper') == 'player two'
assert rps_winner('rock', 'scissors') == 'player one'
assert rps_winner('paper', 'scissors') == 'player two'
assert rps_winner('paper', 'rock') == 'player one'
assert rps_winner('scissors', 'rock') == 'player two'
assert rps_winner('scissors', 'paper') == 'player one'
assert rps_winner('rock', 'rock') == 'tie'
assert rps_winner('paper', 'paper') == 'tie'
assert rps_winner('scissors', 'scissors') == 'tie'