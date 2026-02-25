//Reverse Number

import java.util.*;
public class ReverseNum {
    public static void main(String args[]){
    Scanner s=new Scanner(System.in);
    int n=s.nextInt();  //7789
    int rev=0;         

    while(n>0){    //7789>0t          778>0t        77>0t         7>0t
        int d=n%10; //7789%10=9       778%10=8      77%10=7       7%10=7
        rev=(rev*10)+d; //(0*10+9)=9  (9*10)+8=98   98*10+7=987   9870+7=9877
        n=n/10;        //7789/10=778  778/10=77     77/10=7       7/10=0

    }
    System.out.println(rev); //9877
}
}
