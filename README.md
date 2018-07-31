<div align="center">
  <a href="https://nanonets.com/objectdetection/">
    <img src="https://nanonets.com/logo.png" alt="Celebrity Face Detection using Nanonets API" width="100"/>
    </a>
</div>

<h1 align="center">Celebrity Face Detection using Nanonets API</h1>

** **
Annotations are present for 10 Indian Celebrities:
1) Virat Kohli
2) Katrina Kaif
3) Alia Bhatt
4) Shahrukh Khan
5) Akshay Kumar
6) Salman Khan
7) Deepika Padukone
8) Sachin Tendulkar
9) Amitabh Bachchan
10) Sonam Kapoor


** **

# Build an Object Detector

>**Note:** Make sure you have python and pip installed on your system if you don't visit
[Python](https://www.python.org/downloads/release/python-2714/)
[pip](https://pip.pypa.io/en/stable/installing/)
 
### Step 1: Clone the Repo
```bash
git clone https://github.com/NanoNets/celebrity-detection.git
cd celebrity-detection
sudo pip install requests
```

### Step 2: Get your free API Key
Get your free API Key from http://app.nanonets.com/user/api_key

### Step 3: Set the API key as an Environment Variable
```bash
export NANONETS_API_KEY=YOUR_API_KEY_GOES_HERE
```

### Step 4: Create a New Model
```bash
python ./code/create-model.py
```
 >_**Note:** This generates a MODEL_ID that you need for the next step

### Step 5: Add Model Id as Environment Variable
```bash
export NANONETS_MODEL_ID=YOUR_MODEL_ID
```
 >_**Note:** you will get YOUR_MODEL_ID from the previous step

### Step 6: Upload the Training Data
The training data is found in ```images``` (image files) and ```annotations``` (annotations for the image files)
```bash
python ./code/upload-training.py
```

### Step 7: Train Model
Once the Images have been uploaded, begin training the Model
```bash
python ./code/train-model.py
```

### Step 8: Get Model State
The model takes ~2 hours to train. You will get an email once the model is trained. In the meanwhile you check the state of the model
```bash
python ./code/model-state.py
```

### Step 9: Make Prediction
Once the model is trained. You can make predictions using the model
```bash
python ./code/prediction.py PATH_TO_YOUR_IMAGE.jpg
```

**Sample Usage:**
```bash
python ./code/prediction.py ./images/7972a1733e354ab5191874322080b50e.jpg
```


*Note the python sample uses the comverted json instead of the xml payload for convenience purposes, hence it has no dependencies.*
