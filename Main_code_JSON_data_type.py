def Prompting(top_p, temperature, number_of_API_calls):    
    import json
    with open(r'Conversations.json',"r",encoding="utf-8") as f:
        data=json.load(f)
#from dotenv import load_dotenv
#load_dotenv()

    from langchain_openai import ChatOpenAI
    from langchain_core.prompts import (
        ChatPromptTemplate,
        FewShotChatMessagePromptTemplate)
    import pandas as pd
    import os
## Starting the model
    llm=ChatOpenAI(
     model='gpt-4o',
     temperature=temperature,
     top_p=top_p)

# Examples and example prompt
#examples=[
#{"sentence":"پریزاد فکر میکنم کم کم باید اماده بشی ؟ اماده ای با یک روحیه خوب همچی به خوبی پیش بره"
#, "label":"supportive"},
#{"sentence":"چرا این فرق داره ولی تیم روانشناسی بسیار باید حرفه ای باشه درسته همه انسانها مشگل دارن"
#,"label":"seeking psychological guide"},
#{"sentence":"ما بیمارستان  بستری میشه برای شیمی درمانیو هر جلسه قبل شیمی درمانی نوار قلب و اکو میگیرن"
#,"label":"defining clinical procedure"}
#]
#example_prompt=ChatPromptTemplate.from_messages([('human','{sentence}'),('ai','{label}')])

#few_shot_prompt = FewShotChatMessagePromptTemplate(
#    examples=examples,
#    # This is a prompt template used to format each individual example.
#    example_prompt=example_prompt,

#Final message
    messages =[
        ("system", "You will be provided with a chat between two or more Pancreatice cancer patients, care givers or family members. And assign a persian label to the theme of their conversation"),
        ("human", "{sentence}")]

    prompt_template = ChatPromptTemplate.from_messages(messages)
    outcomes={}
    m=0
    n=0
    for key , value in data.items():
        print(key)
        Conversation=""
        for i in range(len(value)-1, -1,-1):
            dict=value[i]
            Conversation+="The user id:"+" " + dict["from_id"]+"\n"+dict["text"]+"\n"
            prompt = prompt_template.invoke({"sentence":Conversation})
            response=llm.invoke(prompt)
            L=[key,response.content]
            outcomes[Conversation]=response.content
            m+=1
        if m==number_of_API_calls :
            print("done")
            break
    return(outcomes)

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
