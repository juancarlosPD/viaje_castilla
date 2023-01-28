// ------------------VARIABLES (.value para acceder al valor)---------------------------------------------------------

var $metformina = document.getElementById('check_metformina');

var $farmaco1 = document.getElementById('farmaco1');
var $farmaco2 = document.getElementById('farmaco2');
var $farmaco3 = document.getElementById('farmaco3');

var $cetosis = document.getElementById('check_cetosis');
let $FG = document.getElementById('FG');
let $glicada =document.getElementById("glicada");
let $objetivoGlicada = document.getElementById("objetivoGlicada");

let $pprincipal = document.getElementById('pprincipal');
let $psecundaria = document.getElementById('psecundaria');
let $pterciaria = document.getElementById('pterciaria');

let principales = ['Alto riesgo CV / Muy alto riesgo CV', 'Insuficiencia cardíaca', 'Insuficiencia renal crónica', 'Sobrepeso/Obesidad', 'Fragilidad'];
let secundarios = ['IMC ≥ 30', 'IMC < 30', 'De elección', 'iSGLT2 desaconsejado', 'Aclaramiento creatinina > 300', 'FE > 40', 'FE <= 40' ];
let terciarios = ['Prevención primaria', 'Prevención secundaria', 'Obesidad lo más importante', 'FE ≤ 40', "FE > 40"];

var infop = document.getElementById("infop");
var infos = document.getElementById("infos");
var infot = document.getElementById("infot");


var $btnCalcular = document.getElementById('btnCalcular');




//-----------------------METFORMINA----------------------------------------------------

// var $metformina = document.getElementById('check_metformina');
function metformina(){
    if($metformina.checked==true){
        alert("Metformina picada");
    }else if($metformina.checked==false){
        alert("Metformina no picada");
    }
}

$metformina.addEventListener('change', function(){
    // metformina();
})


$metformina.addEventListener('change', function(){
    switch($metformina.checked){
        case true:
            if($farmaco1.value=='Metformina'){
                Swal.fire({
                    titleText : "¡Cuidado!",
                    text: "La metformina no está indicada en este paciente",
                    icon : "warning",
                    confirmButtonText: "Ok",
                });
                $farmaco1.value=1;
                $farmaco2.value='';
                $farmaco2.disabled=true;
                $farmaco3.value='';
                $farmaco3.disabled=true;
            }
            if($farmaco2.value=='Metformina'){
                Swal.fire({
                    titleText : "¡Cuidado!",
                    text: "La metformina no está indicada en este paciente",
                    icon : "warning",
                    confirmButtonText: "Ok",
                });
                $farmaco2.value=2;
                $farmaco3.value='';
                $farmaco3.disabled=true;
            }
            if($farmaco3.value=='Metformina'){
                Swal.fire({
                    titleText : "¡Cuidado!",
                    text: "La metformina no está indicada en este paciente",
                    icon : "warning",
                    confirmButtonText: "Ok",
                });
                $farmaco3.value=3;
                
            }
        break
        case false:
            pass
        break
    }
})

//---------------------------------------------------------------------------------------------
//-----------------------------¿QUÉ ESTÁ TOMANDO?----------------------------------------------
//---------------------------------------------------------------------------------------------

//------------------ Grupos de fármacos. Para comprobar que no asocia el mismo subgrupo 2 veces--------------------------------------

let grupo1, grupo2, grupo3; 
var sulfonilureas = ['Sulfonilureas','Gliclazida', 'Glimepirida', 'Glipizida'];
var iDPP4 = ['iDPP4','Sitagliptina', 'Linagliptina', 'Vildagliptina', 'Saxagliptina', 'Alogliptina', 'arGLP1','Dulaglutida', 'Exenatida Cor', 'Exenatida Lar', 'Liraglutida', 'Lixisenatida', 'Semaglutida SC', 'Semaglutida oral'];
var biguanidas = ['Biguanidas','Metformina'];

var iSGLT2 =['iSGLT2', 'Canagliflozina', 'Dapagliflozina', 'Empagliflozina', 'Ertugliflozina']
var grupos = [sulfonilureas, iDPP4, biguanidas, iSGLT2];

