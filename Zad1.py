
num1 = int(input("Podaj 1 liczbe: "))
num2 = int(input("Podaj 2 liczbe: "))

print(f"Suma {num1} i {num2} = {num1+num2:1.2f}")

print(f"Odejmowanie {num1} i {num2} = {num1-num2:1.2f}")

print(f"Mnożenie {num1} i {num2} = {num1*num2:1.2f}")

print(f"Dzielenie {num1} i {num2} = {num1/num2:1.2f}")
if num1 > num2:
    print(f"{num1} jest większe od {num2}")
elif num2 > num1:
    print(f"{num1} jest mniejsze od {num2}")
else :
    print(f"{num1} jest równe {num2}")
