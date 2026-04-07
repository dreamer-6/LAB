def armstrong_num(num, power):
    if num == 0:
        return 0
    else:
        return (num % 10) ** power + armstrong_num(num // 10, power)

number = int(input("enter a number to check: "))

power = len(str(number))

if number == armstrong_num(number, power):
    print(f"{number} is armstrong number")

else:
    print(f"{number} is not an armstrong number")