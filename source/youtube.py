from pytube import YouTube
from os import path
#from pydub import AudioSegment
#from moviepy.editor import VideoFileClip

class audio_finder:
    
    def __init__(self, link):
        self.youtubeObject = YouTube(link)
    
    def get_audio(self):
        try:
            #extracting mp4 from youtube
            self.youtubeObject = self.youtubeObject.streams.get_audio_only()
            self.youtubeObject.download("./audio_downloads")

            # mp4_file = "./audio_downloads/"+self.youtubeObject.title+".mp4"
            # mp3_file = "./audio_downloads/"+self.youtubeObject.title+".mp3"
            # wav_file = ""

            # #converting mp4 to mp3 file
            # videoclip = VideoFileClip(mp4_file)
            # audioclip = videoclip.audio
            # audioclip.write_audiofile(mp3_file)
            
            # videoclip.close()
            # audioclip.close() 
            

            #converting mp4 to wav file
            # src = "/audio_downloads/"+self.youtubeObject.title+".mp4"
            # dst = "/audio_downloads/"+self.youtubeObject.title+".wav"
            # sound = AudioSegment.from_file(src, format="mp4")
            # sound.export(dst, format="wav")

            print("Download is Sucessful: " + self.youtubeObject.title)
        except:
            print("Error has occurred!!!!")




#for local file testing
# link = input("Enter url: ")
# get_mp4(link)