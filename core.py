class Movie:
    def __init__(self, name, year, duration):
        self.__name = name.title()
        self.year = year
        self.duration = duration
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def add_likes(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.nome = new_name.title()

   


class Series:
    def __init__(self, name, year, seasons):
        self.__name = name.title()
        self.year = year
        self.seasons = seasons
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    def add_likes(self):
        self.__likes += 1

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name):
        self.nome = new_name.title()


    





