#Problem 5 — Create: def analyze_string(text): The function should return:
# Number of characters Number of vowels Number of consonants
#For: "Python" Expected: Characters: 6 Vowels: 1 Consonants: 5

def analyze_string(text):
    charecter=len(text)
    vowel =0 
    consonent=0

    for ch in text:
        if ch.lower() in "aeiou":
            vowel+=1
        elif ch.isalpha():
            consonent+= 1
    return charecter, vowel, consonent

result= analyze_string("Python")
print("Characters =",result[0])
print("Vowels =",result[1])
print("Consonent =",result[2])

