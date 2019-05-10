#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;
const float t = 0.95;
int main(int artc, char** argv) {
	Mat src = imread("./test01.png");
	Mat tpl = imread("./test.png");
	if (src.empty() || tpl.empty()) {
		printf("could not load image...\n");
		return -1;
	}
	imshow("input", src);
	imshow("tpl", tpl);

	int result_h = src.rows - tpl.rows + 1;
	int result_w = src.cols - tpl.cols + 1;
	Mat result = Mat::zeros(Size(result_w, result_h), CV_32FC1);
	matchTemplate(src, tpl, result, TM_CCOEFF_NORMED);
	imshow("result image", result);
	int h = result.rows;
	int w = result.cols;
	for (int row = 0; row < h; row++) {
		for (int col = 0; col < w; col++) {
			float v = result.at<float>(row, col);
			// printf("v = %.2f\n", v);
			if (v > t) {
				rectangle(src, Point(col, row), Point(col + tpl.cols, row + tpl.rows), Scalar(255, 0, 0), 1, 8, 0);
			}
		}
	}
	imshow("template matched result", src);

	waitKey(0);
	return 0;
}
