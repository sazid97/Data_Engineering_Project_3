import pandas as pd


def get_pg_config(dbutils, scope: str = "pg-scope") -> dict:
    keys = ["db-host", "db-port", "db-name", "db-user", "db-password"]
    return {k: dbutils.secrets.get(scope=scope, key=k) for k in keys}

df = get_pg_config()
df.write.format('delta').mode("append").saveAsTable("project_3.bronze.raw_orders")
