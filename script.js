<!-- Function to open the modal with video embeded-->
$(document).on('click', '.tile', function (event) {
  let trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
  let movieTitle = $(this).attr('data-movie-title')
  let sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';

  $('html, body').css({
    overflow: 'hidden',
    height: '100%'
  });

  $("#modal").show();
  $("#modal").css('display','flex');

  $("#modal-video").empty().append($("<iframe></iframe>", {
    'id': 'trailer-video',
    'type': 'text-html',
    'src': sourceUrl,
    'frameborder': 0,
    'width': 1024,
    'height': 576
  }));

  $(".modal_title").append(movieTitle);
});

<!-- Function to close the modal -->
$(document).on('click', '.modal_background, .close', function (event) {
  $("#modal-video").empty();
  $(".modal_title").empty();
  $("#modal").hide();

  $('html, body').css({
    overflow: 'auto',
    height: 'auto'
  });
});
