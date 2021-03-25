package main

import (
	"fmt"
	"math"
	"testing"
)

func IsMinimum(num_list []int) int {
	minimum_int := math.MaxInt32
	for _, i := range num_list {
		if minimum_int > i {
			minimum_int = i
		}
	}
	return minimum_int
}

func main() {
	fmt.Println(IsMinimum([]int{3, 3, 45, 6, 6, 7, 2}))
}

func TestSum(t *testing.T) {
	actual := IsMinimum([]int{3, 3, 45, 6, 6, 7, 2})
	expected := 2
	if actual != expected {
		t.Errorf("actual %v\nwant %v", actual, expected)
	}
}
