import java.util.InputMismatchException;
import java.util.Scanner;

public class RunApp {
    public static void main(String[] args) {
        int number = 1;
        int count = 1;
        Scanner sc = new Scanner(System.in);
        while (true) {
            try {
                System.out.print("Enter a number: ");
                
                number = sc.nextInt();

                if (number < 0) {
                    throw new IllegalArgumentException();
                } else if (number == 0) {
                    break;
                }

                int number_ano = number;

                while (number != 1) {
                    if (number % 2 == 0) {
                        number /= 2;
                    } else {
                        number = number * 3 + 1;
                    }
                    count++;
                }

                System.out.println("For initial n = " + number_ano + ", it took " + count + " steps to reach 1.");
                count = 0;
            } catch (IllegalArgumentException e) {
                System.out.println("Please use valid n");
            } catch (InputMismatchException e) {
                System.out.println("Invalid input");
                sc.next();
            }
        }   
        sc.close();
        System.exit(0);
    }
}
