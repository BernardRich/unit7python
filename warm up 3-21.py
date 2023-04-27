

#-a_list = ['apple','orange', 'pear', 'strawberry', 'grape']
#print(len(a_list))
#print(list(range(o,len(a_list))))

#for i in range():
    #print(i)

def volwelstras(): 
    word = input('please enter a word: ')

    vowels = 'aeiou'

    removed = ['h']

for letters in word:
    if letters in vowels:
        removed.append(letters)

print(removed)