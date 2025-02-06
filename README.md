#自用

#终端安装ffmpeg
apt install ffmpeg
###Anaconda3官网下载地址 ：<https://www.anaconda.com/distribution/#linux>  可选
###下载后安装，过程中需要多个Enter和yes  
wget https://repo.anaconda.com/archive/Anaconda3-2019.10-Linux-x86_64.sh
./Anaconda3-2019.10-Linux-x86_64.sh
#安装cmake
apt-get install cmake
cmake --version

###添加环境变量，初始化conda   可选
export PATH=~/anaconda3/bin:$PATH
conda init bash

创建DeepFaceLab的虚拟环境，并激活。
conda create -y -n deepfacelab python=3.6.6 cudatoolkit=9.0 cudnn=7.3.1
conda activate deepfacelab

#获取DFL源代码，安装python依赖。
git clone https://github.com/tatookan/SL_deepfacelab_linux
cd SL_deepfacelab_linux/DeepFaceLab
python -m pip install -r requirements-cuda.txt