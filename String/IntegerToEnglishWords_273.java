// Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.
// So at most the number is around 2 Billion.
// Reference: https://www.youtube.com/watch?v=RwFQvF0xx_k&t=398s
class Solution {
    String[] thousands = {"", "Thousand", "Million", "Billion"};
    String[] lessthan20 = {"", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", 
    "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"};
    String[] tens = {"", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"};
    public String numberToWords(int num) { 
        if (num == 0) 
            return "Zero";
        int i = 0;
        String res = "";
        while (num > 0){
            if (num % 1000 != 0){
                res = helper(num % 1000) + thousands[i] + " " + res;
            }
            i++;
            num /= 1000;
        }
        return res.trim()   ;
    }
    
    public String helper(int num){
        if (num == 0) return "";
        else if (num < 20) return lessthan20[num] + " ";
        else if (num < 100) return tens[num/10] + " " + helper(num%10);
        else return lessthan20[num/100] + " " + "Hundred" + " " + helper(num%100);
    }
}
