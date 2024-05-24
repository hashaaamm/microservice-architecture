# diagram.py
from diagrams import Diagram, Cluster, Edge, Node
from diagrams.aws.compute import EC2
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB
from diagrams.onprem.client import Users
from diagrams.onprem.network import Kong
from diagrams.onprem.database import Postgresql
from diagrams.onprem.inmemory import Redis
from diagrams.programming.framework import FastAPI, Django
from diagrams.onprem.queue import Rabbitmq
from diagrams.programming.flowchart import Database
from diagrams.onprem.compute import Server
from diagrams.onprem.client import Client
from diagrams.gcp.storage import Storage
from diagrams.gcp.compute import Run
from diagrams.gcp.database import SQL

with Diagram(show=False, filename="ml_services"):


    with Cluster("ML services"):
            ai_generated_image = Server("AI Gen Image")
            ai_generated_image_bucket = Storage("Bucket")
            ai_generated_image >> ai_generated_image_bucket

            id_document_reader = Server("ID Doc Reader")

            face_manipulation = Server("Face Manipulation")
            face_manipulation_bucket = Storage("Bucket")
            face_manipulation >> face_manipulation_bucket

            liveness_detection = Server("Liveness Detection")

            face_recognition_service = Server("Face Recognition")

            document_check = Server("Document Check")

            voice_analysis = Server("Voice Analysis")