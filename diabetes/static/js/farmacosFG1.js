
var FG = document.getElementById('FG');
var farmaco = document.getElementById('farmaco');
var respuesta1 = document.getElementById('respuesta1');
var respuesta2 = document.getElementById('respuesta2');
var respuesta3 = document.getElementById('respuesta3');
var btn = document.getElementById('btn');

FG.addEventListener('focus', function(){

    respuesta1.innerText="";
    respuesta2.innerText="";
    respuesta3.innerText="";
    comentarios.innerText="";
    respuesta4.innerText="";
    mF.innerText="";
    mFG.innerText="";
    dosisC.innerText="";
    
});
farmaco.addEventListener('focus', function(){

    respuesta1.innerText="";
    respuesta2.innerText="";
    respuesta3.innerText="";
    comentarios.innerText="";
    respuesta4.innerText="";
    mF.innerText="";
    mFG.innerText="";
    dosisC.innerText="";
    
    
});

