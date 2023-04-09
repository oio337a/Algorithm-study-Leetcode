import java.util.Arrays;

public class ReverseString_344 {
    public void reverseString(char[] s) {
        int end = s.length - 1;
        for (int i = 0; i <= end / 2; i++)
        {
            char tmp = s[i];
            s[i] = s[end - i];
            s[end - i] = tmp;
        }
    }

    public static void main(String[] args) {
        ReverseString_344 tmp = new ReverseString_344();
        char[] s = {'a','b','c','d','e','f'};
        tmp.reverseString(s);
        System.out.println(Arrays.toString(s));
    }
}
