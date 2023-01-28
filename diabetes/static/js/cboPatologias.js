
function pterciaria(id){
    $('#terciaria').html("")
    $('#pterciaria').val("")
    $.ajax({
            dataType: "json",
            url: "{% url 'api-situacionTerciaria' %}",
            data: {id:id},
            success: function (data) {
                if(data.length !=0){
                    $('#pterciaria').show();                                    
                    $('#pterciaria').append("<option>Seleccione una opción</option>");
                    var option = ""
                    $.each(data, function(key,value){
                        console.log(value)
                        option += "<option value="+value.id+">"+value.situacion+"</option>" 
                    })
                    $('#pterciaria').append(option)
                }else{
                    $('#terciaria').hide();                   
                }   
                
            },
            error: function (error) {
               alert('Ocurrió un error en el servidor');
            }
        });
        var numeroOpciones = data.length;
}

function psecundaria(id){
    $('#psecundaria').html("")
    $('#psecundaria').val("")    

    $.ajax({
            dataType: "json",
            url: "{% url 'api-situacionSecundaria' %}",
            data: {id:id},
            success: function (data) {                
                if(data.length !=0){
                    $('#psecundaria').show();
                    $('#psecundaria').append("<option>Seleccione una opción</option>")
                    var option = ""
                    $.each(data, function(key,value){
                        console.log(value)
                        option += "<option value="+value.id+">"+value.situacion+"</option>" 
                    })
                    $('#psecundaria').append(option)
                    
                }else{
                    $('#psecundaria').hide();
                    $('#pterciaria').hide();
                                      
                }    
            },
            error: function (error) {
               alert('Ocurrió un error en el servidor');
            }
        });
}


function pprincipal(){
    $('#psecundaria').hide();
    $('#pterciaria').hide();
    $.ajax({
            dataType: "json",
            url: "{% url 'api-situacionPrincipal' %}",
            data: {},
            success: function (data) {
                console.log(data)
                $('#pprincipal').append("<option>Seleccione una opción</option>")
                var option = ""
                $.each(data, function(key,value){
                    console.log(value)
                    option += "<option value="+value.id+">"+value.situacion+"</option>" 
                })
                $('#pprincipal').append(option)

            },
            error: function (error) {
               alert('Ocurrió un error en el servidor');
            }
        });
}

jQuery(document).ready(function($){
    pprincipal();
    $("#pprincipal").on('change', function(){
        
        document.querySelector('#pterciaria').innerHTML = ''; //Para limpiar el 3º select cuando cambie el principal
        var p = $("#pprincipal").val()
        psecundaria(p)
            
    })    
    
    $("#psecundaria").on('change', function(){
        $('#pterciaria').html("");   //Para limpiar el select
        var p = $("#psecundaria").val(); 
        pterciaria(p);     
    })
})