public class ReverseBits_190 {
    public int reverseBits(int n) {
        int output = 0;
        for (int i = 0; i < 32; i++) {
            if ((n & 1) == 1) output++;
            n = n >> 1;
            if (i == 31) break;
            output = output << 1;
        }
        return output;
    }

    public static void main(String[] args) {
        ReverseBits_190 tmp = new ReverseBits_190();
        int n = 43261596;
        System.out.println(tmp.reverseBits(n));
    }
    // 964176192
}
