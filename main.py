from pytube import YouTube 	#Download Youtube Videos
from pytube import Playlist #Download Youtube Playlists
import pytube
import os

#Youtube Link
downloadLink = "https://www.youtube.com/watch?v=M_EoNNlRgn4"
#downloadLink = "https://www.youtube.com/watch?v=Edpy1szoG80&list=PL153hDY-y1E00uQtCVCVC8xJ25TYX8yPU"

#Download Directory
#path = "C:\\Users\\s213295245\\Documents\\YoutubeDownloads"


def singleVideoDownload():
	# Create Single Videos Directory if it doesn't exist
	if not os.path.exists("SingleVideos"):
		os.mkdir("SingleVideos")
		print("Directory SingleVideos Created")
	else:
		print("Directory SingleVideos already exists")
    #One Liner Working
	#YouTube(downloadLink).streams.first().download(".\\SingleVideos\\")

	# Creating YouTube object with the link

	myVideo = YouTube(downloadLink)

	# Title of the Video

	print("Title: " + myVideo.title)

	# Length of the Video in Seconds

	print("Duration: " + myVideo.length)

	# Description of the Video

	#print("Description: " + myVideo.description)

	# Total Views of the Video

	print("Views: " + myVideo.views)

	# Age Restricted Content

	print("Age Restricted: " + str(myVideo.age_restricted))

	# ID of the Video

	print("Video ID: " + myVideo.video_id)

	myStream = YouTube(downloadLink).streams.first()

	myStream.download(".\\SingleVideos\\")
		#SINGLE IMAGE DOWNLOAD (Backup)
		#yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
		#yt.download(".\\SingleVideos\\")

	
def playlistDownload():
	# Create Playlist Directory if it doesn't exist
	if not os.path.exists("Playlists"):
	    os.mkdir("Playlists")
	    print("Directory " , "Playlists" ,  " Created ")
	else:    
	    print("Directory " , "Playlists" ,  " already exists")

	
	#Playlist download
	playlistName = "Unknown"
	pl = Playlist(downloadLink)
	playlistName = pl.title()

	# Create target Directory for downloaded playlist
	try:
	    os.mkdir("Playlists\\" + playlistName)
	    print("Directory " , "Playlists\\" + playlistName ,  " Created ") 
	except FileExistsError:
	    print("Directory " , "Playlists\\" + playlistName ,  " already exists")

	#pl.download_all()
	pl.download_all(".\\Playlists\\" + playlistName + "\\")




if downloadLink.find("list") == -1:
	singleVideoDownload()
else:
	playlistDownload()