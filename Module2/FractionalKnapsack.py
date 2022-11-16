# Fractional knapsack!!

def FracKnap(W, w, d, P): # perform Fractional Knapsack!!
    for i in range(len(w)):
        if W>w[i]:
            P=P+w[i]*d[i];
            W-=w[i];
            pass;
        else:
            P=P+W*d[i];
            break;
            pass;
        pass;
    pass;

    return P;

def sortDesc(div, weight, cost): # sort in descending order!!
    temp=0;

    for i in range(len(div)):
        for j in range(len(div)-1):
            if div[j]<div[j+1]:
                div[j], div[j+1]=div[j+1], div[j];
                weight[j], weight[j+1]=weight[j+1], weight[j];
                cost[j], cost[j+1]=cost[j+1], cost[j];
                pass;
            pass;
        pass;
    return;

origWeight=list();
origCost=list();
weight=[5, 10, 15, 22, 25];
cost=[30, 40, 45, 77, 90];
W=60;

#weight=[20, 30, 10];
#cost=[100, 120, 60];
#W=50;

origWeight=weight[:]; # creating a copy of weight
origCost=cost[:]; # creating a copy of cost

div=list();

for i in range(len(weight)):
    div.append(cost[i]/weight[i]);
    pass;

sortDesc(div, weight, cost);

P=0;

P=FracKnap(W, weight, div, P);
print(f"Profit = {P}\n");
