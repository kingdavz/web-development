/**
 * a module that can generate prime numbers using while loop
 */


function printPrimes() {
    let num = 2; 

    while (num <= 50) {
        let i = 2;
        let isPrime = true;

        while (i < num) {
            if (num % i === 0){
                isPrime = false;
                break;
            }
            i++;
        }
        if (isPrime){
            console.log(num);
        }
        num++;
    }
}
printPrimes();