import java.util.Scanner;

public class Main {

    static int special_sum( int a, int b){
        return ((a + b) * (a - b));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        System.out.println(special_sum(a,b));
    }
}