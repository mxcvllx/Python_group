                            SELECT PART 2
1. Write a SQL statement that displays all the information about all salespeople.

``sql
    select * from salesman;
``

                            **RESULT**
![img.png](img.png)

3.Write a SQL statement to display a string "This is SQL Exercise, Practice and Solution".

``sql
select 'This is SQL Exercise, Practice and Solution'
``

                            **RESULT**
![img_1.png](img_1.png)

3.Write a SQL query to display three numbers in three columns

``sql
select 5, 10, 15
``

                            **RESULT**
![img_2.png](img_2.png)

4.Write a SQL query to display the sum of two numbers 10 and 15 from the RDBMS server

``sql
select 10 + 15;
``

                            **RESULT**
![img_3.png](img_3.png)

5.Write an SQL query to display the result of an arithmetic expression.

``sql
select 10 + 15 - 5 * 2
``

                            **RESULT**
![img_4.png](img_4.png)

6.Write a SQL statement to display specific columns such as names and commissions for all salespeople

``sql
select name, commission FROM salesman
``

                            **RESULT**
![img_5.png](img_5.png)

7.Write a query to display the columns in a specific order, such as order date, salesman ID, order number, and purchase amount for all orders

``sql
select ord_date, salesman_id, ord_no, purch_amt from orders
``

                            **RESULT**
![img_6.png](img_6.png)

8.From the following table, write a SQL query to identify the unique salespeople ID. Return salesman_id

``sql
select distinct salesman_id from orders
``

                            **RESULT**
![img_7.png](img_7.png)

9.From the following table, write a SQL query to locate salespeople who live in the city of 'Paris'. Return salesperson's name, city.

``sql
select name,city from salesman 
where city='Paris'
``

                            **RESULT**
![img_8.png](img_8.png)

10.From the following table, write a SQL query to find customers whose grade is 200. Return customer_id, cust_name, city, grade, salesman_id.

``sql
select *from customer where grade=200
``

                            **RESULT**
![img_9.png](img_9.png)

11.From the following table, write a SQL query to find orders that are delivered by a salesperson with ID. 5001. Return ord_no, ord_date, purch_amt

``sql
select ord_no, ord_date, purch_amt from orders where salesman_id=5001
``

                            **RESULT**
![img_10.png](img_10.png)

12.From the following table, write a SQL query to find the Nobel Prize winner(s) for the year 1970. Return year, subject and winner.

``sql
select year,subject,winner from nobel_win where year=1970
``

                            **RESULT**
![img_11.png](img_11.png)

14.From the following table, write a SQL query to locate the Nobel Prize winner ‘Dennis Gabor'. Return year, subject.

``sql
select year, subject from nobel_win where winner = 'Dennis Gabor';
``

                            **RESULT**
![img_12.png](img_12.png)

15.From the following table, write a SQL query to find the Nobel Prize winners in the field of ‘Physics’ since 1950. Return winner

``sql
select winner from nobel_win where year>=1950 and subject='Physics';
``

                            **RESULT**
![img_13.png](img_13.png)

16.From the following table, write a SQL query to find the Nobel Prize winners in ‘Chemistry’ between the years 1965 and 1975. Begin and end values are included. Return year, subject, winner, and country

``sql
select year, subject, winner, country from nobel_win where subject = 'Chemistry' and year>=1965 AND year<=1975;
``

                            **RESULT**
![img_14.png](img_14.png)

17.Write a SQL query to display all details of the Prime Ministerial winners after 1972 of Menachem Begin and Yitzhak Rabin

``sql
select * from nobel_win where year >1972 and winner in ('Menachem Begin','Yitzhak Rabin');
``

                            **RESULT**
![img_15.png](img_15.png)

18.From the following table, write a SQL query to retrieve the details of the winners whose first names match with the string ‘Louis’. Return year, subject, winner, country, and category

``sql
select * from nobel_win where winner like 'Louis %';
``

                            **RESULT**
![img_16.png](img_16.png)

19.From the following table, write a SQL query that combines the winners in Physics, 1970 and in Economics, 1971. Return year, subject, winner, country, and category.

``sql
select * from nobel_win  where (subject ='Physics' and year=1970) union (select * from nobel_win  where (subject ='Economics' and year=1971))
``

                            **RESULT**
