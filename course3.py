#List 
fav_movies = ['Joker' , 'Dune', 'Spider Man']

print(fav_movies)

#List Add insert Delete

print(len(fav_movies))
fav_movies.append('Iron Man')
print(fav_movies)
fav_movies.insert(1, 'Batman')
print(fav_movies)
del(fav_movies[2])
print(fav_movies)

#For Loops

for number in range(10):
  print(number)

for movie in fav_movies:
  print(movie)

#Dictionaries

cats = {
  "Jane": 6,
  "Punk":4,
  "Tom":14,
}
cats['Wilson'] = 1
del(cats["Tom"])
print(len(cats))
print(cats)