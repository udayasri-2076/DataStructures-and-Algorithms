/*Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*
**
***
****
*****

 */

import java.util.*;

class Solution {

    public void pattern2(int n){
        for(int i = 0; i < n; i++){
            for(int j = 0; j <= i; j++){
                System.out.print("*");   // FIXED HERE
            }
            System.out.println();
        }
    }

    public static void main(String args[]){
        Scanner s = new Scanner(System.in);
        System.out.print("Enter n: ");
        int n = s.nextInt();

        Solution obj = new Solution();
        obj.pattern2(n);

        s.close();
    }
}
