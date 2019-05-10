#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

void pyramid_up(Mat &image, vector<Mat> &pyramid_images, int level);
void laplaian_demo(vector<Mat> &pyramid_images, Mat &image);
int main(int artc, char** argv) {
	Mat src = imread("./test.png");
	if (src.empty()) {
		printf("could not load image...\n");
		return -1;
	}
	namedWindow("input", CV_WINDOW_AUTOSIZE);
	imshow("input", src);

	vector<Mat> p_images;
	pyramid_up(src, p_images, 3);
	laplaian_demo(p_images, src);

	waitKey(0);
	return 0;
}

void pyramid_up(Mat &image, vector<Mat> &pyramid_images, int level) {
	Mat temp = image.clone();
	Mat dst;
	for (int i = 0; i < level; i++) {
		pyrDown(temp, dst);
		//imshow(format("pyramid_up_%d", i), dst);
		temp = dst.clone();
		pyramid_images.push_back(temp);
	}
}

void laplaian_demo(vector<Mat> &pyramid_images, Mat &image) {
	for (int t = pyramid_images.size() - 1; t>-1; t--) {
		Mat dst;
		if (t - 1 < 0) {
			pyrUp(pyramid_images[t], dst, image.size());
			subtract(image, dst, dst);
			dst = dst + Scalar(127, 127, 127);
			imshow(format("laplaian_layer_%d", t), dst);
		}
		else {
			pyrUp(pyramid_images[t], dst, pyramid_images[t-1].size());
			subtract(pyramid_images[t - 1], dst, dst);
			dst = dst + Scalar(127, 127, 127);
			imshow(format("laplaian_layer_%d", t), dst);
		}
	}
}
