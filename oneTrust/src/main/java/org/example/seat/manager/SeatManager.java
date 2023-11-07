package org.example.seat.manager;

import java.util.ArrayList;
import java.util.List;

public class SeatManager implements SeatManagerSolution{

    private final List<Boolean> seats;

    public SeatManager(int n){
        seats = new ArrayList<>(n);
        for(int i=0;i<n;i++){
            seats.add(false);
        }
    }
    @Override
    public int reserve() {
        for(int i=0;i<seats.size();i++){
            if(!seats.get(i)){
                seats.set(i , true);
                return i+1;
            }
        }
        throw new RuntimeException("No free seats");
    }

    @Override
    public void unreserve(final int seatNumber) {
        seats.set(seatNumber-1, false);
    }
}
