#!/bin/bash
sudo apt-get install zip unzip  -y
sudo apt-get install ffmpeg libsm6 libxext6  -y
echo 'Loading Model from https://assets.gezdev.com/model-ai/food-class/EfficientnetB4-epoch0800.pb.tar.gz'
wget https://assets.gezdev.com/model-ai/food-class/EfficientnetB4-epoch0800.pb.tar.gz
echo 'Model Unzipping..................'
tar -xvf 'EfficientnetB4-epoch0800.pb.tar.gz'
ls -a
Model_MedWaste_Path = $(pwd)
echo 'Model Saved at ...' + $Model_MedWaste_Path
echo '++++++++++ [Load/Extract Model] Completed ++++++++++'