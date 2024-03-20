package array

import "strings"

/*
	// Use strings.Split() and concatenation
	func MergeAlternately(word1 string, word2 string) string {
		result := ""

		splited1 := strings.Split(word1, "")
		splited2 := strings.Split(word2, "")

		for {
			if len(splited1) == 0 && len(splited2) == 0 {
				break
			}

			if len(splited1) > 0 {
				result += splited1[0]
				splited1 = splited1[1:]
			}

			if len(splited2) > 0 {
				result += splited2[0]
				splited2 = splited2[1:]
			}
		}

		return result
	}

	// Time complexity: O(n)
	// Space complexity: O(n) for result, O(n) for splited1, and O(n) for splited2
*/

// Use strings.Builder
func MergeAlternately(word1 string, word2 string) string {
	var result strings.Builder
	result.Grow(len(word1 + word2)) // ensure the result's capacity

	for i := 0; i < len(word1+word2); i++ {

		if i > len(word1) && i > len(word2) {
			break
		}

		if i < len(word1) {
			result.WriteByte(word1[i])
		}

		if i < len(word2) {
			result.WriteByte(word2[i])
		}
	}

	return result.String()
}

// Time complexity: O(n)
// Space complexity: O(n) for result
