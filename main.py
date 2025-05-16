import os
from collections import defaultdict

# Function to parse input files
def parse_input(file_content):
    lines = file_content.strip().splitlines()
    n, m = map(int, lines[0].split())
    dependencies = [tuple(map(int, line.split())) for line in lines[1:m+1]]
    sprocket_costs = list(map(int, lines[m+1:]))
    return n, m, dependencies, sprocket_costs

# Function to calculate cost using memoization
def calculate_cost(part, dependencies_dict, sprocket_costs, memo):
    if part in memo:
        return memo[part]
    total_cost = sprocket_costs[part]
    for subpart in dependencies_dict[part]:
        total_cost += calculate_cost(subpart, dependencies_dict, sprocket_costs, memo)
    memo[part] = total_cost
    return total_cost

# Function to compute total cost for a single file
def compute_total_cost(file_content):
    n, m, dependencies, sprocket_costs = parse_input(file_content)
    dependencies_dict = defaultdict(list)
    for i, j in dependencies:
        dependencies_dict[j].append(i)
    memo = {}
    total_cost = calculate_cost(n - 1, dependencies_dict, sprocket_costs, memo)
    return f"An omnidroid with {n} parts and {m} dependencies, takes {total_cost} sprockets to build."

# Main execution (modified for single file execution)
if __name__ == "__main__":
    # Prompt user to enter the file name
    input_folder = "input"  # Input folder containing the test files
    filename = input("Enter the name of the input file : ")
    
    # Check if the file exists
    filepath = os.path.join(input_folder, filename)
    if os.path.isfile(filepath):
        with open(filepath, "r") as file:
            content = file.read()
            result = compute_total_cost(content)
            print(f"Result for {filename}:\n{result}\n")
    else:
        print(f"The file '{filename}' does not exist in the input folder.")
