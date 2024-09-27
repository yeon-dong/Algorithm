import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.nextLine();
        int len = a.length();
        String answer = "";
        for (int i = 0; i < len; i++) {
            if (Character.isUpperCase(a.charAt(i))) {
                answer += Character.toLowerCase(a.charAt(i));
            }
            else {
                answer += Character.toUpperCase(a.charAt(i));
            }
        }
        System.out.println(answer);
    }
}