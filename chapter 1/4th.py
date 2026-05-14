vowel ="aeiou"
word = "education"
count = 0
for i in word:
    if i in vowel:
        count+=1
print(f"total vowels in {word} is {count}")        