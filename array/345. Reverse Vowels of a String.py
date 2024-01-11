### Question ###
"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Constraints:
# 1 <= s.length <= 3 * 10^5
# s consist of printable ASCII characters.
"""

### Algorithm ###
"""
First Method:
- Create a vowel list
- Record vowels in string
- Iterate string from the end, if the char is in vowel, then replace by record (from start to iterate)

```
string = [*s]
vowels = set("aeiouAEIOU")
vowelsRecord = []

for vowel in string:
        if vowel in vowels: vowelsRecord.append(vowel)

vowelsRecord.reverse()

for i in range(len(string)):
        if string[i] in vowels: 
            string[i] = vowelsRecord[0]
            vowelsRecord.pop(0)

"".join(string)
```

Second Method (Better):
Avoid to spend O(N) as first idea -> Use Two Pointer to track vowels, and then exchange them.

```
left = 0
right = len(s) - 1
string = [*s]
vowels = "aeiouAEIOU"

while left < right:
    if string[left] not in vowels: left += 1
    if string[right] not in vowels: right -= 1 

    if string[left] in vowels and string[right] in vowels:
        string[left], string[right] = string[right], string[left]
        left += 1
        right -= 1

return "".join(string)
```


# Little tricks to takeaway:
    string unpack method: [*string], or just list(string) also works.
"""

### Complexity ###
"""
Time complexity:
First Method takes O(N) by one-dimensional loop
Second Method takes O(N/2) by two pointers
"""

### Implementation ###

def reverseVowels(s: str) -> str:
        left = 0
        right = len(s) - 1
        string = [*s]
        vowels = "aeiouAEIOU"

        while left < right:
            if string[left] not in vowels: left += 1
            if string[right] not in vowels: right -= 1 

            if string[left] in vowels and string[right] in vowels:
                string[left], string[right] = string[right], string[left]
                left += 1
                right -= 1
                
        return "".join(string)

### Test ###

def testReverseVowels(s, want):
    result = reverseVowels(s)

    return "pass" if result == want else f"want {want}, got {result}"

print(testReverseVowels("hello", "holle"))
print(testReverseVowels("leetcode", "leotcede"))
print(testReverseVowels("aA", "Aa"))