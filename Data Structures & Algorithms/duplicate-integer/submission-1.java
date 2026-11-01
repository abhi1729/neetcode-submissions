class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> matchSet = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            if(!matchSet.contains(nums[i])){
                matchSet.add(nums[i]);
            }
            else{
                return true;
            }
        }
        return false;
    }
}