function recorreGrupo(grupos){
    
    for(let i=0; i<=grupos.length-1; i++){
        for(let j=0; j< grupos[i].length; j++){
            if(grupos[i][j]==comparador){
                subgrupo = grupos[i][0];            
            } 
        }
               
    }
    
    return(subgrupo);

}
//---------------------------------FÁRMACO 1---------------------------------------------------

$farmaco1.addEventListener('change', function(){
    if ($metformina.checked==true){
        if($farmaco1.value=='Metformina'){
            Swal.fire({
                titleText : "¡Cuidado!",
                text: "La metformina no está indicada en este paciente",
                icon : "warning",
                confirmButtonText: "Ok",
            });

            $farmaco1.value='1';
            $farmaco2.value='';
            $farmaco2.disabled=true; 
            $farmaco3.value='';
            $farmaco3.disabled=true;
        }
    }else{
        if ($farmaco1.value == 1){
            $farmaco2.value='';
            $farmaco2.disabled=true; 
            $farmaco3.value='';
            $farmaco3.disabled=true;
        }else{
            $farmaco2.value='2';
            $farmaco3.value='';
            $farmaco3.disabled=true;
        }
    }    
    
    comparador =$farmaco1.value;
    grupo1 = recorreGrupo(grupos);
    
           
})


//---------------------------------FÁRMACO 2---------------------------------------------------
$farmaco2.addEventListener('change', function(){
    if ($metformina.checked==true){
        if($farmaco2.value=='Metformina'){
            Swal.fire({
                titleText : "¡Cuidado!",
                text: "La metformina no está indicada en este paciente",
                icon : "warning",
                confirmButtonText: "Ok",
            });
            $farmaco2.value=2;
            $farmaco2.focus();
            $farmaco3.value='';
            $farmaco3.disabled=true;
        }
        
    }else{
        if($farmaco2.value == $farmaco1.value){
            Swal.fire({
                titleText : "¡Cuidado!",
                text: "Ya está tomando este fármaco",
                icon : "warning",
                confirmButtonText: "Ok",
            });
            $farmaco2.value='2';
            $farmaco2.focus();
            $farmaco3.value='';
            $farmaco3.disabled=true;
        }else{
            if($farmaco2.value == 2){
                $farmaco3.value='';
                $farmaco3.disabled=true;
            }else{
                $farmaco3.value='3';
    }
    

    
    }}
    comparador =$farmaco2.value;
    grupo2 = recorreGrupo(grupos);
    
    
    if (grupo2 == grupo1){
        Swal.fire({
            titleText : "¡Cuidado!",
            text: "El fármaco nº 1 es de este mismo grupo terapéutico",
            icon : "warning",
            confirmButtonText: "Ok",
        });
        $farmaco2.value='2';
        $farmaco2.focus();
        $farmaco3.value='';
        $farmaco3.disabled=true;
    }

})
//---------------------------------FÁRMACO 3---------------------------------------------------
$farmaco3.addEventListener('change', function(){
    if ($metformina.checked==true){
        if($farmaco3.value=='Metformina'){
            Swal.fire({
                titleText : "¡Cuidado!",
                text: "La metformina no está indicada en este paciente",
                icon : "warning",
                confirmButtonText: "Ok",
            });
            $farmaco3.value=3;
            $farmaco3.focus();
        }
    }else{
        if($farmaco3.value == $farmaco2.value || $farmaco3.value == $farmaco1.value){
        alert("Ya está tomando ese fármaco");
        $farmaco3.value=3;
    }
}
comparador =$farmaco3.value;
grupo3 = recorreGrupo(grupos);
if (grupo3 == grupo1){
    Swal.fire({
        titleText : "¡Cuidado!",
        text: "Ya ha usado ese grupo terapéutico",
        icon : "warning",
        confirmButtonText: "Ok",
    });
    $farmaco3.value='3';
    
}
if (grupo3 == grupo2){
    Swal.fire({
        titleText : "¡Cuidado!",
        text: "Ya ha usado ese grupo terapéutico",
        icon : "warning",
        confirmButtonText: "Ok",
    });
    $farmaco3.value='3';
    
}
})

