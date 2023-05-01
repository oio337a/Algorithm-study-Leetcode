/*
    가장 밑줄을 초기 dp 테이블로 세팅하고, 그 윗줄부터 하니씩 타고 올라가면서 검수하는 방식

    1) 가장 밑 부분읠 크기만큼 dp 테이블을 1차원 배열로 만들어 초기값을 세팅합니다
    2) triangle을 한줄 씩 위로 올리면서 dp 테이블과 비교하며 검수
    3) 이전 집털기 로직과 유사, dp table 위의 j, j + 1 인자들 중 min을 구합니다 
        -> 이러면 triangle 원본의 위치에서 근처의 idx들임을 보장
    4) triangle 값을 더해서 dp table 값을 업데이트하는 방식
 */

class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int[] bottom = new int[triangle.size()];
        int height = triangle.size() - 1;
        for (int i = 0; i < triangle.get(height).size(); i++)
            bottom[i] = triangle.get(height).get(i);
        for (int i = height - 1; i >= 0; i--) {
            for (int j = 0; j < triangle.get(i).size(); j++)
                bottom[j] = Math.min(bottom[j], bottom[j + 1]) + triangle.get(i).get(j);
        }
        return bottom[0];
    }
}