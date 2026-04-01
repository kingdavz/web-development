const readline = require('readline');

function welcomeUser(){

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Enter first name: ', function(firstname) {
        rl.question('Enter last name: ',function(lastname) {
            
            let fullname = `${firstname} ${lastname}`;
            console.log(`Welcome ${fullname}`);

            rl.close();
        });
    });
}

welcomeUser();
