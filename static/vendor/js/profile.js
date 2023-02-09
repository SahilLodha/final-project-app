editBtn = document.getElementById('edit-btn')
user_name = document.getElementById('uname')
first_name = document.getElementById('fname')
last_name = document.getElementById("lname")
email = document.getElementById('email')
phone_no = document.getElementById('phone')
submitBtn = document.getElementById('submit-btn')

document.onload = ()=>{
    first_name.disabled = true
    last_name.disabled = true
    email.disabled = true
    phone_no.disabled = true
    user_name.disabled = true
    alert("Here")
}

$(editBtn).click(()=>{
    first_name.disabled = false
    last_name.disabled = false
    email.disabled = false
    phone_no.disabled = false
    user_name.disabled = false
    submitBtn.disabled  = false
})

