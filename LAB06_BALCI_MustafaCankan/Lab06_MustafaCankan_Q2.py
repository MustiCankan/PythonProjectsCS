from Instructor import Instructor

def read_file(file_name):
    """
    Converting the information at file to dictionary
    
    
    Parameters:
    file_name(str): file name 
    
    
    returns:
    dictionary: return hs
    
    
    """
    
    hs = {}
    
    f1 = open(file_name,'r')
    
    for line in f1:
        l = line.split(';')
        pos = l[1].find(' ')
        name = l[1][:pos]
        surname = l[1][pos +1:]
        hours = float(l[3])
        id_num = int(l[0]) 
        hs[id_num] = Instructor(id_num,name, surname,l[2],hours)
    return hs

dict1 = read_file('instructor.txt') 

enter_id = int(input('Enter instructor id:'))
print(dict1[enter_id].__str__())

enter_status = input('Enter status (F - Full-time/ P - Part-time}): ')


l = []
for i in dict1:
    if dict1[i].get_status() == enter_status:
        l.append(dict1[i])
            
print(l)
