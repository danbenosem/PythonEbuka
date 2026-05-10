letter = input("Enter one letter: ").lower()


if len(letter) == 1 and letter.isalpha():
   
    if letter in "aeiou":
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Invalid input")
