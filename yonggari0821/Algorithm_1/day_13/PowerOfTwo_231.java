public class PowerOfTwo_231 {
    public boolean isPowerOfTwo(int n) {
        if (n < 1) return false;
        else if (n <= 2) return true;
        int a = 1;
        int digit = 0;
        for (int i = 0; i < 31; i++)
        {
            if ((n & a) != 0) digit++;
            if (digit > 1) return false;
            a = a << 1;
        }
        if (digit > 1) return false;
        else return true;
    }

    /*
    cf) simple code
    1. return (n > 0 && (n & n - 1 == 0)); => n 이 2의 제곱수 일때만 100...0이라 & 연산 했을 때 0이 나올 수 있음!
    2. return (n > 0 && Integer.bitCount(n) == 1); => 비트가 1인 갯수를 세서 알려주는 자바 Integer 클래스 메서드
     */

    public static void main(String[] args) {
        PowerOfTwo_231 tmp = new PowerOfTwo_231();
        int n = 1073741824;
        System.out.println(n);
        System.out.println(tmp.isPowerOfTwo(n));
    }
}
