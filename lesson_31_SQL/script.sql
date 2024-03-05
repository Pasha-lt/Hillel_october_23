CREATE TABLE Data_script(data_id INTEGER PRIMARY KEY, name TEXT, data INTEGER CHECK(data<10));
INSERT INTO Data_script(name, data) VALUES ('Hello', 3);
INSERT INTO Data_script(name, data) VALUES ('Hello2', 2);
--INSERT INTO Data(name, data) VALUES ('Hello3', 4);
