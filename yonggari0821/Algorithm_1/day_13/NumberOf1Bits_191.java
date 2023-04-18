public class NumberOf1Bits_191 {
    public int hammingWeight(int n) {
        // return Integer.bitCount(n); // cheat
        int cnt = 0;
        for (int i = 0; i < 32; i++) // while (n > 0) 으로 하면 틀림!! java의 음수 표현법 == 2의 보수
        {
            cnt += (n & 1);
            n = n >>> 1;
        }
        return cnt;
    }

    public static void main(String[] args) {
        NumberOf1Bits_191 tmp = new NumberOf1Bits_191();
        int n = 11;
        System.out.println(tmp.hammingWeight(n));
    }
}
