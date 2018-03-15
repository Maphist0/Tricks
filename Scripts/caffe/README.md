# Handy scripts for caffe

1. Quite hard to save the output of caffe (including pycaffe and matcaffe) to a file. \
A by-pass method is to use ```$ script train.log``` to save all outputs to the file ```train.log```, and use ```parse_log.py``` to parse and plot the training result.\
Please edit the script according to your training output.

2. Shorten caffe ```.proto``` file with ```shorten_model.py```.
