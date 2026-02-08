#weapon power evaluator

#function to calculate power

def calculate_weapon_power(damage, accuracy, fire_rate):
    power = damage * accuracy * fire_rate
    return power

#weapon data

weapons = ["Pistol", "Rifle", "ShotGun"]

damage = [30, 45, 70]
accuracy = [0.8, 0.9, 0.5]
fire_rate = [0.6, 0.7, 0.4]

#store computed powers

weapon_powers = []

for i in range(len(weapons)):
    power = calculate_weapon_power(damage[i], accuracy[i], fire_rate[i])
    weapon_powers.append(power)
    print(weapons[i], "power:", round(power, 2))

#Find strongest weapon

max_power = weapon_powers[0]
max_index = 0

for i in range(len(weapon_powers)):
    if weapon_powers[i] > max_power:
        max_power = weapon_powers[i]
        max_index = i

print("Strongest weapon:", weapons[max_index])