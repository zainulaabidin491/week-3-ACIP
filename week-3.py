# Task 1
def get_weights_and_names():
    weights = []
    names = []
    for i in range(30):
        while True:
            name = input(f"Enter name of pupil {i+1}: ")
            if name:  # Check if name is not empty
                names.append(name)
                break
            else:
                print("Name cannot be empty. Please try again.")
        
        while True:
            try:
                weight = float(input(f"Enter weight of {name} in kg: "))
                if weight > 0:  # Validate weight to be positive
                    weights.append(weight)
                    break
                else:
                    print("Weight must be a positive number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    return weights, names

# Task 2
def calculate_weight_difference(initial_weights):
    weight_differences = []
    for i in range(30):
        while True:
            try:
                final_weight = float(input(f"Enter final weight of pupil {i+1} in kg: "))
                if final_weight > 0:  # Validate weight to be positive
                    weight_differences.append(final_weight - initial_weights[i])
                    break
                else:
                    print("Weight must be a positive number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    return weight_differences

# Task 3
def print_significant_weight_changes(names, weight_differences):
    for i in range(30):
        if abs(weight_differences[i]) > 2.5:
            change = "rise" if weight_differences[i] > 0 else "fall"
            print(f"{names[i]} has a {change} in weight of {abs(weight_differences[i]):.2f} kg.")

def main():
    initial_weights, names = get_weights_and_names()
    print("\nInitial Weights:")
    for i in range(30):
        print(f"{names[i]} - {initial_weights[i]} kg")
    
    weight_differences = calculate_weight_difference(initial_weights)
    print("\nSignificant Weight Changes:")
    print_significant_weight_changes(names, weight_differences)

if __name__ == "__main__":
    main()