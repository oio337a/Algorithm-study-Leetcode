import java.util.ArrayList;
import java.util.List;

public class LetterCasePermutation_784 {
    static int len;
    static List<String> ans;
    static String str;
    static char change(char c) // 숫자인 경우도 포함해서 만들어봤습니다.
    {
        if (c >= 48 && c <= 57) return c; // 숫자면 그대로
        else if (c >= 65 && c <= 90) return (char) (c + 32); // 대문자 => 소문자
        else if (c >= 97 && c <= 122) return (char) (c - 32); // 소문자 => 대문자
        else return c; // 원래는 예외처리해야 함
    }
    static void recursive(StringBuilder tsb, int index) // 1) 인덱스 이용하는 방법 2) 매 번 tsb.length 구하는 방법
    {
        if (index == len)
        {
            ans.add(tsb.toString());
            return ;
        }
        else
        {
            char ver1 = str.charAt(index); // 바뀌기 전
            char ver2 = change(ver1); // 바뀐 후
            if (ver1 == ver2) // 같음 => 숫자인 경우
            {
                tsb.append(ver1);
                recursive(tsb, index + 1);
                tsb.deleteCharAt(tsb.length() - 1);
            }
            else // 다름 => 알파벳인 경우 => ver1과 ver2로 모두 재귀 실행 => 즉, 알파벳 하나당 경우의수 x 2 => 최종 경우의 수 == 2의 알파벳 수 제곱
            {
                tsb.append(ver1);
                recursive(tsb, index + 1);
                tsb.deleteCharAt(tsb.length() - 1);
                tsb.append(ver2);
                recursive(tsb, index + 1);
                tsb.deleteCharAt(tsb.length() - 1);
            }
        }
    }
    public List<String> letterCasePermutation(String s) {
        if (s == null) return null;
        str = s;
        len = s.length();
        ans = new ArrayList<>();
        recursive(new StringBuilder(), 0);
        return ans;
    }

    public static void main(String[] args) {
        LetterCasePermutation_784 tmp = new LetterCasePermutation_784();
        String s = "a1b2";
        tmp.letterCasePermutation(s);
        System.out.println(ans);
        // a1b2 A1b2 a1B2 A1B2
    }
}