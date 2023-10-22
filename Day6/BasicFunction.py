#Functions : Reusable, Avoids code repitiion
#Function is a block of code which only runs when it is called
#You can pass data, known as parameters, into a function


#You need to declare a function using the keyword "def"
#Syntax : def function_name():
#           function body

#To call a function, use the function name followed by parenthesis
#Syntax : function_name()

#You can also pass parameters to a function and expect a return value
#Syntax : def function_name(parameter1, parameter2):
#           function body
#           return value

#To call a function with parameters, use the function name followed by parenthesis and pass the parameters
#Syntax : return_value = function_name(parameter1, parameter2)

def sampleFunction():
    print("This function go triggered")
    print("This function will do something")
    print("This function will do something else")
    print("This function got completed")

sampleFunction()