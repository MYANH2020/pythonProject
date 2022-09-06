current_movies = {'The Grinch': '11:00 am',
                  'Rudolph':'1:00pm',
                  'Tom and Jerry':'2:00pm' }
print(" we're showing the following movies:")
for key in current_movies:
    print(key)
movie = input('what movie would you like the showtime for?\n')
showtime = current_movies.get(movie)
if showtime == None:
    print("request showtime is not playting")
else:
    print(movie, " is playing at", showtime)
  