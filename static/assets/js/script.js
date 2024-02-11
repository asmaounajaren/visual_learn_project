let slideIndex = 1;
showSlides(slideIndex);

// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}

function showSlides(n) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  if (n > slides.length) { slideIndex = 1 }
  if (n < 1) { slideIndex = slides.length }
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex - 1].style.display = "block";
  dots[slideIndex - 1].className += " active";
}



$(document).ready(function () {
  $('.show-statistic-btn').click(function () {
    var person = $(this).data('person');
    console.log(person)

    $.ajax({
      type: 'POST',
      url: '/show_statistic',
      data: { person: person },
      success: function (response) {
        console.log(response);
        if (response.image_base64) {
          $('#emotion-chart-image').attr('src', 'data:image/png;base64,' + response.image_base64);
          $('#img').show();

        } else {
          console.error('No image data found in the response.');
        }
      },
      error: function (error) {
        console.error('Error:', error);
      }
    });
  });
});

