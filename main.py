
from generate import multiplications

print()
print("🔍 Welcome to the multiplications generator 🥸")

def about():
    print("Random multiplications generator")
    print("Versión: 1.0")
    print("Autor: Maria Jose Arcila Cano")

selection = ""
while selection != "0":
    print()
    print("      🔢         ✖️         🔢      ")
    print()
    print("👇 Choose an option:")
    print("1. 🫠 Generate random multiplications")
    print("2. ❓ About")
    print("0. 🏃‍♂️‍➡️ Exit")
    selection = input("=> ")
    print()

    match selection:
        case "1":
            multiplications()
        case "2":
            about()
        case "0":
            print("Until next time 👋")
            print()
        case _:
            print("Invalid option ❌")


