
from Workers import Engine


def handle_genre(g):
    genres = ['Action', 'Adventure', 'Animation' 'Comedy', 'Crime',
              'Documentary', 'Drama', 'Family', 'Fantasy', 'History',
              'Horror', 'Music', 'Mystery', 'Romance', 'Science'
              'Thriller', 'War', 'Western']
    for i in range(len(genres)):
        print(i, genres[i])
    choice = input("Enter the index of the genre that you want:\n")
    return choice


def get_search_type():
    search_type = int(input('Enter an option number :\n'
                            '0 Get top-rated movies\n'
                            '1 Get top-rated movies for a genre\n'
                            '2 Get movies similar to a chosen movie\n'))
    return search_type


def num_movies():
    return int(input("How many recommended movies would you like?:\n"))


def handle_input(search_type):
    engine = Engine.Engine()
    if search_type == 0:
        return engine.get_top_movies(num_movies())
    elif search_type == 1:
        chosen = input("Enter the index of the genre that you want:\n")
        return engine.get_top_genre(chosen, num_movies())
    elif search_type == 2:
        chosen = input("Enter a movie title or type 'exit' to quit:  \n")
        return engine.get_content_recommendations(chosen, num_movies())


def get_more_info(recs):
    engine = Engine.Engine()
    quit_words = ['exit', 'close', 'quit', 'no', 'n', 'negative', 'cancel', 'negatory', 'nope', 'escape']
    more = ''
    while more not in quit_words:
        more = input('\nType the title or title index or type "exit":  \n')
        if more in quit_words:
            break
        elif more.isnumeric():
            more = recs.title.values[int(more)]
        if more not in recs.values:
            print("Please enter a value from the list of choices.")
        else:
            print(engine.find_summary(more))
        print()