create table gallery (
    id serial not null primary key,
    user_id int not null default 0,
    img_url varchar(255) not null default '',
    prompt varchar(4096) not null default '',
    size varchar(16) not null default '',
    artist varchar(255) not null default '',
    style varchar(256) not null default '',
    stat smallint not null default 0,
    is_show smallint not null default 0,
    model_name varchar(64) not null default '',
    created_at timestamp not null default now()
)

comment on column gallery.is_show is '是否在画廊展示';

create index idx_uid on gallery(user_Id);
create index idx_stat on gallery(stat);
create index idx_is_show on gallery(is_show);


create table users(
    id serial not null primary key,
    name varchar(255) not null,
    profile_url varchar(255) not null,
    credits int not null default 0,
    gender smallint not null default 1,
    city varchar(64) not null default '',
    province varchar(64) not null default '',
    country varchar(64) not null default '',
    openid varchar(256) not null default '',
    unionid varchar(256) not null default '',
    created_at timestamp not null default now()
);

comment on column users.credits is '信用分';

create index idx_unionid on users(unionid);