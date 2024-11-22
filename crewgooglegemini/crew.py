from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer

## Forming the tech focused crew with some enhanced configuration

from pymongo import MongoClient
client = MongoClient("mongodb+srv://anoop:anoop1234@cluster0.y9iyb.mongodb.net/databases?retryWrites=true&w=majority&appName=Cluster0")

db = client['databases']

collection = db['data']
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'Impact of Artificial Intelligence in cancer'})
collection.insert_one({"result":result})
# print(result)