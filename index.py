from pytube import YouTube
import sys

def get_save_location():
    return input("Enter the path to the folder where you want to save the downloaded file: ")

videoURL = ""
if len(sys.argv) > 1:
    videoURL = sys.argv[1]

if "youtube.com" not in videoURL:
    videoURL = input("Enter YouTube URL: ")

yt = YouTube(videoURL, use_oauth=True, allow_oauth_cache=True)

# List available resolutions
print("Available Resolutions:")
res = []
for stream in yt.streams.filter():
    print(stream)
    res.append(stream.resolution)

res1 = []
for val in res:
    if val != None :
        res1.append(val)

res2 = []
Str  = ""
for item in res1:
    Str = item.rstrip(item[-1])
    Int = int(Str)
    res2.append(Int)


res2.sort()

print(res2)
# Ask the user to select resolution
selected_resolution = input("Enter the resolution without p (e.g., 1080, 720, etc.): ")
selected_resolution += "p"

# Download the video with the selected resolution
video_stream = yt.streams.filter(res=selected_resolution, file_extension="mp4").first()
if video_stream:
    save_location = get_save_location()
    if save_location:
        filename = yt.title.replace(" ", "_") + ".mp4"
        print("Downloading YouTube File: " + yt.title)
        video_stream.download(output_path=save_location, filename=filename)
        print("Download completed.")
    else:
        print("Download canceled. No save location selected.")
else:
    print(f"Video with {selected_resolution}p resolution not found.")
