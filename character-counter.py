print("Enter a sentence (without punctuation or caps): ")
message = input()
count = {}

for character in message:
  count.setdefault(character,0)
  count[character] += 1
  
alphabet = []
for letter in range(97,123):
    alphabet.append(chr(letter))
for i in alphabet:
  print(i+" appears "+str(count.get(i,0))+" times.")
