////////////////////////////////////////////////////////////////////////////
/////Reads folder thresholding pixel values to 0 or 255 for groundtruth/////
/////Sending any colours that don't fit to white.                      /////
/////Converts sky (black) to white since black is 'unlabelled' colour  /////
/////then runs an opening operation to great stronger patches of colour/////
/////and change white speckling to local colour or black (unlabeled).  /////
////////////////////////////////////////////////////////////////////////////


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
using namespace std::chrono;
namespace fs = std::filesystem;

void ScanImageAndReduceIterator(Mat& I, cv::String fn);




int main( int argc, char* argv[])
{

    std::vector<cv::String> fn;
    glob("/home/weaver/PycharmProjects/datasets/gradSet/finalGrad/matched_leftImg_and_gtFine/gtToProcess/threshopened/*.png", fn, false);



   

    size_t count = fn.size(); //number of png files in images folder

//// uncomment loop and out for timing

//    auto start = high_resolution_clock::now();
//    for (int x(0); x<100; x++)
//    {


	for (size_t i = 0; i < count; i++)
        {
            Mat I(imread(fn[i], IMREAD_COLOR));
            ScanImageAndReduceIterator(I, fn[i]);
        }

//    }
//    auto stop = high_resolution_clock::now();
//    auto duration = duration_cast<milliseconds>(stop - start);
//    std::cout << "Time taken by function: "
//      << duration.count()/100 << " milliseconds" << std::endl;

    return 0;
}



//! [scan-iterator]
void ScanImageAndReduceIterator(Mat& I, cv::String fn)
{
//  accept only char type matrices
    CV_Assert(I.depth() == CV_8U);

    MatIterator_<Vec3b> it, end;
    for( it = I.begin<Vec3b>(), end = I.end<Vec3b>(); it != end; ++it)
    {
        if ( (*it)[0] == 0 &&
             (*it)[1] == 0  &&
             (*it)[2] == 0 )
        {
            (*it)[0] = 255;
            (*it)[1] = 255;
            (*it)[2] = 255;
        }

// threshhold to yellow
        if ( (((*it)[0] < 190) && ((*it)[1] > 220) && ((*it)[2] > 220)) || (((*it)[0] < 150) && ((*it)[1] > 200) && ((*it)[2] > 200)) )
        {
            (*it)[0] = 0;
            (*it)[1] = 255;
            (*it)[2] = 255;
        }
// threshhold to magenta
        else if ( ((*it)[0] > 190) && ((*it)[1] < 180) && ((*it)[2] > 190) )
        {
            (*it)[0] = 255;
            (*it)[1] = 0;
            (*it)[2] = 255;
        }
// threshhold to red
        else if ( ((*it)[0] < 170) && ((*it)[1] < 175) && ((*it)[2] > 190) )
        {
            (*it)[0] = 0;
            (*it)[1] = 0;
            (*it)[2] = 255;
        }
// threshhold to green
        else if ( ((*it)[0] < 178) && ((*it)[1] > 200) && ((*it)[2] < 178) )
        {
            (*it)[0] = 0;
            (*it)[1] = 255;
            (*it)[2] = 0;
        }
// threshhold to blue
        else if ( ((*it)[0] > 190) && ((*it)[1] < 180) && ((*it)[2] < 180) )
        {
            (*it)[0] = 255;
            (*it)[1] = 0;
            (*it)[2] = 0;
        }
// threshold to teal
        else if ( ((*it)[0] > 190) && ((*it)[1] > 190) && ((*it)[2] < 180) )
        {
            (*it)[0] = 255;
            (*it)[1] = 255;
            (*it)[2] = 0;
        }
// threshold to black
        else if ( ((*it)[0] < 50) && ((*it)[1] < 50) && ((*it)[2] < 50) )
        {
            (*it)[0] = 0;
            (*it)[1] = 0;
            (*it)[2] = 0;
        }
// otherwise to white
        else
        {
            (*it)[0] = 255;
            (*it)[1] = 255;
            (*it)[2] = 255;
        }
    }

    int morph_size = 1;
    Mat element = getStructuringElement(MORPH_RECT, Size(2 * morph_size + 1, 2 * morph_size + 1),
                                        Point(morph_size, morph_size));
    Mat dst; // result matrix
    // Apply the specified morphology operation

    morphologyEx(I, dst, MORPH_OPEN, element, Point(-1, -1), 1);

    std::string s = fn;     //TODO look ni to cv::string vs std::string
    if (!s.empty())
    {
        s.resize(s.size() - 4);
        s = s + "_gtFine.png";
        fn = s;
    }
    imwrite(fn, dst);
}


