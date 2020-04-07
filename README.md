# SFGCNet-for-hot-metal-slag-segmentation

### Table of Contents
0. [Introduction](#introduction)
0. [Model](#model)
0. [Annotation example](#annotation example)
0. [Traditional results](#traditional results)
0. [Our results](#our results)

### Introduction

This repository contains a diagram of the model, part of our dataset's labeled results, and the results of model testing. The final table lists the test accuracy.


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
#### Result visualization :
##### FCN+SFGCN

<div align=center><img  src="https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/visual/FCN_SFGCN/2-111.gif"/></div>
<div align=center><img  src="https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/visual/FCN_SFGCN/2-50.gif"/></div>
<div align=center><img  src="https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/visual/FCN_SFGCN/2-92.gif"/></div>
<div align=center><img  src="https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/visual/FCN_SFGCN/3-105.gif"/></div>

##### BiSeNet+SFGCN

<div align=center><img  src="https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/visual/BiSeNet_SFGCN/2-111.gif"/></div>
<div align=center><img  src="https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/visual/BiSeNet_SFGCN/2-50.gif"/></div>
<div align=center><img  src="https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/visual/BiSeNet_SFGCN/2-92.gif"/></div>

##### ICNet+SFGCN

<div align=center><img  src="https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/visual/ICNet_SFGCN/2-111.gif"/></div>
<div align=center><img  src="https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/visual/ICNet_SFGCN/2-50.gif"/></div>
<div align=center><img  src="https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/visual/ICNet_SFGCN/2-92.gif"/></div>

##### ResNet50+SFGCN

<div align=center><img  src="https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/visual/ResNet50_SFGCN/2-111.gif"/></div>
<div align=center><img  src="https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/visual/ResNet50_SFGCN/2-50.gif"/></div>
<div align=center><img  src="https://github.com/ustbzjf1/SFGCNet-for-hot-metal-slag-segmentation/blob/master/visual/ResNet50_SFGCN/2-92.gif"/></div>




#### Quantitative results:

Models|hot metal|slag|robotic arm|blow pole|MIoU(%)|PA(%)|inference time(ms)|Params(s)|FLOPs(G)
:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:
BiSeNet |67.49|82.91|82.55|55.77|72.11|97.04|15.47|12.42|48.77
BiSeNet+SFGCN |64.55|82.98|80.66|71.16|77.74|97.26|18.28|13.4|60.35
ICNet|60.74 |69.54|67.17|72.92|67.59|94.61|44.62|28.29|147.68
ICNet+SFGCN|61.47|73.54|68.63|70.05|68.42|95.45|45.79|28.79|153.0
FCN|68.22|83.08|83.62|64.63|74.89|97.15|66.67|18.64|321.78
 FCN+SFGCN|68.24|83.76|84.92|71.23|78.38|97.31|67.46|21.86|324.52
 ResNet50|55.06|78.97|79.15|71.32|71.13|96.38|30.18|28.51|98.18
 ResNet50+SFGCN|66.29|73.04|76.92|72.49|75.00|96.62|30.73|28.75|98.57
```

```
