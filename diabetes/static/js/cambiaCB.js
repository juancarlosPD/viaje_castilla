farmaco1 = document.getElementById('farmaco1');
farmaco2 = document.getElementById('farmaco2');
farmaco3 = document.getElementById('farmaco3');

pprincipal = document.getElementById('pprincipal');
psecundaria = document.getElementById('psecundaria');
pterciaria = document.getElementById('pterciaria');

farmaco2.disabled=true;
farmaco3.disabled=true;
psecundaria.disabled=true;
pterciaria.disabled=true;


farmaco1.addEventListener('change', function(){

    farmaco2.disabled=false;            

})

farmaco2.addEventListener('change', function(){

    farmaco3.disabled=false;
    
})

pprincipal.addEventListener('change', function(){

    psecundaria.disabled=false;
    pterciaria.value="";
    pterciaria.disabled=true;            

})

psecundaria.addEventListener('change', function(){

    pterciaria.disabled=false;            

})