package seat.manager;

import org.example.seat.manager.SeatManager;
import org.example.seat.manager.SeatManagerSolution;
import org.example.seat.manager.SeatManagerWithQueue;
import org.junit.Test;

import static org.junit.Assert.assertEquals;

public class SeatManagerTest {


    @Test
    public void reserveTest(){
        SeatManagerSolution seatManagerSolution = new SeatManagerWithQueue(3);
        int reserve = seatManagerSolution.reserve();
        assertEquals(1, reserve);
    }

    @Test
    public void reserveAllTest(){
        SeatManagerSolution seatManagerSolution = new SeatManagerWithQueue(3);
        seatManagerSolution.reserve();
        seatManagerSolution.reserve();
        int reserve = seatManagerSolution.reserve();
        assertEquals(3, reserve);
    }

    @Test
    public void unreserveTest(){
        SeatManagerSolution seatManagerSolution = new SeatManagerWithQueue(3);
        seatManagerSolution.reserve();
        seatManagerSolution.reserve();
        seatManagerSolution.unreserve(1);
        int reserve = seatManagerSolution.reserve();
        assertEquals(1, reserve);
    }

    @Test
    public void unreserveFirstTest(){
        SeatManagerSolution seatManagerSolution = new SeatManagerWithQueue(3);
        seatManagerSolution.reserve();
        seatManagerSolution.unreserve(1);
        int reserve = seatManagerSolution.reserve();
        assertEquals(1, reserve);
    }

    @Test
    public void unreserveLastTest(){
        SeatManagerSolution seatManagerSolution = new SeatManagerWithQueue(3);
        seatManagerSolution.reserve();
        seatManagerSolution.reserve();
        seatManagerSolution.reserve();
        seatManagerSolution.unreserve(3);
        int reserve = seatManagerSolution.reserve();
        assertEquals(3, reserve);
    }

}
