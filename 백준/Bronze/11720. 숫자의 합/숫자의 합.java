import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        String numbers = sc.nextLine();
        int sum = 0;
        for (int i = 0; i < N; i++) {
            sum += numbers.charAt(i) - '0'; // 문자 '0'의 ASCII 값을 빼서 정수로 변환
        }
        System.out.println(sum);
    }
}