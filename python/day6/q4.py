#Word Frequency- Input:"apple banana apple orange banana apple"
#Create a dictionary containing the frequency of each word.
#Expected concept: apple → 3, banana → 2, orange → 1. Don't use Counter yet.

text="apple banana apple orange banana apple"
words=text.split()
word_count={}
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
print(word_count)