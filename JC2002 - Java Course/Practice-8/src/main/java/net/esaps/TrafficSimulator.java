package net.esaps;

public class TrafficSimulator {

    private static int westQueue = 0;
    private static int southQueue = 0;

    private WestArrivalThread westArrivalThread = new WestArrivalThread();
    private SouthArrivalThread southArrivalThread = new SouthArrivalThread();

    public TrafficSimulator() {
        westArrivalThread.start();
        southArrivalThread.start();
    }

    public static void cross(String direction) {
        try {
            Thread.sleep(2000);

            if (direction.equals("West")) {
                westQueue--;
            } else {
                southQueue--;
            }
            System.out.println("Car crossed from " + direction + " - WestQueue:" + westQueue + ", SouthQueue:" + southQueue);

        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        return;
    }

    public static void incrementSouthQueue() {
        southQueue++;
    }

    public static void incrementWestQueue() {
        westQueue++;
    }
    
}
