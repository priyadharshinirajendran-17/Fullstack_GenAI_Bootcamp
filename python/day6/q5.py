#Q5 — Character Frequency-Input: "programming"
#Create a frequency dictionary.Don't use: Counter()
text="programming"
frequency={}
for char in text:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
print(frequency)