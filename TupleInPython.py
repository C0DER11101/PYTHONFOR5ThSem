# TUPLES IN PYTHON

tup=('Name:', 'Age:', 'Roll:');

print(tup[0]); # output:  Name:

print(tup);# output: ('Name:', 'Age:', 'Roll:')

tup2=('Priyanuj Bora ', '20 ', 'CSE-28/20 ');

for i in range(len(tup)):
    print(tup[i]+tup2[i], end=" "); # output:  Name:Priyanuj Bora  Age:20  Roll:CSE-28/20