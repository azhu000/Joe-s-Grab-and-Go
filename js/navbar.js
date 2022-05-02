$.get("/navigationBAR.html", function(data){
    $("#navbar-placeholder").replaceWith(data);
});