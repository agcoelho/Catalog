from core import Movie, Series

avengers = Movie('avengers - endgame', 2011, 100)
tua = Series('The umbrella academy', 2016, 3)

avengers.add_likes()
avengers.add_likes()
avengers.add_likes()
avengers.add_likes()
tua.add_likes()



print(f'The movie is caled {avengers.name}, was realese in {avengers.year}, and is {avengers.duration} min long\nLikes - {avengers.likes}')

print('#############################################################################################')

print(f'The Series is caled {tua.name}, was realese in {tua.year}, and have {tua.seasons} seasons.\nLikes - {tua.likes}')


movies_series = [avengers, tua]

for program in movies_series:
    print(f'Title -> {program.name}\nYear -> {program.year}\nLikes -> {program.likes}\n') 