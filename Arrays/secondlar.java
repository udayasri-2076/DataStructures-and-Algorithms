import java.util.Scanner;

public class secondlar {
     public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();
        int a[]=new int[n];
        
        for(int i=0;i<n;i++){
            a[i]=s.nextInt();
        }
        
        int max=Integer.MIN_VALUE;
        int smax=Integer.MIN_VALUE;
        
        for(int i=0;i<n;i++){
            if(a[i]>max){
                smax=max;
                max=a[i];
            }
            else if(a[i]>smax && a[i]<max){
                smax=a[i];
            }
        }
        if(smax==Integer.MIN_VALUE){
            System.out.println("No Second Max");
        }
        else{
          System.out.println(smax);  
        }
    }
}

