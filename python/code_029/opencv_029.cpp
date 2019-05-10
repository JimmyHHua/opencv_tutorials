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

	Mat dst;
	double tt = getTickCount();
	edgePreservingFilter(src, dst, 1, 60, 0.44);
	double end = (getTickCount() - tt) / getTickFrequency();
	printf("time consume : %f\n ", end);
	imshow("result", dst);

	waitKey(0);
	return 0;
}
