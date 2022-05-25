import random

def play():
    user = input("What's your choice? 'R' for rock, 'P' for paper, 'S' for scissors: ").lower()
    computer = random.choice(['r', 's', 'p'])
    
    if user == computer:
        return 'It\'s a tie'
    
    if is_win(user, computer):
        return 'You won!'

    return 'You lost'

    
def is_win(player, opponent):
    if (player == 'r'and opponent == 's') or (player == 's' and opponent == 'p') \
        or(player =='p' and opponent == 'r'):
            return True
        
print(play())