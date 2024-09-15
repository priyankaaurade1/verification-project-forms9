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



function updateValue(resp){
    // $(resp).val(resp.value)
}

$('#user_document_submit_btn').click(function (e) {
    e.preventDefault();
    var c = getCookie('csrftoken');
    var formData = new FormData($('#user_document_form')[0]);
    formData.append('csrfmiddlewaretoken', c)
    $.ajax({
        type: 'POST',
        url:  '/investor/investor_document_submit/',
        dataType: 'json',
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function (json) {
            alert(json.message)
            window.location.replace('/investor/investor_documents_gallery/')
        },   
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ":" + xhr.responseText)
        }
    })
})

//  \\ Investor Profile Submit // \\
function getProfileIdFromUrl() {
    var urlParams = new URLSearchParams(window.location.search);
    var profileId = parseInt(urlParams.get('profile_id'));
    return isNaN(profileId) ? '' : profileId;
}


$('#investor_profile_submit_btn').click(function (e) {
    e.preventDefault();
    var c = getCookie('csrftoken');
    var formData = new FormData($('#profile_form')[0]);
    formData.append('csrfmiddlewaretoken', c)
    formData.append('profile_id', getProfileIdFromUrl()) 
    $.ajax({
        type: 'POST',
        url:  '/investor/investor_profile_submit/',
        dataType: 'json',
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function (json) {
            alert(json.message)
        },   
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ":" + xhr.responseText)
        }
    })
})

function imageCheckBox(trigger,id){
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
            console.log(json.message)
        },   
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ":" + xhr.responseText)
        }
    })
}

function fetchUser(){
    var datalist = $('#user_list')
    datalist.empty()
    fetch('/investor/userEmailIdApi/')
    .then((resp) => resp.json())
    .then(function (data) {
        const result = Object.keys(data[0]).reduce((obj, key) => {
            obj[key] = data.map(_ => _[key]);
            return obj;
        }, {});
        var username = result.username
        for(var i = 0;i<username.length;i++){
            var element = document.createElement("option");
            element.innerText = username[i];
            element.setAttribute('value',username[i])
            datalist.append(element);
        }
    })
}

$('#merge_request').click(function (e) {
    e.preventDefault();
    var c = getCookie('csrftoken');
    var formData = new FormData($('#merge_request_form')[0]);
    formData.append('csrfmiddlewaretoken', c)
    $.ajax({
        type: 'POST',
        url:  '/investor/profile_merge_request/',
        dataType: 'json',
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function (json) {
            if(json.message != 400){
                alert(json.message)
                window.location.reload()
            }
            else{
                alert('It seems some error has occured.')
            }
        },   
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ":" + xhr.responseText)
        }
    })
})

$('.merge-approve-button-2').click(function (e) {
    e.preventDefault();
    var c = getCookie('csrftoken');
    var formData = new FormData();
    formData.append('csrfmiddlewaretoken', c)
    formData.append('approved_id', $(this).attr("id"))
    $.ajax({
        type: 'POST',
        url:  '/investor/profile_merge_approved/',
        dataType: 'json',
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function (json) {
            if(json.message != 400){
                alert(json.message)
                window.location.reload()
            }
            else{
                alert('It seems some error has occured.')
            }
        },   
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ":" + xhr.responseText)
        }
    })
})

var bank_form_html="";
$('#add_bank_detail_form').click(function (e) {
    e.preventDefault();
    var form_html = $('.clone')
    var form_len = $('#bank_form_len')
    if(bank_form_html == ""){
        form_html_new = form_html.html().replaceAll(`_${form_len.val()}`,`_${parseInt(form_len.val())+1}`).replace(`<button type="button" id="add_bank_detail_form" class="btn btn-warning mt-5">Add</button>`,'')
        bank_form_html=form_html_new
    }
    else{       
        form_html_new = bank_form_html.replace(new RegExp(`_${form_len.val()}`, 'g'), `_${parseInt(form_len.val())+1}`);
    }
    document.getElementById('bank_form_len').value = parseInt(form_len.val())+1
    $('.clone').append(form_html_new)
});

