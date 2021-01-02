const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// fade out messages
setTimeout(function(){
    $('#message').fadeOut('slow');
}, 3000);