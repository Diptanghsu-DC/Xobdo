from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from fuzzywuzzy import fuzz
import numpy as np
import pandas as pd

df1 = pd.read_csv(r'C:\\Nayan\\Programming\\.vscode\\DPC_sir_project\\newdata\\S08_question_answer_pairs.txt',encoding='latin-1',sep='\t')
df2 = pd.read_csv(r'C:\\Nayan\\Programming\\.vscode\\DPC_sir_project\\newdata\\S09_question_answer_pairs.txt',encoding='latin-1',sep='\t')
df3 = pd.read_csv(r'C:\\Nayan\\Programming\\.vscode\\DPC_sir_project\\newdata\\S10_question_answer_pairs.txt',encoding='latin-1',sep='\t')
df = pd.concat([df1,df2,df3],ignore_index=True)

df = df.rename(columns={'ï»¿ArticleTitle' : 'intents'})

# print(df['Answer'].value_counts())

df = df.drop(['DifficultyFromQuestioner', 'DifficultyFromAnswerer', 'ArticleFile', 'ArticleTitle'], axis = 1)
df = df.dropna(subset=['Answer'])

df['Question'] = df['Question'].apply(lambda x: str(x).lower())

#  Define input question
input_question = "At what age can a zebra breed?"

# Preprocess the input question
input_question = input_question.lower()

X_list = word_tokenize(input_question)
print(X_list)
# Y_list = [word_tokenize(question) for question in df['Question']]
df['Question'] = df['Question'].apply(lambda x: word_tokenize(x))

# print(df['Question'])

sw = stopwords.words('english')  
l1 =[]
l2 =[] 
similarity = []

X_set = {w for w in X_list if not w in sw}

for index, question in enumerate(df['Question']):
    Y_set = {w for w in question if not w in sw}

    rvector = X_set.union(Y_set)

    l1.append([])
    l2.append([])

    for w in rvector: 
        if w in X_set: l1[index].append(1) # create a vector 
        else: l1[index].append(0) 
        if w in Y_set: l2[index].append(1) 
        else: l2[index].append(0) 

    c = 0
  
    # cosine formula  
    for i in range(len(rvector)): 
            c += l1[index][i]*l2[index][i] 
    cosine = c / float((sum(l1[index])*sum(l2[index]))**0.5) 
    similarity.append(cosine)


maxidx = similarity.index(max(similarity))
answer = df['Answer'][maxidx]
print(max(similarity))
print(maxidx)
print(df['Question'][maxidx])
print(df['Answer'][maxidx])


# print(df['Y_set'])

# df['union'] = df['Y_set'].apply(lambda x: X_set.union(x))

# for index, sentence in enumerate(df['union']): 
#     for w in sentence:
#         if w in X_set: l1.append([1]) # create a vector 
#         else: l1.append(0) 
#         if w in df['Y_set'][index]: l2.append(1) 
#         else: l2.append(0) 

# c = 0

# for i in range(df['union'].size): 
#         for j in range(len(df['union'][i])):
             
#             c+= l1[i]*l2[i] 
# cosine = c / float((sum(l1)*sum(l2))**0.5) 

# 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
