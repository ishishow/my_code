package main

import (
	"fmt"
)

func fizzbuzz(num int) {
	i := 1
	for i <= num {
		switch {
		case i%15 == 0:
			fmt.Println("FIZZ BUZZ!")
		case i%3 == 0:
			fmt.Println("FIZZ!")
		case i%5 == 0:
			fmt.Println("BUZZ!")
		default:
			fmt.Println(i)
		}

		i++
	}

}

func main() {
	fizzbuzz(100)
}

func fizzbuzz(slice []string{}, num int) {
		switch num {
		case 6:
			fmt.Println("FIZZ BUZZ!")
		case 2:
			fmt.Println("FIZZ!")
		case 3:
			fmt.Println("BUZZ!")
		default:
			fmt.Println(num)
		}
}
