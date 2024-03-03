class Hours:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def __str__(self) -> str:
        return '''start time{}-end time{}'''.format(self.start_time,self.end_time)
        

class Movie:
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        self.name = name
        self.director = director
        self.year = year
        self.genre = genre
        self.duration = duration
        self.imdb = imdb
        self.hours = list(hours)
        self.price = price

    
    def show_info(self):
        hours=[]
        for i in self.hours:
            dict ={
                'start_time':i.start_time,
                'end_time':i.end_time
            }
            hours.append(dict)
        print(hours)
        

        return '''
        Film Name : {}
        ---------
        Film Director : {}
        ---------
        Film Year : {}
        ---------
        Film genre : {}
        ---------
        Film duration : {}
        ---------
        Film imdb : {}
        ---------
        Film price : {}
        ---------
        Film seance : {}
        '''.format(self.name,self.director,self.year,self.genre,self.duration,self.imdb,self.price,hours)
    

    def year_info(self):
        if int(self.year) < 2000:
            print("Category: Old")
        else:
            print("Category: New")


    def duration_info(self):
        if self.duration < 120:
            print("Category: Short movie")
        else:
            print("Category: Long movie")
            

    def rating_info(self):
        if self.imdb < 6:
            print("E")
        elif 6<=self.imdb < 7:
            print("D")
        elif 7<=self.imdb < 8:
            print("C")
        elif 8<=self.imdb < 9:
            print("B")
        elif 9<=self.imdb < 10:
            print("A")
        else:
            print("Not found!")



class Lucy(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)  

class Artificial_intellegence(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)

class Me_before_you(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)

class Forest_gump(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)
    
class The_Green_Mile(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)

class Forsaj_9(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)

class Godfather(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)

class Fight_club(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)

class Inception(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)

class Matrix(Movie):
    def __init__(self, name, director, year, genre, duration, imdb, hours, price):
        super().__init__(name, director, year, genre, duration, imdb, hours, price)