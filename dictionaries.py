acronyms = {'LOL':'laught out loud', 
            'IDK':" I don't know", 
            'TBH':'To be honest' }
print(acronyms['LOL'])
acronyms['TBH']= 'honestly'
print(acronyms)
acronyms['YOLO']= ' You only live one'
print(acronyms)
definition =acronyms.get('NATO')
print(definition)
if definition:
    print(definition)
else:
    print(" Key does not exist")
    acronyms1={'LOL': 'laught out loud', 'IDK': "I don't know", 'TBH': 'honestly'}
    sentences = 'IDK'+ ' what happened '+'TBH'
    translation = acronyms1.get('IDK')+' what happended '+ acronyms1.get('TBH')
    print("sentence:", sentences)
    print(" translation:",translation)