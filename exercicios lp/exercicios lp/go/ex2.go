package main

import "fmt"

func main() {

	var altura, resp float64

	var genero int

	fmt.Print("Insira sua altura: ")
	fmt.Scan(&altura)

	fmt.Print("Insira seu sexo: ")
	fmt.Scan(&genero)

	if genero == 0 {
		resp = (73 * altura) - 58
		fmt.Printf("O seu peso ideal e de %f Kg", resp)

	} else {
		resp = (62 * altura) - 45
		fmt.Printf("O seu peso ideal e de %f Kg", resp)

	}

}
