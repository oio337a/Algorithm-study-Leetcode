public class PermutationInString_567 {
    public boolean checkInclusion(String s1, String s2) {
        int total = s1.length();
        int len = s2.length();
        int start = 0;
        int end = start + total;
        int t = 0;
        int[] lowerAlpha = new int[123]; // 97 ~123
        int[] tmp = new int[123];
        for (int i = 0; i < total; i++) lowerAlpha[s1.charAt(i)]++;
        boolean flag = true;
        while (true)
        {
//            System.out.println("start = " + start);
//            System.out.println("flag = " + flag);
//            System.out.println("t = " + t);
//            System.out.println("tmp[a] = " + tmp[97]);
//            System.out.println("tmp[b] = " + tmp[98]);
            end = start + total;
            if (end > len) break;
            if (flag) // 다 돌려 봐야 함
            {
                boolean subFlag = false;
                for (int i = start; i < end; i++)
                {
                    int c = s2.charAt(i);
                    if (lowerAlpha[c] > 0) // s1에 있음
                    {
                        if (tmp[c] < lowerAlpha[c]) t++; // 아직 덜 고름
                        tmp[c]++;
                    }
                    else // s1에 없음
                    {
                        start = i + 1;
                        t = 0;
                        tmp = new int[123];
                        subFlag = true;
                        break;
                    }
                }
                if (t == total) return true;
                if (subFlag) flag = true; // 안 이어짐
                else // 이어짐
                {
                    if (tmp[s2.charAt(start)] <= lowerAlpha[s2.charAt(start)]) t--;
                    tmp[s2.charAt(start)]--;
                    flag = false;
                    start += 1;
                }
            }
            else // 이어짐
            {
                boolean subFlag = false;
                int c = s2.charAt(end - 1);
                if (lowerAlpha[c] > 0)
                {
                    if (tmp[c] < lowerAlpha[c]) t++;
                    tmp[c]++;
                }
                else
                {
                    start = end;
                    t = 0;
                    tmp = new int[123];
                    subFlag = true;
                }
                if (t == total) return true;
                if (subFlag) flag = true;
                else
                {
                    if (tmp[s2.charAt(start)] <= lowerAlpha[s2.charAt(start)]) t--;
                    tmp[s2.charAt(start)]--;
                    flag = false;
                    start += 1;
                }
            }
        }
        return false;
    }

    public static void main(String[] args) {
        String s1 = "aabbb";
        String s2 = "baabcaabb";
        PermutationInString_567 tmp = new PermutationInString_567();
        System.out.println(tmp.checkInclusion(s1, s2));
    }
}
