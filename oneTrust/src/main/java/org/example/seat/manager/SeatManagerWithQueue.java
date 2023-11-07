package org.example.seat.manager;

import java.util.PriorityQueue;
import java.util.Queue;

public class SeatManagerWithQueue implements SeatManagerSolution{

    private final Queue<Integer> seats;

    public SeatManagerWithQueue(int n){
        this.seats = new PriorityQueue<>(n);
        for(int i=1;i<=n;i++){
            seats.offer(i);
        }
    }
    @Override
    public int reserve() {
        return seats.poll();
    }

    @Override
    public void unreserve(final int seatNumber) {
        seats.offer(seatNumber);
    }
}
