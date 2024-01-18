create table tbl_papago(
    papago_id bigint auto_increment primary key,
    papago_translate_before varchar(500) not null,
    papago_translate_after varchar(500) not null
);

select * from tbl_papago;