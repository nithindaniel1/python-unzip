import os, zipfile
input = 'input value' # Path of Zip files directory  
output = 'output ' # Path of output directory
entries = os.listdir(input)

for item in entries:
   if item.endswith(".zip"):
      # filePath = input + "/" + item # For linux
      #  or
      filePath=os.path.join(input,output) # For Windows
      print("Unzipping " + item)
      with zipfile.ZipFile(filePath, 'r') as zip_ref:
         zip_ref.extractall(output)
         

print("Done")



