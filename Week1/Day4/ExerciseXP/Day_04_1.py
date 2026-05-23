# Exercise 1 : Dog Class

from dog import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight, ):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
       print(self.bark())
       self.trained = True


    def play(self, *args):
        dog_names = [self.name ]
        for dog in args:
            dog_names.append(dog.name)
        print(f" {', '.join(dog_names)} are playing together!")


    def do_a_trick(self):
        if self.trained:
            tricks = [
                " does a barrel roll!",
                " stands on his back legs!",
                " shakes your hand!",
                " plays dead!"
            ]
            print(f"{self.name} {random.choice(tricks)}")


# Create 3 dogs
dog1 = PetDog("Rex", 5, 20)
dog2 = PetDog("Buddy", 3, 15)       
dog3 = PetDog("Max", 4, 25)

# Train dog1
dog1.train()

# Make the dogs play together
dog1.play(dog2, dog3)





# EXERCISE  4

# Practice working with classes and interactions by modeling a family and its members.

class Person:

    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""

    def is_18(self):
        return self.age >= 18


class Family:

    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []

    def born(self, first_name, age):

        person = Person(first_name, age)

        person.last_name = self.last_name

        self.members.append(person)

    def check_majority(self, first_name):

        for member in self.members:

            if member.first_name == first_name:

                if member.is_18():

                    print("You are over 18, your parents Jane and John accept that you will go out with your friends")

                else:

                    print("Sorry, you are not allowed to go out with your friends.")

    def family_presentation(self):

        print(f"Famille : {self.last_name}")

        for member in self.members:
            print(f"{member.first_name} - {member.age} years old")


# Création de la famille
family = Family("NDAH")


# Ajout des membres
family.born("Stephane", 22)
family.born("Sarah", 15)
family.born("Kevin", 10)


# Vérification majorité
family.check_majority("Stephane")

family.check_majority("Sarah")


# Présentation
family.family_presentation()









# EXERCISE XP GOLD

class BankAccount:
    def __init__(self, username, password, balance=0):
        self.username = username
        self.password = password
        self.balance = balance
        self.authenticated = False

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            return True
        return False

    def deposit(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to deposit money.")
        if not isinstance(amount, int) or amount <= 0:
            raise Exception("Deposit amount must be a positive integer.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to withdraw money.")
        if not isinstance(amount, int) or amount <= 0:
            raise Exception("Withdraw amount must be a positive integer.")
        self.balance -= amount
        return self.balance


class MinimumBalanceAccount(BankAccount):
    def __init__(self, username, password, balance=0, minimum_balance=0):
        super().__init__(username, password, balance)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must be authenticated to withdraw money.")
        if not isinstance(amount, int) or amount <= 0:
            raise Exception("Withdraw amount must be a positive integer.")
        if self.balance - amount < self.minimum_balance:
            raise Exception(
                f"Withdrawal denied: balance cannot drop below the minimum ({self.minimum_balance})."
            )
        self.balance -= amount
        return self.balance


class ATM:
    def __init__(self, account_list, try_limit):
        if not isinstance(account_list, list) or not all(
            isinstance(account, BankAccount) for account in account_list
        ):
            raise Exception("account_list must be a list of BankAccount instances.")
        self.account_list = account_list

        try:
            if not isinstance(try_limit, int) or try_limit <= 0:
                raise Exception("try_limit must be a positive integer.")
            self.try_limit = try_limit
        except Exception as e:
            print(f"Invalid try_limit ({e}). Falling back to default value 2.")
            self.try_limit = 2

        self.current_tries = 0
        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\n===== MAIN MENU =====")
            print("1. Log in")
            print("2. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                self.log_in(username, password)
            elif choice == "2":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

    def log_in(self, username, password):
        for account in self.account_list:
            if account.authenticate(username, password):
                print(f"Welcome, {account.username}!")
                self.current_tries = 0
                self.show_account_menu(account)
                return

        self.current_tries += 1
        remaining = self.try_limit - self.current_tries
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Shutting down.")
            exit()
        else:
            print(f"Invalid credentials. {remaining} attempt(s) remaining.")
            new_username = input("Username: ").strip()
            new_password = input("Password: ").strip()
            self.log_in(new_username, new_password)

    def show_account_menu(self, account):
        if not isinstance(account, BankAccount):
            raise Exception("show_account_menu requires a BankAccount instance.")

        while True:
            print(f"\n===== ACCOUNT MENU ({account.username}) =====")
            print(f"Current balance: {account.balance}")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Choose an option: ").strip()

            if choice == "1":
                try:
                    amount = int(input("Amount to deposit: ").strip())
                    account.deposit(amount)
                    print(f"Deposit successful. New balance: {account.balance}")
                except ValueError:
                    print("Please enter a valid integer.")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "2":
                try:
                    amount = int(input("Amount to withdraw: ").strip())
                    account.withdraw(amount)
                    print(f"Withdrawal successful. New balance: {account.balance}")
                except ValueError:
                    print("Please enter a valid integer.")
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == "3":
                account.authenticated = False
                print("Logged out.")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    accounts = [
        BankAccount(username="alice", password="1234", balance=500),
        MinimumBalanceAccount(
            username="bob", password="abcd", balance=1000, minimum_balance=100
        ),
    ]
    ATM(account_list=accounts, try_limit=3)