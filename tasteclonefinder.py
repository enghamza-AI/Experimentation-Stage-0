#Taste Clone Finder

traits = ["music", "movies", "games", "food"]

you = [8, 6, 7, 5]

people = {
    "Ibrahim": [7, 5, 6, 4],
    "Thejan": [2, 9, 1, 8],
    "Anu": [4, 3, 3.5, 2.5]
}

def magnitude(vec):
    sum_sq = 0
    for v in vec:
        sum_sq += v * v
    return sum_sq ** 0.5

def dot_product(a, b):
    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]
    return total

best_match = None
best_score = -1

for person in people:

    other = people[person]

    dot = dot_product(you, other)
    mag1 = magnitude(you)
    mag2 = magnitude(other)

    cosine = dot / (mag1 * mag2)

    if cosine > best_score:
        best_score = cosine
        best_match = person

print("Your taste clone is:", best_match)
print("Similarity score:", best_score)
