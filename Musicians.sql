CREATE TABLE IF NOT EXISTS "Venue" (
	"venue_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"venue_name"	TEXT NOT NULL,
	"venue_capacity"	INTEGER NOT NULL,
	"profile_id"	INTEGER NOT NULL,
	"venue_type"	TEXT NOT NULL,
	FOREIGN KEY("profile_id") REFERENCES "Profile"("profile_id")
);
CREATE TABLE IF NOT EXISTS "Administrator" (
	"admin_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"admin_name"	TEXT NOT NULL,
	"profile_id"	INTEGER NOT NULL,
	FOREIGN KEY("profile_id") REFERENCES "Profile"("profile_id")
);
CREATE TABLE IF NOT EXISTS "Group/Musician" (
	"musician_id"	INTEGER NOT NULL,
	"group_id"	INTEGER NOT NULL,
	FOREIGN KEY("musician_id") REFERENCES "Musician"("musician_id"),
	FOREIGN KEY("group_id") REFERENCES "Group"("group_id")
);
CREATE TABLE IF NOT EXISTS "Group" (
	"group_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"group_name"	TEXT NOT NULL,
	"genre_id"	INTEGER NOT NULL,
	"profile_id"	INTEGER NOT NULL,
	"availability_status"	INTEGER NOT NULL,
	FOREIGN KEY("genre_id") REFERENCES "Genre"("genre_id"),
	FOREIGN KEY("profile_id") REFERENCES "Profile"("profile_id")
);
CREATE TABLE IF NOT EXISTS "Chat/Musician" (
	"chat_id"	INTEGER NOT NULL,
	"musician_id"	INTEGER NOT NULL,
	FOREIGN KEY("chat_id") REFERENCES "Chat"("chat_id"),
	FOREIGN KEY("musician_id") REFERENCES "Musician"("musician_id")
);
CREATE TABLE IF NOT EXISTS "Chat" (
	"chat_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"chat_content"	TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "Musician" (
	"musician_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"name"	TEXT NOT NULL,
	"gender"	INTEGER NOT NULL,
	"profile_id"	INTEGER NOT NULL,
	"birthdate"	TEXT,
	"availability"	INTEGER NOT NULL,
	FOREIGN KEY("profile_id") REFERENCES "Profile"("profile_id")
);
CREATE TABLE IF NOT EXISTS "Media" (
	"media_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"media_type"	TEXT NOT NULL,
	"genre_id"	INTEGER NOT NULL,
	"media_title"	TEXT NOT NULL,
	"media_content"	BLOB NOT NULL,
	FOREIGN KEY("genre_id") REFERENCES "Genre"("genre_id")
);
CREATE TABLE IF NOT EXISTS "Media/Profile" (
	"profile_id"	INTEGER NOT NULL,
	"media_id"	INTEGER NOT NULL,
	FOREIGN KEY("profile_id") REFERENCES "Profile"("profile_id"),
	FOREIGN KEY("media_id") REFERENCES "Media"("media_id")
);
CREATE TABLE IF NOT EXISTS "Profile" (
	"profile_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"profile_name"	TEXT NOT NULL,
	"profile_description"	TEXT,
	"genre_id"	INTEGER NOT NULL,
	"username"	TEXT NOT NULL,
	"password"	TEXT NOT NULL,
	"email"	TEXT NOT NULL,
	"profile_url"	TEXT NOT NULL,
	"location"	TEXT,
	"rating"	REAL NOT NULL,
	FOREIGN KEY("genre_id") REFERENCES "Genre"("genre_id")
);
CREATE TABLE IF NOT EXISTS "Genre" (
	"genre_id"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"genre_name"	TEXT NOT NULL
);
