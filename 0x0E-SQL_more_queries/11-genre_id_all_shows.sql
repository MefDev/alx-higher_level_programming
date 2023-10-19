-- SELECT FROM DB and its table
SELECT ts.title, tg.genre_id FROM tv_shows ts LEFT JOIN tv_show_genres tg ON ts.id = tg.show_id ORDER BY ts.title ASC, tg.genre_id ASC;
