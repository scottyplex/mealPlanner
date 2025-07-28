import random

# Updated dictionary with Premier Protein Shake
meat_protein_content = {
    "Grilled Chicken": {'protein_per_unit': 6, 'unit': 'oz'},
    "Ground Turkey": {'protein_per_unit': 5, 'unit': 'oz'},
    "Ground Beef": {'protein_per_unit': 20, 'unit': '1/4 lb burger'},  # Assuming 20g of protein per 1/4 lb burger
    "Wild Caught Shrimp": {'protein_per_unit': 4, 'unit': 'oz'},
    "Atlantic Salmon": {'protein_per_unit': 6.5, 'unit': 'oz'},
    "Sirloin Steak": {'protein_per_unit': 5.5, 'unit': 'oz'},
    "Non-Fat Greek Yogurt": {'protein_per_unit': 23, 'unit': 'tablespoon'},
    "Whole Eggs": {'protein_per_unit': 6, 'unit': 'egg'},
    "Peanut Butter": {'protein_per_unit': 3.5, 'unit': 'tablespoon', 'max': 2},
    "Shredded Cheese": {'protein_per_unit': 7, 'unit': 'oz'},
    "Bacon": {'protein_per_unit': 3, 'unit': 'slice', 'max': 4},
    "Premier Protein Shake": {'protein_per_unit': 30, 'unit': 'shake', 'max': 1},
    
    "Can of Tuna": {'protein_per_unit': '20', 'unit': 'can', 'max': 1}
}

# Sample meal templates
meal_recipes = {
    "Breakfast": [
        ["Whole Eggs", "Shredded Cheese", "Bacon"],
        ["Non-Fat Greek Yogurt"],
    ],
    "Lunch": [
        ["Ground Beef", "Shredded Cheese", "Bacon"],  # Example burger meal with a cap on bacon
        ["Atlantic Salmon", "Wild Caught Shrimp"]
    ],
    "Dinner": [
        ["Sirloin Steak", "Ground Beef"],  # Example steak and burger meal
        ["Ground Turkey", "Bacon", "Atlantic Salmon", "Wild Caught Shrimp"]
    ],
    "Snacks": [
        ["Premier Protein Shake", "Peanut Butter"]
    ]
}

def calculate_meat_amount(partial_protein_goal, protein_info):
    amount = partial_protein_goal / protein_info['protein_per_unit']
    if 'max' in protein_info and amount > protein_info['max']:
        amount = protein_info['max']
    return amount

def generate_meal_plan(protein_goal, available_proteins):
    meals = ['Breakfast', 'Lunch', 'Dinner', 'Snacks']
    meal_plan = {}
    remaining_protein = protein_goal

    for meal in meals:
        selected_recipe = random.choice(meal_recipes[meal])
        selected_proteins = [item for item in selected_recipe if item in available_proteins]

        meal_plan[meal] = []
        num_items = len(selected_proteins)
        partial_goal = remaining_protein / (len(meals) - meals.index(meal))

        for protein_source in selected_proteins:
            protein_info = meat_protein_content[protein_source]
            amount = calculate_meat_amount(partial_goal / num_items, protein_info)
            formatted_amount = f"{amount:.2f} {protein_info['unit']} of {protein_source}"
            meal_plan[meal].append(formatted_amount)
            remaining_protein -= amount * protein_info['protein_per_unit']

    return meal_plan

def main():
    protein_goal = 250  # grams
    print("Welcome to the Carnivore Diet Meal Planner!")
    print(f"Your daily protein goal is {protein_goal} grams.\n")

    disliked_proteins = input("Enter any proteins you don't like, separated by commas (leave blank if none): ")
    disliked_proteins = [item.strip() for item in disliked_proteins.split(",") if item.strip() in meat_protein_content]
    available_proteins = [p for p in meat_protein_content if p not in disliked_proteins]

    if not available_proteins:
        print("No proteins available for planning. Please check your dislikes list.")
        return

    meal_plan = generate_meal_plan(protein_goal, available_proteins)
    for meal, items in meal_plan.items():
        print(f"{meal}:")
        for item in items:
            print(f"  - {item}")
        print()  # Blank line for better readability

if __name__ == "__main__":
    main()