var cc_form_html="";
$('#add_cc_detail_form').click(function (e) {
    e.preventDefault();
    var cc_html = $('.cc_clone')
    var form_len = $('#cc_form_len')
    if(cc_form_html == ""){
        form_html_new = cc_html.html().replaceAll(`_${form_len.val()}`,`_${parseInt(form_len.val())+1}`).replace(`<button type="button" id="add_cc_detail_form" class="btn btn-warning mt-5">Add</button>`,'')
        cc_form_html=form_html_new
    }
    else{       
        form_html_new = cc_form_html.replace(new RegExp(`_${form_len.val()}`, 'g'), `_${parseInt(form_len.val())+1}`);
    }
    document.getElementById('cc_form_len').value = parseInt(form_len.val())+1
    $('.cc_clone').append(form_html_new)
});

var nominee_form_html="";
$('#add_nominee_detail_form').click(function (e) {
    
    e.preventDefault();
    var nominee_html = $('.nominee_clone')
    var form_len = $('#nominee_form_len')
    if(nominee_form_html == ""){
        form_html_new = nominee_html.html().replaceAll(`_${form_len.val()}`,`_${parseInt(form_len.val())+1}`).replace(`<button type="button" id="add_nominee_detail_form" class="btn btn-warning mt-5">Add</button>`,'')
        nominee_form_html=form_html_new
    }
    else{       
        form_html_new = nominee_form_html.replace(new RegExp(`_${form_len.val()}`, 'g'), `_${parseInt(form_len.val())+1}`);
    }
    document.getElementById('nominee_form_len').value = parseInt(form_len.val())+1
    $('.nominee_clone').append(form_html_new)
});


function redirectProfile(profile_id){
    window.location.href = '/investor/investor_details/?profile_id=' + profile_id;
}


  window.onload = function () {

    try{
        var profileSelectValue = sessionStorage.getItem("profileSelect");
        if(profileSelectValue){
            var selectElement = document.getElementById("user_select");
            for (var i = 0; i < selectElement.options.length; i++) {
              if (selectElement.options[i].value == profileSelectValue) {
                selectElement.selectedIndex = i;
                break;
              }
            }
            $('#user_select').change()
        }
        else{
            $('#user_select').change()
        }

    }
    
    catch(err){
        console.log(err)
    }
  };

function updateFormStatus(profile_id) {
    var depositoryElements = document.getElementsByClassName('depository');
    $('.input_profile_id').removeAttr('value');
    $('.input_profile_id').attr('value', profile_id);
    sessionStorage.setItem("profileSelect", profile_id)
    for (var i = 0; i < depositoryElements.length; i++) {
      (function () {
        var element = depositoryElements[i];
        var depository_id = element.getAttribute('id').split('_')[1];
        fetch('/investor/getFormStatus/' + parseInt(profile_id) + '/' + parseInt(depository_id) + '/')
          .then(response => response.json())
          .then(data => {
            if (data.message == 200) {
              element.textContent = 'Continue';
            } else {
              element.textContent = 'Begin';
            }
          })
          .catch(error => {
            console.log('Error updating form status:', error);
          });
      })();
    }
  }
  
//   profile upload button
document.addEventListener('DOMContentLoaded', function() {
  const fileLinks = [
    { linkId: 'file-link1', sectionId: 'aadhar_card_self', inputName: 'aadhar_card_self' },
    { linkId: 'file-link2', sectionId: 'pan_card_self', inputName: 'pan_card_self' },
    { linkId: 'file-link3', sectionId: 'aadhar_card_father', inputName: 'aadhar_card_father' },
    { linkId: 'file-link4', sectionId: 'pan_card_father', inputName: 'pan_card_father' },
    { linkId: 'file-link5', sectionId: 'aadhar_card_mother', inputName: 'aadhar_card_mother' },
    { linkId: 'file-link6', sectionId: 'pan_card_mother', inputName: 'pan_card_mother' },
    { linkId: 'file-link7', sectionId: 'aadhar_card_spouse', inputName: 'aadhar_card_spouse' },
    { linkId: 'file-link8', sectionId: 'pan_card_spouse', inputName: 'pan_card_spouse' }
  ];

  fileLinks.forEach(function(fileLink) {
    const link = document.getElementById(fileLink.linkId);
    const section = document.getElementById(fileLink.sectionId);
    const inputField = document.querySelector('.form-control[name="' + fileLink.inputName + '"]');

    link.addEventListener('click', function(event) {
      event.preventDefault();
      section.scrollIntoView({ behavior: 'smooth' });
      inputField.focus();
    });
  });
});

