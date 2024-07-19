from core import Movie, Series, Program

avengers = Movie('avengers - endgame', 2011, 100)
tua = Series('The umbrella academy', 2016, 3)

avengers.add_likes()
avengers.add_likes()
avengers.add_likes()
avengers.add_likes()
tua.add_likes()

movies_series = [avengers, tua]

for program in movies_series:
    Program.line_break()
    print(program)
    Program.line_break()