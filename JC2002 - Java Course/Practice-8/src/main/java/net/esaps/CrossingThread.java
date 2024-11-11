package net.esaps;

public class CrossingThread extends Thread {

    private String direction;

    public CrossingThread(String direction) {
        this.direction = direction;
    }

    @Override
    public void run() {
        TrafficSimulator.cross(direction);
    }
}