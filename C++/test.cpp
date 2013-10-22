#include "opencv2/opencv.hpp"
#include "iostream"

using namespace cv;
using namespace std;

int main(int, char**)
{
    VideoCapture cap(0);
    Mat frame, edges;

    if (!cap.isOpened())
    {
        return -1;
    }

    namedWindow("Video",1);

    while (true)
    {
      cap >> frame;

      if (!frame.empty())
      {
          //cout << frame.size().width << " " << frame.size().height << endl;



          // cvtColor(frame, edges, CV_BGR2GRAY);
          // GaussianBlur(edges, edges, Size(7,7), 1.5, 1.5);
          // Canny(edges, edges, 0, 30, 3);

          imshow("Video", edges);
      }

      if (waitKey(20) >= 0) {
        break;
      }
    }
    // the camera will be deinitialized automatically in VideoCapture destructor
    return 0;
}

/*
#include <opencv2/objdetect/objdetect.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>

#include <iostream>
#include <stdio.h>

using namespace std;
using namespace cv;


int main(int argc, const char** argv)
{
  CvCapture* capture;
  IplImage* img;

  capture = cvCaptureFromCAM(0);
  cvNamedWindow("Video", CV_WINDOW_FULLSCREEN);


  img = cvQueryFrame(capture);
  cout << img << endl;
  // cvShowImage("Video", img);

  cvDestroyWindow("result");

  return 0;
}
*/

/*
  Mat frame, frameCopy, image;

    while (true) {

      IplImage* iplImg = cvQueryFrame(window);
      frame = iplImg;

      if (frame.empty()) {
        break;
      }

      if(iplImg->origin == IPL_ORIGIN_TL) {
        frame.copyTo(frameCopy);
      } else {
        flip(frame, frameCopy, 0);
      }

      cvShowImage("Video", frame);

      if (waitKey(10) >= 0) {
        cvReleaseCapture(&window);
      }
    }


#include <iostream>
#include <cv.h>
#include <highgui.h>
 
using namespace std;
char key;
int main()
{
    cvNamedWindow("Camera_Output", 1);    //Create window
    CvCapture* capture = cvCaptureFromCAM(CV_CAP_ANY);  //Capture using any camera connected to your system
    while(1){ //Create infinte loop for live streaming
 
        IplImage* frame = cvQueryFrame(capture); //Create image frames from capture
        cvShowImage("Camera_Output", frame);   //Show image frames on created window
        key = cvWaitKey(10);     //Capture Keyboard stroke
        if (char(key) == 27){
            break;      //If you hit ESC key loop will break.
        }
    }
    cvReleaseCapture(&capture); //Release capture.
    cvDestroyWindow("Camera_Output"); //Destroy Window
    return 0;
}
*/


