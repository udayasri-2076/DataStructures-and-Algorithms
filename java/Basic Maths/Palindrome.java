//Palindrome

import java.util.*;
public class Palindrome {

    public static void main(String[] args){
        Scanner s= new Scanner(System.in);
        int n=s.nextInt();  //121
        int temp=n;        //temp=121
        int sum=0;

        while(n>0){
            int d=n%10;  //121%10=1      12%10=2   1%10=1
            sum=(sum*10)+d;//0+1=1       10+2=12   120+1=121
            n=n/10;      //121/10=12    12/10=1    1/10=0

        }
        if(temp==sum){    //121==121
            System.out.println(temp+" is a palindrome");
        }
        else{
            System.out.println(temp+" is not a palindrome");
        }

    }
}