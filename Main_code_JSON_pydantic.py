import json
with open(r'Conversations.json',"r",encoding="utf-8") as f:
    data=json.load(f)

from pydantic import BaseModel
from typing import List
from enum import Enum
from dotenv import load_dotenv
load_dotenv()

# do we realy need this? from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import   PromptTemplate 
from langchain_core.prompts import (
    ChatPromptTemplate,
    FewShotChatMessagePromptTemplate)
from langchain.output_parsers import PydanticOutputParser


import pandas as pd

#Iterating over 'html' files and extract all elements with class=text 
from bs4 import BeautifulSoup
import os


class Category( str,Enum):
    Treatment_Decision = "treatment_decision"
    Spiritual_Support = "Spiritual_Support"
    Post_Surgery_Care = "Post_Surgery_Care"
class Theme_Label(BaseModel):
    Theme:List[Category]
    class Config:
        arbitrary_types_allowed = True

parser = PydanticOutputParser(pydantic_object=Theme_Label)


## Starting the model
LLM=ChatOpenAI(
  model='gpt-4o',
 temperature=0.6)


#Final message
prompt = PromptTemplate(
    template="You will be provided with a chat between two or more Pancreatice cancer patients, care givers or family members. And assign a label to the theme of their conversation,\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
#messages =[
#    ("system", "You will be provided with a chat between two or more Pancreatice cancer patients, care givers or family members. And assign a label to the theme of their conversation."),
#    ("human", "{sentence}")]

chain = prompt| LLM|parser
outcomes=[]
m=0
n=0
for key , value in data.items():
    print(key)
    Conversation=""
    for i in range(len(value)-1, -1,-1):
        dict=value[i]
        Conversation+="The user id:"+"  " + dict["from_id"]+"His/Her message: " +dict["text"]+"\n"
    #prompt = prompt_template.invoke({"sentence":Conversation})
    #reposone=llm.invoke(prompt)
    reposone=chain.invoke({"query":Conversation})
    L=[key,reposone]
    outcomes.append(L)
    m+=1
    if m==10:
        print("done")
        break

for i in outcomes:
    print(i[1].Theme[0].value)

## Categorisation
#messages_1 =[
    #("system", "You will be provided with many sentence labels, and you should assign one category to each"),
 #   ("human", "Categorise the label :{label}")]
#prompt_template = ChatPromptTemplate.from_messages(messages_1)
#categorised_outcomes=[]
#for i in outcomes:
   # prompt = prompt_template.invoke({"label":i[1]})
   # reposone=llm.invoke(prompt)
   # L=[i[0],i[1],reposone.content]
   # categorised_outcomes.append(L)
#print('done')
#df=pd.DataFrame(outcomes, columns=["Sentences","Labels"])
#df.to_excel(r'C:\Users\Asus\Pythoneman\thematic_analysis\df.xlsx')
