class Movie:
    def __init__(self, name, year, duration):
        self.name = name
        self.year = year
        self.duration = duration



avengers = Movie('avengers', 2011, 100)


print(f'the movie is caled {avengers.name}, was realese in {avengers.year}, and is {avengers.duration} min long')