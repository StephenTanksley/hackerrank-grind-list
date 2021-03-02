# There is a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2. The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. It is always possible to win the game.

# For each game, you will get an array of clouds numbered 0 if they are safe or 2 if they must be avoided.


# NOT MY SOLUTION...but very snazzy. I kinda wish it was mine Solution belongs to hassanmohsin on HackerRank.

# def jumpingOnClouds(c):
#     if len(c) == 1 : return 0
#     if len(c) == 2: return 0 if c[1]==1 else 1
#     if c[2]==1:
#         return 1 + jumpingOnClouds(c[1:])
#     if c[2]==0:
#         return 1 + jumpingOnClouds(c[2:])

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jumps = 0
    current_node = 0
    keys = {i: value for (i, value) in enumerate(c)}

    while current_node in keys:
        if (current_node + 2 in keys) and (c[current_node + 2] == 0):
            current_node += 2
        elif (current_node + 1 in keys) and (c[current_node + 1] == 0):
            current_node += 1
        else:
            break
        jumps += 1

    return jumps
