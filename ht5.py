class Human:
    def __init__(self, name, sex, year_of_birth):
        self.name = name
        self.sex = sex
        self.born = year_of_birth
        self.age = int(time.ctime()[-4:]) - year_of_birth

class Movie(Human):
    def __init__(self, name, director, year,
               country, duration, age_rating):
        self.name = name
        self.director = director
        self.year = year
        self.country = country
        self.duration = duration
        self.age_rating = age_rating
    def give_critics(self, comment, rate):
        self.comment = comment
        self.rate = rate
    def is_allowed(self,man):
        return man.age >= self.age_rating
    
class Cartoon(Movie):
    technique = None
    series = False
    n_of_episodes = None
    def __init__(self,name, director, year, country,
                duration, age_rating):
        super().__init__(name, director, year,
               country, duration, age_rating)

class Anime(Cartoon):
    def __init__(self, name, director, year,
               duration, age_rating, author):
        super().__init__(name, director, year, "Japan",
                       duration, age_rating)
        self.author = author
    def JoJo(self, scene):
        if self.name == "JoJo Bizzare Adventures":
            if scene == "Ho-ho":
                print("Dio: Oh? \n You`re approaching me?\n Instead of running away you`re coming right to me?")
                print("Jotaro: I can't beat the shit out of you  without getting closer.")
                print("Dio: Oh ho! Then come as close as you like.")
            if scene == "leru":
                print("LERU LERU LERU LERU LERU LERU LERU LERU LERU LERU LERU LERU LERU LERU LERU")
    def Naruto(self):
        if self.name[:6] == "Naruto":
            print("SASUKEEE!")
