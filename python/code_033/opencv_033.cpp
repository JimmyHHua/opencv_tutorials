#include <opencv2/opencv.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int artc, char** argv) {
	Mat image = imread("./test.png");
	if (image.empty()) {
		printf("could not load image...\n");
		return -1;
	}
	namedWindow("input", CV_WINDOW_AUTOSIZE);
	imshow("input", image);

	Mat blured, dst;
	GaussianBlur(image, blured, Size(3, 3), 0);
	Laplacian(blured, dst, CV_32F, 1, 1.0, 127.0, BORDER_DEFAULT);
	convertScaleAbs(dst, dst);
	imshow("result", dst);

	waitKey(0);
	return 0;
}
