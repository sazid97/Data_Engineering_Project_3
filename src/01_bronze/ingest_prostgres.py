import pandas as pd
dbutils.secrets.get()

df.write.format('delta').mode("append").saveAsTable("project_3.bronze.raw_orders")
