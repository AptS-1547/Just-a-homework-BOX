package net.esaps;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JTextField;
import java.awt.GridLayout;

public class GraphicalCalculator {
    private JFrame frame = new JFrame("Calculator");
    private JTextField textField = new JTextField();

    private JButton Clear = new JButton("Clear");
    private JButton Add = new JButton("Add (+)");
    private JButton Subtract = new JButton("Subtract (-)");
    private JButton Multiply = new JButton("Multiply (*)");
    private JButton Divide = new JButton("Divide (/)");
    private JButton Equals = new JButton("Equals (=)");

    public GraphicalCalculator() {
        frame.setSize(400,600);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.setLayout(new GridLayout(7, 1));
        frame.add(textField);
        frame.add(Clear);
        frame.add(Add);
        frame.add(Subtract);
        frame.add(Multiply);
        frame.add(Divide);
        frame.add(Equals);

        frame.setVisible(true);
    }

    public static void main(String[] args) {
        new GraphicalCalculator();
    }
}
