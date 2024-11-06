package net.esaps;

public class Calculator {
    public static int add(int a, int b) {
        return a + b;
    }
    
    public static int subtract(int a, int b) {
        return a - b;
    }

    public static int multiply(int a, int b) {
        return a * b;
    }

    public static int divide(int a, int b) throws Exception {
        if ( a % b == 0) {
            return a / b;
        } else {
            throw new NotDivisibleException("Numbers are not divisible");
        }
    }
}

class NotDivisibleException extends Exception {
    public NotDivisibleException(String message) {
        super(message);
    }
}