package org.example.cell.reacheable;

public class Solution {

    public boolean isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        int x_dist = Math.abs(sx - fx);
        int y_dist = Math.abs(sy - fy);
        int dist = Math.max(x_dist, y_dist);
        return x_dist <= t && y_dist <= t && !(dist == 0 && t == 1);
    }
}
