l = input("Input a letter of the alphabet: ")
#Checking the condition for vowel
if l in ('a','e','i','o','u'):
    print('alphabet is a vowel' , l)
elif l == 'y':
    print('Sometimes letter y stand for vowel, sometimes stand for consonant.')
#If nothing is there then this will we consonant 
else:
    print('alphabet is a consonant.' , l)

