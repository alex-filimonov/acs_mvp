
CREATE USER 'acs'@'%' IDENTIFIED BY '123';
GRANT ALL PRIVILEGES ON * . * TO 'acs'@'%';

FLUSH PRIVILEGES;


create table cpe (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    serial_number varchar(255),
    vendor_name varchar(255),
    model_name varchar(255),
    all_inform text,
    first_inform TIMESTAMP  DEFAULT CURRENT_TIMESTAMP,
    last_inform TIMESTAMP  DEFAULT CURRENT_TIMESTAMP
);

create table commands (
    id INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
    cpe_id integer,
    command integer,
    request text,
    response text,
    status_id integer,
    create_time  TIMESTAMP  DEFAULT CURRENT_TIMESTAMP,
    update_time  TIMESTAMP  DEFAULT CURRENT_TIMESTAMP
);

create table commands_type (
    id INTEGER NOT NULL,
    command_name varchar(255)
);



delete from commands_type;
insert into commands_type (id,command_name) values (1,'GetParametrName');
insert into commands_type (id,command_name) values (2,'GetParametrValue');


GRANT ALL PRIVILEGES ON *.* TO 'acs'@'%';
FLUSH PRIVILEGES;
