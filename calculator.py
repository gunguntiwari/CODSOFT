# Flow: while True ➜ show operators ➜ input numbers ➜ condition se result

while True:
    # 1️⃣  basic maths operators or arthmetic operators
    print("\narthemetic Operators:")
    print(" +  ➜ Addition")
    print(" -  ➜ Subtraction")
    print(" *  ➜ Multiplication")
    print(" /  ➜ Division")

    # 2️⃣  take input from user
    operator = input("Operators choose karo (+  -  *  /): ").strip()

    # 3️⃣  take number input from user whatever he/she or transgenger want to sum
    try:
        num1 = int(input("enter first number: "))
        num2= int(input("enter second number: "))
    except ValueError:
        print("❌ number is wrong once again take input.")
        continue

    # 4️⃣  with the help of if else or we can also say condition statment
    if operator == '+':
        OUTPUT = num1 + num2
    elif operator == '-':
        OUTPUT = num1 - num2
    elif operator == '*':
        OUTPUT = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("❌ cannot divide by zero.")
            continue
        OUTPUT = num1/ num2
    else:
        print("❌ invalid input or operator.")
        continue

    print(f"\nCALC_RESULt: {num1} {operator} {num2} = {OUTPUT}")

    # 5️⃣  you want do it once more or not
    if input("\nyou want to do calculation ? (yes/no): ").lower() != 'yes':
        print("exit  or shutdown calculator THAKYOU! HAVE A GOODD DAY!")
        break



