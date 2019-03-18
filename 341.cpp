#include <vector>
#include <stack>
using namespace std;

class NestedIterator {
private:
    stack<NestedInteger> _stack;
    
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        for (int i = nestedList.size() - 1; i >= 0; i--) {
            _stack.push(nestedList[i]);    
        }
    }

    int next() {
        int val = _stack.top().getInteger();
        _stack.pop();
        return val;
    }

    bool hasNext() {
        if (_stack.top().isInteger()) {
            return true;
        }
        else {
            vector<NestedInteger> listValue;
            for (auto unit: _stack.top().getList()) {
                listValue.push_back(unit);
            }
            
            _stack.pop();

            for (int i = listValue.size() - 1; i >= 0; i--) {
                _stack.push(listValue[i]);
            }
            if (_stack.empty())
            {
                return false;
            }
            return hasNext();
        }
    }
};

