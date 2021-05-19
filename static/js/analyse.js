api_url = "http://127.0.0.1:5000/api/predict";

let upload_btn = document.querySelector("#upload-btn");
document.querySelector(".upload-section").addEventListener("click", ()=>{
    // listener clicks the uplaod input button
    upload_btn.click();
});

upload_btn.addEventListener("change", ()=>{
    // query image to api
    if(upload_btn.files.length == 0){
        return;
    }
    const formdata = new FormData();
    formdata.append("predict_img", upload_btn.files[0]);    
    fetch(api_url,{
        method: "POST",
        mode: 'cors',
        body: formdata,
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));
});
