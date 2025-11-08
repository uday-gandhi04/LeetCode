class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        int j = nums.length - 1;

        while (i <= j) {
            if (nums[i] == val) {
                // Move j backward until we find a non-val element
                while (j >= i && nums[j] == val) {
                    j--;
                }
                if (i < j) {
                    nums[i] = nums[j];
                    j--;
                }
            }
            i++;
        }
        // j points to last valid element, so new length = j + 1
        return j + 1;
    }
}
