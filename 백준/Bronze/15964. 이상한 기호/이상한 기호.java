import java.util.Scanner;

public class Main {

    static long special_sum( long a, long b){
        return ((a + b) * (a - b));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long a = sc.nextLong();
        long b = sc.nextLong();
        System.out.println(special_sum(a,b));
    }
}