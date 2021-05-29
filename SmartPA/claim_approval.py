#!/usr/bin/env python
# coding: utf-8

# In[24]:




# claims = pd.read_csv('/Users/yiming/Desktop/CoverMyMeds/dim_claims.csv')
# # claims = claims.dropna()
# groups = [group.reset_index()[['reject_code', 'bin', 'drug','dim_claim_id']] for _, group in claims.groupby('bin')]
# drugs_payer1 = [group.reset_index()[['reject_code', 'bin', 'drug','dim_claim_id']] for _, group in groups[0].groupby('drug')]
# drugs_payer2 = [group.reset_index()[['reject_code', 'bin', 'drug','dim_claim_id']] for _, group in groups[1].groupby('drug')]
# drugs_payer3 = [group.reset_index()[['reject_code', 'bin', 'drug','dim_claim_id']] for _, group in groups[2].groupby('drug')]
# drugs_payer4 = [group.reset_index()[['reject_code', 'bin', 'drug','dim_claim_id']] for _, group in groups[3].groupby('drug')]

# drugs_payer4[0].head(5)


# In[26]:


# for i in range(0,3):
#     df = drugs_payer1[i]
#     print((1- df['reject_code'].isna().sum()/len(df['reject_code']))*100)
# for i in range(0,3):
#     df = drugs_payer2[i]
#     print((1- df['reject_code'].isna().sum()/len(df['reject_code']))*100)
# for i in range(0,3):
#     df = drugs_payer3[i]
#     print((1- df['reject_code'].isna().sum()/len(df['reject_code']))*100)
# for i in range(0,3):
#     df = drugs_payer4[i]
#     print((1- df['reject_code'].isna().sum()/len(df['reject_code']))*100)


# ### 

# In[31]:
import pandas as pd
import numpy as np
import pickle
df = pd.read_csv("formulary.csv")

def InFormulary(payer,drug):
    #Check for valid input
    if not(drug in df.columns):
        outstring = "Error! Drug is not valid."
    elif not( (df['Payer'] == float(payer)).any()):
        outstring = "Error! Payer is not valid."
    else:
        #Now check for if it is in formulary...
        sel = df.loc[df['Payer']==float(payer),['Acc/Code',drug]]
        
        #Code -1 is accepted
        acc = sel[sel['Acc/Code'] == -1].iat[0,1]
        
        #Code 70 means not in formulary
        nf = sel[sel['Acc/Code'] == 70].iat[0,1]
        
        #Code 75 means in formulary but not preferred
        np =  sel[sel['Acc/Code'] == 75].iat[0,1]
        
        outstring = ""
        
        if(acc > 0.5): outstring = "Drug is in formulary; no PA required unless plan limit is exceeded"
        
        if(np > 0.5): outstring = "Drug is on formulary, but not preferred; a PA will be reqired"
        
        if(nf > 0.5): outstring = "Drug is NOT on formulary; a PA will be required"

    return(outstring)




def pa_approval(correct_diagnosis,tried_and_failed,contraindiction,binn,drug,reject_code):
    pas = pd.read_csv('dim_pa.csv')
    claims = pd.read_csv('dim_claims.csv')
    claims = claims.dropna()
    mega = pas.join(claims.set_index(pas.index))
    mega = mega.drop(columns=['dim_pa_id', 'dim_claim_id','pharmacy_claim_approved' ])
    mega = mega[['reject_code', 'correct_diagnosis', 'tried_and_failed', 'contraindication', 'pa_approved','drug',"bin"]]

    groups = [group.reset_index()[[ 'correct_diagnosis', 'tried_and_failed', 'contraindication', "bin",'reject_code','pa_approved']] for _, group in mega.groupby('drug')]
    if drug == "A":
        j = 0
    if drug == "B":
        j = 1
    if drug == "C":
        j = 2
    data = groups[j].to_numpy()
    count = 0
    approved = 0
    for i in range(0,len(data)):

        if (data[i][:-1] == [float(correct_diagnosis),float(tried_and_failed),float(contraindiction),float(binn),float( reject_code)]).all():
            count += 1
            if data[i][-1] == 1:
                 approved += 1
    if count == 0:
        return "Your claim should not have been rejected"
    else:
        return  "Your PA approval rate is: "+ "{:.2f}".format(approved/count*100) +"%"
#print(claim_pred("A","417380"))


# In[ ]:

def ePAApprove(payer,
               drug,
               correct_diagnosis,
               tried_and_failed,
               contraindication,
               not_in_formulary,
               limit_exceeded):
    #load pickle file
    infile = open('log_reg.pcl','rb')
    log_reg_model = pickle.load(infile)
    infile.close()

    #print(type(log_reg_model))
    
    #Put input parameters into a temporary data frame
    features = ['correct_diagnosis','tried_and_failed','contraindication',
                'not_in_formulary','limit_exceeded','Drug A','Drug B'
                ,417380, 417740, 417614]
    tmp = pd.DataFrame(columns=features)
    #print(tmp.head())

    tmp_list = [correct_diagnosis, tried_and_failed, contraindication,
                not_in_formulary, limit_exceeded]

    dl = [0,0]
    pl = [0,0,0]

    #We would need something more sophisticated for a larger number of drugs, but this will do for now.
    if(drug == 'A'): dl=[1,0]
    if(drug == 'B'): dl=[0,1]

    if(payer == 417380): pl = [1,0,0]
    if(payer == 417740): pl = [0,1,0]
    if(payer == 417614): pl = [0,0,1]
    #https://www.w3schools.com/python/python_lists_add.asp
    tmp_list.extend(dl)
    tmp_list.extend(pl)

    print(tmp_list)

    tmp = tmp.append(pd.DataFrame([tmp_list],columns=features))
    print(tmp.head())
    
    #Predict with unpickled (is that a word?) model

    prob = log_reg_model.predict_proba(tmp)[:,1]
    print("Probability of approvale = ",prob)

    #Compare with cutoff (0.36), 
    approved = 'No' 
    if(prob>0.36): approved = 'Yes'

    return approved


