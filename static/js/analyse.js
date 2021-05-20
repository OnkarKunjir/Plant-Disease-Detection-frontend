api_url = "http://127.0.0.1:8080/api/predict";

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

const upload_btn = document.querySelector("#upload-btn");
document.querySelector(".upload-section").addEventListener("click", ()=>{
    // listener clicks the uplaod input button
    upload_btn.click();
});

upload_btn.addEventListener("change", ()=>{
    // query image to api
    if(upload_btn.files.length == 0){
        return;
    }
    show_toast("Processing your image", true, 50);
    const formdata = new FormData();
    formdata.append("predict_img", upload_btn.files[0]);    
    fetch(api_url,{
        method: "POST",
        mode: 'cors',
        body: formdata,
    })
    .then(response => response.json())
    .then(data => {
        // show data here 
        console.log(data);
        if(data["status"] == "failure"){
            show_toast(data["message"], false, 2);
        }
        else{
            show_toast(data["message"], true, 2);
        }

    })
    .catch(err => {
        console.err(err);
        show_toast("Something went wrong!", false, 2);
    });
});
