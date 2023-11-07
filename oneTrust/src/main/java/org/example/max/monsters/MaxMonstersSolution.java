package org.example.max.monsters;

import java.util.Arrays;

public class MaxMonstersSolution {
    public int eliminateMaximum(int[] dist, int[] speed) {
        double[] time = new double[dist.length];
        for (int i = 0; i < dist.length; i++) {
            time[i] = dist[i] / (double) speed[i];
        }
        Arrays.sort(time);

        for (int i = 0; i < time.length; i++) {
            if (time[i] <= i) {
                return i;
            }
        }
        return time.length;
    }
}
