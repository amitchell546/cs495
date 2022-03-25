package main

import (
	"fmt"
	"github.com/faiface/pixel"
	"github.com/faiface/pixel/pixelgl"
	"golang.org/x/image/colornames"
	"math/rand"
)

var wins = 0
var losses = 0

//code for the window :)
func run() {
	//tutorial from github.com/faiface/pixel
	cfg := pixelgl.WindowConfig{
		Title:  "Rock, Paper, Scissors!",
		Bounds: pixel.R(0, 0, 1024, 768),
		VSync:  true,
	}
	win, err := pixelgl.NewWindow(cfg)
	win.Clear(colornames.Darkred)
	if err != nil {
		panic(err)
	}
	for !win.Closed() {
		win.Update()
	}

}

func main() {

	pixelgl.Run(run)

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

// randomly selecting a 1 2 or 3 for the computer to be either rock paper or scissors
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
