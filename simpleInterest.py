# Simple interest!!

T=input("Simple interest for years/days/months: ");

principal=int(input("enter principal: "));
rate=int(input("enter rate: "));
time=int(input("enter time: "));

if T == "years":
    print(f"Simple interest for {time} year(s): ");
    simple_interest=(principal*rate*time)/100;

elif T == "days":
    print("Simple interest for 365 days: ");
    simple_interest=(principal*rate*time)/(365*100);

elif T == "months":
    print("Simple interest for 12 months: ");
    simple_interest=(principal*rate*time)/(12*100);


print(simple_interest);
