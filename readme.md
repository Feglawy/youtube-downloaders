# youtube downloaders

it is required to have python and run `pip install -r requirement.txt` for installing the required packages

## videoDownloader.cpp

it just uses yt-dlp and c++ to work the defult directory which the downloaded video will be downloaded to is "D:\" this is ofcourse on windows

## videoDownloaderV2.0.cpp

This also like the previous one but added some features like choosing the quality and filetype

## videoDownloader_version_python.py

this one uses pytube package to run

# How to run the cpp files

it is better to make the cpp file in the root directory as this will allow you to directly use it from the terminal
just type in the terminal

to go to the root directory
`cd ~`

to open the file exproler window
`start .`

paste the cpp file there then compile the file in the terminal
`g++ filename.cpp -o OutputFilename`

To run use

`.\OutputFilename.exe "{add the url to the video}" -t {mp3/ mp4} -r {1080/ 720/ 360}`

The inputs in the curly brackets are the options

# !TODO

- [x] add user custom argument -o for the output file location to V2.0
