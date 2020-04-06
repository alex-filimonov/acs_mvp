
function show_inform(cpe_id){
    $.ajax({
        url: 'cpe_inform_ajax?cpe_id='+cpe_id,             // указываем URL и
        success: function (data, textStatus) { // вешаем свой обработчик на функцию success
            $('#cpe_inform_body').text(data);
            $('#cpeInform').modal("show")
        }
    });
}

function show_commands(cpe_id){
    document.location.href = "/cpe_commands?cpe_id="+cpe_id;
}