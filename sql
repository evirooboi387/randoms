

SELECT product_name || unit AS product
FROM products;

select * from products;

select product_name as "My Great Products"
from products;

select * from testproducts;
select * from categories;

SELECT testproduct_id, product_name, category_name
FROM testproducts
INNER JOIN categories ON testproducts.category_id = categories.category_id;

SELECT testproduct_id, product_name, category_name
FROM testproducts
LEFT JOIN categories ON testproducts.category_id = categories.category_id;

SELECT testproduct_id, product_name, category_name
FROM testproducts
RIGHT JOIN categories ON testproducts.category_id = categories.category_id;

SELECT testproduct_id, product_name, category_name
FROM testproducts
FULL JOIN categories ON testproducts.category_id = categories.category_id;


SELECT testproduct_id, product_name, category_name
FROM testproducts
CROSS JOIN categories;

select product_id, product_name from products
union
select testproduct_id, product_name from testproducts
order by product_id;

select product_id, product_name from products
union all
select testproduct_id, product_name from testproducts
order by product_id;


select count(customer_id), country
from customers
group by country;


select customers.customer_name, count(orders.order_id) from orders
left join customers on orders.customer_id=customers.customer_id
group by customer_name;

select count(customer_id), country from customers
group by country
having count(customer_id)>5;


select order_details.order_id, sum (products.price) from order_details
left join products on order_details.product_id=products.product_id
group by order_id
having sum(products.price)>400.00;


SELECT product_name,
CASE
  WHEN price < 10 THEN 'Low price product'
  WHEN price > 50 THEN 'High price product'
ELSE
  'Normal product'
END
FROM products;


select product_name,
case
	when price<10 then 'Low price product'
	when price>50 then 'High price product'
else
	'Normal product'
end as "price category"
from products;

select customers.customer_name
from customers
where exists(
select order_id from orders where customer_id=customers.customer_id
);

select customers.customer_name
from customers
where not exists(
select order_id from orders where customer_id=customers.customer_id
);

select product_name from products
where product_id=any(
select product_id
from order_details
where quantity>120
);

create table fruits(name varchar(255));
insert into fruits values('apple'),('apple'),('orange'),('grapes'),('grapes'),('watermelon');

select * from fruits;





CREATE TABLE customers (
   customer_id INT,
   customer_name VARCHAR(50),
   city VARCHAR(50)
);

CREATE TABLE products (
   product_id INT,
   product_name VARCHAR(50),
   category VARCHAR(50),
   price DECIMAL(10,2)
);

CREATE TABLE orders (
   order_id INT,
   customer_id INT,
   product_id INT,
   quantity INT,
   order_date DATE
);

select * from customers where city="Mumbai";

select customer_name, country from customers;

select distinct country from customers;

select count(distinct country) from customers;

select * from customers
where city='London';



CREATE TABLE cars (
brand VARCHAR(255),
model VARCHAR(255),
year INT);

INSERT INTO cars(brand, model, year)
VALUES ('Ford', 'Mustang', 1964);

SELECT * FROM cars;

SELECT brand,year FROM cars;

ALTER TABLE cars ADD color VARCHAR(255);

UPDATE cars
SET color='red'
WHERE brand ='Volvo';

SELECT * FROM cars;
UPDATE cars
SET color='red'
WHERE brand= 'Ford';
SELECT * FROM cars;

alter table cars
drop column color;

select * from cars;



