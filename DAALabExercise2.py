# Write a program in Python to check a leap year using if statement. Also write the algorithm.
year=int(input("enter a year: "));

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f"{year} is a leap year!\n");
        else:
            print(f"{year} is not a leap year!\n");
    else:
        print(f"{year} is a leap year!\n");

else:
    print(f"{year} is not a leap year!\n");
