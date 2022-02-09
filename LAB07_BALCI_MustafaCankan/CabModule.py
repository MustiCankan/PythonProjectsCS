class Cab:
    def __init__(self,kms,type_of_cab,year):
        self.__kms = kms
        self.__type_of_cab = type_of_cab
        self.__year = year 
    
    def get_kms(self):
        """
        
        Returns kms 
    
        Parameters:
        self
    
    
        returns:
        int: return self.__hms
    
    
        """
        return self.__kms
    
    def get_type_of_car(self):
        """
        
        Returns type of car
    
        Parameters:
        self
    
    
        returns:
        int: return self.__type_of_car
    
    
        """
        return self.__type_of_cab
    
    def get_year(self):
        """
        
        Returns year
    
        Parameters:
        self
    
    
        returns:
        int: return self.__year
    
    
        """
        return self.__year
    
    def __gt__(self,other):
        return self.__year > other.get_year()
    
    def __eq__(self,other):
        return self.__year == other.get_year() and self.__type_of_cab == other.get_type_of_car()
    
    def __repr__(self):
        print(f"kms: {self.__kms} type of car {self.__type_of_cab} year : {self.__year}")
    
    
class Sedan(Cab):
    def __init__(self,kms,type_of_cab,year):
        Cab.__init__(self,kms,type_of_cab,year)
        self.__price_per_km = 2.5
        
    def calculate_fare(self):
        """
        
        Calculation of Fare
    
        Parameters:
        self
    
    
        returns:
        int: return Cab.get_kms(self) * self.__price_per_km
    
    
        """
        return Cab.get_kms(self) * self.__price_per_km
    
    
class Hatchback(Cab):
    def __init__(self,kms,type_of_cab,year):
        Cab.__init__(self,kms,type_of_cab,year)
        self.__price_per_km = 2.2
        
    def calculate_fare(self):
        """
        
        Calculation of Fare
    
        Parameters:
        self
    
    
        returns:
        int: return Cab.get_kms(self) * self.__price_per_km
    
    
        """
        return Cab.get_kms(self) * self.__price_per_km
