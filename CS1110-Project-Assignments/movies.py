# PA07: Movies
# Carson Crenshaw (cgc8gdt)

# Helper Functions (Functions 1-4)
def get_name(movie):
    """
    :param movie: A list that contains the movie’s corresponding values in the following order: [movie name, gross earning, year, rating out of 10, number of ratings].
    :return: The name of the movie in the provided list.
    """
    return movie[0]

def get_gross(movie):
    """
    :param movie: A list that contains the movie’s corresponding values in the following order: [movie name, gross earning, year, rating out of 10, number of ratings].
    :return: The gross earnings in the provided list.
    """
    return movie[1]

def get_rating(movie):
    """
    :param movie: A list that contains the movie’s corresponding values in the following order: [movie name, gross earning, year, rating out of 10, number of ratings].
    :return: The rating in the provided list.
    """
    return movie[3]

def get_num_ratings(movie):
    """
    :param movie: A list that contains the movie’s corresponding values in the following order: [movie name, gross earning, year, rating out of 10, number of ratings].
    :return: The number of ratings in the provided list.
    """
    return movie[4]

# Higher Rating Function (Function 5)
def better_movies(movie_name, movies_list):
    """
    :param movie_name: A string whose value is corresponding to a movie_name in movies_list.
    :param movies_list: A list of lists, where the lists inside the larger list contain a movie’s information in the following order: [movie name, gross earning, year, rating out of 10, number of ratings].
    :return: A list of all movies’ information that have a higher rating than that of movie_name.
    """
    for sub_list in movies_list:
        if movie_name in sub_list:
            observedmovierate = get_rating(sub_list)
            new_list = []
            for sub_list in movies_list:
                rates = get_rating(sub_list)
                if rates > observedmovierate:
                    new_list.append(sub_list)
            return new_list

# Average Value Function (Function 6)
def average(category, movies_list):
    """
    :param category: A string whose value will either be “rating”, “gross’, or ”number of ratings."
    :param movies_list: A list of lists, where the lists inside the larger list contain a movie’s information in the following order: [movie name, gross earning, year, rating out of 10, number of ratings].
    :return: The average for all movies based on the provided category.
    """
    if category == "rating":
        rating_list = []
        for sub_list in movies_list:
            ratings = get_rating(sub_list)
            rating_list.append(ratings)
        return sum(rating_list)/len(rating_list)
    if category == "gross":
        gross_list = []
        for sub_list in movies_list:
            grossnumber = get_gross(sub_list)
            gross_list.append(grossnumber)
        return sum(gross_list)/len(gross_list)
    if category == "number of ratings":
        ratingsnumb_list = []
        for sub_list in movies_list:
            ratingsnumber = get_num_ratings(sub_list)
            ratingsnumb_list.append(ratingsnumber)
        return sum(ratingsnumb_list) / len(ratingsnumb_list)





