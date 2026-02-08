#Effort meter

subjects = ["Math", "Programming", "Physics", "Design"]

study_hours = [3, 4, 2, 1]

#calculate magnitude

sum_square = 0

for h in study_hours:
    sum_square += h * h

magnitude = sum_square ** 0.5

print("study vector:", study_hours)
print("Total effort magnitude:", magnitude)

