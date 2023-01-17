character=input("Enter the Alphabets : ")

vowel=['a','e','i','o','u','A','E','I','O','U']

if character in vowel:
    print("The Alphabet '{}' is Vowel".format(character))
elif(character == 'y' or character=='Y'):
    print("Sometimes letter y stand for vowel,Sometimes stand for consonant.")
else:
    print("The Alphabet '{}' is Consonant".format(character))
    
