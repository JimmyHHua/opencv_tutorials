#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int artc, char** argv) {
	Mat src1 = imread("./test.png");
	Mat src2 = imread("./Mat.png");
	Mat src3 = imread("./test.png");
	Mat src4 = imread("./test.png");

	imshow("input1", src1);
	imshow("input2", src2);
	imshow("input3", src3);
	imshow("input4", src4);

	Mat hsv1, hsv2, hsv3, hsv4;
	cvtColor(src1, hsv1, COLOR_BGR2HSV);
	cvtColor(src2, hsv2, COLOR_BGR2HSV);
	cvtColor(src3, hsv3, COLOR_BGR2HSV);
	cvtColor(src4, hsv4, COLOR_BGR2HSV);

	int h_bins = 60; int s_bins = 64;
	int histSize[] = { h_bins, s_bins };
	float h_ranges[] = { 0, 180 };
	float s_ranges[] = { 0, 256 };
	const float* ranges[] = { h_ranges, s_ranges };
	int channels[] = { 0, 1 };
	Mat hist1, hist2, hist3, hist4;
	calcHist(&hsv1, 1, channels, Mat(), hist1, 2, histSize, ranges, true, false);
	calcHist(&hsv2, 1, channels, Mat(), hist2, 2, histSize, ranges, true, false);
	calcHist(&hsv3, 1, channels, Mat(), hist3, 2, histSize, ranges, true, false);
	calcHist(&hsv4, 1, channels, Mat(), hist4, 2, histSize, ranges, true, false);

	normalize(hist1, hist1, 0, 1, NORM_MINMAX, -1, Mat());
	normalize(hist2, hist2, 0, 1, NORM_MINMAX, -1, Mat());
	normalize(hist3, hist3, 0, 1, NORM_MINMAX, -1, Mat());
	normalize(hist4, hist4, 0, 1, NORM_MINMAX, -1, Mat());

	for (int i = 0; i < 4; i++)
	{
		int compare_method = i;
		double src1_src2 = compareHist(hist1, hist2, compare_method);
		double src3_src4 = compareHist(hist3, hist4, compare_method);
		printf(" Method [%d]  : src1_src2 : %f, src3_src4: %f,  \n", i, src1_src2, src3_src4);
	}

	waitKey(0);
	return 0;
}



