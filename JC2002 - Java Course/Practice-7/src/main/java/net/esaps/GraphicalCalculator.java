package net.esaps;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionListener;

public class GraphicalCalculator {
    private JFrame frame = new JFrame("Calculator");
    private JTextField textField = new JTextField();

    private JButton Clear = new JButton("Clear");
    private JButton Add = new JButton("Add (+)");
    private JButton Subtract = new JButton("Subtract (-)");
    private JButton Multiply = new JButton("Multiply (*)");
    private JButton Divide = new JButton("Divide (/)");
    private JButton Equals = new JButton("Equals (=)");

    private float storedValue = 0;
    private float secondValue = 0;
    private float resultValue = 0;
    private Operation status = Operation.NONE;

    private enum Operation {
        NONE, ADD, SUBTRACT, MULTIPLY, DIVIDE
    }

    public GraphicalCalculator() {
        frame.setSize(400, 600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new GridLayout(7, 1));

        frame.add(textField);
        frame.add(Clear);
        frame.add(Add);
        frame.add(Subtract);
        frame.add(Multiply);
        frame.add(Divide);
        frame.add(Equals);

        Clear.addActionListener(e -> clear());
        Add.addActionListener(e -> setOperation(Operation.ADD, Add));
        Subtract.addActionListener(e -> setOperation(Operation.SUBTRACT, Subtract));
        Multiply.addActionListener(e -> setOperation(Operation.MULTIPLY, Multiply));
        Divide.addActionListener(e -> setOperation(Operation.DIVIDE, Divide));
        Equals.addActionListener(e -> calculate());

        frame.setVisible(true);
    }

    private void clear() {
        textField.setText("");
        storedValue = 0;
        secondValue = 0;
        resultValue = 0;
        status = Operation.NONE;
        resetButtonBackgrounds();
    }

    private void setOperation(Operation operation, JButton button) {
        try {
            storedValue = Float.parseFloat(textField.getText());
            textField.setText("");
            status = operation;
            resetButtonBackgrounds();
            button.setBackground(Color.gray);
        } catch (NumberFormatException ex) {
            showError("Invalid number");
        }
    }

    private void calculate() {
        if (status == Operation.NONE) return;
        try {
            secondValue = Float.parseFloat(textField.getText());
        } catch (NumberFormatException ex) {
            showError("Invalid number");
            return;
        }
        switch (status) {
            case ADD:
                resultValue = storedValue + secondValue;
                break;
            case SUBTRACT:
                resultValue = storedValue - secondValue;
                break;
            case MULTIPLY:
                resultValue = storedValue * secondValue;
                break;
            case DIVIDE:
                resultValue = storedValue / secondValue;
                break;
        }
        textField.setText(String.valueOf(resultValue));
        status = Operation.NONE;
        resetButtonBackgrounds();
    }

    private void showError(String message) {
        JOptionPane.showMessageDialog(null, message, "Error", JOptionPane.ERROR_MESSAGE);
    }

    private void resetButtonBackgrounds() {
        Add.setBackground(null);
        Subtract.setBackground(null);
        Multiply.setBackground(null);
        Divide.setBackground(null);
    }

    public static void main(String[] args) {
        new GraphicalCalculator();
    }
}