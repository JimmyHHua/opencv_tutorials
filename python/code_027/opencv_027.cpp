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
	pyrMeanShiftFiltering(src, dst, 15, 50, 1, TermCriteria(TermCriteria::COUNT + TermCriteria::EPS, 5, 1));
	imshow("result", dst);

	waitKey(0);
	return 0;
}
