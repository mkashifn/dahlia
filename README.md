# Dahlia

### Required Python Version
* Python 2.7 is required, you can verify your environment using:
  ```
  python dahlia.py verifyenv
  ```
### Dependencies
Dahlia depends upon the following Python packages:
  * numpy
  * pickle
  * graphviz
  * random
  * math
  * warnings
  * sklearn
  * time
  * multiprocessing
  * modlamp
  * pandas
  * pylab

  
### Downloading Dataset
#### N-BaIoT Dataset
* URL: https://www.kaggle.com/mkashifn/nbaiot-dataset
* The directory structure should look like:<br>
  - datasets/nbaiot-dataset/1.benign.csv
  - datasets/nbaiot-dataset/1.gafgyt.combo.csv
  - ...
  - datasets/nbaiot-dataset/9.mirai.udpplain.csv
* Run the following command to verify if the dataset is valid
  ```
  python celosia.py verifydataset -d nbaiot
  ```
  Correct output:
  ```
  Success! 89 data files present in the N-BaIoT dataset.
  ```

### Running Experiments

### Kaggle Notebooks

This following experiments has been moved to Kaggle. Please follow the links to access the complete code and output. Alternatively, you can also access the Jupyter notebook files in the `snapshots` directory of this repository.