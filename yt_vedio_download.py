from pytube import YouTube
from time import sleep
sleep(2)


print('----------------starting---------------------')



sleep(2)


print("""""""""
██╗░░░██╗████████╗  ██████╗░░█████╗░░██╗░░░░░░░██╗███╗░░██╗██╗░░░░░░█████╗░░█████╗░██████╗░
╚██╗░██╔╝╚══██╔══╝  ██╔══██╗██╔══██╗░██║░░██╗░░██║████╗░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗
░╚████╔╝░░░░██║░░░  ██║░░██║██║░░██║░╚██╗████╗██╔╝██╔██╗██║██║░░░░░██║░░██║███████║██║░░██║
░░╚██╔╝░░░░░██║░░░  ██║░░██║██║░░██║░░████╔═████║░██║╚████║██║░░░░░██║░░██║██╔══██║██║░░██║
░░░██║░░░░░░██║░░░  ██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░██║░╚███║███████╗╚█████╔╝██║░░██║██████╔╝
░░░╚═╝░░░░░░╚═╝░░░  ╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░╚═╝░░╚══╝╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░
CCREATED BY LASSANHACKERANDCODER 
ALL RIGHTS TO LASSANHACKERANDCODER 
""""""""")

link = input("ENTER THE VIDIO LINK : ")
yt = YouTube(link)

sleep(2)

print("detecting THE YOUTUBE THAT YOU WANT TO DOWNLOAD")

sleep(3)

print(" Detecting vedio informations")

sleep(3)

print("Title: " , yt.title)

sleep(3)

print("VIEWS : ", yt.views)


yd = yt.streams.get_highest_resolution()


print("DOWNLOADING THE VEDIO ")

yd.download(input("ENTER THE INSTALLITIONS PATH :"))

sleep(4)

print("DOWNLOADING THE YOUTUBE VEDIO")

sleep(10)

print(" vedio downloaded successfull") 

download_thum = input("DO YUU WANT TO DOWNLOAD THUMNAILO OF THE VEDIO  (Y,N) :")
print("thanks for using this tool")