from Ipython.display import clear_output
!pip install --upgrade kaggle 
clear_output()
from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
    print('User uploaded file "{name}" with length {length} bytes'.format(
        name = fn, length = len(uploaded[fn])))

# Then move kaggle.json into the folder where the API expects to find it. 
!mkdir -p ~/.kaggle/ && mv kaggle.json ~/.kaggle/ && chmod 600 ~/.kaggle/kaggle.json 
