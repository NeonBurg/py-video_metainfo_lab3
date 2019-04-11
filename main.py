from googleapiclient.discovery import build
from pytube import YouTube
import enzyme
import os
import ffmpeg

def downloadYouTube(videourl, path):

    yt = YouTube(videourl)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    yt.download(path)

DEVELOPER_KEY = 'AIzaSyAb4KWGpUE997XQBGNu8xsOpjZG3TqdbWU'
youtube = build('youtube', 'v3', developerKey=DEVELOPER_KEY)

ids = 'ftPZsKeAZTY'
results = youtube.videos().list(id=ids, part='snippet').execute()

for result in results.get('items', []):

    video_title = result['snippet']['title']

    project_path = os.getcwd()
    video_dir_path = project_path + '/video_download'
    video_path = video_dir_path + '/' + video_title + '.mp4'

    #downloadYouTube('https://www.youtube.com/watch?v=' + ids, video_dir_path)

    #video_stream = ffmpeg.input(video_path)

    #print(ffmpeg.probe('in.mp4')['format']['duration']))
    probe = ffmpeg.probe(video_path)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    #print (video_stream)

    for key in video_stream:
        print('video_stream[%s] = %s \n' % (key, video_stream[key]))

    print ('---> id: %s\n' % result['id'])
    print ('---> description: %s\n' % result['snippet']['description'])
    print ('---> title: %s\n' % video_title)
    print ('---> tags: %s\n' % result['snippet']['tags'])


    #if os.path.exists(video_path):
        #with open(video_path, 'rb') as f:
            #mp4video = enzyme.MKV(f)
            #print('mkv.info: %s' % mp4video.info)

    #print (video_parser.getVideoDetails(video_path))

    #for k in result['snippet']:
        #print('result[snippet][%s] = %s\n' % (k, result['snippet'][k]))

#yt = YouTube("https://www.youtube.com/watch?v="+ids)
#yt = yt.get('mp4', '720p')
#yt.download('/video_download')

#YouTube("https://www.youtube.com/watch?v="+ids).streams.first().download('/video_download')

#Работа выполнена и сдана