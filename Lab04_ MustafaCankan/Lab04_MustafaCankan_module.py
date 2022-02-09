def district_density(file_one,file_two,city_name):
    """
    Show the city, whose density is smaller than val

    Parameters:
    file_one (func): Open first file
    file_two (func): Open second file
    city_name (str): The name of city 

    returns:
    string: return file_name


    """
    dis = file_one.readline()
    val = file_two.readline()
    file_name = city_name+"_density.txt"
    f3= open(file_name,"w")

    for line in file_one:
        val = file_two.readline()
        dis = file_one.readline()
        pos = val.find("\t")
        pos2 = val.find(",")
        pos4 = dis.find("\t")
        city = dis[:pos4]
        if pos != -1:
            if "," in val[pos+1:]:
                pos3 = val.rfind(",")
                flo = val[pos3+1:]
                area = float(val[pos+1:pos3] + flo)
                
            else:
                area = float(val[pos+1:])
            

            if pos2 != -1:
                flo = val[pos2+1:pos]
                pop = float(val[:pos2] + flo)
            else:
                pop = float(val[:pos])
            
            density = pop/area
            
            # print(f'{density:.1f}')

            result = dis[pos4 +1:(len(dis)-1)]+","+ f'{density:.1f} \n'
        if city == city_name:
            f3.write(result)
        

    f3.close()
    return file_name
    


def find_districts(fileCountry,val):
    """
    Show the city, whose density is smaller than val

    Parameters:
    fileCountry (str): Name of the file
    val (int): compare parameter

    returns:
    boolean: return counter


    """
    fc = open(fileCountry,"r")

    line = fc.readline()
    counter = False

    while line:
        pos = line.find(",")
        density = float(line[pos+1:len(line)-1])
        country = line[:pos]
        if density < val:
            print(country)
            counter = True
        line = fc.readline()
    fc.close()
    return counter
