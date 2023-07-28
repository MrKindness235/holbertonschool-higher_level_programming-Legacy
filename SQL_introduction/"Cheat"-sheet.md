# Table structure in SQL

When we actually build the database, each relation scheme becomes the structure for one table.
The SQL syntax for creating the table includes a data type for each attribute, 
which is needed for the database but a data type is not the same as the domain of the attribute.
Example: customers table

CREATE TABLE customers (
   first_name VARCHAR(20) NOT NULL,
   last_name  VARCHAR(20) NOT NULL,
   phone      VARCHAR(20) NOT NULL,
   street     VARCHAR(50),
   zipcode    VARCHAR(5));

In this example, VARCHAR is a datatype in SQL databases that state the values of the column are 
variable-length character string of no more than the number of characters in parentheses.
Consult your own system documentation for supported data types.
We will explain the extra keyword NOT NULL when we look at rows and tables.

---------------------------------------------------------------------------------------------------------------------------------------------------

# Inserting rows

In practice, when we create a table row in SQL, we are actually making the 
assignment of domain values to attributes, just as in the tuple definition.

INSERT INTO customers(first_name, last_name, phone, street, zipcode)
  VALUES ('Tom', 'Jewett', '714-555-1212', '10200 Slater', '92708');

## SQL statement to insert one row with values for all columns.
---------------------------------------------------------------------------------------------------------------------------------------------------

In SQL, you can omit the attribute names from the INSERT INTO statement, as long as you keep the comma-delimited list
of values in exactly the same order as was used to create the table. This syntax is more prone to errors, so use sparingly. 
It is provided for completion. Removing the attribute names from the above statement, gives the SQL statement below.

INSERT INTO customers
  VALUES ('Tom', 'Jewett', '714-555-1212', '10200 Slater', '92708');

## SQL statement to insert one row with values for all columns in the order specified when the table was created.

-------------------------------------------------------------------------------------------------------------------------------------------------

It is also possible to list only some of the attribute names, the ones we provide values for; in that case, 
the remaining attributes will be assigned NULL in such rows, assuming there is no constraint prohibiting NULLs in such columns. 
In the case of the customers table, it was created with NOT NULL constraint on the name and phone number columns, 
so non-NULL values for these must be inserted. On the other hand, there is no such constraint on the other columns, so NULL is allowed.

INSERT INTO customers(first_name, last_name, phone)
  VALUES ('Alvaro', 'Monge', '562-985-4671'),
         ('Wayne', 'Dick', '562-985-1190');

## SQL statement to insert two rows, omitting values for some columns.

-------------------------------------------------------------------------------------------------------------------------------------------------

# Updating rows

The UPDATE statement is used to modify the value for one or more attributes in the specified rows of a table. 
When we change the data in a table row using SQL, we are also following the tuple definition of assigning domain values to attributes.

The statement below will modify all rows in table customers that have a phone number of '714-555-1212' 
and change them to have the phone number specified in the SET clause.

UPDATE customers
  SET phone = '714-555-2323'
  WHERE phone = '714-555-1212';

## SQL statement to update a phone number in the table.
-------------------------------------------------------------------------------------------------------------------------------------------------

# Deleting rows

The SQL DELETE statement is used to delete rows. When deleting rows, you can specify the rows to delete via an optional condition. The following figures provide two examples.

The statement below will delete all rows in table customers that have a value of '90840' in the cZipCode column.

DELETE FROM customers
  WHERE cZipCode = '90840';

## SQL statement to delete rows from a table.

The statement below will delete all rows in table customers; in this case, no criteria is specified in a WHERE clause, so all rows are deleted. Beware running such statements as you will lose all rows in the table.

DELETE FROM customers;

## SQL statement to delete all rows from a table.
-------------------------------------------------------------------------------------------------------------------------------------------------