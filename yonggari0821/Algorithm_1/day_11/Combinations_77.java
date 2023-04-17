import java.util.*;

public class Combinations_77 {
    static int N, K;
    static List<List<Integer>> ans = new ArrayList<>();

    static void recursive(List<Integer> list, int last)
    {
        if (list.size() == K)
        {
//            List<Integer> toput = new ArrayList<>();
//            toput.addAll(list);
//            ans.add(toput);
            ans.add(new ArrayList<>(list));
            return ;
        }
        for (int i = last + 1; i <= N; i++)
        {
            list.add(i);
            recursive(list, i);
            list.remove(list.size() - 1);
        }
    }
    public List<List<Integer>> combine(int n, int k) {
        N = n;
        K = k;
        List<Integer> tmp = new ArrayList<Integer>();
        recursive(tmp, 0);
        return ans;
    }
/* 시간 복잡도랑 공간 복잡도 측면에서 되게 좋은 코드가 있어서 클론 코딩 해보려고 넣었습니다. 제 코드랑 비교해보려구요.
    public List<List<Integer>> combine(int n, int k) {
        List<Integer> comb = new ArrayList<Integer>();
        List<List<Integer>> result = new ArrayList<List<Integer>>();

        function(1, k, n, comb, result); // 매개 변수로 현재 넣어야 되는 값, 골라야할 갯수, 고를 수 있는 수의 최대 값, 조합 1개, 최종 조합들의 리스트를 넘겨줌
        => 저는 이 부분에서 상당 부분을 static으로 뺐는데 이 코드가 시공간 복잡도 모두에서 더 좋더라구요. 이유를 잘 모르겠습니다...

        return result;
    }

    public void function(int pos, int k, int limit, List<Integer> comb, List<List<Integer>> result){

        if(comb.size() + (limit - pos + 1) < k ) return;
        // 이 부분이 이 코드의 시공간복잡도를 줄여주는데 상당한 기여를 하는 거 같습니다.
        리스트의 사이즈 + 넣을 수 있는 최대 값 - 넣어주려는 값 + 1 < 고른 갯수 이면 바로 리턴을 하는데
        예를 들면 [1, 2, 3, 4, 5] k = 3 일 때,
        [3] pos = 5면 1 + 5 - 5 + 1 < 3 이므로 5를 추가한 다음, 그 다음을 볼 필요가 없이 바로 리턴이 됩니다.
        즉 처음 넣은 값부터 가능한 곳까지만 넣고 나머지는 아예 보지도 않습니다.

        if(comb.size() == k){
            result.add(new ArrayList<>(comb));
            return;
        }

        for(int i= pos;i<= limit;i++){

            comb.add(i);
            function(i+1, k, limit, comb, result);
            comb.remove(comb.size()-1);
        }
    }
 */

    public static void main(String[] args) {
        Combinations_77 tmp = new Combinations_77();
        int tn = 4;
        int tk = 2;
        int i = 0;
        tmp.combine(tn, tk);
        while (i < ans.size()) System.out.println(ans.get(i++));
    }
}
