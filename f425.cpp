#include <iostream>
#include <cmath>
#include <vector>
using namespace std;
int main(){
    int s,n,temp;
    vector<int> pointXY;
    for(int i=0;i<3;i++){
        cin>>s;
        pointXY.push_back(s);
    }
	for (int index = 0; index < (pointXY.size()); index++)
	{
		cout<<pointXY[index];
		
	}

}