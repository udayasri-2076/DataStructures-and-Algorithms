import java.util.*;

public class arraycreation{
    public static void main(String args[]){
        Scanner s=new Scanner(System.in);
        int n=s.nextInt(); //5
        int a[]=new int[n];

        for(int i=0;i<n;i++){
            a[i]=s.nextInt(); //6 7 8 0 3
        }
           for(int i=0;i<n;i++){
            System.out.print(a[i]+" ");
        }
        

    }
}
