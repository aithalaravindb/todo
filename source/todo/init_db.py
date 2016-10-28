INIT_DB = [
	"""
	CREATE TABLE `Task` (
		`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		`title`	TEXT NOT NULL,
		`created`	TEXT NOT NULL DEFAULT (datetime('now')),
		`deadline`	TEXT,
		`start`	TEXT NOT NULL DEFAULT (datetime('now')),
		`priority`	INTEGER NOT NULL DEFAULT 1,
		`done`	TEXT,
		`context`	INTEGER NOT NULL
	);
	""",
	"""
	CREATE TABLE `Context` (
		`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
		`path`	TEXT NOT NULL UNIQUE,
		`priority`	INTEGER NOT NULL DEFAULT 1,
		`visibility`	TEXT NOT NULL DEFAULT 'normal'
	);
	""",
	"""
	INSERT INTO `Context` (path) VALUES ('')
	"""
]