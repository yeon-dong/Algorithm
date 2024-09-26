import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String word = scanner.nextLine();
        int length = word.length();
        System.out.println(length);
        scanner.close();
    }
}