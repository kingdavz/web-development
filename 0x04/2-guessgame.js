/**
 *  a module that plays a guess game
 */

const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const number = Math.floor(Math.random() * 10) + 1;

function ask() {
    rl.question("Guess a number between 1 and 10: ", (guess) => {
        guess = Number(guess);

        if (guess > number) {
            console.log("Too high!");
            ask();
        } else if (guess < number) {
            console.log("Too low!");
            ask();
        } else {
            console.log(" Correct!");
            rl.close();
        }
    });
}

ask();