```sql
create table Students
(
    id             serial,
    first_name     varchar(100)        not null,
    last_name      varchar(100)        not null,
    username       varchar(100) unique not null,
    phone          varchar(15) unique  not null,
    dob            date,
    date_joined    date,
    date_graduated date,
    is_graduated   boolean default false,
    is_active      boolean default true,
    gpa            real    default 0,
    grade          integer             not null,
    region_id      integer,
    group_id       integer
);
```