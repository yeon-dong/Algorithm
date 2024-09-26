import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] numbers = new int[9];
        for (int i = 0; i < 9; i++) {
            numbers[i] = sc.nextInt();
        }
        int max = numbers[0];
        int maxIDX = 1;
        for (int i = 1; i < 9; i++) {
            if(max<numbers[i]){
                max = numbers[i];
                maxIDX = i+1;
            }
        }
        System.out.println(max);
        System.out.println(maxIDX);
    }
}