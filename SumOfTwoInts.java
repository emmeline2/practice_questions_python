class Solution {
    public int getSum(int a, int b) {
        
        // while there is still a carry value
        while(b != 0){
            int sum = a ^ b; // xor
            int carry = (a & b) << 1; 
            a = sum; // a holds current sum
            b = carry; // b holds current carry
        }

        return a;
    }
}
