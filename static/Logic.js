$(document).ready(function() {
    function addSongToSession() {
      // get song data from clicked row
      console.log('addSongToSession called');
      var title = $(this).find('td:nth-child(1)').text();
      var artist = $(this).find('td:nth-child(2)').text();
      var song_id = $(this).find('td:nth-child(3)').text();
      var mood = $(this).find('td:nth-child(4)').text();
      var self = this;
      var data = {
        'title': title,
        'artist': artist,
        'song_id': song_id, 
        'mood': mood
      };
      $.ajax({
        type: "POST",
        url: "/add_song_to_session",
        data: JSON.stringify(data),
        contentType: "application/json",
        success: function(response) {
          if (response.success) {
            var currentSessionTable = $('.current-session-table tbody');
            var item = '<tr><td>' + title + '</td><td>' + artist + '</td><td style="display:none">' + song_id + '</td><td>' + mood;
            currentSessionTable.prepend(item);
            // remove song from songs table
            $(self).remove();
            
            

            //Add currently playing song
            $.ajax({
              url: '/current_song',
              type: 'GET',
              success: function(response) {
                console.log(response)
                  $('#current-song').text(response.title);
                  $('#artist-name').text(response.artist);
                  $('#song-mood').text(response.mood)
              }
            });
            
            if (currentSessionTable.children().length >= 5) {
              console.log("More children, stop !")
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
                    var row = '<tr><td>' + song.title + '</td><td>' + song.artist + '</td><td style="display:none">' + song.song_id + '</td><td>' + song.mood;
                    console.log("Songs recommended successfully !")
                    // $('.recommended-songs-table tr').click(function() {
                    //     console.log("Clicked on reco song")  
                    //     console.log("song name : ", song.title)
                    //     addSongToSession.call(this);
                    //   });
                    recommendedSongsTable.append(row);
                  }
                }
              });

              // get current mood
              $.ajax({
                url: '/current_session_mood',
                type: 'GET',
                success: function(response) {
                  console.log(response)
                    $('#current-mood').text(response.mood);
                }
              });
            }
          }
        }
      });
    }

    const toggle = $('#toggle');
    
    toggle.change(function() {
        const toggleValue = toggle.prop('checked');
        $.ajax({
            type: 'POST',
            url: '/toggle',
            data: { toggle: toggleValue },
            success: function(response) {
                console.log('Toggle value submitted successfully');
            },
            error: function(err) {
                console.log('Error submitting toggle value:', err);
            }
        });
    });
  
    // add click event listener to songs table rows
    $('.songs-table tr').click(function() {
      addSongToSession.call(this);
    });
  
    // add click event listener to another table component
    // $('.recommended-songs-table tr').click(function() {
    //   console.log("Clicked on reco song")  
    //   addSongToSession.call(this);
    // });

    // add click event listener to parent of recommended table
    $(document).on('click', '.recommended-songs-table tr', function() {
        addSongToSession.call(this);
    });

    $(document).on('click', '.end-session', function() {
      window.location.href = "/";
  });
  });
  