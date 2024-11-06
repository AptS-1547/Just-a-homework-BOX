package net.esaps;

import javax.swing.JFrame;
import javax.swing.JLabel;

public class FrameTest {
    private JFrame frame = new JFrame("Frame Test");
    private JLabel label = new JLabel("Hello World - ESAP");

    public FrameTest() {
        frame.setSize(400, 400);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);

        frame.add(label);
    }
    
}
