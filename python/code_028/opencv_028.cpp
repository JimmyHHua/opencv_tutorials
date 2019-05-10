#include <opencv2/opencv.hpp>
#include <iostream>
using namespace cv;
using namespace std;
void blur_demo(Mat &image, Mat &sum);
void edge_demo(Mat &image, Mat &sum);
int getblockSum(Mat &sum, int x1, int y1, int x2, int y2, int i);
int main(int argc, char** argv) {
	Mat src = imread("./test.png");
	if (src.empty()) {
		printf("could not load image...\n");
		return -1;
	}
	namedWindow("input", CV_WINDOW_AUTOSIZE);
	imshow("input", src);
	namedWindow("output", CV_WINDOW_AUTOSIZE);
	// �������ͼ
	Mat sum, sqrsum;
	integral(src, sum, sqrsum, CV_32S, CV_32F);
	// ����ͼӦ��
	int type = 0;
	while (true) {
		char c = waitKey(100);
		if (c > 0) {
			type = (int)c;
			printf("c : %d\n", type);
		}
		if (c == 27) {
			break; // ESC
		}
		if (type == 49) { // ���ּ� 1
			blur_demo(src, sum);
		}
		else if (type == 50) { // ���ּ� 2
			edge_demo(src, sum);
		}
		else {
			blur_demo(src, sum);
		}
	}
	waitKey(0);
	return 0;
}
void blur_demo(Mat &image, Mat &sum) {
	int w = image.cols;
	int h = image.rows;
	Mat result = Mat::zeros(image.size(), image.type());
	int x2 = 0, y2 = 0;
	int x1 = 0, y1 = 0;
	int ksize = 5;
	int radius = ksize / 2;
	int ch = image.channels();
	int cx = 0, cy = 0;
	for (int row = 0; row < h + radius; row++) {
		y2 = (row + 1)>h ? h : (row + 1);
		y1 = (row - ksize) < 0 ? 0 : (row - ksize);
		for (int col = 0; col < w + radius; col++) {
			x2 = (col + 1)>w ? w : (col + 1);
			x1 = (col - ksize) < 0 ? 0 : (col - ksize);
			cx = (col - radius) < 0 ? 0 : col - radius;
			cy = (row - radius) < 0 ? 0 : row - radius;
			int num = (x2 - x1)*(y2 - y1);
			for (int i = 0; i < ch; i++) {
				// ����ͼ���Һͱ����������
				int s = getblockSum(sum, x1, y1, x2, y2, i);
				result.at<Vec3b>(cy, cx)[i] = saturate_cast<uchar>(s / num);
			}
		}
	}
	imshow("output", result);
	imwrite("./result.png", result);
}
/**
* 3x3 sobel ��ֱ��Ե�����ʾ
*/
void edge_demo(Mat &image, Mat &sum) {
	int w = image.cols;
	int h = image.rows;
	Mat result = Mat::zeros(image.size(), CV_32SC3);
	int x2 = 0, y2 = 0;
	int x1 = 0, y1 = 0;
	int ksize = 3; // ���Ӵ�С�������޸ģ�Խ���ԵЧӦԽ����
	int radius = ksize / 2;
	int ch = image.channels();
	int cx = 0, cy = 0;
	for (int row = 0; row < h + radius; row++) {
		y2 = (row + 1)>h ? h : (row + 1);
		y1 = (row - ksize) < 0 ? 0 : (row - ksize);
		for (int col = 0; col < w + radius; col++) {
			x2 = (col + 1)>w ? w : (col + 1);
			x1 = (col - ksize) < 0 ? 0 : (col - ksize);
			cx = (col - radius) < 0 ? 0 : col - radius;
			cy = (row - radius) < 0 ? 0 : row - radius;
			int num = (x2 - x1)*(y2 - y1);
			for (int i = 0; i < ch; i++) {
				// ����ͼ���Һͱ����������
				int s1 = getblockSum(sum, x1, y1, cx, y2, i);
				int s2 = getblockSum(sum, cx, y1, x2, y2, i);
				result.at<Vec3i>(cy, cx)[i] = saturate_cast<int>(s2 - s1);
			}
		}
	}
	Mat dst, gray;
	convertScaleAbs(result, dst);
	normalize(dst, dst, 0, 255, NORM_MINMAX);
	cvtColor(dst, gray, COLOR_BGR2GRAY);
	imshow("output", gray);
	imwrite("D:/edge_result.png", gray);
}
int getblockSum(Mat &sum, int x1, int y1, int x2, int y2, int i) {
	int tl = sum.at<Vec3i>(y1, x1)[i];
	int tr = sum.at<Vec3i>(y2, x1)[i];
	int bl = sum.at<Vec3i>(y1, x2)[i];
	int br = sum.at<Vec3i>(y2, x2)[i];
	int s = (br - bl - tr + tl);
	return s;
}