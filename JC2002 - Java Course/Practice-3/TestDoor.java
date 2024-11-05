import java.util.Scanner;

public class TestDoor {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        DoorWithCodeLock door = new DoorWithCodeLock();
        while (true) {
            int choice = getNumber(sc);
            switch (choice) {
                case 1:
                    door.openDoor();
                    break;
                case 2:
                    door.closeDoor();
                    break;
                    
                case 3:
                    door.lockDoor();
                    break;
                case 4:
                    door.unlockDoor();
                    break;
                case 5:
                    System.out.println("bye");
                    sc.close();
                    System.exit(0);
                default:
                    System.out.println("Invalid option!");
            }
        }
    }

    private static int getNumber(Scanner sc) {
        while (true) {
            if (sc.hasNextInt()) {
                return sc.nextInt();
            } else {
                System.out.println("Invalid option!");
            }
        }
    }
}

class Door {
    public boolean isOpen = false;
    public static Scanner sc = new Scanner(System.in);
    
    public void openDoor() {
        if (isOpen) {
            System.out.println("Door already open!");
            return;
        }
        isOpen = true;
        System.out.println("Door opened!");
        return;
    }

    public void closeDoor() {
        if (!isOpen) {
            System.out.println("Door already closed!");
            return;
        }
        isOpen = false;
        System.out.println("Door closed!");
        return;
    }
}

class DoorWithLock extends Door {
    public boolean isLocked = false;
    
    @Override
    public void openDoor() {
        if (isOpen) {
            System.out.println("Door already open!");
            return;
        } else if (isLocked && !isOpen) {
            System.out.println("Door is locked and cannot be opened!");
            return;
        }
        isOpen = true;
        System.out.println("Door opened!");
        return;
    }

    public void lockDoor() {
        if (isOpen) {
            System.out.println("Open door cannot be locked!");
            return;
        } else if (!isOpen && isLocked) {
            System.out.println("Door already locked!");
            return;
        }
        isLocked = true;
        System.out.println("Door locked!");
        return;
    }

    public void unlockDoor() {
        if (!isLocked) {
            System.out.println("Door is not locked!");
            return;
        }
        isLocked = false;
        System.out.println("Door unlocked!");
        return;
    }
        
}

final class DoorWithCodeLock extends DoorWithLock {
    private int code = 0;

    @Override
    public void lockDoor() {
        if (isOpen) {
            System.out.println("Open door cannot be locked!");
            return;
        } else if (!isOpen && isLocked) {
            System.out.println("Door already locked!");
            return;
        }
        System.out.println("Enter your code Number to set the lock code:");
        int enteredCode = sc.nextInt();
        code = enteredCode;
        isLocked = true;
        System.out.println("Door locked!");
        return;
    }

    @Override
    public void unlockDoor() {
        if (!isLocked) {
            System.out.println("Door is not locked!");
            return;
        }
        System.out.println("Enter the code to unlock the door:");
        int enteredCode = sc.nextInt();
        if (enteredCode == code) {
            isLocked = false;
            System.out.println("Door unlocked!");
            return;
        }
        System.out.println("Invalid code!");
        return;
    }
}
