data = [
    {"Color": "Red", "Type": "Sports", "Origin": "Domestic", "Stolen": "Yes"},
    {"Color": "Red", "Type": "Sports", "Origin": "Domestic", "Stolen": "No"},
    {"Color": "Red", "Type": "Sports", "Origin": "Domestic", "Stolen": "Yes"},
    {"Color": "Yellow", "Type": "Sports", "Origin": "Domestic", "Stolen": "No"},
    {"Color": "Yellow", "Type": "Sports", "Origin": "Imported", "Stolen": "Yes"},
    {"Color": "Yellow", "Type": "SUV", "Origin": "Imported", "Stolen": "No"},
    {"Color": "Yellow", "Type": "SUV", "Origin": "Imported", "Stolen": "Yes"},
    {"Color": "Yellow", "Type": "SUV", "Origin": "Domestic", "Stolen": "No"},
    {"Color": "Red", "Type": "SUV", "Origin": "Imported", "Stolen": "No"},
    {"Color": "Red", "Type": "Sports", "Origin": "Imported", "Stolen": "Yes"},
]

# Print dataset
print("Dataset:")
for row in data:
    print(row)

# Calculate and print rows and columns
num_rows = len(data)

# Calculate and print P(Stolen)
count_yes = sum(1 for row in data if row["Stolen"] == "Yes")
count_no = num_rows - count_yes
prob_yes, prob_no = count_yes / num_rows, count_no / num_rows
print(f"\nP(Stolen='Yes'): {prob_yes}")
print(f"P(Stolen='No'): {prob_no}")

# Function to calculate attribute probability
def calculate_prob(attribute, value):
    return sum(1 for row in data if row[attribute] == value) / num_rows

# Calculate and print individual probabilities
prob_color_red = calculate_prob("Color", "Red")
prob_color_yellow = calculate_prob("Color", "Yellow")
prob_type_sports = calculate_prob("Type", "Sports")
prob_type_suv = calculate_prob("Type", "SUV")
prob_origin_domestic = calculate_prob("Origin", "Domestic")
prob_origin_imported = calculate_prob("Origin", "Imported")

print(f"\nP(Color='Red'): {prob_color_red}")
print(f"P(Color='Yellow'): {prob_color_yellow}")
print(f"P(Type='Sports'): {prob_type_sports}")
print(f"P(Type='SUV'): {prob_type_suv}")
print(f"P(Origin='Domestic'): {prob_origin_domestic}")
print(f"P(Origin='Imported'): {prob_origin_imported}")

# Function to calculate conditional probability
def calculate_conditional_prob(attribute, value, outcome):
    count_outcome = sum(1 for row in data if row["Stolen"] == outcome)
    return sum(1 for row in data if row[attribute] == value and row["Stolen"] == outcome) / count_outcome

# Calculate and print conditional probabilities
prob_red_given_yes = calculate_conditional_prob("Color", "Red", "Yes")
prob_red_given_no = calculate_conditional_prob("Color", "Red", "No")
prob_suv_given_yes = calculate_conditional_prob("Type", "SUV", "Yes")
prob_suv_given_no = calculate_conditional_prob("Type", "SUV", "No")
prob_domestic_given_yes = calculate_conditional_prob("Origin", "Domestic", "Yes")
prob_domestic_given_no = calculate_conditional_prob("Origin", "Domestic", "No")

print(f"\nP(Color='Red'|Stolen='Yes'): {prob_red_given_yes}")
print(f"P(Color='Red'|Stolen='No'): {prob_red_given_no}")
print(f"P(Type='SUV'|Stolen='Yes'): {prob_suv_given_yes}")
print(f"P(Type='SUV'|Stolen='No'): {prob_suv_given_no}")
print(f"P(Origin='Domestic'|Stolen='Yes'): {prob_domestic_given_yes}")
print(f"P(Origin='Domestic'|Stolen='No'): {prob_domestic_given_no}")

# Classify a new tuple using Bayes' theorem
def classify_bayes(color, type_, origin):
    p_x_given_yes = prob_red_given_yes * prob_suv_given_yes * prob_domestic_given_yes * prob_yes
    p_x_given_no = prob_red_given_no * prob_suv_given_no * prob_domestic_given_no * prob_no

    # Print the formulas
    print(f"\nP(X|Yes) = P(Color='Red'|Yes) * P(Type='SUV'|Yes) * P(Origin='Domestic'|Yes) * P(Yes)")
    print(f"P(X|Yes) = {prob_red_given_yes} * {prob_suv_given_yes} * {prob_domestic_given_yes} * {prob_yes} = {p_x_given_yes}\n")

    print(f"P(X|No) = P(Color='Red'|No) * P(Type='SUV'|No) * P(Origin='Domestic'|No) * P(No)")
    print(f"P(X|No) = {prob_red_given_no} * {prob_suv_given_no} * {prob_domestic_given_no} * {prob_no} = {p_x_given_no}\n")

    if p_x_given_yes > p_x_given_no:
        print("\nP(X|Yes) > P(X|No)")
        return "Yes"
    else:
        print("\nP(X|Yes) < P(X|No)")
        return "No"

# Classify new tuple (Color='Red', Type='SUV', Origin='Domestic')
new_tuple_class = classify_bayes("Red", "SUV", "Domestic")
print(f"\nNew tuple classified as: {new_tuple_class}")
