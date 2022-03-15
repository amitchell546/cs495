// Copyright 2000-2021 JetBrains s.r.o. and contributors. Use of this source code is governed by the Apache 2.0 license that can be found in the LICENSE file.
import androidx.compose.material.MaterialTheme
import androidx.compose.desktop.ui.tooling.preview.Preview
import androidx.compose.foundation.layout.Column
import androidx.compose.material.Button
import androidx.compose.material.Text
import androidx.compose.material.TextField
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.text.input.TextFieldValue
import androidx.compose.ui.window.Window
import androidx.compose.ui.window.application
import kotlin.random.Random

@Composable
@Preview
//This is my composable function, it handles all the creating of the elements in my window
fun App() {

    var submitResult = mutableStateOf(false)
    var answer = mutableStateOf(selectWord())

    MaterialTheme {
        var input = remember { mutableStateOf("") }
        Column{
            Text(text="Try and guess the 5 letter word, if you have an incorrect character, you will see an X. If you have" +
                    "the correct character in the incorrect position, you will see an O. If every thing is correct, you " +
                    "will see a C")
            if(submitResult.value){
                var response = compareGuess(input.value, answer.value)
                Text(text=response)
            }
            TextField(
                value = input.value,
                onValueChange = { input.value = it },
                label = { Text("Type your guess here!") }
            )
            Button(
                onClick = {submitResult.value=true}
            )
            {
                Text("Click to submit answer")
            }
        }
    }
}

fun main() = application {
    Window(
        onCloseRequest = ::exitApplication,
        title = "Wordle Game"
        ) {
        App()
    }
}

//function for selecting our word
fun selectWord(): String {

    val wordArrays = arrayOf("rated", "train", "crane", "irate", "write")
    val randomInt = Random.nextInt(wordArrays.size - 1)

    return(wordArrays[randomInt])
}

fun isCorrect(replyString:String): Boolean{
    val replyArr = replyString.split("")
    var returnBoolean = true
    for(i in 1..5) {
        if(replyArr[i] != "C")
        {
            returnBoolean = false
        }
    }
    return returnBoolean
}

fun compareGuess(guess: String, correct: String): String{

    if(guess.length!=correct.length) {
        return ""
    }
    else {

        val guessArr = guess.split("")
        val correctArr = correct.split("")
        var returnArr = arrayOfNulls<Char>(5)

        for(i in 1..5) {

            var guessChar = guessArr[i]

            //checking if the characters are exact matches
            if(guessChar == correctArr[i]) {
                returnArr[i-1] = 'C'
            }
            //checking if any of the other characters are matches
            else {
                returnArr[i-1] = 'X'

                for(j in 1..5){
                    if(guessChar == correctArr[j]){
                        returnArr[i-1] = 'O'
                    }
                }
            }
        }

        var returnString = ""
        for(char in returnArr) {
            returnString += char
        }

        return returnString;
    }
}