## OpenCV DNN 为模型运行设置目标设备与计算后台

OpenCV中加载网络模型之后，可以设置计算后台与计算目标设备，OpenCV DNN模块支持这两个设置的相关API如下：
cv::dnn::Net::setPreferableBackend(
	int backendId
)
backendId 表示后台计算id，
-	DNN_BACKEND_DEFAULT (DNN_BACKEND_INFERENCE_ENGINE)表示默认使用intel的预测推断库(需要下载安装Intel® OpenVINO™ toolkit， 然后重新编译OpenCV源码，在CMake时候enable该选项方可)， 可加速计算！
-	DNN_BACKEND_OPENCV 一般情况都是使用opencv dnn作为后台计算，

void cv::dnn::Net::setPreferableTarget(
	int targetId
)
常见的目标设备id如下：
-	DNN_TARGET_CPU其中表示使用CPU计算，默认是的
-	DNN_TARGET_OPENCL 表示使用OpenCL加速，一般情况速度都很扯
-	DNN_TARGET_OPENCL_FP16 可以尝试
-	DNN_TARGET_MYRIAD 树莓派上的