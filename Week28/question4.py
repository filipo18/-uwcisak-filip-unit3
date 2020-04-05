# This will Define a class which has at least two methods: 

# getString: to get a string from console input
# printString: to print the string in upper case.

class String():
    def __init__(self):
        pass

    def getString(self):
        self.string = input("enter a string: ") # I am not sure what is ment by "console input" is it ment that way? 
    
    def printString(self):
        print(self.string.upper())


testing = StringP()

testing.getString()
testing.printString()