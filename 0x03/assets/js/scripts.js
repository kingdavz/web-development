const countElement = document.getElementById("count")
const decreaseButton = document.getElementById("decrease")
const resetButton = document.getElementById("reset")
const increaseButton = document.getElementById("increase")
const saveButton = document.getElementById("save")
const display = document.getElementById("saved-counts")
let count = 0

function updateCounter() {
    countElement.textContent = count
    countElement.style.color = count > 0 ?"#10b981" : count < 0 ?"#f97316" : "#1e2433"
}

decreaseButton.addEventListener("click",function(){
    count -= 1
    updateCounter()
})

resetButton.addEventListener("click", function(){
    count = 0
    updateCounter()
})

increaseButton.addEventListener("click", function(){
    count += 1
    updateCounter()
})

saveButton.addEventListener("click", function(){
 
    if (count == 0){
        return;
    }
    const list = document.createElement('li')
    list.textContent = count
    display.append(list)
   
    
    count = 0
    updateCounter()
})


updateCounter()