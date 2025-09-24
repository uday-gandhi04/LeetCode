class Solution {
    public boolean isPalindrome(String s) {
        String sb = s.replaceAll("[^a-zA-Z0-9]", "");
        System.out.println(sb);
        int n = sb.length();

        for (int i=0; i<n/2;i++){
            if (Character.toLowerCase(sb.charAt(i))!=Character.toLowerCase(sb.charAt(n-i-1))){
                return false;
            }
        }      

        return true;

    }
}