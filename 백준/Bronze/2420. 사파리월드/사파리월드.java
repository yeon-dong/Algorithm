import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextInt();
        long b = sc.nextInt();
        long c = a-b;
        if(c<0){
            System.out.println(-c);
        }else {
            System.out.println(c);
        }
    }
}