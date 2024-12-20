import itertools

num = "202aaaa71046a"
# Create a list of replacement options for 'a'
replace_options = ['1', '2', '3']

# Find all positions of 'a' in the string
a_positions = [i for i, char in enumerate(num) if char == 'a']

# Generate all combinations of '1', '2', '3' for each 'a' in the string
combinations = itertools.product(replace_options, repeat=len(a_positions))

# For each combination, replace 'a' with the corresponding number
results = []
for combo in combinations:
    num_list = list(num)
    for idx, position in enumerate(a_positions):
        num_list[position] = combo[idx]
    results.append(''.join(num_list))

# Print all possible combinations
for result in results:
    print(result)

# Write the results to a file
with open("pool.txt", "w") as file:
    for result in results:
        file.write(result + '\n')
