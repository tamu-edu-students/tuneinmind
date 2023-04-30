$(document).ready(function() {
    function addSongToSession() {
      // get song data from clicked row
      var title = $(this).find('td:nth-child(1)').text();
      var artist = $(this).find('td:nth-child(2)').text();
      var song_id = $(this).find('td:nth-child(3)').text();
      var self = this;
      var data = {
        'title': title,
        'artist': artist,
        'song_id': song_id
      };
      $.ajax({
        type: "POST",
        url: "/add_song_to_session",
        data: JSON.stringify(data),
        contentType: "application/json",
        success: function(response) {
          if (response.success) {
            var currentSessionTable = $('.current-session-table tbody');
            var item = '<tr><td>' + title + '</td><td>' + artist;
            currentSessionTable.prepend(item);
            // remove song from songs table
            $(self).remove();
  
            if (currentSessionTable.children().length >= 5) {
              // Show the recommended songs table
              // $('.recommended-songs-table').show();
              // Make an AJAX request to fetch recommended songs
              $.ajax({
                url: '/get_recommended_songs',
                type: 'GET',
                success: function(response) {
                  // Populate the recommended songs table with the response data
                  var recommendedSongsTable = $('.recommended-songs-table tbody');
                  recommendedSongsTable.empty(); // Clear the table body
                  for (var i = 0; i < response.length; i++) {
                    var song = response[i];
                    var row = '<tr><td>' + song.title + '</td><td>' + song.artist + '</td></tr>';
                    recommendedSongsTable.append(row);
                  }
                }
              });
            }
          }
        }
      });
    }
  
    // add click event listener to songs table rows
    $('.songs-table tr').click(function() {
      addSongToSession.call(this);
    });
  
    // add click event listener to another table component
    $('.recommended-songs-table tr').click(function() {
      addSongToSession.call(this);
    });
  });
  