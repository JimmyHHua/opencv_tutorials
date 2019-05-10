#include<opencv2/opencv.hpp>
#include<iostream>

using namespace cv;
using namespace std;

int main(int argc, char** argv) {
	// ������ͷ
	// VideoCapture capture(0); 

	// ���ļ�
	VideoCapture capture;
	capture.open("./test.avi");
	if (!capture.isOpened()) {
		printf("could not read this video file...\n");
		return -1;
	}
	Size S = Size((int)capture.get(CV_CAP_PROP_FRAME_WIDTH),
		(int)capture.get(CV_CAP_PROP_FRAME_HEIGHT));
	int fps = capture.get(CV_CAP_PROP_FPS);
	printf("current fps : %d \n", fps);
	VideoWriter writer("./test_cp.mp4", CV_FOURCC('D', 'I', 'V', 'X'), fps, S, true);

	Mat frame;
	namedWindow("camera-demo", CV_WINDOW_AUTOSIZE);
	while (capture.read(frame)) {
		imshow("camera-demo", frame);
		writer.write(frame);
		char c = waitKey(50);
		if (c == 27) {
			break;
		}
	}
	capture.release();
	writer.release();
	waitKey(0);
	return 0;
}