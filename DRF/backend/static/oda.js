
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
const rooms = JSON.parse(document.getElementById('data').textContent)








console.log(csrftoken)

function theFunction(i ,a) {
    mylink=document.getElementById('mylink-'+i)
    
    obj=mylink.getAttribute('arguments')
    console.log(i)
    
    
    for (let j = 0; j < rooms.length; j++) {
        if (rooms[j].abc ==i){
            odam = rooms[j]
        }
        
    }
    console.log(odam.abc)
    console.log(typeof(odam))
    url = `http://127.0.0.1:8000/chat/start_chat/${odam.abc}/`
    url2 = `http://127.0.0.1:8000/chat/${odam.abc}/`
    odam=JSON.stringify(odam)
    
    $.ajaxSetup({ data: {csrfmiddlewaretoken: '{{ csrftoken }}' },});


    $.ajax({
        type: "POST",
        url: url,
        
        data: odam,
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin',
        contentType: "application/json",
        
        cache:false,
        sucess: function (data) {
            //console.log(data)
            alert('sff')
            console.log("123")
            
        },
        error: function(xhr, status, error) {
            console.log('!212')
            
         },
         complete: function (response) {
            
            roomid=response.responseJSON.data
            window.location.href =  `http://127.0.0.1:8000/chat/${roomid}/`
          }

    });
    

} 


function the2function(username , id ){
    a=document.getElementById('user-'+id)
    obj=a.getAttribute('arguments' )
    
    datam = {'username' : username , 'usernameId' : id}

    url = `http://127.0.0.1:8000/chat/dms/`
    
    datam=JSON.stringify(datam)
    
    

    $.ajax({
        type: "POST",
        url: url,
        
        data: datam ,
        headers: {'X-CSRFToken': csrftoken},
        mode: 'same-origin',
        contentType: "application/json",
        
        cache:false,
        async:false,

        error: function(xhr, status, error) {
            console.log('!212')
            
         },
         complete: function (response) {
            
            roomid=response.responseJSON.data
            user2=response.responseJSON.user2
            console.log(roomid)
            window.location.href =`http://127.0.0.1:8000/chat/dms/start?id=${roomid}&username=${user2}`

            console.log('completed')
            
          }

    });
    
}

