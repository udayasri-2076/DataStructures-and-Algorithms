
/*
Find the Maximum Element
You are given an integer N, representing the number of elements in an array. Then, you are given N space-separated integers.
Your task is to find and print the maximum element from the array.

input :5                           input2:6
9 11 2 11 1                               1 2 0 9 5 8

output:11                          output:9

*/
import java.util.*;
public class max {
     public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();//5
        int a[]=new int[n];
        
        for(int i=0;i<n;i++){
            a[i]=s.nextInt();//9 11 2 11 1
        }
        int max=0;
        for(int i=0;i<n;i++){
            if(a[i]>max){ 
                max=a[i];
            }
        }
        System.out.println(max);
        
    }
}
