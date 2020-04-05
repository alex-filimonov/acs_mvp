
CREATE USER 'acs'@'localhost' IDENTIFIED BY '123';
GRANT ALL PRIVILEGES ON * . * TO 'acs'@'localhost';

/*drop database acs; */
create database acs;

create table cpe (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    serial_number varchar(255),
    vendor_name varchar(255),
    model_name varchar(255),
    all_inform text,
    first_inform TIMESTAMP NOT NULL,
    last_inform TIMESTAMP NOT NULL
);


