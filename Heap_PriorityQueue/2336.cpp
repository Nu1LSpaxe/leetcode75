#include <iostream>
#include <set>

class SmallestInfiniteSet {
public:
    SmallestInfiniteSet() {
        for (int i = 1; i <= 1000; i++)
            s.insert(i);
    }

    int popSmallest() {
        int smallest = *s.begin();
        s.erase(s.begin());
        return smallest;
    }

    void addBack(int num) {
        s.insert(num);
    }

private:
    std::set<int> s;
};

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet* obj = new SmallestInfiniteSet();
 * int param_1 = obj->popSmallest();
 * obj->addBack(num);
 */