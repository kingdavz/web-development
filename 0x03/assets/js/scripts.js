let i
let x

const e = 1
const name = "david"
const price = 100.0
const amount = 500

var j // global in scope

console.log(typeof(e))
console.log(typeof(name))
console.log(typeof(price))
console.log(typeof(amount))

let fullName = "DAvid uzoma"
let firstName = "David "
let lastName = "uzoma"


console.log(firstName + " " +  lastName)
console.log(`${firstName} ${lastName}`)

fullName = prompt("what is your name?")
alert(`Hello ${fullName}`)
const response = confirm("Are you sure you want to continue?")

if (response) {
    alert("Thank you")
} else {
    alert("bye")
}