import pandas as pd
from databricks.sdk.runtime import dbutils

def get_pg_config(dbutils, scope:str ='pg-scope'):
    keys = ["db-host", "db-name", "db-user", "db-password", "db-port"]
    config = {}
    for key in keys:
        config[key] = dbutils.secrets.get(scope=scope, key=key)
    return config

cnfg = get_pg_config(dbutils)
# df = (
#     spark.read.format("jdbc").option(
#         "url", f'jdbc:postgresql://{cnfg["db-host"]}:{cnfg["db-port"]}/{cnfg["db-name"]}'
#     ).option("dbtable", "oltp.raw_orders").option("user", cnfg["db-user"]).option("password", cnfg["db-password"]).option(
#         "driver", "org.postgresql.Driver"
#     ).option("sslmode", "require").load()
# )

df = (
    spark.read.format("jdbc").option(
        "url", f'jdbc:postgresql://{cnfg["db-host"]}:{cnfg["db-port"]}/{cnfg["db-name"]}'
    ).option("dbtable", "oltp.Customers").option("user", cnfg["db-user"]).option("password", cnfg["db-password"]).option(
        "driver", "org.postgresql.Driver"
    ).option("sslmode", "require").load()
)
df.write.format('delta').mode("overwrite").saveAsTable("project_3.bronze.Customers")
