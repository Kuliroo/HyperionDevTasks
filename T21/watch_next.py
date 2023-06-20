import spacy  # importing spacy
nlp = spacy.load("en_core_web_md") # specifying the model we want to use. 

movies = open(r"E:\Dropbox\Dropbox\JW23010007376\Data Science (Fundamentals)\T21\movies.txt") # put in the directory of TXT file with movie description

# Title and description of the last movie an user watched
last_movie = 'Planet Hulk: Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.'

# Function which recommends most similar movie to the last watched based on short description
def recommendation_engine(x):
    movie_list = []
    title_list = []
    model_movie = nlp(x)
    for movie in movies:
        similarity = nlp(movie).similarity(model_movie)
        movie_list.append(similarity)
        title_list.append(movie[:8])
    best_match = max(movie_list)
    best_match_index = movie_list.index(best_match)
    print("The best possible movie to watch after your last movie is: " + title_list[best_match_index])

recommendation_engine(last_movie)