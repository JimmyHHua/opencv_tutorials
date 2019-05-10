#include<opencv2/opencv.hpp>
#include<iostream>

using namespace cv;
using namespace std;

int main(int argc, char** argv) {
	Mat src = imread("./test.png");
	namedWindow("input", WINDOW_AUTOSIZE);
	imshow("input", src);
	int h = src.rows;
	int w = src.cols;

	// ��ȡROI
	int cy = h / 2;
	int cx = w / 2;
	Rect rect(cx - 100, cy - 100, 200, 200);
	Mat roi = src(rect);
	imshow("roi", roi);

	Mat image = roi.clone();
	// modify ROI
	roi.setTo(Scalar(255, 0, 0));
	imshow("result", src);

	// modify copy roi
	image.setTo(Scalar(0, 0, 255));
	imshow("result", src);
	imshow("copy roi", image);

	// example with ROI - generate mask
	Mat src2 = imread("./test.png");
	imshow("src2", src2);
	Mat hsv, mask;
	cvtColor(src2, hsv, COLOR_BGR2HSV);
	inRange(hsv, Scalar(35, 43, 46), Scalar(99, 255, 255), mask);
	imshow("mask", mask);

	// extract person ROI
	Mat person;
	bitwise_not(mask, mask);
	bitwise_and(src2, src2, person, mask);
	imshow("person", person);

	// generate background
	Mat result = Mat::zeros(src2.size(), src2.type());
	result.setTo(Scalar(255, 0, 0));

	// combine background + person
	Mat dst;
	bitwise_not(mask, mask);
	bitwise_or(person, result, dst, mask);
	add(dst, person, dst);

	imshow("dst", dst);
	waitKey(0);
	return 0;
}

