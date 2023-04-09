class Solution {
	public String reverseWords(String s) {
			/*
			 * 자바으 str 뒤집기는
			 * 1. stringbuilder / buffer의 reverse 함수 사용
			 * 2. char[]를 정성스럽게 하나씩 뒤집는다
			 * 344에서 정성스럽게 뒤집었으니 이번엔 함수를 사용해보겠슴다
			 */
			String[] tmp = s.split(" "); // 공백 기준으로 str 덩어리들을 뒤집어야하므로, string 배열로 나눠줌다
			StringBuffer res = new StringBuffer();
			for (String str : tmp) { // 나눠진 string 배열들을 돌면서 뒤집은 결과 값들을 res에 저장
				StringBuffer sb = new StringBuffer(str);
				res.append(sb.reverse() + " ");
			}

			return (res.toString().substring(0, s.length())); // stringbuffer->string 변환, 끝에 달린 스페이스바 제거
	}
}