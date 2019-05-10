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

	Mat grad_x, grad_y;
	Mat dst;
	Sobel(src, grad_x, CV_32F, 1, 0, 3, 1, 0, BORDER_DEFAULT);
	Sobel(src, grad_y, CV_32F, 0, 1, 3, 1, 0, BORDER_DEFAULT);
	
	convertScaleAbs(grad_x, grad_x);
	convertScaleAbs(grad_y, grad_y);

	add(grad_x, grad_y, dst, Mat(), CV_16S);
	convertScaleAbs(dst, dst);

	imshow("gradient", dst);

	waitKey(0);
	return 0;
}
