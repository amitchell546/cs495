package main

import (
	"bufio"
	"fmt"
	"math/rand"
	"os"
	"strings"
)

var wins = 0
var losses = 0

func main() {

	var done = false
	var welcomeMessage = "Lets play rock, paper, scissors!" +
		"\n which do you choose? rock, paper, scissors or done?"

	reader := bufio.NewReader(os.Stdin)

	for !done {

		fmt.Println("wins: ", wins)
		fmt.Println("losses: ", losses)

		fmt.Println(welcomeMessage)

		//loop for making sure a user selects proper input
		correctInput := false
		for !correctInput {
			var input, _ = reader.ReadString('\n')
			fmt.Println("you chose", input)
			var intInput = determineInput(input)
			if intInput != 4 || intInput != 5 {
				correctInput = true
				isWinner(intInput, computerChoice())
			}
			if intInput == 4 {
				done = true
				correctInput = true
			}
			if intInput == 5 {
				fmt.Println("incorrect input")
			}
		}

	}

}

//getting input for the user to play against
func computerChoice() int {
	randInt := rand.Intn(4)
	if randInt == 1 {
		fmt.Println("Your opponent chose rock")
	}
	if randInt == 2 {
		fmt.Println("Your opponent chose paper")
	}
	if randInt == 3 {
		fmt.Println("Your opponent chose scissors")
	}
	return randInt
}

// determining if the user said rock paper scissors or done
func determineInput(input string) int {
	lowerInput := strings.ToLower(input)
	if lowerInput == "rock\r\n" {
		return 1
	}
	if lowerInput == "paper\r\n" {
		return 2
	}
	if lowerInput == "scissors\r\n" {
		return 3
	}
	if lowerInput == "done\r\n" {
		return 4
	}

	return 5
}

//1 is rock, 2 is paper, 3 is scissor
// if the user won or not
func isWinner(input int, correct int) bool {
	if input == correct {
		fmt.Println("You Tied!")
		return false
	} else if input == 1 {
		if correct != 3 {
			fmt.Println("You Lose!")
			losses++
			return false
		} else {
			fmt.Println("You Win!")
			wins++
			return true
		}
	} else if input == 2 {
		if correct != 1 {
			fmt.Println("You Lose!")
			losses++
			return false
		} else {
			fmt.Println("You Win!")
			wins++
			return true
		}
	} else if input == 3 {
		if correct != 2 {
			fmt.Println("You Lose!")
			losses++
			return false
		} else {
			fmt.Println("You Win!")
			wins++
			return true
		}
	}

	return false
}
