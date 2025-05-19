def Conversation_extractor(number_of_conversations):    
    import json
    with open(r'ChatExport_2024-12-22/ChatExport_2025-01-05\result.json',"r",encoding="utf-8") as f: 
        data=json.load(f)

    def create_dict_of_beloved_keys(dict,key_to_extract):   
        extracted_dict={key:dict[key] for key in key_to_extract if key in dict}
        return(extracted_dict)

    Conversations={}
    a=1
    for i in range(0, number_of_conversations):
        List=[]
        agar=1
        while agar==1:
            the_dict=next((item for item in data["messages"] if item.get("id")==i),None)
        #    b=0
            if the_dict is None:    
                break
            if "reply_to_message_id" in the_dict :
                i = the_dict["reply_to_message_id"]
                dict={}
                dict=create_dict_of_beloved_keys(the_dict, ["id","reply_to_message_id","from_id","text"])
                List.append(dict)
                agar=1
                continue
            if "reply_to_message_id" not in the_dict:
                dict={}
                dict=create_dict_of_beloved_keys(the_dict, ["id","reply_to_message_id","from_id","text"])
                List.append(dict)
                break
        if len(List)>1:
            Conversations[f"conversation_{a}"]=List
            a+=1
    
#Saving the Conversations dictionary in json format
    with open("Conversations.json", "w", encoding="utf-8") as file:
        json.dump(Conversations, file,indent=4,ensure_ascii=False)
