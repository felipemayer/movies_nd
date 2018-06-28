// Function to open the modal with video embeded
$(document).on('click', '.tile', function (event) {
  let trailerYouTubeId = $(this).attr('data-yt-id')
  let movieTitle = $(this).attr('movie-title')
  let sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';

  // avoid scrool when modal are open
  $('html, body').css({
    overflow: 'hidden',
    height: '100%'
  });

  // open modal and changing css attributes
  $("#modal").show();
  $("#modal").css('display','flex');

  // addind iframe to show video
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

// Function to close the modal
$(document).on('click', '.modal_background, .close', function (event) {
  $("#modal-video").empty();
  $(".modal_title").empty();
  $("#modal").hide();

  // enable scrool when modal are closed
  $('html, body').css({
    overflow: 'auto',
    height: 'auto'
  });
});
