









import java.util.*;
public class Armstrong {
     public static void main(String args[]){
        Scanner s=new Scanner(System.in);
        int n=s.nextInt(); //371
        int sum=0;
        int temp=n;//temp=371

        while(n>0){ //371>0t
            int d=n%10;//371%10=1           37%10=7          3%10=3
            sum=sum+(d*d*d);//0+(1*1*1)=1   1+(7*7*7)=344    344+27=371
            n=n/10; //371/10=37             37/10=3          3/10=0
        }
        if(temp==sum){ //371==371t 
            System.out.print("Armstrong number");
        }
        else{
            System.out.print("not Armstrong number");
        }
     }

}
