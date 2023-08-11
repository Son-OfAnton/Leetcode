class Solution {
public:
    int getSum(int a, int b) {
        if(b == 0) 
            return a;
        return getSum(a ^ b, (a & b) << 1);
    }
};

/*
    Single bit addition is almost the same as the XOR.
    The only difference is that when both bits are set
    addition passes a carry on top of producing a zero
    output. The carry will be transferred to the next
    pair of bits to the left. Basically arithmetic addition
    is XORing every pair bit and transfering the carry to
    the left. The carry for a pair of bits if found be ANDing
    them. So we will keep adding the carry until the carry 
    becomes zero.

*/