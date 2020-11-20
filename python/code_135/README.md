## OpenCV DNN 实时快速的图像风格迁移

OpenCV DNN模块现在还支持图像风格迁移网络模型的加载与使用，支持的模型是基于李飞飞等人在论文《Perceptual Losses for Real-Time Style Transfer and Super-Resolution》中提到的快速图像风格迁移网络，基于感知损失来提取特征，生成图像特征与高分辨率图像。

整个网络模型是基于DCGAN + 5个残差层构成，是一个典型的全卷积网络。

模型下载地址:

[GitHub - jcjohnson/fast-neural-style](https://github.com/jcjohnson/fast-neural-style)

这个网络可以支持任意尺寸的图像输入，作者提供了很多种预训练的风格迁移模型提供使用，我下载了下面的预训练模型。：
- composition_vii.t7
- starry_night.t7
- la_muse.t7
- the_wave.t7
- mosaic.t7
- the_scream.t7
- feathers.t7
- candy.t7
- udnie.t7

这些模型都是torch框架支持的二进制权重文件，加载模型之后，就可以调用forward得到结果，通过对输出结果反向加上均值，rescale到0~255的RGB色彩空间，即可显示。

Tyep | Image
---|---
Feathers.t7 | <img src=result_6.png>
Candy.t7 | <img src=result_7.png>