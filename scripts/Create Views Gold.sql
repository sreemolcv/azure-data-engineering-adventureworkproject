---create view calender
CREATE VIEW gold.calender
AS
SELECT 
    *
    FROM
        OPENROWSET(
            BULK'https://awdatastroragelake.blob.core.windows.net/silver/AdventureWorks_Calendar/',
            FORMAT = 'PARQUET'
        ) as QUER1



---create view Customers
CREATE VIEW gold.customers
AS
SELECT 
    *
    FROM
        OPENROWSET(
            BULK'https://awdatastroragelake.blob.core.windows.net/silver/AdventureWorks_Customers/',
            FORMAT = 'PARQUET'
        ) as QUER1




---create view Products
CREATE VIEW gold.products
AS
SELECT 
    *
    FROM
        OPENROWSET(
            BULK'https://awdatastroragelake.blob.core.windows.net/silver/AdventureWorks_Products/',
            FORMAT = 'PARQUET'
        ) as QUER1



---create view Returns
CREATE VIEW gold.returns
AS
SELECT 
    *
    FROM
        OPENROWSET(
            BULK'https://awdatastroragelake.blob.core.windows.net/silver/AdventureWorks_Returns/',
            FORMAT = 'PARQUET'
        ) as QUER1



---create view Sales
CREATE VIEW gold.sales
AS
SELECT 
    *
    FROM
        OPENROWSET(
            BULK'https://awdatastroragelake.blob.core.windows.net/silver/AdventureWorks_Sales/',
            FORMAT = 'PARQUET'
        ) as QUER1



---create view Subcategories
CREATE VIEW gold.subcat
AS
SELECT 
    *
    FROM
        OPENROWSET(
            BULK'https://awdatastroragelake.blob.core.windows.net/silver/AdventureWorks_Subcategories/',
            FORMAT = 'PARQUET'
        ) as QUER1



---create view Territories
CREATE VIEW gold.territories
AS
SELECT 
    *
    FROM
        OPENROWSET(
            BULK'https://awdatastroragelake.blob.core.windows.net/silver/AdventureWorks_Territories/',
            FORMAT = 'PARQUET'
        ) as QUER1