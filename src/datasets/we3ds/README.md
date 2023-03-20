# WE3DS dataset

The WE3DS dataset contains 2,568 RGB-D images (color image and distance map) and hand-annotated ground-truth masks for
semantic segmentation and is the first RGB-D image dataset for multi-class plant species semantic segmentation task.
Images were taken under natural light conditions using an RGB-D sensor consisting of two RGB cameras in a stereo setup.

More information about the data acquisition and pre-processing can be found in 
[Kitzler et al. 2023](https://doi.org/10.3390/s23052713), the dataset can be downloaded manually from 
[Zenodo](https://zenodo.org/record/7457983).

**Please cite the original source when using this dataset.**

## Prepare dataset

1. Install requirements:
    ```bash
    pip install -r ./requirements.txt [--user]
    ```

2. Download the WE3DS dataset manually and provide the path to the downloaded unzipped dataset folder or use the script
   to download and unzip it (takes some time):  
    ```bash
    python prepare_dataset.py ../../../datasets/we3ds path/to/download/folder
    ```

## Use dataset
```python
# see ../../src/prepare_data.py
```
