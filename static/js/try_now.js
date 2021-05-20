const url = "http://127.0.0.1:8080/api/";
const analyse_url = "http://127.0.0.1:8080/analyse"
let action = "signin";

const email = document.querySelector("#email");
const password = document.querySelector("#password");
const switch_action = document.querySelector("#switch-action");
const submit_button = document.querySelector("#submit-button");

const toast = document.querySelector(".toast");
const show_toast = (msg, success, sec) => {
    toast.innerHTML = msg;
    toast.classList.remove("deactivate", "success", "failure");
    toast.classList.add("activate");
    if(success){
        toast.classList.add("success");
    }
    else{
        toast.classList.add("failure");
    }
    setTimeout(() => {
        toast.classList.replace("activate", "deactivate");
    }, 1000*sec);
};

switch_action.addEventListener("click", () => {
    if(action == "signin"){
        action = "signup";
        submit_button.innerHTML = "Sign Up";
        switch_action.innerHTML = "Sign in into existing account";
    }
    else{
        action = "signin";
        submit_button.innerHTML = "Sign In";
        switch_action.innerHTML = "Create new acccount";
    }
});

submit_button.addEventListener("click", () => {
    if((email.value.trim().length == 0) || (password.value.trim().length == 0)){
        show_toast("Enter emaill and password", false, 2);
        return;
    }
    const formdata = new FormData();
    formdata.append("email", email.value.trim());
    formdata.append("password", password.value.trim());
    // send request to api.
    fetch(url + action, {
        method: "POST",
        mode: "cors",
        body: formdata,
    })
    .then(response => response.json())
    .then(data => {
        console.log(data)
        if(data["status"] == "success"){
            if(action == "signup"){
                action = "signin";
                submit_button.click();
            }
            else{
                document.location.replace(analyse_url);
            }
        }
        else{
            show_toast(data["message"], false, 2);
        }
    })
    .catch(err => show_toast("Something went wrong", false, 2));
});
