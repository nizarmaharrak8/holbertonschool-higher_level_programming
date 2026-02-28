-- Write a query to find the genre_id for each show. The result should include the show title and genre_id, and be ordered by show title and genre_id in ascending order.
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;