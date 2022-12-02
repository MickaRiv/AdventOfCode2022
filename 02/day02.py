import numpy as np

trad = {"A":1, "X":1, "B":2, "Y":2, "C":3, "Z":3}
win_points = 6
draw_points = 3

def score1(moves):
    opp_move, my_move = (trad[move] for move in moves)
    return (my_move +
            draw_points*(my_move==opp_move) + 
            win_points*((my_move-opp_move)%3==1))

data = np.loadtxt("input",dtype="str")

print(f"My final score is {np.sum([score1(d) for d in data])}")

def score2(moves):
    opp_move, result = (trad[move] for move in moves)
    my_move = (opp_move+result-3)%3 + 1
    return (my_move +
            draw_points*(result==2) + 
            win_points*(result==3))

print(f"My final score is now {np.sum([score2(d) for d in data])}")