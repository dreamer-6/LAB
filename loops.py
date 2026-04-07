def num_guess():
    secret_no = 7
    attempt = 0

    while True:
        try:
            guess = int(input("Enter number between 1 to 10: "))
            attempt += 1

            if guess > secret_no:
                print("too high")
            elif guess < secret_no:
                print("too low")
            else:
                print(f"you correct gueed in {attempt} attempts")
                break
        except ValueError:
            print("invalid Input")

num_guess()