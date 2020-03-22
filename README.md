# SFGCNet-for-hot-metal-slag-segmentation

By Lele Chen, Yue Wu, [Adora M. DSouza](https://www.rochester.edu/college/gradstudies/profiles/adora-dsouza.html),Anas Z. Abidin, [Axel W. E. Wismuelle](https://www.urmc.rochester.edu/people/27063859-axel-w-e-wismueller), [Chenliang Xu](https://www.cs.rochester.edu/~cxu22/).

University of Rochester.

### Table of Contents
0. [Introduction](#introduction)
0. [Citation](#citation)
0. [Model](#model)
0. [Annotation example](#annotation)
0. [Traditional result](#traditional)
0. [Our results](#ourresults)

### Introduction

This repository contains a diagram of the model, part of our dataset's labeled results, and the results of model testing. The final table lists the test accuracy.

![model](https://github.com/lelechen63/MRI-tumor-segmentation-Brats/blob/master/image/spie.gif)


### Citation

If you use these models or the ideas in your research, please cite:


### Model

0. The design details of SFGCN  
	![SFGCN](https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/images/SFGCN.png)

	
0. The SFGCNet architecture

	![architecture](https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/images/architecture.png)

### Annotation example

![architecture](https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/images/image-label.png)


### Traditional result

![traditional_result](https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/images/traditional_result.png)


### Our results
0. Result visualization :
	![visualization](https://github.com/lelechen63/MRI-tumor-segmentation-Brats/blob/master/image/h.png)
	![visualization](https://github.com/lelechen63/MRI-tumor-segmentation-Brats/blob/master/image/v.png)

0. Quantitative results:

	model|whole|peritumoral edema (ED)|FGD-enhan. tumor (ET)
	:---:|:---:|:---:|:---:
	Dense24 |0.74| 0.81| 0.80
	Dense48 | 0.61|0.78|0.79
	no-dense|0.61|0.77|0.78
	dense24+n4correction|0.72|0.83|0.81
