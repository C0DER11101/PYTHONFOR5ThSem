# FUNCTIONS IN PYTHON: PART-2

def getInteger():
    result = int(input("enter an integer: "));
    return result;

def Main():
    print("Started");
    
    output=getInteger();
    
    print(output);
    
if __name__ == "__main__": # checks if the python intepreter is running this file as "main"
    Main();