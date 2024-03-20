package array_test

import (
	"leetcode/array"
	"testing"
)

func TestMergeAlternately(t *testing.T) {
	tests := []struct {
		word1 string
		word2 string
		want  string
	}{
		{"abc", "pqr", "apbqcr"},
		{"ab", "pqrs", "apbqrs"},
		{"abcd", "pq", "apbqcd"},
	}

	for _, test := range tests {
		result := array.MergeAlternately(test.word1, test.word2)
		if result != test.want {
			t.Errorf("want %s, got %s\n", test.want, result)
		}
	}
}
