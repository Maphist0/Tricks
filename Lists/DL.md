## General
### CUDA
1. [Check the CUDA Compute Compatible (CC) architecture (sm_xx) for your GPU](https://en.wikipedia.org/wiki/CUDA#Supported_GPUs).
1. [Set specific GPU for Python program](https://github.com/keras-team/keras/issues/6031#issuecomment-289921206). Works for Keras, Tensorflow, and Pytorch. More info [here](http://www.acceleware.com/blog/cudavisibledevices-masking-gpus).

### Handy
1. [Matlab API for Python](https://cn.mathworks.com/help/matlab/matlab-engine-for-python.html). A [tool](?)(upload later) to convert ***from*** an array returned from Matlab script ***to*** numpy array.
1. [Combine images to a video](https://askubuntu.com/questions/610903/how-can-i-create-a-video-file-from-a-set-of-jpg-images#610945).
1. [Zip files in parallel](http://dschrempf.github.io/posts/Linux/2015-01-07-GNU-Parallel.html).
1. Enable port redirecting: ```ssh -L ${local_port}:127.0.0.1:${remote_port} -N -f -l ${user} ${ip} -p ${port}```
1. Set proxy: ```${proxy} <==> https://${user}:${pass}@${ip}:${port}``` in different tools:

      | Tool              | Command                                          |
      |:----------------- |:------------------------------------------------ |
      | pip               | ```$ pip --proxy=${proxy} install ...```         |
      | git clone         | ```$ git config --global https.proxy ${proxy}``` |
      | git (always)      | ```$ vim ~/.gitconfig``` Then enter: <br> ```[http]``` <br> ```[https]``` <br> &nbsp;&nbsp;&nbsp;&nbsp; ```proxy = ${proxy}```|
      | wget (always)     | ```$ vim ~/.wgetrc``` Then enter: <br> ```use_proxy=yes``` <br> ```https_proxy=${proxy}``` <br> ```http_proxy=${proxy}```                                          |
      | anaconda (always) | ```$ vim ~/.condarc``` Then enter: <br> ```proxy_servers:``` <br> &nbsp;&nbsp;&nbsp;&nbsp;```http: ${proxy}``` <br> &nbsp;&nbsp;&nbsp;&nbsp;```https: ${proxy}```     |

    

### System
1. [Colaboratory](https://colab.research.google.com/notebooks/welcome.ipynb), "free" GPUs from Google.
1. [Paperspace](https://www.paperspace.com/ml), "free" VMs for ML.
1. [Codalab](https://github.com/codalab/codalab-competitions), website for competitions.


-------------------------------------------------------------------------------------------------------------------

## DL Framework
### Keras
1. [Plot loss and accuracy curves while training](http://block.arch.ethz.ch/blog/2016/08/dynamic-plotting-with-matplotlib/).
1. [Show intermediate result in layer](https://stackoverflow.com/questions/41711190#41712013).
1. The ID of each unnamed layer (doesn't have ```name``` property) will keep increasing if the same program has more than one models. e.g. ID of the first Conv layer in model one starts from ```conv2d_1```, last Conv layer in model one is ```conv2d_99```. Then the first Conv layer in model two is ***NOT*** ```conv2d_1```, but ```conv2d_100```. This causes problem while loading the second model's weight by ```model.load_weights(path, by_name=True)```. Pay attention to the ```by_name``` property.

-------------------------------------------------------------------------------------------------------------------

## DL Resources

### CV & Video related

#### Pre-processing
1. [Optical Flow in OpenCV](https://www.docs.opencv.org/3.2.0/d7/d8b/tutorial_py_lucas_kanade.html).
1. FlowNet 2.0 [caffe](https://github.com/lmb-freiburg/flownet2), [pytorch](https://github.com/NVIDIA/flownet2-pytorch) ***<<---- only work with python 2.x***. [Customized pytorch verison for python 3.5](?) (upload later).

#### Video Object Segmentation
1. [LVO](http://lear.inrialpes.fr/research/lvo/)
1. OSVOS [caffe](https://github.com/kmaninis/OSVOS-caffe), [pytorch](https://github.com/kmaninis/OSVOS-PyTorch), [tensorflow](https://github.com/scaelles/OSVOS-TensorFlow).
#### Instance Segmentation
1. "Simple Does It: Weakly Supervised Instance and Semantic Segmentation", [tensorflow](https://github.com/philferriere/tfwss).
1. [Mask R-CNN](https://github.com/matterport/Mask_RCNN)


### Dataset

#### Image
1. [Process CIFAR](yelangya3826850.github.io/downloads/toolbox/get_cifar100.py).
1. [UnicodeDecodeError while using cPickle to load CIFAR train dataset (py3)](https://github.com/tflearn/tflearn/issues/57) .
1. [CIFAR VGG](https://github.com/geifmany/cifar-vgg).
1. [CIFAR Wide Residual Networks in Keras](https://github.com/asmith26/wide_resnets_keras).
