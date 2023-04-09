import java.util.Arrays;

public class ReverseWordsInAString_557 {
    public String reverseWords(String s) {
        int len = s.length();
        if (len == 1) return s;
        int start = 0;
        StringBuilder sb = new StringBuilder(s);
        while (start < len)
        {
            char tmp = sb.charAt(start);
            if (tmp != ' ')
            {
                int end = start + 1;
                while (end < len && sb.charAt(end) != ' ') end++;
                int next = end + 1;
                end--;
                while(start < end)
                {
                    tmp = sb.charAt(start);
                    sb.setCharAt(start, sb.charAt(end));
                    sb.setCharAt(end, tmp);
                    start++;
                    end--;
                }
                start = next;
            }
            else start++;
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        ReverseWordsInAString_557 tmp = new ReverseWordsInAString_557();
        String s = "abc def ghijkl mnop";
        System.out.println(tmp.reverseWords(s));
    }
}
