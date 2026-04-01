#include <iostream>
using namespace std ; 

int main (){

 //[1,8,6,2,5,4,8,3,7]

class Solution {
public:

      int diff ( int i , int j){

        if( i > j ){ return i - j ; }
        if( i < j ){ return j - i ; }
        if( i == j ){ return 0 ; }

      }

      int maxArea(vector<int>& height) {


        int max = 0 ; 
        int temp = 0 ;
        int i = 0 ;
        int j = height.size()-1 ; 


        while(i != j){

                if (height[i] < height[j]) {
                    if (height[i] * diff(i, j)) {

                        temp = height[i] * diff(i, j);
                        if(temp>max){ max = temp ;};
                        cout << " Max is " << max << "\n";

                        i ++ ;
                    }

                } else if (height[i] > height[j]) {
                    if (height[j] * diff(i, j)) {

                        temp = height[j] * diff(i, j);
                        if(temp>max){ max = temp ;};
                        cout << " Max is " << max << "\n";

                        j ++ ;
                    }

                } else {
                  
                    temp = height[i] * diff(i, j);
                    if(temp>max){ max = temp ;};
                    cout << " Max is " << max << "\n";

                    i ++ ;
                };




        }
        return max ; 
      } 
    
    
    return max;
}
}
;










    return 0 ; 
}