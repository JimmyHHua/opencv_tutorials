#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

void add_salt_pepper_noise(Mat &image);
void gaussian_noise(Mat &image);
int main(int artc, char** argv) {
	Mat src = imread("./test.png");
	if (src.empty()) {
		printf("could not load image...\n");
		return -1;
	}
	namedWindow("input", CV_WINDOW_AUTOSIZE);
	imshow("input", src);
	gaussian_noise(src);

	Mat result1, result2, result3, result4;
	blur(src, result1, Size(5, 5));
	imshow("result-1", result1);

	GaussianBlur(src, result2, Size(5, 5), 0);
	imshow("result-2", result2);

	medianBlur(src, result3, 5);
	imshow("result-3", result3);

	fastNlMeansDenoisingColored(src, result4, 15, 15, 10, 30);
	imshow("result-4", result4);

	waitKey(0);
	return 0;
}

void add_salt_pepper_noise(Mat &image) {
	RNG rng(12345);
	int h = image.rows;
	int w = image.cols;
	int nums = 10000;
	for (int i = 0; i < nums; i++) {
		int x = rng.uniform(0, w);
		int y = rng.uniform(0, h);
		if (i % 2 == 1) {
			image.at<Vec3b>(y, x) = Vec3b(255, 255, 255);
		}
		else {
			image.at<Vec3b>(y, x) = Vec3b(0, 0, 0);
		}
	}
	imshow("salt pepper", image);
}

void gaussian_noise(Mat &image) {
	Mat noise = Mat::zeros(image.size(), image.type());
	randn(noise, (15, 15, 15), (30, 30, 30));
	Mat dst;
	add(image, noise, dst);
	imshow("gaussian noise", dst);
	dst.copyTo(image);
}
