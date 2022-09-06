#empty list
empty = []
# list of string
acronyms = ['dog', 'cat', 'fish']
#list of numbers
numbers= [99, 200, 500]
# list of mixed items
anything = [200, 'moon', 'sun']
#list of lists
#lists = [['moon', 'cat'], ['laptop', 'mouse']]
#acronyms =['LOL', 'IDK','TBH','LOL']
#firstItem = acronyms[0]
acronyms =[]
acronyms.append('LOL')
acronyms.append('IDK')
acronyms.append('NATO')
print(acronyms)
del acronyms[1]
print(acronyms)
acronyms.remove('LOL')
print(acronyms)
acronyms1=['LOL','IDK', 'NATO', 'APEC']
word = 'YOLO'
if word in acronyms1:
    print(word + ' is in the list \n')
else:
    print(word +' is not in the list\n')
for acronym in acronyms1:
    print(acronym)