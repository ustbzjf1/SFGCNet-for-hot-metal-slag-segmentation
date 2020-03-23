# SFGCNet-for-hot-metal-slag-segmentation

By 


### Table of Contents
0. [Introduction](#introduction)
0. [Citation](#citation)
0. [Model](#model)
0. [Annotation example](#annotation)
0. [Traditional results](#traditional)
0. [Our results](#ourresults)

### Introduction

This repository contains a diagram of the model, part of our dataset's labeled results, and the results of model testing. The final table lists the test accuracy.


### Citation

If you use these models or the ideas in your research, please cite:


### Model

0. The design details of SFGCN  
	![SFGCN](https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/images/SFGCN.png)

	
0. The SFGCNet architecture

	![architecture](https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/images/architecture.png)

### Annotation example

![annotation](https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/images/image-label.png)


### Traditional result

![traditional_result](https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/images/traditional_result.png)


### Our results
0. Result visualization :
	![deep_result](https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/images/deep_result.png)


0. Quantitative results:

	Models|hot metal|slag|robotic arm|blow pole|MIoU(%)|PA(%)|inference time(ms)
	:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:
	BiSeNet |67.49|82.91|82.55|55.77|72.11|97.04|15.47
	BiSeNet+SFGCN |64.55|82.98|80.66|71.16|74.84|96.97|18.28
	ICNet|60.74 |69.54|67.17|72.92|67.59|94.61|44.62
	ICNet+SFGCN|61.47|73.54|68.63|70.05|68.42|95.45|45.79  
	FCN|68.22|83.08|83.62|64.63|74.89|97.15|66.67
    FCN+SFGCN|68.24|83.76|84.92|71.23|77.04|97.26|67.46
    ResNet50|55.06|78.97|79.15|71.32|71.13|96.38|30.18
    ResNet50+SFGCN|66.29|73.04|76.92|72.49|72.19|95.62|30.73
