import java.util.ArrayList;
import java.util.List;

public class Permutations_46 {
    static int len;
    static int[] numbers;
    static List<List<Integer>> ans;
    static void recursive (boolean[] pick, List<Integer> list)
    {
        if (list.size() == len)
        {
            ans.add(new ArrayList<>(list));
            return ;
        }
        for (int i = 0; i < len; i++)
        {
            if (!pick[i])
            {
                pick[i] = true;
                list.add(numbers[i]);
                recursive(pick, list);
                pick[i] = false;
                list.remove(list.size() - 1);
            }
        }
    }
    public List<List<Integer>> permute(int[] nums) {
        len = nums.length;
        boolean[] picked = new boolean[len];
        numbers = nums;
        ans = new ArrayList<>();
        recursive(picked, new ArrayList<>());
        return ans;
    }

    public static void main(String[] args) {
        int[] nums = {1, 2, 3};
        Permutations_46 tmp = new Permutations_46();
        tmp.permute(nums);
        System.out.println(ans);
    }
}
