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

	Mat dst1, dst2;
	blur(src, dst1, Size(5, 5), Point(-1, -1), 4);
	GaussianBlur(src, dst2, Size(5, 5), 15, 0, 4);


	imshow("blur", dst1);
	imshow("gaussian blur", dst2);

	waitKey(0);
	return 0;
}



