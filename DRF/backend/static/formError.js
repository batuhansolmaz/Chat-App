

// for (let j = 0; j < a.length; j++) {
//     if (a[j].checked){
//         console.log(a[j])
//     }
    
// }

function abcd() {
    a = document.getElementById('group-name').value
    console.log(a)
    var format = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]+/;

    if(format.test(a)){
    alert('please give proper name')
   
    }

    if ( a.trim().length === 0) {
        alert('Group name can not be blank')
    }
   


}