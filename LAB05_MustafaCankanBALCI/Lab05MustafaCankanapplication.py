import Lab05MustafaCankanmodule as mv

file_movies = open('movie_data.csv',"r")
hs_movies = mv.load_movies(file_movies)


while True:
    enter_year = int(input("Enter year to search: "))
    list_ret_y = mv.get_movies_by_year(hs_movies,enter_year)
    if list_ret_y != []:
        print("Movies made in ",enter_year," :")
        mv.print_list(list_ret_y)
    else:
        print("No movies from",enter_year,"found")
    print()
    enter_value = input("Enter keyword to search: ")
    list_ret_k = mv.get_movies_by_keyword(hs_movies,enter_value)
    if list_ret_k != []:
        mv.print_list(list_ret_k)
    else:
        print('No movies with the "',enter_value,'" found')
    print()
    
    

file_movies.close()