![img_17.png](img_17.png)

20.From the following table, write a SQL query to find the Nobel Prize winners in 1970 excluding the subjects of Physiology and Economics. Return year, subject, winner, country, and category

``sql
select * from nobel_win where year=1970 and subject not in('Physiology','Economics')
``

                            **RESULT**
![img_18.png](img_18.png)

21.From the following table, write a SQL query to combine the winners in 'Physiology' before 1971 and winners in 'Peace' on or after 1974. Return year, subject, winner, country, and category.

``sql
select * from nobel_win where (subject ='Physiology' and year<1971) union (select * from nobel_win where (subject ='Peace' and year>=1974))
``

                            **RESULT**
![img_19.png](img_19.png)

22.From the following table, write a SQL query to find the details of the Nobel Prize winner 'Johannes Georg Bednorz'. Return year, subject, winner, country, and category.

``sql
select * from nobel_win where winner='Johannes Georg Bednorz'
``

                            **RESULT**
![img_20.png](img_20.png)

23.From the following table, write a SQL query to find Nobel Prize winners for the subject that does not begin with the letter 'P'. Return year, subject, winner, country, and category. Order the result by year, descending and winner in ascending

``sql
select * from nobel_win where subject not like 'P%' order by year desc, winner
``

                            **RESULT**
![img_21.png](img_21.png)

24.From the following table, write a SQL query to find the details of 1970 Nobel Prize winners. Order the results by subject, ascending except for 'Chemistry' and ‘Economics’ which will come at the end of the result set. Return year, subject, winner, country, and category. 

``sql
select * from nobel_win where year=1970 order by  case when subject in ('Economics','Chemistry') then 1 else 0 end asc, subject, winner
``

                            **RESULT**
![img_22.png](img_22.png)

25.From the following table, write a SQL query to select a range of products whose price is in the range Rs.200 to Rs.600. Begin and end values are included. Return pro_id, pro_name, pro_price, and pro_com.

``sql
select * from item_mast where pro_price between 200 AND 600
``

                            **RESULT**
![img_23.png](img_23.png)

26.From the following table, write a SQL query to calculate the average price for a manufacturer code of 16. Return avg

``sql
select avg(pro_price) from item_mast where pro_com=16
``

                            **RESULT**
![img_24.png](img_24.png)

27.From the following table, write a SQL query to display the pro_name as 'Item Name' and pro_priceas 'Price in Rs.'

``sql
select pro_name as "Item Name", pro_price as "Price in Rs." from item_mast
``

                            **RESULT**
![img_25.png](img_25.png)

28.From the following table, write a SQL query to find the items whose prices are higher than or equal to $250. Order the result by product price in descending, then product name in ascending. Return pro_name and pro_price

``sql
select pro_name, pro_price from item_mast where pro_price >= 250 order by pro_price desc, pro_name
``

                            **RESULT**
![img_26.png](img_26.png)

29.From the following table, write a SQL query to calculate average price of the items for each company. Return average price and company code

``sql
select avg(pro_price), pro_com from item_mast group by pro_com
``

                            **RESULT**
![img_27.png](img_27.png)

30.From the following table, write a SQL query to find the cheapest item(s). Return pro_name and, pro_price. 

``sql
select pro_name, pro_price from item_mast where pro_price = (select min(pro_price) from item_mast)
``

                            **RESULT**
![img_28.png](img_28.png)

31.From the following table, write a SQL query to find the unique last name of all employees. Return emp_lname.

``sql
select distinct emp_lname from emp_details
``

                            **RESULT**
![img_29.png](img_29.png)

32.From the following table, write a SQL query to find the details of employees whose last name is 'Snares'. Return emp_idno, emp_fname, emp_lname, and emp_dept.

``sql
select * from emp_details where emp_lname= 'Snares' 
``

                            **RESULT**
![img_30.png](img_30.png)

33.From the following table, write a SQL query to retrieve the details of the employees who work in the department 57. Return emp_idno, emp_fname, emp_lname and emp_dept.

``sql
select * from emp_details where emp_dept= 57    
``

                            **RESULT**
![img_31.png](img_31.png)