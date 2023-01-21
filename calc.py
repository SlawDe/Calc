
num1 = float(input("Liczba 1 : "))
num2 = float(input("Liczba 2 : "))

operation = input("Wybierz operację: \n"
             "1. Dodawanie\n"
             "2. Odejmowanie\n"
             "3. Mnożenie\n"
             "4. Dzielenie\n")

if operation == "1":
    print("Wynik: ", num1 + num2)
elif operation =="2":
    print("Wynik: ", num1 - num2)
elif operation =="3":
    print("Wynik: ", num1 * num2)
elif operation =="4":
    print("Wynik: ", num1 / num2)
    
