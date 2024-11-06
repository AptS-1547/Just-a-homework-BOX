package net.esaps;

import java.util.Scanner;

public class RunApp {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        int a = 0;
        int b = 0;
        char operation = ' ';

        while (true) {
            try {
                System.out.print("Enter first number: ");
                a = scanner.nextInt();

                System.out.print("Enter operator (+, -, *, /, or q to quit): ");
                operation = scanner.next().charAt(0);

                if (operation == 'q' || operation == 'Q') {
                    System.out.println("Quitting...");
                    break;
                }

                System.out.print("Enter second number: ");
                b = scanner.nextInt();

                int result = 0;
                switch (operation) {
                    case '+':
                        result = Calculator.add(a, b);
                        break;
                    case '-':
                        result = Calculator.subtract(a, b);
                        break;
                    case '*':
                        result = Calculator.multiply(a, b);
                        break;
                    case '/':
                        result = Calculator.divide(a, b);
                        break;
                    default:
                        System.out.println("Invalid operation");
                        continue;
                }
                System.out.println("Result: " + result);

            } catch (ArithmeticException e) {
                System.out.println("Division by zero");
            } catch (NotDivisibleException e) {
                System.out.println("Not divisible");
            }
        }
        scanner.close();
    }
}