public class Solution {
	public boolean checkInclusion(String s1, String s2) {
			int[] count = new int[26]; // a-z 26개라 메모리 적게 하려고 a 빼면서 다녔어여

			if (s1.length() > s2.length())
					return false;
			/*
			 * 1. s1만큼 검수를 하면서 카운터에 s1의 문자가 위치한 곳은 더해주고, s2의 문자가 위치한 곳은 빼줌
			 * 2. 완성된 카운터가 모두 다 0인가? 그럼 s1을 포함했음 true 반환 끝
			 */
			for (int i = 0; i < s1.length(); i++) { 
					count[s1.charAt(i) - 'a']++;
					count[s2.charAt(i) - 'a']--;
			}
			if (isZero(count))
					return true;

			/*
			 * s1만큼 검수를 했는데 모두 0으로 안끝났다 == s1의 길이만큼에선 포함하지 않았다.
			 * 그럼 s1 길이 뒤부터 s2 끝나기 전까지 값들을 검수해보자
			 * 카운터의 s2 문자를 빼주면서 기준의 왼쪽 값에는 더해주는 방식으로 검수를 마저 한다
			 * 더하고 빼고 한 뒤에 한바퀴 돌아서 카운터가 모두 0이다? s1을 뒤에서라도 포함했다 true
			 * 끝까지 카운터가 모두 0이되는 케이스가 없다 == s1을 연속적으로 포함하지 않았다 false
			 */
			for (int i = s1.length(); i < s2.length(); i++) {
					count[s2.charAt(i) - 'a']--;
					count[s2.charAt(i - s1.length()) - 'a']++;
					if (isZero(count))
							return true;
			}
			return false;
	}

	public boolean isZero(int[] count) {
			for (int i = 0; i < count.length; i++) {
					if (count[i] != 0)
							return false;
			}
			return true;
	}
}