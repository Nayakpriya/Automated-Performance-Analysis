import pandas as pd
import networkx as nx 
from networkx_query import search_nodes
import json
from user.settings import BASE_DIR

student_id = 2  #Login
whichTest = 1   #Student Selection

suggested_questions = pd.DataFrame()

test = pd.read_excel(f"{BASE_DIR}\student\DTL_Sample_Tests.xlsx", sheet_name ="Test"+str(whichTest))
marks = pd.read_excel(f"{BASE_DIR}\student\DTL_Sample_Marks.xlsx", sheet_name ="Test"+str(whichTest), index_col = "Student_ID")


means = marks.mean(axis = 0)#Means of each question
standard_deviations = marks.std(axis = 0)

student_marks = marks.loc[student_id]
#TODO Calculate standard deviations based on that recommender depth of search
#and CO level for recommended questions
z_score = (student_marks-means)/standard_deviations

question_bank = pd.ExcelFile(r"C:\Users\PRIYA\Desktop\DTL\student\DTL_Knowledge_Graph_Test.xlsx")

print(student_marks)
print(z_score)
print(test)
for i in test.iterrows():
    question_number = "Q"+str(i[0]+1)
    query_question = i[1]["Question"]
    CO = i[1]["COs"]

    topic = ""
    flag = False

    # try:
    #     i = 0
    #     while(flag == False):

    #         df = question_bank.parse(sheet_name=i)
            
    #         for question in df["Question"]:
    #             if(question == query_question): #Better check than string comparison
    #                 topic = question_bank.sheet_names[i]
    #                 flag = True
    #                 break
    #         i+=1
    # except:
    #     print("Manually input the topic ")
    #     topic = input()

    topic = "C" #This needs to get the topic of the question

    KG = nx.read_graphml(r"C:\Users\PRIYA\Desktop\DTL\student\KG.graphml") #Contains the KG


    for node_id in search_nodes(KG, {"==": [("labelV",), topic]}):
        for i in sorted(nx.bfs_tree(KG, source=node_id, depth_limit=2)):
            question_bank = pd.ExcelFile(KG.nodes[i]['path_to_excel']) #Returns the questions for a topic
            df = question_bank.parse(sheet_name = KG.nodes[i]['labelV']) #Returns the questions
            if(z_score.loc[question_number] >=0.5):
                if(CO==5):
                    print(df[df["COs"]==(CO)])
                    suggested_questions = suggested_questions.append(df[df["COs"]==(CO)])
                    print("===========================")
                elif(CO == 4):
                    print(df[df["COs"].apply(lambda x:x>=(CO) and x<=(CO+1))])
                    suggested_questions = suggested_questions.append(df[df["COs"].apply(lambda x:x>=(CO) and x<=(CO+1))])
                    print("===========================")
                else:
                    print(df[df["COs"].apply(lambda x:x>=(CO) and x<=(CO+2))])
                    suggested_questions = suggested_questions.append(df[df["COs"].apply(lambda x:x>=(CO) and x<=(CO+2))])
                    # for i in df[df["COs"].apply(lambda x:x>=(CO) and x<=(CO+2))]:
                    #     print(i)
                    print("===========================")
            elif(z_score.loc[question_number] >=0.25 and z_score.loc[question_number] <0.5):
                if(CO==5):
                    print(df[df["COs"]==(CO)])
                    suggested_questions = suggested_questions.append(df[df["COs"]==(CO)])

                    print("===========================")
                else:
                    print(df[df["COs"].apply(lambda x:x>=(CO) and x<=(CO+1))])
                    suggested_questions = suggested_questions.append(df[df["COs"].apply(lambda x:x>=(CO) and x<=(CO+1))])
                    print("===========================")
            elif(z_score.loc[question_number] >=-0.25 and z_score.loc[question_number] <0.25):
                if(CO==1):
                    print(df[df["COs"]==(CO)])
                    suggested_questions = suggested_questions.append(df[df["COs"]==(CO)])
                    print("===========================")
                else:
                    print(df[df["COs"].apply(lambda x:x==CO)]) 
                    suggested_questions = suggested_questions.append(df[df["COs"].apply(lambda x:x==CO)])
                    print("===========================")
            elif(z_score.loc[question_number] <=-0.25 and z_score.loc[question_number] >-0.5):
                if(CO==1):
                    print(df[df["COs"]==(CO)])
                    suggested_questions = suggested_questions.append(df[df["COs"]==(CO)])

                    print("===========================")
                else:
                    print(df[df["COs"].apply(lambda x:x>=(CO-1) and x<=(CO))]) #Displays subset of questions TODO how to select the level
                    suggested_questions = suggested_questions.append(df[df["COs"].apply(lambda x:x>=(CO-1) and x<=(CO))])
                    print("===========================")
            elif(z_score.loc[question_number] <=-0.5 and z_score.loc[question_number] >-1):
                if(CO==1):
                    print(df[df["COs"]==(CO)])
                    suggested_questions = suggested_questions.append(df[df["COs"]==(CO)])

                    print("===========================")
                elif(CO == 2):
                    print(df[df["COs"]==(CO-1)])
                    suggested_questions = suggested_questions.append(df[df["COs"]==(CO-1)])
                    print("===========================")
                else:
                    print(df[df["COs"].apply(lambda x:x>=(CO-2) and x<=(CO-1))])
                    suggested_questions = suggested_questions.append(df[df["COs"].apply(lambda x:x>=(CO-2) and x<=(CO-1))])
                    print("===========================")
            elif(z_score.loc[question_number] <=-1):
                if(CO==1):
                    print(df[df["COs"]==(CO)])
                    suggested_questions = suggested_questions.append(df[df["COs"]==(CO)])
                    print("===========================")
                elif(CO == 2):
                    print(df[df["COs"]==(CO-1)])  
                    suggested_questions = suggested_questions.append(df[df["COs"]==(CO-1)])
                    print("===========================") 
                elif(CO == 3):
                    print(df[df["COs"]==(CO-2)])
                    suggested_questions = suggested_questions.append(df[df["COs"]==(CO-2)])
                    print("===========================")
                else:
                    print(df[df["COs"].apply(lambda x:x>=(CO-3) and x<=(CO-2))])
                    suggested_questions = suggested_questions.append(df[df["COs"].apply(lambda x:x>=(CO-3) and x<=(CO-2))])
                    print("===========================")
suggested_questions = suggested_questions.to_json(orient = 'records')
suggested_questions=json.loads(suggested_questions)
print(type(suggested_questions))
