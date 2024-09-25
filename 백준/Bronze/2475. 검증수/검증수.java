import java.util.Scanner;

public class Main {

    static int square(short a) {
        return a*a;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        short a = sc.nextShort();
        short b = sc.nextShort();
        short c = sc.nextShort();
        short d = sc.nextShort();
        short e = sc.nextShort();
        System.out.println((square(a)+square(b)+square(c)+square(d)+square(e))%10);
    }
}