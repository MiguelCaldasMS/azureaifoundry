from azure.identity.aio import DefaultAzureCredential
from azure.ai.projects.aio import AIProjectClient
 
project_connection_string="your_connection_string"

project = await AIProjectClient.from_connection_string(
  conn_str=project_connection_string,
  credential=DefaultAzureCredential())