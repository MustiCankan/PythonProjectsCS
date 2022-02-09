from Country import Country

def readCountries(file_name,list_country):
    file_country = open(file_name,'r')
    for line in file_country:
        l_split = line.split(',')
        country = l_split[0].strip()
        continent = l_split[1].strip()
        life_m = float(l_split[2])
        life_f = float(l_split[3])
        list_country.append(Country(country,continent,life_m,life_f))
        
def selectionSort(list_country):
    counter = 0
    while counter != len(list_country):
        min_val = counter
        for i in range(counter, len(list_country)):
            if list_country[min_val].getContinent() > list_country[i].getContinent() :
                min_val = i
            elif list_country[min_val].getContinent() == list_country[i].getContinent() and list_country[min_val].getCountry() > list_country[i].getCountry():
                min_val = i
        
        list_country[counter],list_country[min_val] = list_country[min_val],list_country[counter]
        
        counter += 1
        
        
def searchCountries(list_country,search_continent,counter,l):
    if counter == len(list_country):
        print("List of Countries in " + search_continent)
        for j in l:
            print(j)
    else:
        if list_country[counter].getContinent() == search_continent:
            l.append(list_country[counter])
        return searchCountries(list_country,search_continent,counter +1,l)
        
        
        
        
        
list_country = []
        
readCountries("country.txt",list_country)

enter_continent = input('Enter continent to search: ')

searchCountries(list_country,enter_continent,0,[])

enter_country_class = input('Enter country name,continet, life expectany for Men and life expectany for Women: ')


l = enter_country_class.split(",")
country = l[0].strip()
continent = l[1].strip()
life_m = float(l[2])
life_f = float(l[3])
list_country.append(Country(country,continent,life_m,life_f))
print("New Country added")

selectionSort(list_country)
print("")
print("Countries by Continent and Name:")
print(list_country)
