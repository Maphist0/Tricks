# Keras
1. [Use specific GPU instead of all](https://github.com/keras-team/keras/issues/6031#issuecomment-289921206), 
more information [here](http://www.acceleware.com/blog/cudavisibledevices-masking-gpus)
1. [Plot loss and accuracy curves while training](http://block.arch.ethz.ch/blog/2016/08/dynamic-plotting-with-matplotlib/)
1. [Show intermediate result in layer](https://stackoverflow.com/questions/41711190#41712013)
1. The ID of each unnamed layer (doesn't have ```name``` property) will keep increasing if the same program has more than one models. e.g. ID of the first Conv layer in model one starts from ```conv2d_1```, last Conv layer in model one is ```conv2d_99```. Then the first Conv layer in model two is ***NOT*** ```conv2d_1```, but ```conv2d_100```. This causes problem while loading the second model's weight by ```model.load_weights(path, by_name=True)```. Pay attention to the ```by_name``` property.

# Dataset
1. [Process CIFAR](yelangya3826850.github.io/downloads/toolbox/get_cifar100.py)
1. [UnicodeDecodeError while using cPickle to load CIFAR train dataset (py3)](https://github.com/tflearn/tflearn/issues/57) 
1. [CIFAR VGG](https://github.com/geifmany/cifar-vgg)
1. [CIFAR Wide Residual Networks in Keras](https://github.com/asmith26/wide_resnets_keras)
