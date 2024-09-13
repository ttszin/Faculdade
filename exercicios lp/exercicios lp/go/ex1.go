package main

import "fmt"

func main() {

	var celsius, fahrenheit float64

	fmt.Print("Informe a temperatura a ser convertida: ")
	fmt.Scan(&fahrenheit)

	celsius = (((fahrenheit - 32) * 5) / 9)

	fmt.Printf("A temperatura convertida é: %f Graus Celsius", celsius)
}
