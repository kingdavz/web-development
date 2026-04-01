function addNumber(a,b){
    add = a + b;
    return add;
}

function subNumber(a,b){
    sub = a - b;
    return sub;
}

function mulNumber(a,b){
    mul = a * b;
    return mul
}

function divNumber(a,b){
    div = a / b;
    return div
}

function triangle(width, height){
    area = 0.5 * width * height;
    return area;
}

const areaofCircle = (r) => Math.PI * r * r
const areaofRectangle = (l,w) => l*w


let hotel ={
    name: 'Reiz Continental Hotel',
    location: 'Lagos, Nigeria',
    rating: 4.5,
    rooms: 200,
    booked: 45,
    checkAvailaility: function(){
        return this.rooms - this.booked
    }
}

document.writeln(hotel.name)
document.writeln(hotel.location)
document.writeln(hotel.rating)
document.writeln(hotel.checkAvailaility())