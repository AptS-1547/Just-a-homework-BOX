package net.esaps;

import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

/**
 * Unit test for simple App.
 */
public class AppTest {

    /**
     * Rigorous Test :-)
     */
    @Test
    public void shouldAnswerWithTrue() {
        assertTrue(Calculator.add(4984415, 2561892) == 7546307);
        assertTrue(Calculator.add(1, 1) == 2);
        assertTrue(Calculator.subtract(1, 1) == 0);
        assertTrue(Calculator.subtract(4984415, 2561892) == 2422523);
        assertTrue(Calculator.multiply(1, 1) == 1);
        assertTrue(Calculator.multiply(99, 99) == 9801);
        try {
            assertTrue(Calculator.divide(3, 1) == 3);
            assertTrue(Calculator.divide(784312, 4) == 196078);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
