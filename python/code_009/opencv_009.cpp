#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, const char *argv[])
{
	Mat src = imread("test.jpg");
	if (src.empty()) {
		printf("could not load image...\n");
		return -1;
	}
	namedWindow("input", WINDOW_AUTOSIZE);
	imshow("input", src);

	// RGB to HSV
	Mat hsv;
	cvtColor(src, hsv, COLOR_BGR2HSV);
	imshow("hsv", hsv);

	// RGB to YUV
	Mat yuv;
	cvtColor(src, yuv, COLOR_BGR2YUV);
	imshow("yuv", yuv);

	// RGB to YUV
	Mat ycrcb;
	cvtColor(src, ycrcb, COLOR_BGR2YCrCb);
	imshow("ycrcb", ycrcb);

	Mat src2 = imread("test.png");
	imshow("src2", src2);
	cvtColor(src2, hsv, COLOR_BGR2HSV);
	Mat mask;
	inRange(hsv, Scalar(35, 43, 46), Scalar(99, 255, 255), mask);
	imshow("mask", mask);

	waitKey(0);
	return 0;
}