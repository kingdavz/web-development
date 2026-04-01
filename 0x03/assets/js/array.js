 let Hotels = [
    'Freshland hotel',
    'melvino hotel',
    'transcorp hotel',
    'jabi hotel',
    'bloomsburry hotel',
 ]

 console.log(Hotels[0])

 for(let i = 0; i < Hotels.length; i++){
    document.writeln(Hotels[i])
 }

 for (let hotel of Hotels) {
    document.writeln(hotel)
 }

 Hotels.forEach((hotel)=> {
    document.writeln(hotel)
 })

document.writeln(window.history.length)
document.writeln(window.location.href)
document.writeln(window.navigator.userAgent)
document.writeln(window.innerHeight)
document.writeln(window.innerWidth)
document.writeln(window.pageXOffset)
document.writeln(window.pageYOffset)
document.writeln(window.screenX)
document.writeln(window.screenY)
document.writeln(window.location)
document.writeln(window.document)
document.writeln(window.history)
document.writeln(window.screen)
document.writeln(window.screen.width)
document.writeln(window.screen.heigth)


let saying = 'Home sweet home'
document.writeln(
   saying.toUpperCase(),
   saying.toLowerCase(),
   saying.length,
   saying.charAt(12),
   saying.indexOf('ee'),
   saying.lastIndexOf('e'),
   saying.substring(8,14)
)