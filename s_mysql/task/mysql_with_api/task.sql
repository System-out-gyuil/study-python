create table tbl_papago(
    papago_id bigint auto_increment primary key,
    papago_translate_before varchar(500) not null,
    papago_translate_after varchar(500) not null
);

drop table tbl_papago;
select * from tbl_papago;

create table tbl_user(
    user_id bigint auto_increment primary key,
    user_email varchar(255) not null unique,
    user_password varchar(255) not null
);

select * from tbl_user;

create table tbl_image(
    image_id bigint auto_increment primary key,
    image_name varchar(255) not null,
    image_content varchar(500) not null,
    image_url varchar(500) not null
);

select * from tbl_image;