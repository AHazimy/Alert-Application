
import pandas as pd

# df = pd.read_excel("trial.xlsx")
# print(df.at[0,"Status"])
# df.at[0, "Status"] = input("Enter the number:")
# df.to_excel("trial.xlsx")
i=0
while i in range(100):    
    x=input("Enter number:\n")
    df=pd.DataFrame([x],columns=["Status"])
    print("The current status is: "+str(df.loc[0,'Status']))
    df.to_csv('trial_2.csv', index=False)
