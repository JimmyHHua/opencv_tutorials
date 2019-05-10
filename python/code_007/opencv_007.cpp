#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, const char *argv[])
{
	// create image one
	Mat src1 = Mat::zeros(Size(400, 400), CV_8UC3);
	Rect rect(100, 100, 100, 100);
	src1(rect) = Scalar(0, 0, 255);
	imshow("input1", src1);
	printf("create first image...\n");

	// create image two
	Mat src2 = Mat::zeros(Size(400, 400), CV_8UC3);
	rect.x = 150;
	rect.y = 150;
	src2(rect) = Scalar(0, 0, 255);
	imshow("input2", src2);
	printf("create second image...\n");

	// �߼�����
	Mat dst1, dst2, dst3;
	bitwise_and(src1, src2, dst1);
	bitwise_xor(src1, src2, dst2);
	bitwise_or(src1, src2, dst3);

	// show results
	imshow("dst1", dst1);
	imshow("dst2", dst2);
	imshow("dst3", dst3);

	Mat src = imread("./test.png");
	namedWindow("input", WINDOW_AUTOSIZE);
	imshow("input", src);
	// ȡ������
	Mat dst;
	bitwise_not(src, dst);
	imshow("dst", dst);

	waitKey(0);
	return 0;
}