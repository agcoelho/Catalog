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
       



class Movie(Program):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration
        

   


class Series(Program):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons
        



    





