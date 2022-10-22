
          const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
          function exitFunc(i) {
            
            console.log(i)
            

            $.ajaxSetup({ data: {csrfmiddlewaretoken: '{{ csrftoken }}' },});  
           
            url = `http://127.0.0.1:8000/profile/exit`
            $.ajax({
                type: "POST",
                url: url,
                
                data: i,
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
          