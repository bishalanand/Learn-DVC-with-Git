import pandas as pd
import os


data={"name":["Alice","Bob","Ravi"],
      "age":[25,34,26],
      "city":["Newyork","Delhi","Bangalore"]
      }

dc={"name":"radhika","age":22,"city":"Mumbai"}

df=pd.DataFrame(data)
df.loc[len(df.index)]=dc

data_dir='data'
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'sampledata.csv')
df.to_csv(file_path,index=False)
print("filesaved")