//---------------------------------------------------------------------------------------------
//-----------------------------ES NECESARIO CONOCER----------------------------------------------
//---------------------------------------------------------------------------------------------

// ------------------------------------------CETOSIS-------------------------------------------
// var $metformina = document.getElementById('check_metformina');
function cetosis(){
    if($cetosis.checked==true){
        alert("Este paciente tiene cetosis");
    }else if($cetosis.checked==false){
        alert("Este paciente no tiene cetosis");
    }
}

$cetosis.addEventListener('change', function(){
    // cetosis();
})

// ---------------------------FG-------------------------------------------
// let $FG = document.getElementById('FG');

$FG.addEventListener('change', function (){
    
    // document.getElementById("glicada").value="";
    // document.getElementById("objetivoGlicada").value="";
    // document.getElementById("glicada").focus();    
})

// ---------------------------GLICADA-------------------------------------------
//   $glicada = document.getElementById("glicada");        Para acceder al input
//   var glicada = document.getElementById("glicada").value="";  Para acceder al valor del input

// ---------------------------OBJETIVO GLICADA-------------------------------------------
//   $objetivoGlicada = document.getElementById("glicada");        Para acceder al input
//   var objetivoGlicada = document.getElementById("glicada").value="";  Para acceder al valor del input


//---------------------------------------------------------------------------------------------
//-----------------------------SITUACIÓN CLÍNICA----------------------------------------------
//---------------------------------------------------------------------------------------------

//Quitamos las i informativas

infop.style.display = "none"
infos.style.display = "none"
infot.style.display = "none"


// function mostrarPatologias(arreglo, lugar){
//     let elementos = '<option selected disables>-------Seleccione-------</option>'

//     for(let i = 0; i<arreglo.length; i++){
//         elementos += '<option value ="' + arreglo[i] + '" >' +
//         arreglo[i] + '</option>'
//     }

//     lugar.innerHTML = elementos;
// }
// mostrarPatologias(principales, $pprincipal);

// ---------------------------PATOLOGÍA PRINCIPAL-------------------------------------------



// ---------------------------PATOLOGÍA SECUNDARIA-------------------------------------------

// $psecundaria.addEventListener('change', function() {
//     let valorSecundario = $psecundaria.value;
//     let valorPrincipal = $pprincipal.value;
     

    
//     switch(valorPrincipal){
//         case 'Alto riesgo CV / Muy alto riesgo CV':
//             if (valorSecundario == 'IMC ≥ 30'){
//                 let recortarS1 = terciarios.slice(0,3);
//                 mostrarPatologias(recortarS1, $pterciaria);
//                 $pterciaria.disabled=false;                 
//             }else if(valorSecundario == 'IMC < 30'){
//                 let recortarS1 = terciarios.slice(0,2);
//                 mostrarPatologias(recortarS1, $pterciaria);
//                 $pterciaria.disabled=false;               
//             }
//         break
//         case 'Insuficiencia cardíaca':
//             if (valorSecundario == 'IMC ≥ 30'){
                
//                     let recortarS1 = terciarios.slice(3,6);
//                     mostrarPatologias(recortarS1, $pterciaria);
//                     $pterciaria.disabled=false;
                
//             }else if(valorSecundario == 'IMC < 30'){
                
//                     let recortarS1 = terciarios.slice(3,6);
//                     mostrarPatologias(recortarS1, $pterciaria);
//                     $pterciaria.disabled=false;
                
//             }
//         break
            
//     }    
// })



// ---------------------------MOSTRAR BOTONES INFORMATIVOS------------------------------------------
document.getElementById('infop').onclick = function(){
    var valorPrincipal = $pprincipal.value;
    

    switch(valorPrincipal){
        case 'Alto riesgo CV / Muy alto riesgo CV':
            
            $('#rcv').modal('show');
            $('#ic').modal('hide');
            $('#irc').modal('hide');
            
            
        break
        case 'Insuficiencia cardíaca':
            $('#rcv').modal('hide');
            $('#ic').modal('show');
            $('#irc').modal('hide');
        break
        case 'Insuficiencia renal crónica':
            $('#rcv').modal('hide');
            $('#ic').modal('hide');
            $('#irc').modal('show');
        break
        case 'Otros':
            
        break
    }
};





   

