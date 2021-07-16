

public class Main {
    public static void main(String args[]) {
        JDBC jdbc;
        for (int i = 0; i < 5; i++) {
            jdbc = JDBC.getInstance();
            System.out.println("Number of created objects = " + jdbc.getCount());
        }

    }
}

class JDBC {
    private static JDBC instance;
    private static int count = 0;

    private JDBC() {
        count++;
    }

    /** Lazy initialization */
    public static JDBC getInstance() {
        if (instance == null) instance = new JDBC();
        return instance;
    }

    public int getCount() {
        return count;
    }
}