//clear form after submit
$(document).ready(function() {
  $('#investor_profile_submit_btn').click(function(event) {
    $('.clearinput').val('');
  
  });
});

// 
  $('#create-profile-submit').click(function (e) {
    e.preventDefault();
    console.log('working')
    var c = getCookie('csrftoken');
    var formData = new FormData($('#create_profile_form')[0]);
    formData.append('csrfmiddlewaretoken', c)
    // formData.append('approved_id', $(this).attr("id"))
    $.ajax({
        type: 'POST',
        url:  '/investor/create_profile_form/',
        dataType: 'json',
        data: formData,
        cache: false,
        processData: false,
        contentType: false,
        enctype: 'multipart/form-data',
        success: function (json) {
           alert(json.message)
        },   
        error: function (xhr, errmsg, err) {
            console.log(xhr.status + ":" + xhr.responseText)
        }
    })
})
// 
  $(document).ready(function() {
      $('.bill-note-1').hide();
      if ($('#bill_name').val() === 'OTHER') {
        $('.bill-note-1').show();
      }     
      $('#bill_name').change(function() {
        if ($(this).val() === 'OTHER') {
          $('.bill-note-1').show();
        } else {
          $('.bill-note-1').hide();
        }
      });
    });

// 

  $(document).ready(function() {
    $('.Unemployed').hide(); 
    $('.others_specify').hide();
  
    if ($('#employeement').val() === 'Student' || $('#employeement').val() === 'Unemployed' || $('#employeement').val() === 'Housewife') {
      $('.Unemployed').hide();
      $('.others_specify').hide();
    } else if ($('#employeement').val() === 'Others') {
      $('.Unemployed').show();
      $('.others_specify').show();
    } else {
      $('.Unemployed').show(); 
      $('.others_specify').hide();
    }
  
    $('#employeement').change(function() {
      if ($(this).val() === 'Student' || $(this).val() === 'Unemployed' || $(this).val() === 'Housewife') {
        $('.Unemployed').hide();
        $('.others_specify').hide();
      } else if ($(this).val() === 'Others') {
        $('.Unemployed').show();
        $('.others_specify').show();
      } else {
        $('.Unemployed').show(); 
        $('.others_specify').hide();
      }
    });
  });



// 
     $(function(){
        var dtToday = new Date();
    
        var month = dtToday.getMonth() + 1;// jan=0; feb=1 .......
        var day = dtToday.getDate();
        var year = dtToday.getFullYear() - 18;
        if(month < 10)
            month = '0' + month.toString();
        if(day < 10)
            day = '0' + day.toString();
    	var minDate = year + '-' + month + '-' + day;
        var maxDate = year + '-' + month + '-' + day;
    	$('#dob').attr('max', maxDate);
    });

// 

// 
function openImage(base64data) {
  var newWindow = window.open();
  newWindow.document.write('<img src="data:image/jpeg;base64,' + base64data + '">');
  return false;
}

