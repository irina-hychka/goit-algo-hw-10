import pulp

# Create the optimization model for maximizing production
model = pulp.LpProblem("Beverage_Production_Optimization", pulp.LpMaximize)

# Define decision variables (non-negative integers)
lemonade_units = pulp.LpVariable('Lemonade_Units', lowBound=0, cat='Integer')
fruit_juice_units = pulp.LpVariable('Fruit_Juice_Units', lowBound=0, cat='Integer')

# Objective function: Maximize total number of beverage units produced
model += lemonade_units + fruit_juice_units, "Total_Production"

# Constraints based on available resources
model += 2 * lemonade_units + 1 * fruit_juice_units <= 100, "Water_Constraint"
model += lemonade_units <= 50, "Sugar_Constraint"
model += lemonade_units <= 30, "Lemon_Juice_Constraint"
model += 2 * fruit_juice_units <= 40, "Fruit_Puree_Constraint"

# Solve the model
model.solve()

# Display the results
print("-" * 50)
print("Optimal production plan:")
print(f"Lemonade units to produce: {int(pulp.value(lemonade_units))}")
print(f"Fruit juice units to produce: {int(pulp.value(fruit_juice_units))}")
print("-" * 50)
print(f"Maximum total units produced: {int(pulp.value(model.objective))}")
print(f"Solution status: {pulp.LpStatus[model.status]}")