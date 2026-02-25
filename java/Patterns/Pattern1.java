/* Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
*****
*****
*****
*****
*****
*/

//code

import java.util.*;

class Solution{
    public void pattern1(int n){ //3
        for(int i=0;i<n;i++){ //i=0         i=1
            for(int j=0;j<n;j++){ //j=0,1,2
                System.out.print("*"); 
    
            }
            System.out.println();
        }
    }

    public static void main(String[] args){
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();

        Solution obj=new Solution();
        obj.pattern1(n);

        s.close();


    }
}