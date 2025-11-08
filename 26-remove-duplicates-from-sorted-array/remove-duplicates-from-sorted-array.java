class Solution {
    public int removeDuplicates(int[] nums) {
        Set<Integer> s = new LinkedHashSet <>();
        int n=nums.length;
        for ( int i = 0 ; i<n ;i++){
            s.add(nums[i]);
        }
        int i=0;

        for ( int num : s) {
            nums[i++]=num;
        }

        return s.size();
        
    }
}