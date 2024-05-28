#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        std::cerr << "Usage: " << argv[0] << " <URL> [-o <output_path>]" << std::endl;
        return 1;
    }

    string URL = argv[1];
    URL = URL.substr(0, URL.find('&'));

    string outputPath = "D:\\"; // Default output path

    // Check for optional output path argument
    for (int i = 2; i < argc; ++i)
    {
        if (string(argv[i]) == "-o" && i + 1 < argc)
        {
            outputPath = argv[i + 1];
            break;
        }
    }

    // Note: Escape the double quotes in the command string
    string command = "yt-dlp -f best \"" + URL + "\" -o \"" + outputPath + "\\%(title)s.%(ext)s\"";
    system(command.c_str());

    return 0;
}
