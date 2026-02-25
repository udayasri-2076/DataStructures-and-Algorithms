//count of digits

import java.util.*;
public class CountDigits{
    public static void main(String args[]){
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();//156
        int c=0;

        while(n>0){  //156>0t           15>0t    1>0t
            int d=n%10; //d=156%10=6    15%10=5  1%10=1
            c++;        //c=1           c=2      c=3
            n=n/10;    //156/10=15      15/10=1  1/10=0
        }
        System.out.println(c);
    }
}