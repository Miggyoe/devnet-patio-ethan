"""
Midterm Practical Exam — Pet Adoption Records Manager
Student: Ethan Miguel P. Patio
"""

pets = []  # starts empty — the user adds pets as the program runs

def display_menu():
    print("""
=== Pet Adoption  ===
1. Add a pet
2. View all pets
3. Count available vs adopted
4. Find a pet by name
5. Exit
    """)
    choice = int(input("Choose an option: "))
    return choice


def add_pet():
    # ask for name, animal type, status — build the string, add to the list
    pet_name = input("Pet name: ")
    animal_type = input("Animal type: ")
    pet_status = input("Status: ")
    pet_list.append(pets)
    

def view_pets(pet_list):
    # loop through and print every pet — handle empty list
    i = 0
    while i < len(pets):
        print(pets[i])
        i = i + 1

def count_available_adopted(pet_list):
    # loop through, count Available vs Adopted, return both
    pass

def find_pet(pet_list):
    # ask for a name, search the list, print result or "not found"
    pass

# BONUS (optional)
def remove_pet(pet_list):
    # your code here
    pass

def main():
    running = True
    while running:
        choice = display_menu()
        # use if/elif to call the right function based on choice
        if choice == 1:
            add_pet()

        elif choice == 2:
            view_pets()

        elif choice == 3:
            count_available_adopted()

        elif choice == 4:
            find_pet()

        elif choice == 5:
            print("Goodbye!")
            running = False

        else:
            print("Invalid")
        # set running = False when the user picks Exit


main()