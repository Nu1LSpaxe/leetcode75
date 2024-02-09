class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # two strings are 'close' if they can equal by executing operations (no limit times)
        # operation 1: swap any two existing elements
        # operation 2: transform every occurence of two existing elements

        # length must equal
        if len(word1) != len(word2): return False

        # occurence array should be the same, i.e. [1,2,3] != [2,2,2], although amount equal
        lis1 = sorted([word1.count(i) for i in set(word1)])
        lis2 = sorted([word2.count(i) for i in set(word2)])

        # the precondition of operation2 is "two sets must equal", otherwise no elements can be changed.
        return lis1 == lis2 and set(word1) == set(word2)