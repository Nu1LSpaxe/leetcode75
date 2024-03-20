class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.strip().split(" ")[::-1]


        return " ".join([i for i in s if i])
    
    """
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")[::-1]

        result = []

        for i in s:
            if i is not '':
                result.append(i)

        return " ".join(result)
    """