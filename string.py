def string_operations():
    print("--- String Operations ---")
    
    s = input("Enter a main string: ")
    
    print("\n1. Reverse String")
    print("Reversed string:", s[::-1])
    
    print("\n2. String Length")
    print("String length:", len(s))
    
    print("\n3. String Concatenation")
    s1 = input("Enter another string to concatenate: ")
    print("Concatenated string:", s + s1)
    
    print("\n4. String Uppercase/Lowercase")
    print("Uppercase:", s.upper())
    print("Lowercase:", s.lower())
    
    print("\n5. String Search")
    target = input("Enter target string to search for: ")
    if target in s:
        print("Target string found!")
    else:
        print("Target string not found.")
        
    print("\n6. String Split")
    words = input("Enter multiple words separated by spaces: ")
    print("Split list:", words.split())
    
    print("\n7. String Join")
    lst = input("Enter words separated by commas: ").split(',')
    # Strips any accidental spaces the user might type after a comma before joining
    clean_lst = [word.strip() for word in lst] 
    print("Joined string:", ' '.join(clean_lst))
    
    print("\n8. Palindrome Check")
    # Converts to lowercase to ensure 'Racecar' is still caught as a palindrome
    if s.lower() == s[::-1].lower():
        print("The main string is a palindrome!")
    else:
        print("The main string is not a palindrome.")

if __name__ == "__main__":
    string_operations()