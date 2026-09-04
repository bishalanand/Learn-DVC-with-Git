import pandas as pd
import os


data={"name":["Alice","Bob","Ravi"],
      "age":[25,34,26],
      "city":["Newyork","Delhi","Bangalore"]
      }

df=pd.DataFrame(data)

data_dir='data'
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'sampledata.csv')
df.to_csv(file_path,index=False)
print("filesaved")