#career alignment checker

traits = ["math", "creativity", "social", "risk"]

user = [0.9, 0.6, 0.4, 0.7]

#career vectors

careers = {
    "Engineer": [0.95, 0.3, 0.2, 0.4],
    "Designer": [0.2, 0.9, 0.5, 0.3],
    "Founder": [0.6, 0.7, 0.8, 0.9]
}

best_career = None
best_score = -1

for career in careers:

    vector = careers[career]
    scope = 0

    for i in range(len(user)):
        score += user[i] * vector[i]

    if score > best_score:
        best_score = score
        best_career = career

print("Best career match:", best_career)
print("Alignment score:", best_score)


