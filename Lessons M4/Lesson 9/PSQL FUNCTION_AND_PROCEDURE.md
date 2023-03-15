LESSONS
1. aircrafts_data table ma'lumotlarida model ustunda json turli en va ru uchun ma'lumotlar berilgan. en yoki ru kalit kiritilganda value sini qaytaradigan funksiya yarating.

```sql
create or replace function en_ru_func(f varchar)
    returns varchar
    language plpgsql
as
$$
declare
    result varchar := ' ';
begin
    if f = 'en' then
        select model['en']
        into result
        from aircrafts_data;
        return result;
    elseif f = 'ru' then
        select model['ru']
        into result
        from aircrafts_data;
        return result;
    end if;
end;
$$;

select en_ru_func(f := 'en')
from bookings;
```


2. airports_data table ma'lumotlaridan foydalanib timezone kiritilganda ma'lumot qaytaradigan funksiya yarating.

```sql
create function airport_timezone(tmz varchar)
    returns airports_data
    language plpgsql
as
$$
begin
    return query
    select * from airports_data
    where timezone = tmz;
end;

$$;

select airport_timezone('Asia/Yekaterinburg');
```

3. airports_data table ma'lumotlaridan foydalanib city ustunda json ma'lumot value larini katta harflarda funksiya yarating

```sql
create or replace function city()
    returns varchar
    language plpgsql
as
$$
declare
    result varchar := ' ';
begin
    select city['en']
    into result
    from airports_data;
    return upper(result);
end;
$$;

select city()
from bookings;
```
