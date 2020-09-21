"""
players = {
    "ST": "Werner",
    "CB": "Silva",
    "RW": "Havertz",
    "CM": "Mount",
    "LB": "Chilwell"
}
"""

#center_back = players["CB"]
#right_wing = players["RW"]

#print(center_back)
#print(right_wing)
#print(players["LB"])
#print(players)

"""
players = {
    "ST": "Werner",
    "CB": "Silva",
    "RW": "Havertz",
    "CM": "Mount",
    "LB": "Chilwell"
}

print(list(players.values())[1])

teams = {
    'barca': ['Messi', 'Suarez', 'Neymar'],
    'chelsea': ['Werner', 'Havertz', 'Mount'],
    'spurs': ['Kane', 'Son', 'Bale'],
    'man city': ['Mahrez', 'Foden', 'Sterling']
}
"""
import random
def weighted_lottery(weights):
    container_list = []
    for (name, weight) in weights.items():
        for _ in range(weight):
            container_list.append(name)
        return random.choice(container_list)
    

other_weights = {
    'winning': 1,
    'break_even': 2,
    'losing': 3
}

weighted_lottery(other_weights)

print(weighted_lottery(other_weights))