# Week 1.2, Session 2: Task 6
def getTemperature():
    """Gets and returns the tempertaure via user input, -300 means invalid user input"""
    try:
        rawInput = input("Enter the machine's temperature (°C): ")
        temperature = int(rawInput)

        if(not type(temperature) is int):
            raise TypeError()
        
        if(temperature < -273):
            raise ValueError()
        
        return temperature
    except ValueError:
        print("Invalid temperature, make sure the temperature is -273 or higher")
        return -300
    
    except TypeError:
        print("Invalid temperature, make sure it is an integer")
        return -300 #celsius can be negative but can't be below -273 (absolute zero) so this is a nice error number
def getPsi():
    """"Gets and returns the pressure via user input, -1 means invalid user input"""
    try:
        rawInput = input("Enter the machine's pressure (PSI): ")
        pressure = int(rawInput)
        if(pressure < 0):
            raise ValueError()
        return pressure
    except ValueError:
        print("Invalid pressure, cannot be negative")
        return -1
    except:
        print("Invalid pressure, make sure it is an integer")
        return -1
def getOpStatus():
    """"Gets and returns the operating status via user input, -1 means invalid user input"""
    try:
        rawInput = input("Enter machine's operating status code (0,1)")
        opStatus = int(rawInput)
        if(opStatus < 0 or opStatus > 1):
            raise ValueError()
        return opStatus
    except ValueError:
        print("Invalid operating status, make sure it is either 0 or 1")
        return -1
    except:
        print("Invalid operating status, make sure it is an integer")
        return -1

temperature = -300 #-300 is the invalid value
while temperature == -300:
    temperature = getTemperature()

psi = -1
while psi == -1:
    psi = getPsi()

opStatus = -1
while opStatus == -1:
    opStatus = getOpStatus()

print(temperature)