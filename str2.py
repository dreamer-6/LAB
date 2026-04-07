def string():
    print("String Operation")

    s = input("Enter a String: ")

    print("Reversed String: ", s[::-1])

    print("String Length: ", len(s))

    s1 = input("Enter another string: ")

    print("Concatenation: ", s + s1)

    word = input("Enter a word separated by space: ")
    print("Spilt: ", s1.split())

    print("Upper: ",s.upper())
    print("lower: ",s.lower())

    target = input("Enter target letter: ")
    if target in s:
        print("Target is found")
    else:
        print("target not found")

    print("Palindrome Check")

    if s == s[::-1]:
        print(f" {s} is palindrome")
    else:
        print(f" {s} is not palindrome")


string()