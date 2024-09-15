function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({       
    headers: { "X-CSRFToken": getCookie("csrftoken") }

});

// Form Submit 🫡

// \\------- Start's Here ------------ \\ //

function formSubmit(event,formName,formUrl){
    event.preventDefault();
    var isValid = validateForm(formName);
    if (!isValid) {
        showAlert('Please fill all required details', 'error');
        event.stopPropagation();
        return false;
      }
    var c = getCookie('csrftoken');
    var formData = new FormData($(`#${formName}`)[0]);
    formData.append('csrfmiddlewaretoken', c)
    formData.append('request_no', $('#request_no').val())
    formData.append('depository', $('#depository').val())
    formData.append('profile_id',parseInt(sessionStorage.getItem("profileSelect")))
    $.ajax({
        type: 'POST',
        url:  `/investor/${formUrl}/`,
        dataType: 'json',
        data: formData,
        enctype: 'multipart/form-data',
        cache: false,
        processData: false,
        contentType: false,
        success: function (json) {
            if (json.message==700){
                /*  added by sarvesh on 24 - sweet alert  */
                showAlert('forms has been saved successfully','success');
                location.replace('/investor/investor_submitted_form/');
            }
            else{ 
                /*  added by sarvesh on 24 - sweet alert  */
                showAlert(json.message,'success');
            }
        },   
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ":" + xhr.responseText)
        }
    })
}


// \\ ------- End's Here ------------ \\ //



// Load Data From Prev Saved Form 🫡

// \\------- Start's Here ------------ \\ //

// Form Auto fill   

function formAutoFill(formFields,data){
    formFields.forEach(function(field) {
        const key = field.getAttribute('name');
        if (field.type === 'radio') {
            if (field.value === data[key]) {
                field.checked = true;
            }
        } 
        else if (field.type === 'checkbox') {
            field.checked = data[key];
        }
        else if (data[key]) {
            field.value = data[key];
        }
    });
}

function autofill(event,fillUrl,fillSelector){ 
    event.preventDefault();
    fetch(`/investor/${fillUrl}/9999`)
    .then((resp) => resp.json())
    .then(function (data) {
        if(data){
            const formFields = document.querySelectorAll(`#${fillSelector} input[name]`,`#${fillSelector} select[name]`);
            formAutoFill(formFields,data) 
        }
    })
    .catch(function (error) {
        alert('No latest record found !')
        console.error(error.response.data.error);
    });
}

window.onload = function () {
    var loadTime = window.performance.timing.domContentLoadedEventEnd-window.performance.timing.navigationStart; 
    console.log('Page load time is '+ loadTime);
    checkImage();
    fetchDocumentManager();

}

//  function for Doucments/Images
//  starts here:

function checkImage() {
    var elements = document.querySelectorAll('.imagecount');
    elements.forEach(function(element) {
        fetchImageCount(element.id)
    });
  }


function fetchImageCount(imagetag){ 
    var req_no  = $('#request_no').val()
    fetch(`/investor/fecthImageCount/${imagetag}/${req_no}`)
    .then((resp) => resp.json())
    .then(function (data) {
        document.getElementById(''+ imagetag +'').innerHTML = data.selected_count
        if(data.selected_count==0){
            document.getElementById(''+ imagetag +'').style.color = "red"
        }
        else{
            document.getElementById(''+ imagetag +'').style.color = "green"

        }
    })
    .catch(function (error) {
        // alert('No latest record found !')
        console.error(error.response.data.error);
    });
 
}



function showImagesModal(imagetag){
    $('#image_modal_heading').html(imagetag)
    $('#modal_image_upload').val(imagetag)
    $('#image_modal_row').empty()
    $('#imageModalShow').modal('show');
    var req_no  = $('#request_no').val()
    fetch(`/investor/fecthImages/${imagetag}/${req_no}`)
    .then((resp) => resp.json())
    .then(function (data) {
        if(data.images){
            for ( j in data.images){
                var image = data.images[j];
                var checkboxChecked = image[2] ? 'checked' : '';
                var html = `<div class="col-md-4 mb-4">
                    <input class="form-check-input other-radio" type="checkbox" name="sign_proof_checkbox" ${checkboxChecked} onchange="imageCheckBox(this.checked, '${image[1]}','${imagetag}')">
                    <a href="data:image/jpeg;base64,${image[0]}" data-fancybox="gallery">
                        <img class="img-fluid" src="data:image/jpeg;base64,${image[0]}" alt="Image Gallery">                                                                
                    </a>
                </div>`;
                $('#image_modal_row').append(html);
            }
        }
    })
    .catch(function (error) {
        // alert('No latest record found !')
        console.error(error.response.data.error);
    });

}


