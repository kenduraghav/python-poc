from datetime import datetime
import textwrap

class Cinema:
    def __init__(self):
        self.movies = []

    def add_movies(self, movie):
        self.movies.append(movie)
    
    def show_all_movies(self):        
        print("Wecolme to Golden Village Cinemas!!!")
        print(textwrap.dedent("""
        Available Movies:
        ==============================
              """).strip())
        for movie in self.movies:
            id = movie.id
            title =  movie.title
            genre = movie.genre
            for showtime in movie.showtimes:
                date = showtime.date
                time = showtime.time
                seats = showtime.total_seats_available
                movie_desc = f"""                   
                        S.No: {id}
                        Title: {title}
                        Genre: {genre}
                        Showtimes:
                        ------------
                        Date: {date}
                        Time slots: {time}
                        Seats Available: {seats}
                        {"==="*10}
                    """
                print(textwrap.dedent(movie_desc).strip())
            

class Movie:
    def __init__(self, id, title, genre, screen_name, showtimes):
        self.id = id
        self.title = title
        self.genre = genre
        self.screen_name = screen_name
        self.showtimes = showtimes
       

   
class Showtimes:
    def __init__ (self, date, time, total_seats_available):
        self.date = date
        self.time = time
        self.total_seats_available = total_seats_available    

    def check_availablity(self):
        if self.total_seats_available > 0:
            return True
        return False

    def book_seats(self, tickets):
        if self.check_availablity() is True:
            self.total_seats_available -= tickets
            return f"{tickets} booked successfully" 
        else: 
            return f"No seats available for the selected date {self.date} and time {self.time}"



class Person:
    def __init__(self, name, phone, email):
        self.name=name
        self.phone=phone
        self.email=email




if __name__ == "__main__":
    cinema = Cinema()
    showtimes = [Showtimes(datetime.now().strftime('%d-%m-%Y'), 
                       ["10:00","13:00", "16:30","20:30"],50)]
    cinema.add_movies(Movie(1,"Inception", "Sci-Fi", "Screen 1", showtimes))
    cinema.add_movies(Movie(2, "Titanic","Romance", "Screen 2", showtimes))
    cinema.add_movies(Movie(3, "Kung Fu Panda","Kids-Comedy", "Screen 3", showtimes))
    cinema.show_all_movies()