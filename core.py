class Program:
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def add_likes(self):
        self._likes += 1

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self.nome = new_name.title()

    def __str__(self):
        
        return f'Title -> {self._name}\nYear -> {self.year}\nLikes -> {self._likes}'

    def line_break():
        print('\n#############################################################################################\n')
       



class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'Title -> {self._name}\nYear -> {self.year}\nDuration -> {self.duration} Min\nLikes -> {self._likes}'
        

   


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons


    def __str__(self):
        return f'Title -> {self._name}\nYear -> {self.year}\nSeasons -> {self.seasons}\nLikes -> {self._likes}'
        

class Playlist(list):
    def __init__(self, name, index):
        self.name = name
        self.index = index

    @property   
    def listing(self):
        return self.index
    
    @property
    def size(self):
        return len(self.index)








    





