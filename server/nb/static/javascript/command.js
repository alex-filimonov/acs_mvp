
function add_command_form(id_cpe){
    $('#input_parameter').val("");
    $('#commandForm').modal("show");
}

var g_id=undefined;
var g_cpe_id=undefined;

function command_delete(id,cpe_id){
    g_id=id;
    g_cpe_id=cpe_id;
    $('#confirmDelete').modal("show");
}

function command_delete_confirm(){
    document.location.href = "/cpe_del_commands?cpe_id="+g_cpe_id+"&id="+g_id;
}