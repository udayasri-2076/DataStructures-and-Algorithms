/*Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

1
1 2
1 2 3
1 2 3 4

 */


import java.util.*;

class Pattern3 {

    public void Pattern3(int n) {

        for(int i=1;i<=n;i++){
            for(int j=1;j<=i;j++){
                System.out.print(j + " ");
            }
            System.out.println();
        }

    }

    public static void main(String args[]){

        Scanner s = new Scanner(System.in);

        System.out.print("Enter n: ");
        int n = s.nextInt();

        Pattern3 obj3 = new Pattern3();
        obj3.Pattern3(n);

        s.close();
    }
}