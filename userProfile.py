def display_info(person):
    print(f"Name: {person['name']}")
    print(f"Age: {person['age']}")
    print(f"Country: {person['country']}")
    print("_" * 20)

def get_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if age > 0:
                return age
            else:
                print("Please enter a positive number")
        except ValueError:
            print("Invalid input. Please enter a valid number")

def main():
    name = input("Enter your name: ")
    age = get_age()
    country = input("Enter your country: ")

    personInfo = {"name": name, "age": age, "country": country}

    display_info(personInfo)

    while True:
        more_info = input("Do you want to enter another person? (yes/no): ").strip().lower()
        if more_info == "yes":
            name = input("Enter your name: ")
            age = get_age()
            country = input("Enter your country: ")

            personInfo = {"name": name, "age": age, "country": country}
            display_info(personInfo)
        elif more_info == "no":
            print("Thank for using the program!")
            break
        else:
            print("Please answer 'yes' or 'no' ")

if __name__ == "__main__":
    main()
        