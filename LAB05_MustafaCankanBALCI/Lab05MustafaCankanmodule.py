def load_movies(file_movies):
    """
    The storing the movies by their years from csv file

    Parameters:
    file_movies (func):file pointer 

    returns
    dictionary: return hs

    """
    hs = {}
    
    for line in file_movies:
        list_file_movies = line.split(",")
        movie_year = int(list_file_movies[0])
        movie = list_file_movies[1][:-1]
        if movie_year in hs:
            hs[movie_year].append(movie)
        else:
            hs[movie_year] = [movie]
    return hs

def get_movies_by_year(hs_movie, year):
    """
    Showing the movies that released that year 

    Parameters:
    hs_movie (dic): information about movies
    year (int): The year that movie released 

    returns:
    list: return 

    """
    if year in hs_movie:
        return hs_movie[year]
    else:
        return []


def get_movies_by_keyword(hs_movie, enter_val):
    """
    Showing the movies that consists of entered word 

    Parameters:
    hs_movie (dic): information about movies
    enter_val (str): Entered keyword

    returns:
    list: return list_tuple

    """
    list_tuple = []
    for year in hs_movie:
        for movie_name in hs_movie[year]:
            search = movie_name.find(enter_val)
            if search != -1:
                list_tuple.append((year, movie_name))
    return list_tuple

def print_list(enter_list):
    """
    Printing elements in the list

    Parameters:
    enter_list (list): given list

    Returns:
        return None

    """
    for i in enter_list:
        print(i)
