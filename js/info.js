function send(){
    var em = document.getElementById("email").value
    var pa = document.getElementById("password").value
    var xhr= new XMLHttpRequest();
    var url = "http://192.168.29.41/cgi-bin/back.py?email="+em+"&pass="+pa;
    // console.log(url);
    xhr.open("GET",url, true);
    xhr.send();
    
    xhr.onload = function(){
    var  output  = xhr.response;
    console.log(output);
    } 
    alert("Info added succesfully");
}