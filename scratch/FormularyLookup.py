import pandas as pd
import numpy as np

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
