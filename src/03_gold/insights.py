from pyspark.sql import functions as F

df_raw_orders = spark.read.table("project_3.bronze.raw_orders")
df_customers = spark.read.table("project_3.bronze.Customers")

df_rw = df_raw_orders.groupBy("cust_id").agg(
    F.count("order_id").alias("total_orders"),
    F.sum("order_amount").alias("total_order_amount"),
    F.avg("order_amount").alias("avg_order_amount")
)
df_summery = df_rw.join(df_customers, on="cust_id", how="left").orderBy(F.desc("total_order_amount"))
df_summery.write.format('delta').mode("overwrite").saveAsTable("project_3.gold.customer_order_summary")
