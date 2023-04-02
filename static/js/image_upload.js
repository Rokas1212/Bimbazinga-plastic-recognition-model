/*  ==========================================
    SHOW UPLOADED IMAGE
* ========================================== */
function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
        $('#imageResult').attr('src', e.target.result);
        localStorage.setItem('imageData', e.target.result);
      };
      reader.readAsDataURL(input.files[0]);
    }
  }


$('#buttonas').click(function() {
    var imageData = localStorage.getItem('imageData');
    if (imageData) {
      sessionStorage.setItem('imageData', imageData);
    }
    window.location.href = 'next-page.html';
  });
  
  var imageData = sessionStorage.getItem('imageData');
  if (imageData) {
    $('#imageResult').attr('src', imageData);
  }

$(function () {
    $('#upload').on('change', function () {
        readURL(input);
    });
});

/*  ==========================================
    SHOW UPLOADED IMAGE NAME
* ========================================== */
var input = document.getElementById( 'upload' );
var infoArea = document.getElementById( 'upload-label' );

// input.addEventListener( 'change', showFileName );
// function showFileName( event ) {
//   var input = event.srcElement;
//   var fileName = input.files[0].name;
//   infoArea.textContent = 'File name: ' + fileName;
// }
