package LeetCode;

public class FirstBadVersion_278 extends VersionControl {
    /* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */
    public int firstBadVersion(int n) {
        if (n == 1) return 1;
        int start = 1;
        int end = n;
        while (start <= end)
        {
            int mid = start + (end - start) / 2;
            if (!isBadVersion(mid)) start = mid + 1;
            else end = mid - 1;
        }
        return start;
    }
}
