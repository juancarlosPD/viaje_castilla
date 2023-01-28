from django.test import TestCase

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
                    alert(data.length)
                    $('#psecundaria').hide();
                    alert('Funciona')
                    
                }    
            },
            error: function (error) {
               alert('Ocurrió un error en el servidor');
            }
        });
}
