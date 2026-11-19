import pandas as pd
from databricks.sdk.runtime import dbutils

def get_pg_config(dbutils, scope: str = "pg-scope") -> dict:
    keys = ["db-host", "db-port", "db-name", "db-user", "db-password"]
    return {k: dbutils.secrets.get(scope=scope, key=k) for k in keys}

cfg = get_pg_config(dbutils)
df = (spark.read.format("jdbc")
      .option("url", "jdbc:postgresql://{}:{}/{}".format(cfg["db-host"], cfg["db-port"], cfg["db-name"]))
      .option("dbtable", "<source-table>")
      .option("user", cfg["db-user"])
      .option("password", cfg["db-password"])
      .option("driver", "org.postgresql.Driver")
      .load())
df.write.format('delta').mode("append").saveAsTable("project_3.bronze.raw_orders")
