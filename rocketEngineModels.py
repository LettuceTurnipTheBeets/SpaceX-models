class RocketEngine(object):
    """
    RocketEngine class to model a Merlin engine used in a SpaceX Falcon 9
    rocket.
    """       
    def __init__(self, cycle, thrust, weight, modelNumber):
        """
        The constructor for RocketEngine class.
        
        Parameters:
            cycle (str): power cycle
            thrust (int): engine thrust (kN)
            weight (int): engine weight (kg)
            modelNumber (str): engine model number
        """      
        self.cycle = cycle
        self.thrust = thrust
        self.weight = weight
        self.modelNumber = modelNumber

    def __repr__(self):
        """ 
        repr method for RocketEngine class. 
  
        Parameters: 
            self 
          
        Returns: 
            A string representation of the RocketEngine object. 
        """
        return "RocketEngine('{}', {}, {}, '{}', '{}')".format(
            self.cycle,
            self.thrust,
            self.weight,
            self.modelNumber
            )

    def __str__(self):
        """
        str dunder method for RocketEngine class.

        Parameters:
            self

        Returns:
            A formatted model number string.
        """
        return 'RocketEngine: {}'.format(self.modelNumber)


class Engine(object):
    """
    Engine base class to model an engine used in a SpaceX rocket.
    """       
    def __init__(self, cycle, thrust, weight, modelNumber):
        """
        The constructor for Engine class.
        
        Parameters:
            cycle (str): power cycle
            thrust (int): engine thrust (kN)
            weight (int): engine weight (kg)
            modelNumber (str): engine model number
        """     
        self.cycle = cycle
        self.thrust = thrust
        self.weight = weight
        self.modelNumber = modelNumber

    def __repr__(self):
        """ 
        repr method for Engine class. 
  
        Parameters: 
            self 
          
        Returns: 
            A string representation of the RocketEngine object. 
        """
        return "{}('{}', {}, {}, '{}')".format(
            self.__class__.__name__,
            self.cycle,
            self.thrust,
            self.weight,
            self.modelNumber
            )

    def __str__(self):
        """
        str dunder method for Engine class.

        Parameters:
            self

        Returns:
            A formatted model number string.
        """
        return '{}: {}'.format(self.__class__.__name__, self.modelNumber)


class MerlinEngine(Engine):
    """
    MerlineEngine class inherits from the base Engine model.
    """      
    def __init__(self, cycle, thrust, weight, modelNumber, balanceList):
        """
        The constructor for MerlinEngine class.
        
        Parameters:
            cycle (str): power cycle
            thrust (int): engine thrust (kN)
            weight (int): engine weight (kg)
            modelNumber (str): engine model number
            balanceList (list): list of the engine balance numbers.  This
                                will be sorted from smallest to largest. 
        """   
        super().__init__(
            cycle,
            thrust,
            weight,
            modelNumber
            )
        if isinstance(balanceList, (list,)):
            balanceList.sort()
            self.balanceList = balanceList
        else:
            raise TypeError("balanceList must be of type 'list'")

    def __len__(self):
        """
        len dunder method for MerlinEngine class.

        Parameters:
            self

        Returns:
            Length of balanceList.
        """
        return len(self.balanceList)
        

class RaptorEngine(Engine):
    """
    RaptorEngine class inherits from the base Engine model.
    """    
    def __init__(self, cycle, thrust, weight, modelNumber, actuators):
        """
        The constructor for RaptorEngine class.
        
        Parameters:
            cycle (str): power cycle
            thrust (int): engine thrust (kN)
            weight (int): engine weight (kg)
            modelNumber (str): engine model number
            actuators (int): number of engine actuators
        """   
        super().__init__(
            cycle,
            thrust,
            weight,
            modelNumber
            )
        self.actuators = actuators
        
