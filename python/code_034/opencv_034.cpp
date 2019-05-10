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

	Mat sharpen_op = (Mat_<char>(3, 3) << 0, -1, 0,
		-1, 5, -1,
		0, -1, 0);

	Mat result;
	filter2D(src, result, CV_32F, sharpen_op);
	convertScaleAbs(result, result);

	imshow("sharpen image", result);

	waitKey(0);
	return 0;
}
