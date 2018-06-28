import webbrowser
import os
import re


# The page head declaring scripts and styles
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Favorite Movies!</title>

    <link rel="stylesheet" type="text/css" href="style.css">
    <!-- Bootstrap 3 for JS -->
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="script.js" type="text/javascript" charset="utf-8"></script>
</head>'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Main Page Content -->
    <!-- The Modal -->
    <div class="modal_background" id="modal">
      <!-- Modal content -->
      <div class="modal-content">
          <div class="modal-header">
            <p class="modal_title"></p>
            <span class="close">&times;</span>
          </div>
          <div class="modal-body">
            <div id="modal-video">
            </div>
          </div>
      </div>

    </div>
    <div id="header">
        <h1>Next movies to watch!</h1>
    </div>
    <div id="body-tiles">
        {movie_tiles}
    </div>
</body>
</html>
'''

# A single movie entry html template
movie_tile_content = '''
    <div class="tile"  data-yt-id="{youtube_id}" movie-title="{movie_title}">
        <img class="image-tile" src="{poster_image_url}">
        <h2>{movie_title} - {release_date}</h2>
    </div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        youtube_id = (youtube_id_match.group(0) if youtube_id_match else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            release_date=movie.release_date,
            poster_image_url=movie.poster_url,
            youtube_id=youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('next_movie.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
