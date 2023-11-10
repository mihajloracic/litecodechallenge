package cell.reachable;

import org.example.cell.reacheable.Solution;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class CellReachableTest {

    @Test
    public void simpleTestTrue() {
        Solution solution = new Solution();

        boolean reachableAtTime = solution.isReachableAtTime(1, 1, 2, 2, 1);

        assertEquals(true, reachableAtTime);
    }

    @Test
    public void simpleTestFalse() {
        Solution solution = new Solution();

        boolean reachableAtTime = solution.isReachableAtTime(1, 1, 3, 3, 1);

        assertEquals(false, reachableAtTime);
    }

    @Test
    public void leetCodeExample1() {
        Solution solution = new Solution();

        boolean reachableAtTime = solution.isReachableAtTime(2, 4, 7, 7, 6);

        assertEquals(true, reachableAtTime);
    }

    @Test
    public void leetCodeExample2() {
        Solution solution = new Solution();

        boolean reachableAtTime = solution.isReachableAtTime(3, 1, 7, 3, 3);

        assertEquals(false, reachableAtTime);
    }

    @Test
    public void leetCodeTestWhereFieldIsReachableButHasToStepOut() {
        Solution solution = new Solution();
        boolean reachableAtTime = solution.isReachableAtTime(1, 2, 1, 2, 1);

        assertEquals(false, reachableAtTime);
    }

    @Test
    public void leetCodeReachable() {
        Solution solution = new Solution();
        boolean reachableAtTime = solution.isReachableAtTime(1, 3, 2, 2, 2);

        assertEquals(true, reachableAtTime);
    }
}
