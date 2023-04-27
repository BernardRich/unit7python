message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis et euismond nisl. Nulla facilisi. Aliquam euismod lectus ac ipsum cursus, vel aliquam elit semper. Nullam elementum massa quis quam "

words = message.lower().replace(".","").replace(",","").split(" ")

#dictionary = capture the key/ value pair

wordcount = {
    'lorem': '1',
    'ipsum': '2',
    'dolor': '1',
    'sit': '1',
    'amet':'1',
    'consectetur':'1',
    'adipiscing':'1',
    'elit': '2',
    'duis':'1',
    'et':'1',
    'euismond':'2',
    'nisl':'1',
    'nulla':'1',
    'facilisi':'1',
    'aliquam':'2',
    'lectus':'1',
    'ac':'1',
    'cursus':'1',
    'vel':'1',
    'semper':'1',
    'nullam':'1',
    'elementum':'1',
    'massa':'1',
    'quis':'1',
    'quam':'1'    
}
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] +=1
    else:
        word_count[word] = 1

userInput = input('enter a word: ')

if userInput in word_count:
    print(f"the word '{userInput}' occurred {word_count[userInput]} times.")
else:
    print(f"the word'{userInput}'did not occur.")
    