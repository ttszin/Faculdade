package main

import "fmt"

func main() {

	var num, i, resultado int
	fmt.Print("Digite um numero para saber se e primo: ")
	fmt.Scan(&num)

	resultado = 0

	for i = 2; i <= num/2; i++ {
		if num%i == 0 {
			resultado++
			break
		}
	}

	if resultado == 0 {
		fmt.Printf("%d e um numero primo\n", num)
	} else {
		fmt.Printf("%d nao e um numero primo\n", num)

	}

}
