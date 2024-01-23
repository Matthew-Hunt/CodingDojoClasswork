class Player:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        self.position = data['position']
        self.team = data['team']


    def __repr__(self):
        print = f'Player: {self.name}, is {self.age} years old, his position is {self.position} and players for the {self.team}'

kevin = {
    "name": "Kevin Durant",
    "age":34,
    "position": "small forward",
    "team": "Brooklyn Nets"
}
jason = {
    "name": "Jason Tatum",
    "age":24,
    "position": "small forward",
    "team": "Boston Celtics"
}
kyrie = {
    "name": "Kyrie Irving",
    "age":32, "position": "Point Guard",
    "team": "Brooklyn Nets"
}

player_one = Player(kevin)
#print(player_one.name)

player_two = Player(kevin)
#print(player_two.name)

player_three = Player(kevin)
#print(player_three.name)


players = [
    {
        "name": "Kyrie Irving1",
        "age":32, "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Kyrie Irving2",
        "age":32, "position": "Point Guard",
        "team": "Brooklyn Nets"
    },
    {
        "name": "Kyrie Irving3",
        "age":32, "position": "Point Guard",
        "team": "Brooklyn Nets"
    }
]


team_list = []
for data in players:
    player = Player(data)
    team_list.append(data)
print(team_list)