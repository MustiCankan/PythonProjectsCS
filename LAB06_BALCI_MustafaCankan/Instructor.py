class Instructor():
    def __init__(self,id_num ,name, surname,status,hours):
        self.__id_num = id_num
        self.__name = name
        self.__surname = surname
        self.__status = status
        self.__hours = hours
        
    def get_id(self):
        """
        
        Returns id_number 
    
        Parameters:
        self
    
    
        returns:
        int: return self.__id_num
    
    
        """
        return self.__id_num
    
    def get_name(self):
        """
        Returns name  
    
        Parameters:
        self
    
    
        returns:
        string: return self.__name
    
    
        """
        return self.__name
    
    def get_status(self):
        """
        Returns working status
    
        Parameters:
        self
    
    
        returns:
        string: return self.__status
    
    
        """
        return self.__status
    
    def get_hours(self):
        """
        Returns number of hours worked 
    
        Parameters:
        self
    
    
        returns:
        int: return self.__hours
    
    
        """
        return self.__hours
    
    
    def calculate_salary(self):
        """
        Calculating the Salary
        Parameters:
        self
    
    
        returns:
        integer: return salary
    
    
        """
        if self.__status == 'F':
            salary = 500*(self.__hours) +5000
        elif self.__status == 'P':
            salary = 400*(self.__hours)
        return salary
    
    def __str__(self):
        rev = "Name:"+self.__name +' '+self.__surname+'\n'
        rev += "Status: "+self.__status +'\n'
        rev += "Salary: "+str(self.calculate_salary()) +' TL'
        return rev
    
    def __repr__(self):
        rev = "Id:"+str(self.__id_num) + '\n'
        rev += "Name:"+self.__name +' '+self.__surname+'\n'
        rev += "Salary: "+str(self.calculate_salary()) +' TL'
        return rev
