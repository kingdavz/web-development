/**
 * a module that solves the prolem of finding the roots of a quadratic equation
 */

const readline = require('readline')


const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
})

function quadratic (a,b,c){
    x1 = (-b + Math.sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - Math.sqrt(b**2 - 4*a*c)) / (2*a)
    return [x1,x2]
}


rl.question('Enter the value of a: ', (a) => {
    rl.question('Enter the value of b: ', (b) =>{
        rl.question('Enter the value of c: ', (c) => {
            const result = quadratic(parseFloat(a),parseFloat(b),parseFloat(c));
            console.log(result)
            rl.close()
        })
    })
})