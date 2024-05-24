from diagrams import Diagram

from diagrams.onprem.client import Users


with Diagram(show=False, filename="users"):
    users = Users("Users")
