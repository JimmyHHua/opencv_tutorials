#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

const int bins = 256;
Mat src;
const char* winTitle = "input image";
void backProjection_demo(Mat &image, Mat &model);
int main(int argc, char** argv) {
	Mat src = imread("./Mat.png");
	Mat model = imread("./test.png");
	if (src.empty() || model.empty()) {
		printf("could not load image...\n");
		return 0;
	}
	namedWindow(winTitle, WINDOW_AUTOSIZE);
	imshow(winTitle, src);
	imshow("model", model);

	backProjection_demo(src, model);
	waitKey(0);
	return 0;
}

void backProjection_demo(Mat &image, Mat &model) {
	Mat model_hsv, image_hsv;
	cvtColor(model, model_hsv, COLOR_BGR2HSV);
	cvtColor(image, image_hsv, COLOR_BGR2HSV);

	// ����ֱ��ͼ����������
	int h_bins = 32; int s_bins = 32;
	int histSize[] = { h_bins, s_bins };
	// hue varies from 0 to 179, saturation from 0 to 255
	float h_ranges[] = { 0, 180 };
	float s_ranges[] = { 0, 256 };
	const float* ranges[] = { h_ranges, s_ranges };
	int channels[] = { 0, 1 };
	Mat roiHist;
	calcHist(&model_hsv, 1, channels, Mat(), roiHist, 2, histSize, ranges, true, false);
	normalize(roiHist, roiHist, 0, 255, NORM_MINMAX, -1, Mat());
	MatND backproj;
	calcBackProject(&image_hsv, 1, channels, roiHist, backproj, ranges, 1.0);
	imshow("BackProj", backproj);
}