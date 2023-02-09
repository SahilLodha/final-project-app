const form = document.querySelector('form');
const fileBrowser = document.querySelector("#file-browser")
const fileInput = document.getElementById('file-input')
const progressArea = document.querySelector('.progress-area')
const uploadedArea = document.querySelector('.uploaded-area')
const category = document.getElementById('category')

fileInput.onchange = ({target})=>{
    for (let i = 0; i < target.files.length ; i++) {
        size = target.files[i].size / 1024;
        progressArea.innerHTML += `
            <li class="row-custom">
                <i class="fas fa-file-alt"></i>
                <div class="content">
                    <div class="details">
                        <span class="file_name">${ target.files[i].name }</span>
                        <span class="size">${ size.toFixed(2)} KB</span>
                    </div>
                </div>
            </li>
        `
    }
}

fileBrowser.addEventListener("click", ()=>{
    fileInput.click();
})
