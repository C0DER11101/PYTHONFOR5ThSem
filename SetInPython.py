# SET IN PYTHON

a=["C++", "C", "Python", "Java", "C++", "Go", "JavaScript", "Java"];

Set=set(a);

print(Set); # output: {'C', 'Go', 'C++', 'Java', 'JavaScript', 'Python'}

s2=set(['a', 'b', 'a', 'c', 'd', 'b']);

print(s2); # output: {'c', 'd', 'a', 'b'}

t=(1, 4, 5, 1, 6);

s3=set(t);
print(s3);  #output: {1, 4, 5, 6}

d={
   1:'one',
   2:'two',
   1: 'one'
   };
   
s4=set(d);
print(s4); #output: {1, 2}