import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int time = sc.nextInt();
        a = a + (b + time) / 60;
        b = (b + time) % 60;
        if(a>23){
            a = a % 24;
        }
        System.out.println(a+" "+b);
    }
}