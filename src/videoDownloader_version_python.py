from pytube import YouTube
from pytube import Playlist
from colorama import Fore
import time
import os
import shutil
import sys



os.system("cls")


def Loading():
    from progress.bar import ShadyBar
    sbar= ShadyBar("Loading...")
    finish = False
    while not finish:
        for i in range(100):
            time.sleep(0.01)
            sbar.next()
        finish= True
    sbar.finish()


file_path=os.path.dirname(os.path.realpath(__file__))
if not os.path.exists("VIDEOS"):
    os.mkdir('VIDEOS')

file_path_vid=file_path+'\VIDEOS'


def program():
    
    print(Fore.RED+"Youtube downloader".center(120," "))
    print(".By Feglawy".center(170," "))
    


    url=input(Fore.CYAN+"URL:>>")
    video=YouTube(url)
    
    def finish():
        print("Finish!")
    
    
    if video.length >=3600:
        print(f"""
        Title: {video.title}
        Length: {
    time.strftime('%H:%M:S', time.gmtime(video.length))}""")
        
        if video.views>=1000 and video.views< 1000000:
            print(f"        views: {round(video.views/1000,2)} K")
        elif video.views >= 1000000:
            print(f"        Views: {round(video.views/1000000,2)} M")
        elif video.views < 1000:
            print(f'Views: {video.views}')
    
    
    elif video.length >= 60:
        print(f"""
        Title: {video.title}
        Length: {
    time.strftime('%M:%S', time.gmtime(video.length))}""")
        
        if video.views>=1000 and video.views< 1000000:
            print(f"        views: {round(video.views/1000,2)} K")
        elif video.views >= 1000000:
            print(f"        Views: {round(video.views/1000000,2)} M")
        elif video.views < 1000:
            print(f'Views: {video.views}')
    
    
    elif video.length <=60:
        print(f"""
        Title: {video.title}
        Length: {time.strftime('%S', time.gmtime(video.length))} s""")
        
        if video.views>=1000 and video.views< 1000000:
            print(f"        views: {round(video.views/1000,2)} K")
        elif video.views >= 1000000:
            print(f"        Views: {round(video.views/1000000,2)} M")
        elif video.views < 1000:
            print(f'Views: {video.views}')     
    def mp3_4():
        print("\nchoose what u want:")
        print("1:mp3(audio)")
        print("2:mp4(video)")

        option=input("(1/2)>>") 
        
        
        
        if option=="1":
            
            
            video.streams.get_by_itag('251').download(file_path_vid)
            time.sleep(1)
            print("Now downloading ",(video.title))
            video.register_on_progress_callback(Loading())
            video.register_on_complete_callback(finish())
        
        
        
        elif option=="2":
            
            print(f"""
            1:144p  ,8fps
            2:360p  ,30fps
            3:720p  ,30fps
            """)
            choice=input("(1/2/3):>>")
            
            
            
            
            
            if choice in ('1','2','3'):
                if choice == '1':
                    video.streams.get_by_itag('17').download(file_path_vid)
                    time.sleep(1)
                    print("Now downloading ",(video.title))
                    video.register_on_progress_callback(Loading())
                    video.register_on_complete_callback(finish())
                elif choice== "2":
                    video.streams.get_by_itag('18').download(file_path_vid)
                    time.sleep(1)
                    print("Now downloading ",(video.title))
                    video.register_on_progress_callback(Loading())
                    video.register_on_complete_callback(finish())
                elif choice== "3":
                    video.streams.get_by_itag('22').download(file_path_vid)
                    time.sleep(1)
                    print("Now downloading ",(video.title))
                    video.register_on_progress_callback(Loading())
                video.register_on_complete_callback(finish())
            else:
                choice=input("(1/2/3):>>")        
        else:
            print("Error")
            mp3_4()
    mp3_4()
program()
def again():    
    while True:

        print(Fore.RED+'do you want to run the program again??'.center(120,' '))
        print('<type Y for yes or N for no>')
        x=input("(Y/N)>>>")
        while x=="":
            x=input("(Y/N)>>>")
        if x in ('Y','y'):
            os.system("cls")
            program()
        elif x in('n','N'):
            print("Bye")
            break
        else:
            os.system('cls')
            print('error')
            again()
again()