// fetch documents by selecting nationality
function fetchDocumentManager() {
  var selectedNationality = $('#nationality').val(); 
  fetch(`/investor/fetchDocumentManager/${selectedNationality}`)
    .then((resp) => resp.json())
    .then(function (data1) {
      var selectedData = data1.selected_data;
      if (selectedData.includes('AADHAR CARD SELF')) {$('.aadhar_card_self').show();} else { $('.aadhar_card_self').hide();}
      if (selectedData.includes('AADHAR CARD FATHER')) {$('.aadhar_card_father').show();} else { $('.aadhar_card_father').hide();}
      if (selectedData.includes('AADHAR CARD MOTHER')) {$('.aadhar_card_mother').show();} else { $('.aadhar_card_mother').hide();}
      if (selectedData.includes('PAN CARD SELF')) {$('.pan_card_self').show();} else { $('.pan_card_self').hide();}
      if (selectedData.includes('PAN CARD FATHER')) {$('.pan_card_father').show();} else { $('.pan_card_father').hide();}
      if (selectedData.includes('PAN CARD MOTHER')) {$('.pan_card_mother').show();} else { $('.pan_card_mother').hide();}
      if (selectedData.includes('PAN CARD SPOUSE')) {$('.pan_card_spouse').show();} else { $('.pan_card_spouse').hide();}
      if (selectedData.includes('AADHAR CA  RD SPOUSE')) {$('.aadhar_card_spouse').show();} else { $('.aadhar_card_spouse').hide();}
 
      if (selectedData.includes('PASSPORT')) {$('.passport').show();} else { $('.passport').hide();}
      if (selectedData.includes('VISA')) {$('.visa').show();} else { $('.visa').hide();}
      if (selectedData.includes('OVERSEA TAX')) {$('.oversea_tax_id').show();} else { $('.oversea_tax_id').hide();}
      if (selectedData.includes('UTILITY BILL')) {$('.bill').show();} else { $('.bill').hide();}
      if (selectedData.includes('BANK PASSBOOK')) {$('.bank_passbook').show();} else { $('.bank_passbook').hide();}
      if (selectedData.includes('BANK STATEMENT')) {$('.bank_statement').show();} else { $('.bank_statement').hide();}
      if (selectedData.includes('BANK CHEQUE')) {$('.bank_cheque').show();} else { $('.bank_cheque').hide();}
      if (selectedData.includes('CREDIT CARD')) {$('.cc_sign').show();} else { $('.cc_sign').hide();}
      console.log(data1)
    })
    .catch(function (error) {
      // alert('No latest record found !')
      console.error(error.response.data.error);
    });
}

// fetch documents by selecting marital_status
function fetchMaritalStatus() {
  var selectedMaritalStatus = $('#martial_status').val(); 
  fetch(`/investor/fetchMaritalStatus/${selectedMaritalStatus}`)
    .then((resp) => resp.json())
    .then(function (data) {
      var selectedData = data.selected_status; 
      if (selectedData && Array.isArray(selectedData)) {
        if (selectedData.includes('AADHAR CARD SELF')) {$('.aadhar_card_self').show();} else { $('.aadhar_card_self').hide();}
        if (selectedData.includes('AADHAR CARD FATHER')) {$('.aadhar_card_father').show();} else { $('.aadhar_card_father').hide();}
        if (selectedData.includes('AADHAR CARD MOTHER')) {$('.aadhar_card_mother').show();} else { $('.aadhar_card_mother').hide();}
        if (selectedData.includes('PAN CARD SELF')) {$('.pan_card_self').show();} else { $('.pan_card_self').hide();}
        if (selectedData.includes('PAN CARD FATHER')) {$('.pan_card_father').show();} else { $('.pan_card_father').hide();}
        if (selectedData.includes('PAN CARD MOTHER')) {$('.pan_card_mother').show();} else { $('.pan_card_mother').hide();}
        if (selectedData.includes('PAN CARD SPOUSE')) {$('.pan_card_spouse').show();} else { $('.pan_card_spouse').hide();}
        if (selectedData.includes('AADHAR CARD SPOUSE')) {$('.aadhar_card_spouse').show();} else { $('.aadhar_card_spouse').hide();}
        console.log(data)
      }  
    })
    .catch(function (error) {
      console.error(error.response.data.error);
    });
}

$(document).ready(function() {
  $('.spouse_name').hide();
  $('#pan_spouse1').hide();
  $('#aadhar_spouse').hide();
  if ($('#martial_status').val() === 'MARRIED') {
    $('.spouse_name').show();
    $('#pan_spouse1').show();
    $('#aadhar_spouse').show();
  } 
      
  $('#martial_status').change(function() {
    if ($(this).val() === 'MARRIED') {
      $('.spouse_name').show();
      $('#pan_spouse1').show();
      $('#aadhar_spouse').show();
    } else {
      $('.spouse_name').hide();
      $('#pan_spouse1').hide();
      $('#aadhar_spouse').hide();
    }
  });
  
  fetchMaritalStatus(); 
});