function imageCheckBox(trigger,id,imagetag){
    var c = getCookie('csrftoken');
    var formData = new FormData();
    formData.append('csrfmiddlewaretoken', c)
    formData.append('trigger', trigger)
    formData.append('id', id)
    $.ajax({
        type: 'POST',
        url:  '/investor/document_checkbox/',
        dataType: 'json',
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function (json) {
            fetchImageCount(imagetag)
        },   
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ":" + xhr.responseText)
        }
    })
}

function modalImageUpload(imagetag){
    var c = getCookie('csrftoken');
    var formData = new FormData();
    formData.append('csrfmiddlewaretoken', c)
    formData.append('imagetag', imagetag)
    formData.append('request_no',  $('#request_no').val())
    $.each($("#modal_file")[0].files, function(i, file) {
        formData.append("files", file);
      });
    $.ajax({
        type: 'POST',
        url:  '/investor/modalimageupload/',
        dataType: 'json',
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function (json) {
            if(json.response_code==200){
                showAlert(json.message,'success');
                showImagesModal(imagetag)
                $("#modal_file").val('')
            }
            else{
                showAlert(json.message,'error')
            }
        },   
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ":" + xhr.responseText)
        }
    })
}


function fetchDocumentManager() {
    var selectedNationality = $('#nationality').val(); 
    fetch(`/investor/fetchDocumentManager/${selectedNationality}`)
      .then((resp) => resp.json())
      .then(function (data) {
        var selectedData = data.selected_data;
        
        
        var columns = document.getElementsByClassName('col');
        for (var i = 0; i < columns.length; i++) {
          var column = columns[i];
          var jValue = column.getElementsByClassName('image-column')[0].getElementsByTagName('p')[0].textContent;
          if (!selectedData.includes(jValue)) {
            column.style.display = 'none';
          } else {
            column.style.display = 'block';  
          }
        }
        
        var visibleColumns = document.querySelectorAll('.row .col[style="display: block;"]');
        var chunkSize = 3;
        for (var j = 0; j < visibleColumns.length; j += chunkSize) {
          var chunk = Array.from(visibleColumns).slice(j, j + chunkSize);
          chunk.forEach(function (col) {
            col.classList.remove('col-md-4');
            col.classList.add('col-md-4');
          });
        }
      });
  }
//  ends here



//  form Validator  - added by priyanka/sarvesh -28/06/23
function validateForm(formName) {
    var isValid = true;
    var form = document.forms[formName];
    var inputs = $(form).find('input, select');
  
    // Reset error messages
    $(form).find('.text-danger').remove();
  
    // Validate each input field
    inputs.each(function() {
      var input = this;
  
      if (input.type === 'submit') {
        return;
      }
  
      if (input.type === 'checkbox' || input.type === 'radio') {
        // Checkbox and radio button validation
        var groupName = input.getAttribute('name');
        var groupInputs = $(form).find('input[name="' + groupName + '"]:checked');
        if (groupInputs.length === 0) {
          var errorSpan = document.createElement('span');
          errorSpan.className = 'text-danger';
          errorSpan.textContent = 'Please select an option';
          input.parentNode.appendChild(errorSpan);
          isValid = false;
        }
      } else if (input.tagName === 'SELECT') {
        // Select element validation
        if (input.value === 'Select') {
          var errorSpan = document.createElement('span');
          errorSpan.className = 'text-danger';
          errorSpan.textContent = 'Please select an option';
          input.parentNode.insertBefore(errorSpan, input.nextSibling);
          isValid = false;
        }
      } else {
        // Text input validation
        input.classList.remove("is-invalid");
        if (input.value.trim() === '') {
          // var errorSpan = document.createElement('span');
          // errorSpan.className = 'text-danger';
          // errorSpan.textContent = 'This field is required';
          // input.parentNode.appendChild(errorSpan);
          isValid = false;
          input.classList.add("is-invalid");
        }
      }
    });
  
    return isValid;
  }

// chckbox address fild
var checkbox = document.getElementById('checkbox-1');
var permanentAddressInputs = [
    document.getElementById('permanent_address'),
    document.getElementById('permanent_city'),
    document.getElementById('permanent_district'),
    document.getElementById('permanent_pincode'),
    document.getElementById('permanent_state'),
    document.getElementById('permanent_country')
  ];
checkbox.addEventListener('change', function() {
  var residenceAddressInputs = [
      document.getElementById('residence_address'),
      document.getElementById('residence_city'),
      document.getElementById('residence_district'),
      document.getElementById('residence_picode'),
      document.getElementById('residence_state'),
      document.getElementById('residence_country')
    ];
  for (var i = 0; i < permanentAddressInputs.length; i++) {
    if (checkbox.checked) {
      permanentAddressInputs[i].value = residenceAddressInputs[i].value;
    } else {
      permanentAddressInputs[i].value = '';
    }
    permanentAddressInputs[i].readOnly = checkbox.checked;
  }
});




