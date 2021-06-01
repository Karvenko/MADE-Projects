add JAR /usr/local/hive/lib/hive-serde.jar;

set hive.exec.max.dynamic.partitions.pernode=116;
set hive.exec.dynamic.partition.mode=nonstrict;

drop table if exists ip_regions;
drop table if exists users;
drop table if exists logs_raw;
drop table if exists logs;

create external table ip_regions (
    ip string,
    region string
)  
row format
    serde 'org.apache.hadoop.hive.serde2.RegexSerDe'
    with serdeproperties (
        "input.regex" = "^(\\S*)\\t(\\S*).*"
    )
stored as textfile
location "/data/user_logs/ip_data_M";

create external table users (
    ip string,
    browser string,
    sex string,
    age int
)
row format
    serde 'org.apache.hadoop.hive.serde2.RegexSerDe'
    with serdeproperties (
        "input.regex" = "^(\\S*)\\t(\\S*)\\t(\\S*)\\t(\\S*).*"
    )
stored as textfile
location "/data/user_logs/user_data_M";

create external table logs_raw (
    ip string,
    `date` string,
    request string,
    page_size int,
    http_status int,
    user_agent string
)
row format
    serde 'org.apache.hadoop.hive.serde2.RegexSerDe'
    with serdeproperties (
        "input.regex" = "^(\\S*)\\t+(\\S*)\\t+(\\S*)\\t+(\\S*)\\t+(\\S*)\\t+(\\S*).*"
    )
stored as textfile
location "/data/user_logs/user_logs_M";

create external table logs (
    ip string,
    `date` string,
    request string,
    page_size int,
    http_status int,
    user_agent string
)
partitioned by (r_date string);

INSERT OVERWRITE TABLE logs PARTITION(r_date) 
SELECT ip, `date`, request, page_size, http_status, user_agent, substr(`date`, 1, 8) from logs_raw;
