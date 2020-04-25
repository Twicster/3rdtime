import pandas as pd

data = pd.read_csv("GTExData.csv")  #load data in dataframe

#separates all pathology values
CatPan=[]
CatPanComp=[0]*len(data["Pathology.Categories_pancreas"])
n=0
for i in data["Pathology.Categories_pancreas"]:
    if isinstance(i,str):
        CatPan+=list(i.split(", "))
        CatPanComp[n]=list(i.split(", "))
        n+=1
    else:
        CatPan+=[i]
        n+=1
PanEntry=[]
for i in CatPan:
    if i not in PanEntry and isinstance(i,str):
        PanEntry+=[i]
#Making binary CSV for pathology
with open('PathologylistPancreas.csv', 'w') as f:
    for i in range(len(PanEntry)):
        f.write(f"{PanEntry[i]}")
        if i<len(PanEntry)-1:
            f.write(",")
    f.write("\n")
    for i in CatPanComp:
        if isinstance(i,list):
            for s in range(len(PanEntry)):
                if PanEntry[s] in i:
                    f.write("1")
                else:
                    f.write("0")
                if s < len(PanEntry) - 1:
                    f.write(",")
            f.write("\n")
        else:
            f.write("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n")

#Now for liver
#separates all pathology values
CatLiv=[]
CatLivComp=[0]*len(data["Pathology.Categories_liver"])
n=0
for i in data["Pathology.Categories_liver"]:
    if isinstance(i,str):
        CatLiv+=list(i.split(", "))
        CatLivComp[n]=list(i.split(", "))
        n+=1
    else:
        CatLiv+=[i]
        n+=1
LivEntry=[]
for i in CatLiv:
    if i not in LivEntry and isinstance(i,str):
        LivEntry+=[i]
#Making binary CSV for pathology
with open('PathologylistLiver.csv', 'w') as f:
    for i in range(len(LivEntry)):
        f.write(f"{LivEntry[i]}")
        if i<len(LivEntry)-1:
            f.write(",")
    f.write("\n")
    for i in CatLivComp:
        if isinstance(i,list):
            for s in range(len(LivEntry)):
                if LivEntry[s] in i:
                    f.write("1")
                else:
                    f.write("0")
                if s < len(LivEntry) - 1:
                    f.write(",")
            f.write("\n")
        else:
            f.write("0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0\n")
