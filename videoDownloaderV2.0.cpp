#include <iostream>
#include <string>
#include <cstdlib> // For system function
#include <sstream> // For string manipulation

using namespace std;

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        cerr << "Usage: " << argv[0] << " <URL> [-t mp3/mp4] [-r 1080/720/360]" << endl;
        return 1;
    }

    string URL = argv[1];
    URL = URL.substr(0, URL.find('&'));

    string outputPath = "D:\\"; // Default output path

    string fileType = "mp4"; // Default file type
    int resolution = 1080;   // Default resolution for mp4

    // Parse command line arguments
    for (int i = 2; i < argc; ++i)
    {
        if (string(argv[i]) == "-t" && i + 1 < argc)
        {
            fileType = argv[i + 1];
            i++; // Skip the next argument since it's the file type
        }
        else if (string(argv[i]) == "-r" && i + 1 < argc)
        {
            resolution = stoi(argv[i + 1]);
            i++; // Skip the next argument since it's the resolution
        }
    }

    // Construct the appropriate command based on file type and resolution
    stringstream commandStream;
    commandStream << "yt-dlp \"" << URL << "\"";

    if (fileType == "mp4")
    {
        // Append resolution if fileType is mp4
        commandStream << " -f \"bestvideo[height<=" << resolution << "]+bestaudio/best[height<=" << resolution << "]\"";
    }

    commandStream << " -o \"" << outputPath << "\\%(title)s.%(ext)s\"";

    string command = commandStream.str();

    // Execute the command using system call
    int result = system(command.c_str());
    if (result != 0)
    {
        cerr << "Error: Failed to execute command." << endl;
        return 1;
    }

    return 0;
}
