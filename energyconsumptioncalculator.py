#Energy Consumption Calculator

#defining devices and their power usage

devices = ["Fan", "Laptop", "Phone", "Light"]
power_watts = [50, 60, 10, 40]

#Hours each device was used
hours_used = [5, 8, 3, 6]

#Initializing total energy
total_energy = 0

#Loop through devices and calculate energy
for i in range(len(devices)):
    energy = power_watts[i] * hours_used[i]
    print(f"{devices[i]} used {energy} watt-hours")
    total_energy += energy

print("Total energy consumption:", total_energy, "watt-energy")