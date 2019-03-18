#include <iostream>
#include <unordered_map>

using namespace std;



class Solution {
    
private:
    
public:
    inline size_t key(int i,int j) {return (size_t) i << 32 | (unsigned int) j;}
    
    int dfs(int start, int end) {
        if (start >= end) {
            return 1;
        }
        
        // if (mem.find(key(start, end)) != mem.end()) {
        //     return mem[key(start, end)];
        // }
        
        
        int res = 0;
        for (auto index = start; index <= end; index ++) {
            res += dfs(start, index - 1) * dfs(index + 1, end);
        }
        
        // mem[key(start, end)] = res;
        return res;
    }
    
    int numTrees(int n) {
        return dfs(1, n);
    }
};


int main() {
    cout << Solution().numTrees(5) << endl;
    int a;
    cin >> a;
    return 0;
}
