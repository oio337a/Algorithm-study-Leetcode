class Solution {
	public void reverseString(char[] s) {
			int i = 0;
			int len = s.length - 1;
			while (i < len) {
					char tmp = s[i];
					s[i] = s[len];
					s[len] = tmp;
					i++;
					len--;
			}
	}
}
