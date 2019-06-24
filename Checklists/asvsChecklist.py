import json

def val(x):
    with open('Dataset/level1.json') as json_file:  
            data = json.load(json_file)
            a=data['items']
    for i in range(0,len(a)):
            y=a[i]['checklist_items_checklistID'].split('.')
            if y[0]==x:
                print(a[i]['checklist_items_checklistID']+" "+a[i]['checklist_items_content'])

def val2(x):
    with open('Dataset/asvslevel2.json') as json_file:  
            data = json.load(json_file)
            a=data['items']
    for i in range(0,len(a)):
            y=a[i]['checklist_items_checklistID'].split('.')
            if y[0]==x:
                print(a[i]['checklist_items_checklistID']+" "+a[i]['checklist_items_content'])
    
def checklist():
    user_query=input("Enter your question ")
    if 'security' in user_query:
        print('Select the Checklist type:')
        print('1 ASVS LEVEL 1')
        print('2 ASVS LEVEL 2')
        user_option=int(input())

    if user_option==1:
        print("Do you want whole checklist? Y/N")
        user_ans=input()
        if user_ans=='y' or user_ans=='Y':
            with open('Dataset/level1.json') as json_file:  
                data = json.load(json_file)
                a=data['items']
            for i in range(0,len(a)):
                print(a[i]['checklist_items_checklistID']+" "+a[i]['checklist_items_content'])

            user_optn=input("Please enter your choice")
            
            for i in range(0,len(a)):
                if str(user_optn).strip()==str(a[i]['checklist_items_checklistID']).strip():
                    print(a[i]['kb_items_content'])
                

        else:
            with open('Dataset/level1.json') as json_file:  
                data = json.load(json_file)
                a=data['items']
            for i in range(0,len(a)):
                x=a[i]['checklist_items_checklistID'].split('.')
                if x[1]=='0':
                    print(a[i]['checklist_items_checklistID']+" "+a[i]['checklist_items_content']+" y/n")
                    ui=input()
                    if ui=='y' or ui=='Y':
                        val(x[0])
                        
                        
                    else:
                        pass
                     
    if user_option==2:
        print("Do you want whole checklist? Y/N")
        user_ans=input()
        if user_ans=='y' or user_ans=='Y':
            with open('Dataset/asvslevel2.json') as json_file:  
                data = json.load(json_file)
                a=data['items']
            for i in range(0,len(a)):
                print(a[i]['checklist_items_checklistID']+" "+a[i]['checklist_items_content'])

            user_optn=input("Please enter your choice")
            
            for i in range(0,len(a)):
                if str(user_optn).strip()==str(a[i]['checklist_items_checklistID']).strip():
                    print(a[i]['kb_items_content'])

                
        else:
            with open('Dataset/asvslevel2.json') as json_file:  
                data = json.load(json_file)
                a=data['items']
            for i in range(0,len(a)):
                x=a[i]['checklist_items_checklistID'].split('.')
                if x[1]=='0':
                    print(a[i]['checklist_items_checklistID']+" "+a[i]['checklist_items_content']+" y/n")
                    ui=input()
                    if ui=='y' or ui=='Y':
                        val2(x[0])
                        break;
                        
                    else:
                        pass

                      
checklist()

