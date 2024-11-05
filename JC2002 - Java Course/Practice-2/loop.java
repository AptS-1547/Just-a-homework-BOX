import java.util.Scanner;

public class loop {
    private static int start, end;
    private static int sum = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        start = getNumber(sc);
        end = getNumber(sc);

        if (start > end) {
            System.out.println("The start number should be less than the end number");
            System.exit(1);
        }

        for (int i = start; i <= end; i++) {
            sum += i;
        }
        System.out.println("The sum of the numbers between " + start + " and " + end + " is: " + sum);
        sc.close();
    }

    private static int getNumber(Scanner sc) {
        while (true) {
            System.out.print("Enter a number: ");
            if (sc.hasNextInt()) {
                return sc.nextInt();
            } else {
                System.out.println("Please enter a valid Int number");
            }
        }
    }
}