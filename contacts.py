from operator import contains


contacts ={
    "numbers": 4,
    "students":
    [
        {" name":" Jane Lee", "email": "jlee@mail.com"},
        {" name":" Peter Johns", "email": "peterj@mail.com"}, 
        {" name":" Meo Han", "email": "meoh@mail.com"}, 
        {" name":" Moon Cheese", "email": "moonc@mail.com"} 
    ]
}
for student in contacts["students"]:
    print(student["email"])