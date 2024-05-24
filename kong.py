
from diagrams import Diagram, Cluster
from diagrams.onprem.network import Kong
from diagrams.onprem.database import Postgresql
from diagrams.onprem.inmemory import Redis

with Diagram( show=False, filename="kong"):

    with Cluster("Kong"):
        kong_db = Postgresql("PostgreSQL")
        kong = Kong("Kong")
        kong_redis = Redis("Redis")