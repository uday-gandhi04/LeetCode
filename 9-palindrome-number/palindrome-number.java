class Solution {
    public boolean isPalindrome(int x) {

        if (x<0){
            return false;
        }

        ArrayList<Integer> arr = new ArrayList<>();

        int temp=x;

        while(temp>0){

            arr.add(temp%10);
            temp/=10;
        }

        int n=arr.size(); 

        for (int i=0; i<n/2;i++){
            if (arr.get(i)!=arr.get(n-i-1)){
                return false;
            }
        }      

        return true;
    }
}