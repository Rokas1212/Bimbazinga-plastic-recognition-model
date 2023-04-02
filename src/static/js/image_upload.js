/*  ==========================================
    SHOW UPLOADED IMAGE and STORE IN SESSION
* ========================================== */
function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function (e) {
        $('#imageResult').attr('src', e.target.result);
        localStorage.setItem('imageData', e.target.result);
      };
      reader.readAsDataURL(input.files[0]);
    }else if (input.srcElement && input.srcElement.localName === "video") {
        var canvas = document.createElement('canvas');
        canvas.width = input.srcElement.videoWidth;
        canvas.height = input.srcElement.videoHeight;
        var ctx = canvas.getContext('2d');
        ctx.drawImage(input.srcElement, 0, 0, canvas.width, canvas.height);
        var dataURL = canvas.toDataURL();
        $('#imageResult').attr('src', dataURL);
        localStorage.setItem('imageData', dataURL);
    }
  }

/** =====================================
 * RESTORE IMAGE FROM SESSION
 ======================================*/
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

const startCameraBtn = document.getElementById('startCameraBtn');
const video = document.getElementById('videoFeed');
const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

startCameraBtn.addEventListener('click', () => {
  navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
      video.srcObject = stream;
      video.style.display = 'block';
    })
    .catch(err => console.error(err));
});

function takeSnapshot() {
    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
    const dataURL = canvas.toDataURL('image/jpeg'); // Change file type to JPEG
    const imageResult = document.getElementById('imageResult');
    imageResult.setAttribute('src', dataURL);
    localStorage.setItem('imageData', dataURL);
}


// document.getElementById('captureBtn').addEventListener('click', () => {
//     ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
//     const imageData = canvas.toDataURL('image/png');
//     fetch('/', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/x-www-form-urlencoded'
//       },
//       body: `imageData=${encodeURIComponent(imageData)}`
//     })
//     .then(response => response.text())
//     .then(imageUrl => {
//       const img = document.getElementById('imageResult');
//       img.src = imageUrl;
//       img.style.display = 'block';
//     });
//   });


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
