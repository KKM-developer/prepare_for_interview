console.log('!!!Hello!!!')

$(document).ready(function() {
    console.log('After page load')

    $('#ajaxButton').on('click', function(){
        $.get( "/ajax_test/", function( data ) {
            $( "#testTable" ).html( data );
            alert( "Load was performed." );
    });
    })


});