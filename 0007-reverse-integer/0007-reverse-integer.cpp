class Solution {
public:
    int reverse(int x) {
        int lastDigit;
        int n = 0;

        while(x != 0){
            lastDigit = x % 10;

            //checking for overflow before multiplying
            if (n > INT_MAX/10 || (n == INT_MAX/10 && lastDigit > 7))
            return 0;
            if (n < INT_MIN/10 || (n == INT_MIN/10 && lastDigit < -8))
                return 0;

            n = n * 10 + lastDigit;
            x = x/10;
        }
        return n;
    }
};