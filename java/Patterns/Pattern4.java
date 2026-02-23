/* iven an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

1
2 2
3 3 3
4 4 4 4
*/


import java.util.*;
class Pattern4{
public void Pattern4(int n) {
    for(int i=1;i<=n;i++){     //i=1 1<=3t        i=2 2<=4t                       i=3t                                 i=4f
        for(int j=1;j<=i;j++){ //j=1 1<=1t 2<=1f  j=1 1<=2t,j=2 2<=2t,j=3 3<=2f   j=1 1<=3t,2 2<=3t, 3 3<=3t,4 4<=3f
            System.out.print(i+" ");/*1
                                      2  2
                                      3  3  3
                                      */
        }
        System.out.println();

    }
}

public static void main(String args[]){
    Scanner s=new Scanner(System.in);
    System.out.print("enter n:");
    int n=s.nextInt();

    Pattern4 obj=new Pattern4();
    obj.Pattern4(n);
}
}
