#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int artc, char** argv) {
	Mat src1 = imread("./test0.jpg");
	Mat src2 = imread("./test1.jpg");
	if (src1.empty() || src2.empty()) {
		printf("could not load image...\n");
		return -1;
	}
	namedWindow("input", CV_WINDOW_AUTOSIZE);
	imshow("input1", src1);
	imshow("input2", src2);
	int height = src1.rows;
	int width = src1.cols;

	int b1 = 0, g1 = 0, r1 = 0;
	int b2 = 0, g2 = 0, r2 = 0;
	int b = 0, g = 0, r = 0;
	Mat result = Mat::zeros(src1.size(), src1.type());
	for (int row = 0; row < height; row++) {
		for (int col = 0; col < width; col++) {
				b1 = src1.at<Vec3b>(row, col)[0];
				g1 = src1.at<Vec3b>(row, col)[1];
				r1 = src1.at<Vec3b>(row, col)[2];

				b2 = src2.at<Vec3b>(row, col)[0];
				g2 = src2.at<Vec3b>(row, col)[1];
				r2 = src2.at<Vec3b>(row, col)[2];

				result.at<Vec3b>(row, col)[0] = saturate_cast<uchar>(b1 + b2);
				result.at<Vec3b>(row, col)[1] = saturate_cast<uchar>(g1 + g2);
				result.at<Vec3b>(row, col)[2] = saturate_cast<uchar>(r1 + r2);
		}
	}
	imshow("output", result);

	Mat add_result = Mat::zeros(src1.size(), src1.type());
	add(src1, src2, add_result);
	imshow("add_result", add_result);

	Mat sub_result = Mat::zeros(src1.size(), src1.type());
	subtract(src1, src2, sub_result);
	imshow("sub_result", sub_result);

	Mat mul_result = Mat::zeros(src1.size(), src1.type());
	multiply(src1, src2, mul_result);
	imshow("mul_result", mul_result);

	Mat div_result = Mat::zeros(src1.size(), src1.type());
	divide(src1, src2, div_result);
	imshow("div_result", div_result);
	
	waitKey(0);
	return 0;
}
