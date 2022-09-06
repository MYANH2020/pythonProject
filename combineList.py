menu={'Breakfast': ['Eggs', 'Bagel', ' Coffee'], 
      'Lunch': ['BLT', 'Turkey Sandwich', 'Beefsteak'], 
     'Dinner': ['Soup', 'Salad', 'Taco']}
for name, menu in menu.items():
    print(name, ':',menu)
name1 ={'Anh Huynh': [' data engineering'], 
            'Anna':[' Contact Center'], 
            'Peter': ['DevOps']}
for fullName, department in name1.items():
    print(fullName, ":", department)
person = { 'fName': ['Anna Lee'],
          'Occupation':['Doctor'],
          'Gender':['Female']}
print(person.get('fName'), " is ", person.get('Gender'), "and a", person.get('Occupation'))
