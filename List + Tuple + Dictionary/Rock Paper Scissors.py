
user1 = input()
user2 = input()

def compre(u1, u2):
    if u1 == u2:
        return("tie")
    elif u1 == 'rock':
        if u2 == 'scissors':
            return(f"{u1} win")
        else:
            return(f"{u2} win")
    elif u1 == 'paper':
        if u2 == 'scissors':
            return(f"{u2} win")
        else:
            return(f"{u1} win")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return(f"{u1} win")
        else:
            return(f"{u2} win" )
    else:
        return("Invalid input! You have not entered rock, paper or scissors, try again.")

print(compre(user1, user2))
#gon hon

user1 = input()
user2 = input()

def compare(u1, u2):

    win = {
        "rock" : "scissors",
        "scissors" : "paper",
        "paper" : "rock",
    }

    if u1 not in win or u2 not in win:
        return "invalid"
    if win[u1] == u2:
        return f"{u1} win"
    else:
        return f"{u2} win"

print(compare(user1, user2))