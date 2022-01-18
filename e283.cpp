#include <iostream>
using namespace std;
int main(){
    int n;
    int num;
    int a[4];
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    while(cin>>n){
        for (int i=0;i<n;i++){
            cin>>a[0]>>a[1]>>a[2]>>a[3];
            num=a[0]*8+a[1]*4+a[2]*2+a[3];
            if(num==5){
                cout<<"A";
            }
            else if(num==7){
                cout<<"B";
            }
            else if(num==2){
                cout<<"C";
            }
            else if(num==13){
                cout<<"D";
            }
            else if(num==8){
                cout<<"E";
            }
            else if(num==12){
                cout<<"F";
            }
        }
        cout<<"\n";
    }
}