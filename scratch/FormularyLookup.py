import pandas as pd
import numpy as np
import pickle

df = pd.read_csv("formulary.csv")

def InFormulary(payer,drug):
    #Check for valid input
    if not(drug in df.columns):
        outstring = "Error! Drug is not valid."
    elif not( (df['Payer'] == payer).any()):
        outstring = "Error! Payer is not valid."
    else:
        #Now check for if it is in formulary...
        sel = df.loc[df['Payer']==payer,['Acc/Code',drug]]
        
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


def ePAApprove(payer=417614,
               drug='A',
               correct_diagnosis=1,
               tried_and_failed=1,
               contraindication=0,
               not_in_formulary=0,
               limit_exceeded=0):
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
    approved = False 
    if(prob>0.36): approved = True

    return approved

    
