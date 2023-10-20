# Game Rock Paper Scissors


def rps_game(player1, player2):
    
    if player1 == 'rock' and player2 == 'paper':
        return "The winner_is the second player"
    
    elif player1 == 'rock' and player2 == 'scissors':
        return "The winner_is the first player"
    
    elif player1 == 'paper' and player2 == 'scissors':
        return "The winner_is the second player"
    
    elif player1 == 'paper' and player2 == 'rock':
        return "The winner_is the first player"
    
    elif player1 == 'scissors' and player2 == 'rock':
        return "The winner_is the second player"
    
    elif player1 == 'scissors' and player2 == 'paper':
        return "The winner_is the first player"



