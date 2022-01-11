#include<iostream>
using namespace std;
// Linear Search in 2d
// int ispresent(int arr[][2],int target, int r, int c){
//     for (int i = 0; i <r; i++)
//     {
//       for (int j = 0; i < c; j++)
//       {
//          if (arr[i][j]==target){
//              return 0;
//          }
//       }
      
//     }
    
// }

// Row wise sum problem
void rsum(int arr[][3], int r, int c){
    for (int i = 0; i < r; i++){
       int sum=0;
       for (int j = 0; j<c; j++){
           sum+=arr[i][j];
       }
       cout<<sum<<" ";
       
    }
}

int main(){
int arr[3][3];
// int arr[3][4]={{1,11,111,1111},{2,22,222,2222},{3,33,333,3333}};

for (int i = 0; i < 3; i++)
{
   for (int j = 0; j < 3; j++)
   {
       cout<<"Enter elements at postion "<<i<<","<<j<<" ";

       cin >>arr[i][j];
   }
   
}

// for (int i = 0; i < 3; i++)
// {
//    for (int j = 0; j < 3; j++)
//    {
//        cout<<arr[i][j]<<" ";
//    }
//    cout<<endl;
   
// }

// cout<<"Enter the target: ";
// int target;
// cin >> target;
int r=3;
int c=3;
// ispresent(arr,r,c)
  
rsum(arr,r,c);




return 0;
}
