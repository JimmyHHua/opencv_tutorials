#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int artc, char** argv) {
	Mat src = imread("./test.png");
	if (src.empty()) {
		printf("could not load image...\n");
		return -1;
	}
	namedWindow("input", CV_WINDOW_AUTOSIZE);
	imshow("input", src);

	Mat blur_img, usm;
	GaussianBlur(src, blur_img, Size(0, 0), 25);
	addWeighted(src, 1.5, blur_img, -0.5, 0, usm);
	imshow("mask image", usm);

	waitKey(0);
	return 0;
}
