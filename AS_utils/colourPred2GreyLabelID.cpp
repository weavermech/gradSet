//////////////////////////////////
//  Converts colour predication //
// masks to greyscale label IDs	//
//////////////////////////////////

#include <string>
#include <vector>
#include <opencv2/core.hpp>
#include <opencv2/core/utility.hpp>
#include "opencv2/imgproc.hpp"
#include "opencv2/imgcodecs.hpp"
#include <opencv2/highgui.hpp>
#include <iostream>
#include <sstream>
#include <filesystem>

using namespace cv;
namespace fs = std::filesystem;
//Scans pixel by pixel converting pixel values to label values
//converts to greyscale and appends filename
void ScanImageAndID(Mat& I, cv::String fn);


int main( int argc, char* argv[])
{
    //get filenames fn
    std::vector<cv::String> fn;
    glob("/home/weaver/PycharmProjects/datasets/CSresults/grad14th_2300/", fn, false);


    size_t count = fn.size(); 

    for (size_t i = 0; i < count; i++)
    {
        Mat I(imread(fn[i], IMREAD_COLOR));
        ScanImageAndID(I, fn[i]);
    }

}


void ScanImageAndID(Mat& I, cv::String fn)
{
    // accept only char type matrices
    CV_Assert(I.depth() == CV_8U);

    MatIterator_<Vec3b> it, end;
    for( it = I.begin<Vec3b>(), end = I.end<Vec3b>(); it != end; ++it)
    {

        if ( (*it)[0] == 0 &&          //if green
            (*it)[1] == 255 &&
            (*it)[2] == 0 )
        {
            (*it)[0] = 7;              //to label 7
            (*it)[1] = 7;
            (*it)[2] = 7;
        }
        else if ( (*it)[0] == 255 &&   //blue
                  (*it)[1] ==  0 &&
                  (*it)[2] == 0 )
        {
            (*it)[0] = 8;
            (*it)[1] = 8;
            (*it)[2] = 8;
        }

        else if ( (*it)[0] == 0 &&     //yellow
                  (*it)[1] == 255 &&
                  (*it)[2] == 255 )
        {
            (*it)[0] = 11;
            (*it)[1] = 11;
            (*it)[2] = 11;
        }

        else if ( (*it)[0] == 255  &&  //magenta
                  (*it)[1] == 0  &&
                  (*it)[2] ==  255 )
        {
            (*it)[0] = 12;
            (*it)[1] = 12;
            (*it)[2] = 12;
        }

        else if ( (*it)[0] == 0 &&     //red
                  (*it)[1] == 0 &&
                  (*it)[2] == 255 )
        {
            (*it)[0] = 13;
            (*it)[1] = 13;
            (*it)[2] = 13;
        }

        else if ( (*it)[0] == 255 &&   //teal
                  (*it)[1] == 255 &&
                  (*it)[2] == 0 )
        {
            (*it)[0] = 17;
            (*it)[1] = 17;
            (*it)[2] = 17;
        }

        else if ( (*it)[0] == 255 &&   //white
                  (*it)[1] == 255 &&
                  (*it)[2] == 255 )
        {
            (*it)[0] = 19;
            (*it)[1] = 19;
            (*it)[2] = 19;
        }

// otherwise to black
        else
        {
            (*it)[0] = 0;              //unlabeled/ignored
            (*it)[1] = 0;
            (*it)[2] = 0;
        }
    }


    //convert to (greyscale) 2D matrix
    cv::cvtColor(I, I, CV_BGR2GRAY);

    std::string s = fn;     //TODO look in to cv::string vs std::string
    if (!s.empty())
    {
        s.resize(s.size() - 4); ////Check what to remove! ".png" or "_out.png"  ???
        s = s + "LabelIds.png";
        fn = s;
    }

    imwrite(fn, I);
}

