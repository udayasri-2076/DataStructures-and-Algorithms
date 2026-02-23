/*Given the input n.Print this Pattern
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
* 
*/


import java.util.*;
public class Pattern5 {
    public void Pattern5(int n){
        for(int i=0;i<=n;i++){
            for(int j=0;j<n-i+1;j++){
                System.out.print("*"+" ");
            }
            System.out.println();
        }

    }

public static void main(String args[]){
    Scanner s=new Scanner(System.in);
    System.out.print("Enter n: ");
    int n=s.nextInt();

       Pattern5 obj=new Pattern5();
       obj.Pattern5(n);
}
}
