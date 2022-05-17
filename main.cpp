#include <iostream>
using namespace std;
int Nr[1000],n,i;
int main()
{
 cout <<"nr trepte = "; cin>>n;
 Nr[1] = 1;
 Nr[2] = 2;
 for(i=3;i<=n;i++)
 Nr[i] = Nr[i-1] + Nr[i-2];
 cout<<Nr[n]<<" modalitati de urcare pe o scara cu "<<n<<" trepte.";
 return 0;
}