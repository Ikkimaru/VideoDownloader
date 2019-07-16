from pytube import YouTube 	#Download Youtube Videos
from pytube import Playlist #Download Youtube Playlists
import os

#Youtube Link
downloadLink = "https://www.youtube.com/watch?v=E1ZVSFfCk9g"

#Download Directory
#path = "C:\\Users\\s213295245\\Documents\\YoutubeDownloads"

#YouTube(downloadLink).streams.first().download(path)	#One Liner Working

#SINGLE IMAGE DOWNLOAD
# Create Single Videos Directory if it doesn't exist
if not os.path.exists("SingleVideos"):
    os.mkdir("SingleVideos")
    print("Directory " , "SingleVideos" ,  " Created ")
else:    
    print("Directory " , "SingleVideos" ,  " already exists")

#yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
#yt.download(".\\SingleVideos\\")

#PLAYLIST DOWNLOAD
# Create Playlist Directory if it doesn't exist
if not os.path.exists("Playlists"):
    os.mkdir("Playlists")
    print("Directory " , "Playlists" ,  " Created ")
else:    
    print("Directory " , "Playlists" ,  " already exists")


pl = Playlist("https://www.youtube.com/watch?v=Edpy1szoG80&list=PL153hDY-y1E00uQtCVCVC8xJ25TYX8yPU")

playlistName = pl.title()

try:
    # Create target Directory
    os.mkdir("Playlists\\" + playlistName)
    print("Directory " , "Playlists\\" + playlistName ,  " Created ") 
except FileExistsError:
    print("Directory " , "Playlists\\" + playlistName ,  " already exists")

#pl.download_all()
#pl.download_all(".\\Playlists\\" + playlistName + "\\")

#video = YouTube('https://www.youtube.com/watch?v=d3D7Y_ycSms')
#print(video.thumbnail_url)


#yt = YouTube(downloadLink)
#yt.thumbnail_url