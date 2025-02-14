//Rainfall_Groups
//Min 255 Max 4103

//rainfall 255 & 1200 - Low
//rainfall 1200 2800 - Medium
//Rainfall 2800 & 4103 - High

alter table agriculture
add rainfall_groups string;

select * from agriculture;

//1st Update
update agriculture
set rainfall_groups = 'Low'
where rainfall>=255 and rainfall<1200

//2nd update
update agriculture
set rainfall_groups = 'Medium'
where rainfall >=1200 and rainfall<2800

//3rd update
update agriculture
set rainfall_groups='High'
where rainfall >=2800

select * from agriculture;
