import webbrowser
import fresh_tomatoes

class Movies():
    
    """this is the definition of Class Movies. it takes parameters title,
    storyline, poster image and trailer link of a movie. also a method 
    'show_trailer is defined that shows the trailer of the movie"""
    
    def __init__(self,movie_title,movie_storyline, poster_image,trailer_youtube):
        
        self.title=movie_title
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
        self.storyline=movie_storyline
        
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
    
"""Now here we are creating different instances of the movies 
that will hold data of different movies"""

  
social_network= Movies(" The Social Network", " This is the story of the Marks Jukarbergs and the facebook",
"https://upload.wikimedia.org/wikipedia/en/thumb/7/7a/Social_network_film_poster.jpg/220px-Social_network_film_poster.jpg"
,"https://www.youtube.com/watch?v=2RB3edZyeYw")

pirates_of_siliconvalley= Movies("Pirates of Silicon Valley", "The story of the evolution of the microsoft and Apple",
"https://upload.wikimedia.org/wikipedia/en/3/30/Movieposterposv.jpg", "https://www.youtube.com/watch?v=xZGVgSw4Pho" )

jobs=Movies("Jobs", "The life story of steve Jobs","https://upload.wikimedia.org/wikipedia/en/e/e0/Jobs_%28film%29.jpg",
"https://www.youtube.com/watch?v=FrvkCS0ZGPU" )  
   
artificial_intelligence= Movies("A. I. Artificial Intelligence", " the story of the artificial evaluation over the time",
"https://upload.wikimedia.org/wikipedia/en/e/e6/AI_Poster.jpg","https://www.youtube.com/watch?v=kYr8RwDGfe8")

algorithms= Movies("Algorithm", "Algorithm is a 2014 crime and thriller movie",
"https://images-na.ssl-images-amazon.com/images/M/MV5BOGEzMjhmOGMtMDEyNC00MzRhLWIzMjctZjkwOTMzMWIwNzdhXkEyXkFqcGdeQXVyNjU5MTkwMTc@._V1_QL50_.jpg",
"https://www.youtube.com/watch?v=QzOIf4QA0tM")

imitation_game= Movies("The Imitation Game", "The story of Alan Turing",
"https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/The_Imitation_Game_poster.jpg/250px-The_Imitation_Game_poster.jpg", 
"https://www.youtube.com/watch?v=S5CjKEFb-sM") 


""" Here we are creating list of the different movie 
object by naming it movie_collection!"""
   
movies_collection=[social_network,pirates_of_siliconvalley,jobs,
                  artificial_intelligence,algorithms, imitation_game]


""" the code below is accessing the fuction'open_movies_page' defined in python
file fresh_tomatoes. fresh_tomatoes.py takes list of movies as input and outputs 
a website show poster of all movies having links to their trailers """
  
fresh_tomatoes.open_movies_page(movies_collection)
