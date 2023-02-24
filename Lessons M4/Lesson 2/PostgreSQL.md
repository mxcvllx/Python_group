SELECT PART1

1. Categories jadval barcha ustun ma’lumotlarini bilan qaytaring
   
   
   select * from categories
   
   **Result**
   ![img.png](img.png)


2. Categories jadval category_name va description ustun ma’lumotlarini qaytaring.

    select category_name, description from categories
   ![img_1.png](img_1.png)


3. Categories jadval barcha ustun ma’lumotlari olishda ustun nomlarini o’zbekcha tarjimada

   select category_name as nomi, description as tavsifi, picture as rasm from categories
   ![img_2.png](img_2.png)


4. Categories jadvaldan kategoriya nomi ’Confections’ ga teng bo’lgan ma’lumotlarni qaytaring

   select * from categories
   
   where category_name='Confections'
   ![img_3.png](img_3.png)


5. Categories jadvaldan kategoriya nomi ‘Produce’ yoki ‘Seafood’ bo’lgan ma’lumotlarni qaytaring.

    select * from categories

    where category_name='Seafood' or category_name='Produce'
    ![img_4.png](img_4.png)


6. Categories jadvaldan quyida belgilangan ma’lumotlarni qaytaring

   select * from categories

   where category_name='Seafood' or category_name='Produce' or category_name='Meat/Poultry'
   ![img_5.png](img_5.png)


7. Categories jadvaldan ma’lumotlarni description alifbo bo’yicha Z-A tartibida chiqaring.

   select * from categories
   
   order by description desc
   ![img_6.png](img_6.png)


8. Customers jadvalidan barcha ma’lumotlarni oling

   select * from customers
   ![img_7.png](img_7.png)


9. Customers jadvalida ustun nomlarini o’zbekcha holatda oling.

   select
   
   customer_id as Mijoz_idisi,
   
   company_name as Shirkat_nomi,
   
   contact_name as kontakt_nomi,
   
   contact_title as kontakt_sarlavhasi,
   
   address as manzil,
   
   city as shahar,
   
   region as mintaqa,
   
   postal_code as Pochta_kodi,
   
   country as mamlakat,
   
   phone as telefon,
   
   fax as faks
   
   from customers
   ![img_8.png](img_8.png)


10. Customers jadvalidan contact_title ‘Owner’ bo’lgan ma’lumotlarni qaytaring.

   select * from customers

   where contact_title='Owner'
   ![img_9.png](img_9.png)


11. Customers jadvalidan city ‘London’ bo’lgan ma’lumotlarni qaytaring.

    select * from customers
    
    where city='London'
    ![img_10.png](img_10.png)


12. Customers jadvalidan region ustun NULL bo’lgan ma’lumotlarni qaytaring.

    select contact_name, region from customers
    
    where region is null
    ![img_11.png](img_11.png)


13. Customers jadvalidan region ustun NULL bo’lmagan ma’lumotlarni qaytaring.

    select contact_name, region from customers
    
    where region is not null
    ![img_12.png](img_12.png)


14. Customers jadvalidan country ustun Germany bo’lgan ma’lumotlarni qaytaring.

    select * from customers
    
    where country='Germany'
    ![img_13.png](img_13.png)


15. Customers jadvalidan country ustun Germany bo’lgan qatorlar sonini qaytaring.

    select count(county) from customers
    
    where country='Germany'
    ![img_14.png](img_14.png)


16. Customers jadvalidan fax ustun NULL bo’lmalgan ma’lumotlarni contact_name ustun alifbo tartiba tartiblab qaytaring.

    select fax, contact_name from customers
    
    where fax is not null
    
    order by contact_name asc
    ![img_15.png](img_15.png)


17. Employees jadvaldan barcha ma’lumotlarni qaytaring

    select * from employees
    ![img_16.png](img_16.png)


18. Employees jadval ustun nomlarini o’zbekcha qaytaring.

    select
    
    employee_id as xodim_identifikatori,

    last_name as Ism,
    
    first_name as Familiya,

    title as sarlavha,
    
    title_of_courtesy as sarlavhasi,
    
    birth_date as tugilgan_kun_sanasi,
    
    hire_date as ishga_qabul_qilingan_sanasi,
    
    address as manzil,
    
    city as shahar,
    
    region as mintaqa,
    
    postal_code as Pochta_kodi,
    
    country as mamlakat,
      
    home_phone as Uy_telefoni,
    
    extension as kengaytma,
    
    photo as rasm,
    
    notes as eslatmalar,
    
    reports_to as hisobotlar,
    
    photo_path as rasm
    
    from employees
    ![img_17.png](img_17.png)


19. Employess jadvaldan title_of_courtest ‘Mr’ bo’lgan xodimlarni firts_name alifbo tartibida qaytaring

    select title_of_courtesy, first_name from employees
   
    where title_of_courtesy='Mr.'
    
    order by first_name asc
    ![img_18.png](img_18.png)


20. Employes jadvalda title ‘Sales Representative’ bo’lgan xodimlar sonini qaytaring

    select count(*) from employees
    
    where title='Sales Representative'
    ![img_19.png](img_19.png)


21. Employes jadvalda hire_date 1994-yilda bo’lgan ma’lumotlarni qaytaring.

    select hire_date from employees
    
    where hire_date between '1994-01-01' and '1994-12-31'
    ![img_20.png](img_20.png)


22. Employes jadvaldan region NULL bo’lmagan xodimlarni first_name, last_name, title, city,

    home_phone ma’lumotlarini first_name Z-A alifbo tartibida qaytaring.
    
    select region, first_name, last_name, title, city,home_phone from employees
    
    where region is not null
    
    order by first_name desc
    ![img_21.png](img_21.png)


23. Orders jadvaldan customer_id ‘VINET’ bo’lgan buyurtmalarni qaytaring

    select order_id, ship_address, ship_name, customer_id from orders
    
    where customer_id='VINET'
    ![img_22.png](img_22.png)


24. Orders jadvaldan order_date ustuni orqali 1996-yildagi ma’lumotlarni qaytaring.

    select * from orders
    
    where order_date between '1996-01-01' and '1996-12-31'
    
    and shipped_date between '1996-01-01' and '1996-12-31'
    
    and required_date between '1996-01-01' and '1996-12-31'
    ![img_23.png](img_23.png)


25. Orders jadvaldan ship_region ustun NULL bo’lmagan ma’lumotlarni qaytaring.

    select * from orders
    
    where ship_region is not null
    ![img_24.png](img_24.png)


26. Orders jadvaldan order_id 10300 va 10400 orasida bo’lgan ma’lumotlarni qaytaring.

    select * from orders
    
    where order_id between '10300' and '10400'
    ![img_25.png](img_25.png)


27. Order Details jadvaldan unit_price ustun umumiy qiymatini qaytaring.

    select sum(unit_price) from order_details
    ![img_26.png](img_26.png)
