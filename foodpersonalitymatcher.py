#food personality matcher

traits = ["Spicy", "sweet", "crunchy"]

#user taste vector

user = [0.8, 0.6, 0.7]

#Food database (vectors)

foods = {
    "pizza": [0.3, 0.2, 0.4],
    "Tacos": [0.7, 0.3, 0.5],
    "Donut": [0.1, 0.9, 0.2],
    "Fried Chicken": [0.6, 0.2, 0.8]
}

best_food = None
best_distance = 999999

#loop through food

for food_name in foods:

    food_vector = foods[food_name]
    distance = 0

    for i in range(len(user)):
        diff = abs(user[i] - food_vector[i])
        distance += diff

    if distance < best_distance:
        best_distance = distance
        best_food = food_name

print("Best match food:", best_food)
print("Distance score:", best_distance)