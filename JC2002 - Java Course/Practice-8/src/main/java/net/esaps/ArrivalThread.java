package net.esaps;

import java.util.Random;

public class ArrivalThread extends Thread {

    private String direction;
    private Random random = new Random();

    public ArrivalThread(String direction) {
        this.direction = direction;
        System.out.println("ArrivalThread created for " + direction);
    }

    @Override
    public void run() {
        while (true) {
            try {
                Thread.sleep(500 + random.nextInt(2000));
                System.out.println("Car arrived from " + direction);
                if (direction.equals("West")) {
                    TrafficSimulator.incrementWestQueue();
                } else if (direction.equals("South")) {
                    TrafficSimulator.incrementSouthQueue();
                }
                new CrossingThread(direction).start();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}