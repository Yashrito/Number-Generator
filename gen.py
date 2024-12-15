# Script to generate numbers from 9200000000 to 9699999999
filename = "num.txt"

with open(filename, "w") as file:
    # Loop through the specified range
    for i in range(9200000000, 9700000000):
        file.write(f"{i}\n")

print(f"File '{filename}' generated successfully with numbers from 9200000000 to 9699999999.")
