from CabModule import Sedan , Hatchback

def read_file(f1):
    """
    Converting the information at file to list
    
    
    Parameters:
    f1(str): file name 
    
    
    returns:
    list: return l
    
    
    """
    file_one = open(f1,'r')
    l = []
    for line in file_one:
        l_split = line.split(';')
        if l_split[0] == "Sedan":
            l.append(Sedan(int(l_split[1]),l_split[0],int(l_split[2])))
        elif l_split[0] == "Hatchback":
            l.append(Hatchback(int(l_split[1]),l_split[0],int(l_split[2])))
    return l

def find_greater(l,cab,year):
    """
    Compraing list objects in their years  according to their cab type 
    
    
    Parameters:
    l(list): list of car
    cab(str): type of car
    year(int): year 
    
    returns:
    str: return a
    
    
    """
    counter_year = 0
    temp_km = 0
    for i in l:
        if cab == 'Sedan':
            if i.get_type_of_car() == cab and i > s1:
                counter_year += 1
        elif cab == "Hatchback":
            if i == h1:
                temp_km += i.get_kms()
    if cab == 'Sedan':
        a = f'There are {counter_year} {cab} cars newer than 2015.'
        return a
    else:
        a = f'All {cab} cars of {year}  have travelled {temp_km} kms.'
        return a
    
    
list_cars = read_file("cabs.txt")
counter = 1
for i in range(len(list_cars)):
    if list_cars[i].get_type_of_car() == "Sedan":
        print("Sedan ",counter, "will pay",list_cars[i].calculate_fare(),"TL")
        counter += 1

h1 = Hatchback(10000,'Hatchback',2020)
s1 = Sedan(10000,'Sedan',2015)
print("")
        
print(find_greater(list_cars,"Sedan",2015))

print("")

print(find_greater(list_cars,"Hatchback",2020))
