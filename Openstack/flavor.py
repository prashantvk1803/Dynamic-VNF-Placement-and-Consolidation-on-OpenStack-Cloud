#specify the flavor for Vm ,depending on that the filter hosts algorithm will eliminate the compute nodes

flavor = input("Enter the flavor (e.g., m1.tiny or m1.small): ")

with open("flavor.txt", "w") as file:
    file.write(flavor)
    print(f"Flavor '{flavor}' has been saved to flavor.txt")