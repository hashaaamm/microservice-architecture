# diagram.py
from diagrams import Diagram, Cluster

from diagrams.programming.flowchart import Database


with Diagram(show=False, filename="rabbit"):

    with Cluster("RabbitMQ Queue"):
        Database("Webhook Queue")
        Database("Notification Queue")
        Database("Hill Queue")
        Database("Result Queue")
        Database("Task Queue X 7")
