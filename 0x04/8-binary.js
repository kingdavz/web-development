/**
 * A MODULE THAT CHANGES BINARY TO DECIMAL AND DECIMAL TO BINARY
 */

function binary(binaryy){
    let decimal = 0
    let i = 0;

    let index = binaryy.length - 1;

    while (index >= 0){
        if (binaryy [index] === '1'){
            decimal += Math.pow(2, i);
        }
        i++;
        index--;
    }
    return decimal
}

const decimalBinary = (num) => {
    let binary = ""

    while (num / 2 != 0){
        binary += (num % 2).toString()
        num = Math.floor(num / 2)
    }
    return binary.split('').reverse().join('')
}




console.log(binary("101101"))
const result = decimalBinary(45)
console.log(result)