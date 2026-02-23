

import java.util.*;
public class Pattern6 {
    public void Pattern6(int n){
        for(int i=1;i<=n;i++){
            for(int j=1;j<=n-i+1;j++){
                System.out.print(j+" ");
            }
            System.out.println();
        }

    }

public static void main(String args[]){
    Scanner s=new Scanner(System.in);
    System.out.print("enter n:");
    int n=s.nextInt();

    Pattern6 obj=new Pattern6();
    obj.Pattern6(n);

}
}
