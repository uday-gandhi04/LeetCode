class Solution {
    public int sumFourDivisors(int[] nums) {

        int out=0;

        for (int i =0; i<nums.length;i++){
            int temp=0;
            int count=0;
            for (int j=1;j<nums[i]+1;j++){
                if (nums[i]%j==0){
                    count+=1;
                    temp+=j;
                    if (count>4){
                        break;
                    }
                }
            }
        
            if (count==4){
                out+=temp;
            }
        }

        return out;
        
    }
}