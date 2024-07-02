USE UNI_DB;

-- CREATE USER1

CREATE USER 'user1'@'localhost' IDENTIFIED BY 'user1@';

GRANT SELECT ON ourViewTable TO 'user1'@'localhost';

SHOW GRANTS FOR 'user1'@'localhost';


-- CREATE USER2

CREATE USER 'user2'@'localhost' IDENTIFIED BY 'user2@';

GRANT ALTER ON ourViewTable TO 'user2'@'localhost';

SHOW GRANTS FOR 'user2'@'localhost';


-- CREATE USER3

CREATE USER 'user3'@'localhost' IDENTIFIED BY 'user3@';

GRANT CREATE,INSERT,UPDATE,DELETE ON ourViewTable TO 'user3'@'localhost';

SHOW GRANTS FOR 'user3'@'localhost';