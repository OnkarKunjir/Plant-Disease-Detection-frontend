const api_url = "http://127.0.0.1:8080/api/predict";
const logout_url = "http://127.0.0.1:8080/logout";
const home = "http://127.0.0.1:8080/";
// toast
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

// display result
const main_section = document.querySelector("main");
const result_section = document.querySelector(".result-section");
const image_preview = document.querySelector(".uploaded-image img");
const display_result = ()=>{
    // function displays the reuslt..
    main_section.classList.add("hidden");
    result_section.classList.remove("hidden");
    // let reader = new FileReader();
    // reader.onload = (e) => image_preview.src = reader.result;
    // reader.readAsDataURL(upload_btn.files[0]);
};
document.querySelector(".back-button p").addEventListener("click", ()=>{
    main_section.classList.remove("hidden");
    result_section.classList.add("hidden");
});

// uploading image and feathing results
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
            display_result();
        }

    })
    .catch(err => {
        console.error(err);
        show_toast("Something went wrong!", false, 2);
    });
});


// logout functionality 
document.querySelector("#logout").addEventListener("click", ()=>{
    fetch(logout_url,{
        method: "POST",
        mode: "cors"
    })
    .then(response => document.location.replace(home));
});