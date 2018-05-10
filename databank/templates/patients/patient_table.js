$(document).ready(function () {
    $.getJSON(url,
        function (json) {
            var tr;
            for (var i = 0; i < json.length; i++) {
                tr = $('<tr/>');
                tr.append("<td>" + json[i].Nombre + ">");
                tr.append("<td>" + json[i].Apellido + ">");
                tr.append("<td>" + json[i].Doctor + ">");
                tr.append("<td/" + json[i].Enfermedad + ">");
                $('table').append(tr);
            }
        });
});