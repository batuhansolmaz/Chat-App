const roomName = JSON.parse(document.getElementById('room-name').textContent)
const user = JSON.parse(document.getElementById('user').textContent)
console.log(roomName)
console.log(user)
const conversation = document.getElementById('conversation')

const sendButon= document.getElementById('send')
const inputField = document.getElementById('comment')





const chatSocket = new WebSocket("ws://" + window.location.host + "/ws/chat/" +roomName +"/") 

chatSocket.onmessage= function(e) {
    const data = JSON.parse(e.data)
    console.log(data)
    console.log(data.user)

    if (user ==data.user){
        var message = ` <div class="row message-body">
        <div class="col-sm-12 message-main-sender">
        <div class="sender">
            <div class="message-text">
            ${data.message}
            <div>
            <span class="message-time pull-right">
            ${data.created_date}
              </span>
            </div> 
            </div>
            
            
        </div>
        </div>
        </div>`
            conversation.innerHTML += message
    }

    else {var message = ` <div class="row message-body">
    <div class="col-sm-12 message-main-receiver">
    <div class="receiver">
    <span class="message-user pull-left">
            <font size="1"
          face="arial"
          color="blue">
          ${data.user}
            </font>
        </span>
        <div class="message-text">
        ${data.message}
        </div>
        <span class="message-time pull-right">
        ${data.created_date}
        </span>
    </div>
    </div>
    </div>`
    conversation.innerHTML += message}
    

};
chatSocket.onopen = function(e) {
    console.log('açıldı')
}
chatSocket.onclose = function(e) {
    console.error('beklenmedik şeklilde kapandı')
}

inputField.focus()

document.querySelector("#comment").onkeyup = function(e){
    if (e.keyCode==13){
        sendButon.click()
    }


}

sendButon.onclick = function(e){
    const message = inputField.value
    console.log(message)
    chatSocket.send(JSON.stringify({'message' : message}))
    inputField.value=''
}





