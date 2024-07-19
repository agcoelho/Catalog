from core import Movie, Series, Program, Playlist

boys = Series('the boys', 2019, 4)
modern = Series('modern family', 2018, 6)
tua = Series('The umbrella academy', 2016, 3)
got = Series('game of thrones', 2015, 4)
gf = Series('gravity falls', 2013, 3)
orphan = Movie('orfan', 2009, 120)
scream =Movie('scream 4', 2021, 110)
poor = Movie('poor creatures', 2023, 130)
spider = Movie('spiderman - across the spiderverse', 2023, 123)
avengers = Movie('avengers - endgame', 2011, 100)



avengers.add_likes()
avengers.add_likes()
avengers.add_likes()
avengers.add_likes()
tua.add_likes()

movies_series = [avengers, orphan, scream, poor, spider, tua, boys, modern, got, gf]
weekend_playlist = Playlist('weekend', movies_series)

for program in weekend_playlist:
    Program.line_break()
    print(program)
    Program.line_break()


print(f'playlist size is: {len(weekend_playlist)}')
Program.line_break()