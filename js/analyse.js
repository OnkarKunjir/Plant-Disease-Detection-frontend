api_url = "http://127.0.0.1:5000/";

let upload_btn = document.querySelector("#upload-btn");
document.querySelector(".upload-section").addEventListener("click", ()=>{
    upload_btn.click();
    if(upload_btn.files.length == 0){
        return;
    }
    const formdata = new FormData();
    formdata.append("image", upload_btn.files[0]);    
    
    fetch(api_url,{
        method: "POST",
        mode: 'cors',
        body: formdata,
    })
    .then(response => response.json())
    .then(data => console.log(data))
    .catch(err => console.error(err));
});