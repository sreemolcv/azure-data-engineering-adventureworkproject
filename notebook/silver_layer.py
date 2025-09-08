# Databricks notebook source
from pyspark.sql.functions import *
from pyspark.sql.types import *

# COMMAND ----------

# MAGIC %md
# MAGIC ## SILVER LAYER SCRIPT

# COMMAND ----------

# MAGIC %md
# MAGIC ### DATA ACCESSS USING APPLICATION

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type.awdatastroragelake.dfs.core.windows.net", "OAuth")
spark.conf.set("fs.azure.account.oauth.provider.type.awdatastroragelake.dfs.core.windows.net", "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider")
spark.conf.set("fs.azure.account.oauth2.client.id.awdatastroragelake.dfs.core.windows.net", "")
spark.conf.set("fs.azure.account.oauth2.client.secret.awdatastroragelake.dfs.core.windows.net", "")
spark.conf.set("fs.azure.account.oauth2.client.endpoint.awdatastroragelake.dfs.core.windows.net", "https://login.microsoftonline.com//oauth2/token")

# COMMAND ----------

# MAGIC %md
# MAGIC ### DATA LOADING

# COMMAND ----------

# MAGIC %md
# MAGIC ####Read Calender Data

# COMMAND ----------

df_cal = spark.read.format('csv')\
                .option("header",True)\
                .option("inferSchema",True)\
                .load('abfss://bronze@awdatastroragelake.dfs.core.windows.net/AdventureWorks_Calendar')

# COMMAND ----------

df_cus = spark.read.format('csv')\
                .option("header",True)\
                .option("inferSchema",True)\
                .load('abfss://bronze@awdatastroragelake.dfs.core.windows.net/AdventureWorks_Customers')

# COMMAND ----------

df_procat = spark.read.format('csv')\
                .option("header",True)\
                .option("inferSchema",True)\
                .load('abfss://bronze@awdatastroragelake.dfs.core.windows.net/AdventureWorks_Product_Categories')

# COMMAND ----------

df_pro = spark.read.format('csv')\
                .option("header",True)\
                .option("inferSchema",True)\
                .load('abfss://bronze@awdatastroragelake.dfs.core.windows.net/AdventureWorks_Products')

# COMMAND ----------

df_ret = spark.read.format('csv')\
                .option("header",True)\
                .option("inferSchema",True)\
                .load('abfss://bronze@awdatastroragelake.dfs.core.windows.net/AdventureWorks_Returns')

# COMMAND ----------

df_sales = spark.read.format('csv')\
                .option("header",True)\
                .option("inferSchema",True)\
                .load('abfss://bronze@awdatastroragelake.dfs.core.windows.net/AdventureWorks_Sales*')

# COMMAND ----------

df_ter = spark.read.format('csv')\
                .option("header",True)\
                .option("inferSchema",True)\
                .load('abfss://bronze@awdatastroragelake.dfs.core.windows.net/AdventureWorks_Territories')

# COMMAND ----------

df_subcat = spark.read.format('csv')\
                .option("header",True)\
                .option("inferSchema",True)\
                .load('abfss://bronze@awdatastroragelake.dfs.core.windows.net/Product_Subcategories')

# COMMAND ----------

# MAGIC %md
# MAGIC #### TRANSFORMATIONS

# COMMAND ----------

df_cal.display()

# COMMAND ----------

df_cal = df_cal.withColumn('Month', month(col('Date')))\
               .withColumn('Year', year(col('Date')))
df_cal.display()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Calender

# COMMAND ----------

df_cal.write.format('parquet')\
            .mode('append')\
            .option("path","abfss://silver@awdatastroragelake.dfs.core.windows.net/AdventureWorks_Calendar")\
            .save()

# COMMAND ----------

# MAGIC %md 
# MAGIC #### Customers

# COMMAND ----------

df_cus.display()

# COMMAND ----------

df_cus = df_cus.withColumn('fullName',concat_ws(' ',col('Prefix'),col('FirstName'),col('LastName')))
df_cus.display()

# COMMAND ----------

df_cus.write.format('parquet')\
            .mode('append')\
            .option("path","abfss://silver@awdatastroragelake.dfs.core.windows.net/AdventureWorks_Customers")\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Subcategories

# COMMAND ----------

df_subcat.display()

# COMMAND ----------

df_subcat.write.format('parquet')\
            .mode('append')\
            .option("path","abfss://silver@awdatastroragelake.dfs.core.windows.net/AdventureWorks_Subcategories")\
            .save()


# COMMAND ----------

# MAGIC %md
# MAGIC #### Products

# COMMAND ----------

df_pro.display()

# COMMAND ----------

df_pro = df_pro.withColumn('productSKU',split(col('ProductSKU'),'-')[0])\
              .withColumn('productName',split(col('ProductName'),' ')[0])

# COMMAND ----------

df_pro.display()

# COMMAND ----------

df_pro.write.format('parquet')\
            .mode('append')\
            .option("path","abfss://silver@awdatastroragelake.dfs.core.windows.net/AdventureWorks_Products")\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC #### Returns 

# COMMAND ----------

df_ret.display()

# COMMAND ----------

df_ret.write.format('parquet')\
            .mode('append')\
            .option("path","abfss://silver@awdatastroragelake.dfs.core.windows.net/AdventureWorks_Returns")\
            .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Territories

# COMMAND ----------

df_ter.display()

# COMMAND ----------

df_ter.write.format('parquet')\
            .mode('append')\
            .option("path","abfss://silver@awdatastroragelake.dfs.core.windows.net/AdventureWorks_Territories")\
            .save()


# COMMAND ----------

# MAGIC %md
# MAGIC Sales

# COMMAND ----------

df_sales.display()

# COMMAND ----------

df_sales = df_sales.withColumn('StockDate', to_timestamp('StockDate'))

# COMMAND ----------

df_sales = df_sales.withColumn('OrderNumber',regexp_replace(col('OrderNumber'),'S','T'))

# COMMAND ----------

df_sales = df_sales.withColumn('multiply',col('OrderLineitem')*col('OrderQuantity'))


# COMMAND ----------

df_sales.display()

# COMMAND ----------

df_sales.write.format('parquet')\
            .mode('append')\
            .option("path","abfss://silver@awdatastroragelake.dfs.core.windows.net/AdventureWorks_Sales")\
            .save()


# COMMAND ----------

# MAGIC %md
# MAGIC #### Sales Analysis

# COMMAND ----------

df_sales.groupBy('OrderDate').agg(count('OrderNumber').alias('total_order')).display()

# COMMAND ----------

df_procat.display()

# COMMAND ----------

df_ter.display()

# COMMAND ----------

