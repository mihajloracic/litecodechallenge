package of;

import org.example.winned.of.SimulatorSolution;
import org.example.winned.of.Solution;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class ArrayGameTest {

    private final Solution solution = new SimulatorSolution();

    @Test
    public void simpleTest(){
        int[] array = new int[]{1,2,3};
        int k = 10;
        int winner = solution.getWinner(array, k);

        assertEquals(3, winner); // JUnit assertion
    }

    @Test
    public void testWithDifferentOrder(){
        int[] array = new int[]{3,2,1};
        int k = 10;
        int winner = solution.getWinner(array, k);

        assertEquals(3, winner); // JUnit assertion
    }

    @Test
    public void notMaxWinsInTime(){
        int[] array = new int[]{2,1,3,5,4,6,7};
        int k = 2;
        int winner = solution.getWinner(array, k);

        assertEquals(5, winner); // JUnit assertion
    }

    @Test
    public void largerThanArraySizeMaxAlwaysWins(){
        int[] array = new int[]{2,1,3,5,4,6,7};
        int k = 15;
        int winner = solution.getWinner(array, k);

        assertEquals(7, winner); // JUnit assertion
    }

    @Test
    public void kLargerThanArrays(){
        int[] array = new int[]{1,11,22,33,44,55,66,77,88,99};
        int k = 1000000000;
        int winner = solution.getWinner(array, k);

        assertEquals(99, winner); // JUnit assertion
    }
}
