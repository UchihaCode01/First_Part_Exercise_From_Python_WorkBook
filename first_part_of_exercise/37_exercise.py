
letter = str.lower(input("Enter your letter : "))

if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
    print(f"Your letter '{letter}' is vowel")
elif letter == "y":
    print(f"Your letter '{letter}' can be vowel and consonant")
else:
    print(f"Your letter '{letter}' is consonant")
