#include<iostream>
#include<stdlib.h>
#include<conio.h>

using namespace std;

int main(void)
{
	int *a, size=5;

	a=new int[size];

	for(int i=1; i<=size;i++)
		a[i]=i;

	for(int i=1; i<=size;i++)
		cout<<a[i]<<" ";

	cout<<"\n";

	delete a;
	return 0;
}
