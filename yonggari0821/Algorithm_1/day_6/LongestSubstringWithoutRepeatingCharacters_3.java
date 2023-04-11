public class LongestSubstringWithoutRepeatingCharacters_3 {
    public int lengthOfLongestSubstring(String s) {
        int max = 0;
        for (int i = 0; i < s.length(); i++) {
            boolean[] used = new boolean[127];
            used[s.charAt(i)] = true;
            int tmp = 1;
            for (int j = i + 1; j < s.length(); j++) {
                if (!used[s.charAt(j)])
                {
                    used[s.charAt(j)] = true;
                    tmp++;
                }
                else break;
            }
            max = max > tmp ? max : tmp;
        }
        return max;
    }

    public int lengthOfLongestSubstringBySlidingWindow(String s) {
        int[] map = new int[128]; // 각 글자가 마지막에 나온 자리 인덱스 + 1
        int res = 0; // 최종적으로 가장 긴 길이
        int end = 0; // 마지막으로 끊긴 지점 => 여기까진 볼 필요 없음
        for(int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            end = Math.max(end, map[c]);
            res = Math.max(res, i + 1 - end);
            map[c] = i + 1;
        }
        return res;
    }

    public static void main(String[] args) {
        String s = "pwwkew";
        LongestSubstringWithoutRepeatingCharacters_3 tmp = new LongestSubstringWithoutRepeatingCharacters_3();
        System.out.println(tmp.lengthOfLongestSubstring(s));
    }
}
