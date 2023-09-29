class TrieNode {
public:
    TrieNode() {
        children[0] = nullptr;
        children[1] = nullptr;
        val = 0;
    }
    TrieNode* children[2];
    int val;
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }
    void insert(int num) {
        TrieNode* curr = root;
        for (int i = 31; i >= 0; i--) {
            int bit_val = (num & (1 << i)) ? 1 : 0;
            if (!curr->children[bit_val]) {
                curr->children[bit_val] = new TrieNode();
            }
            curr = curr->children[bit_val];
        }
        curr->val = num;
    }
    int findMaxXOR(int num) {
        TrieNode* curr = root;
        for (int i = 31; i >= 0; i--) {
            int bit = (num & (1 << i)) ? 1 : 0;
            int opposite_bit = 1 - bit;
            if (curr->children[opposite_bit]) {
                curr = curr->children[opposite_bit];
            } else {
                curr = curr->children[bit];
            }
        }
        return (curr->val != 0) ? curr->val : 0;
    }
private:
    TrieNode* root;
};


class Solution {
public:
    int findMaximumXOR(vector<int>& nums) {
        Trie bitTrie;

        for (int num : nums) {
            bitTrie.insert(num);
        }

        int max_xor = 0;
        for (int num : nums) {
            int best_xor_pair = bitTrie.findMaxXOR(num);
            max_xor = std::max(max_xor, best_xor_pair ^ num);
        }

        return max_xor;
    }
};