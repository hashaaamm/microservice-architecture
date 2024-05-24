# # diagram.py
# from diagrams import Diagram, Cluster, Edge, Node
# from diagrams.aws.compute import EC2
# from diagrams.aws.database import RDS
# from diagrams.aws.network import ELB
# from diagrams.onprem.client import Users
# from diagrams.onprem.network import Kong
# from diagrams.onprem.database import Postgresql
# from diagrams.onprem.inmemory import Redis
# from diagrams.programming.framework import FastAPI, Django
# from diagrams.onprem.queue import Rabbitmq
# from diagrams.programming.flowchart import Database
# from diagrams.onprem.compute import Server
# from diagrams.onprem.client import Client
# from diagrams.gcp.storage import Storage
# from diagrams.gcp.compute import Run
# from diagrams.gcp.database import SQL
#
# with Diagram(show=False, filename="client_facing_apps", outformat="svg", graph_attr={"bgcolor": "white"}) as diag:
#
#
#     with Cluster("Client facing apps"):
#         with Cluster("HIL service"):
#             notification_service = Run()
#             notification_service_db = SQL("Database")
#             notification_service >> notification_service_db
#
#         with Cluster("Webhook & Notification service"):
#             webhook_service = Run()
#             webhook_service_db = SQL("Database")
#             webhook_service >> webhook_service_db
#
#         with Cluster("File upload service"):
#             file_upload_service = Run()
#             file_upload_service_db = SQL("Database")
#             file_upload_bucket = Storage("Bucket")
#             file_upload_service >> file_upload_service_db
#             file_upload_service_db >> file_upload_bucket
#
#         with Cluster("Result service"):
#             result_service = Run()
#             result_service_db = SQL("Database")
#             result_service >> result_service_db
#
#         with Cluster("Account service"):
#             account_service = Run()
#             account_service_db = SQL("Database")
#             account_service >> account_service_db
#         # client_app_group = [file_upload_service, account_service,result_service, notification_service, webhook_service]
#
#         diag.dot.renderer = "cairo"
from diagrams import Diagram, Cluster, Node
from diagrams.gcp.storage import Storage
from diagrams.gcp.compute import Run
from diagrams.gcp.database import SQL

graph_attr = {
    "bgcolor": "white"
}

cluster_attr = {
    "bgcolor": "white"
}

with Diagram("Client Facing Apps", show=False, filename="client_facing_apps", outformat="svg", graph_attr=graph_attr) as diag:
    with Cluster("Client facing apps", graph_attr=cluster_attr):
        with Cluster("HIL service", graph_attr=cluster_attr):
            notification_service = Run("Notification Service")
            notification_service_db = SQL("Database")
            notification_service >> notification_service_db

        with Cluster("Webhook & Notification service", graph_attr=cluster_attr):
            webhook_service = Run("Webhook Service")
            webhook_service_db = SQL("Database")
            webhook_service >> webhook_service_db

        with Cluster("File upload service", graph_attr=cluster_attr):
            file_upload_service = Run("File Upload Service")
            file_upload_service_db = SQL("Database")
            file_upload_bucket = Storage("Bucket")
            file_upload_service >> file_upload_service_db
            file_upload_service_db >> file_upload_bucket

        with Cluster("Result service", graph_attr=cluster_attr):
            result_service = Run("Result Service")
            result_service_db = SQL("Database")
            result_service >> result_service_db

        with Cluster("Account service", graph_attr=cluster_attr):
            account_service = Run("Account Service")
            account_service_db = SQL("Database")
            account_service >> account_service_db

    diag.dot.renderer = "cairo"
