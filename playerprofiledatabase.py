#player profile database

#store player data

players = {
    "Hamza": [80, 70, 90],
    "Ibrahim": [75, 85, 80],
    "Thejan": [60, 65, 70]
}

#Function to calculate average skill

def calculate_score(stats):
    total = 0
    for value in stats:
        total += value
        return total / len(stats)
    
#Find best player

best_player = None
best_score = 0

for name in players:
    score = calculate_score(players[name])
    print(name, "score:", round(score, 2))

    if score > best_score:
        best_score = score
        best_player = name

print("Best Player is:", best_player)