class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        Map<Integer,Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++){
                int test = target - nums[i];
                if (map.containsKey(test)){
                    result[1] = i;
                    result[0] = map.get(test);
                    return result;
                }
                map.put(nums[i], i);
            }
        return null;
    }
}