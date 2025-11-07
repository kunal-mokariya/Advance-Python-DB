import _sqlite3 as sq
cnn = sq.connect("my.db");
cursor = cnn.cursor();
cursor.execute("create table if not exists abc(name text)");
cursor.execute("insert into abc(name)values(?)",("admin",));
cursor.close();
cnn.commit()
cnn.close();
