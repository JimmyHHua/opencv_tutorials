#include<opencv2/opencv.hpp>
#include<iostream>

using namespace cv;
using namespace std;

int main(int argc, char** argv) {
	Mat src = imread("./test.png");
	if (src.empty()) {
		printf("could not load image...\n");
		return -1;
	}
	imshow("input", src);

	int h = src.rows;
	int w = src.cols;
	float fx = 0.0, fy = 0.0;
	Mat dst = Mat::zeros(src.size(), src.type());
	resize(src, dst, Size(w * 2, h * 2), fx = 0, fy = 0, INTER_NEAREST);
	imshow("INTER_NEAREST", dst);

	resize(src, dst, Size(w * 2, h * 2), fx = 0, fy = 0, INTER_LINEAR);
	imshow("INTER_LINEAR", dst);

	resize(src, dst, Size(w * 2, h * 2), fx = 0, fy = 0, INTER_CUBIC);
	imshow("INTER_CUBIC", dst);

	resize(src, dst, Size(w * 2, h * 2), fx = 0, fy = 0, INTER_LANCZOS4);
	imshow("INTER_LANCZOS4", dst);

	waitKey(0);
	return 0;
}

