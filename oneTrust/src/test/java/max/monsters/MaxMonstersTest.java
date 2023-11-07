package max.monsters;

import org.example.max.monsters.MaxMonstersSolution;
import org.example.winner.of.SimulatorSolution;
import org.example.winner.of.Solution;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class MaxMonstersTest {

    private final MaxMonstersSolution solution = new MaxMonstersSolution();

    @Test
    public void simpleTest(){
        int[] dists = new int[]{1,2,3};
        int[] speeds = new int[]{1,1,1};
        int numberOfEliminatedMonsters = solution.eliminateMaximum(dists, speeds);

        assertEquals(3, numberOfEliminatedMonsters); // JUnit assertion
    }

    @Test
    public void simpleTestWith1(){
        int[] dists = new int[]{1};
        int[] speeds = new int[]{1};
        int numberOfEliminatedMonsters = solution.eliminateMaximum(dists, speeds);

        assertEquals(1, numberOfEliminatedMonsters); // JUnit assertion
    }

    @Test
    public void ifShoots2(){
        int[] dists = new int[]{1, 3, 3};
        int[] speeds = new int[]{2, 2, 2};
        int numberOfEliminatedMonsters = solution.eliminateMaximum(dists, speeds);

        assertEquals(2, numberOfEliminatedMonsters); // JUnit assertion
    }

    @Test
    public void ifShoots1(){
        int[] dists = new int[]{1, 1, 1};
        int[] speeds = new int[]{1, 1, 1};
        int numberOfEliminatedMonsters = solution.eliminateMaximum(dists, speeds);

        assertEquals(1, numberOfEliminatedMonsters); // JUnit assertion
    }

    @Test
    public void leetCodeExample(){
        int[] dists = new int[]{1,1,2,3};
        int[] speeds = new int[]{1, 1, 1, 1};
        int numberOfEliminatedMonsters = solution.eliminateMaximum(dists, speeds);

        assertEquals(1, numberOfEliminatedMonsters); // JUnit assertion
    }

}
