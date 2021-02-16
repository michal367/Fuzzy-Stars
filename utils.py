
PLAYER_PLAYER = 1
PLAYER_COMPUTER = 2
DIFFICULTY_NORMAL = 1
DIFFICULTY_HARD = 2

def dist_square(pos, pos2):
    return (pos.x - pos2.x)**2 + (pos.y - pos2.y)**2

def dist_square2(pos, pos2):
    return ((pos.x + pos.size/2) - (pos2.x + pos2.size/2))**2 + ((pos.y + pos.size/2) - (pos2.y + pos2.size/2))**2