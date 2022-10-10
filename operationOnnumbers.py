def switch(opt, num1, num2, num3):

    if opt==1:
        return ("{:e}".format(((num1/num2)/num3)));

    elif opt==2:
        return (num1*num2*num3);

    elif opt==3:
        return -1;

    else:
        print("Invalid option!!\n");

    return -2;

num1=int(input("enter first number: "));
num2=int(input("enter second number: "));
num3=int(input("enter third number: "));
opt=0;

if __name__=="__main__":

    while opt!=-1:
        print("\n\nChoose one option:\n");
        print("\n-- Menu --");
        print("1. Divide.");
        print("2. Multiply.");
        print("3. Quit.");
        opt=int(input(":"));

        opt=switch(opt, num1, num2, num3);


        if(opt==-2):
            print("invalid option!!\n\n");
        elif opt!=-1:
            print("The result is: ", opt);
