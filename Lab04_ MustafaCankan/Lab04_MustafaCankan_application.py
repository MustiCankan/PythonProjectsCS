from Lab04_MustafaCankan_module import district_density, find_districts

f1 = open('city_districts.txt','r')
f2 = open('city_values.txt','r')

enter_city = input('Enter city to search("quit" to exit):')


while enter_city != "quit":
    if enter_city == "Ankara" or enter_city == "Istanbul":
        name = district_density(f1,f2,enter_city)
        print("")
        val = float(input("Enter maximum density:"))
        bool1 = find_districts(name,val)
        if bool1 == False:
            print("No districts in " + enter_city + " with population density below " + str(val))
        print("")
    else:
        print(enter_city,' not found...')
        print("")
    enter_city = input('Enter city to search("quit" to exit):')

print("Thank you-Goodbye")
    
