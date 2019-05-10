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

	int t = 127;
	Mat gray, binary;
	cvtColor(src, gray, COLOR_BGR2GRAY);
	Scalar m = mean(src);
	t = m[0];
	binary = Mat::zeros(src.size(), CV_8UC1);

	// ֱ�Ӷ�ȡͼ������
	int height = src.rows;
	int width = src.cols;
	for (int row = 0; row < height; row++) {
		for (int col = 0; col < width; col++) {
			int pv = gray.at<uchar>(row, col);
			if (pv > t) {
				binary.at<uchar>(row, col) = 255;
			}
			else {
				binary.at<uchar>(row, col) = 0;
			}
		}
	}
	imshow("binary", binary);

	waitKey(0);
	return 0;
}
