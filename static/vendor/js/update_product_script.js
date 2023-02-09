const category = document.getElementById('category')
const subcategory = document.getElementById('subcategory')

function populate(dataArray){
    subcategory.disabled = false
    subcategory.innerHTML = '<option value="">Select a Category First</option>'
    for(i=0; i<dataArray.length; i++){
        subcategory.innerHTML += `<option value="${dataArray[i].id}">${dataArray[i].subcategory_name}</option>`
    }
}


category.onchange = ()=>{
    if(category.value !== ''){
        $.get(`/category/get/subcategory/${category.value}`, function(data, status){
            populate(data)
        })
    }else{
        subcategory.innerHTML = '<option value="">Select a Category First</option>'
        subcategory.disabled = true
    }
}



