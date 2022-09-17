# RETURN KEYWORDS IN PYTHON.

def fun():
    S=0;

    for i in range(10):
        S+=i;


    return S;

def Fun():
    S=0;

    for i in range(10):
        S+=i;
        yield S;


print("fun() using return keyword\n\n");
print(fun());


print("Fun() using yield keyword\n\n");

for i in Fun():
    print(i);
