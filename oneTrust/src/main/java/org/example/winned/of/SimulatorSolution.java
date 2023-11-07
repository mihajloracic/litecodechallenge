package org.example.winned.of;

import java.util.ArrayList;
import java.util.List;

public class SimulatorSolution implements Solution{

    @Override
    public int getWinner(final int[] arr, final int k) {
        final List<Integer> list = new ArrayList<>(arr.length);
        for (int value : arr) {
            list.add(value); // Auto-boxing from int to Integer
        }
        if(k > list.size()){
            return list.stream().max(Integer::compare).get();
        }
        int winStreak = 0;
        int winner = list.get(0);
        while(winStreak < k) {
            if(winner > list.get(1)){
                winStreak++;
                list.add(list.remove(1));
            } else {
                winner = list.get(1);
                list.add(list.remove(0));
                winStreak = 1;
            }
            if(winStreak == k){
                return winner;
            }
            //shift list
        }
        return 0;
    }
}
