import sqlite3

# Open database connection and cursor object
conn = sqlite3.connect('sqlite\\chinook.db')
c = conn.cursor()

# Fetch all table names from database
c.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(c.fetchall())

# Fetch result from SQL query
c.execute("SELECT Album.AlbumId, Artist.Name, Album.Title, Track.Name, Genre.Name  FROM Artist, Genre, Track LEFT JOIN Album ON Album.ArtistId = Artist.ArtistId AND Album.AlbumId = Track.AlbumId LIMIT 100;")
result = c.fetchall() # Tuple object
print(result)
# Close the database connection and the cursor object
c.close()
conn.close()

# Store SQL query result in CSV file
# Open CSV file
with open('tracks.csv', 'w', encoding='utf-8') as f:
    f.write('Id, Artist, Album, Track, Genre\n')
    
    # Format and write SQL query into CSV file
    for tracks in result:
        track = str(tracks)
        track = track.replace('(', ' ')
        track = track.replace(')', ' ')
        f.write(track + '\n')

# Close the file
f.close()





# LIMIT 10 OFFSET 10
# Shows results between 10 and 20 instead of 1 and 10

# DISTINCT
# Removes duplicates from selected data
    # e. g. SELECT DISTINCT Country from CUSTOMER;

# ORDER BY
# Sorts the selected data ascending
    # e. g. SELECT Name, AlbumId FROM Track ORDER BY AlbumId;
# Descending DESC
    # SELECT Name, AlbumId FROM Track ORDER BY AlbumId DESC;
# Multiple sorting is possible too
    # SELECT Name, Milliseconds, AlbumId
    # FROM Track ORDER BY AlbumId ASC, Milliseconds DESC;
# Find specific entry
    # WHERE = 'something'

# SELECT TrackId, Name, Composer FROM Track
# WHERE Composer = “Miles Davis ” or Composer = “David Brown”;
# Is the same as
# SELECT TrackId, Name, Composer FROM Track
# WHERE Composer IN (“Miles Davis ” , “David Brown”);

# Look for something alike in WHERE with LIKE
# SELECT TrackId, Name, Composer FROM Track
# WHERE Composer LIKE “%Mozart%”;

# COUNT amount
    # SELECT AlbumId, COUNT(TrackId) FROM Track GROUP BY AlbumId;
# SUM of something
    # SELECT AlbumId, SUM(Milliseconds) FROM Track GROUP BY AlbumId;
# MAX value
# MIN value
# HAVING some value specified like count > 10
    # SELECT AlbumId, COUNT(TrackId) FROM Track GROUP BY AlbumId
    # HAVING COUNT(TrackId) > 10;

# INNER JOIN Gets data from multiple tables if the tables both have a value for the JOIN statement
    # SELECT TrackId, Name, Title FROM Album INNER JOIN Track ON Track.AlbumId = Album.AlbumId;
    # Only entries where all tables have an AlbumId
    # Shows only entries that have values
# LEFT JOIN Gets data from multiple tables een though the right table doesn't have values for the WHERE
    # SELECT AlbumId, Name, Title FROM Artist LEFT JOIN Album ON Album.ArtistId = Artist.ArtistId WHERE AlbumId IS NULL;
    # Shows all entries in the left table. Shows NULL if a value isn't in the right table as well
    # Shows all entries

# ? Is like {0} in C#, JavaScript. Something to do with security to rather do it this way
    # cursor.execute(“SELECT * FROM Track WHERE Composer = ?”, favorite_artist)
