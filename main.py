import urllib.request, scrapetube
from bs4 import BeautifulSoup
from utilities.utils import clear, setup, title, formatter, output_result
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound


def channel_identifier(file):
    """
    finds channel id for each channel using the source code from youtube.
    though not reliable so im trying to find a better way...
    """
    clear()
    print("Gathering channel ID(s) from the selected  channel(s)")

    channel_id_list = []
    with open(file, "r") as channels:
        channels = channels.read().splitlines()
        for channel in channels:
            grab_link = urllib.request.urlopen(channel).read()
            soup = BeautifulSoup(grab_link, "html.parser")
            text = soup.prettify()

            channel_id = text.split('{"key":"browse_id","value":"')[1]
            channel_id = channel_id[0:24]
            channel_id_list.append(channel_id)
            print(channel_id)
    return channel_id_list


def fetch_videos(channels):
    """
    finds all videos from a specific youtube channel to later search for
    content - should get EVERY available video there is
    """
    all_videos = []
    for channel in channels: # finds all yt vid links for all channels
        clear()
        print('Hang on! Grabbing videos from selected channels')
        print(f'Current channel: {channel}')
        videos = scrapetube.get_channel(channel)
        for video in videos:
            all_videos.append(video['videoId'])
    return all_videos


def fetch_instances(videos_list):
    """
    finds all instances where desired content from specific yt channels
    has been mentioned - doesn't work on vids with turned off subtitles though
    """
    DEVIATION = 2 # changes how much is subtracted so it matches - in secs
    instances_found = []
    for index, video_id in enumerate(videos_list):
        clear()

        vl_len = len(videos_list)
        for msg in instances_found: 
            print(f'{msg}')
        print('---\n')
        print('Searching for instances from selected channels')
        print(f'Current video: {video_id}\nVideos left: {vl_len-index}')

        try: # statement used since no subtitles for a video crashes everything
            get_transcript = YouTubeTranscriptApi.get_transcript(video_id)
            transcript_split = str(get_transcript).split(", {")
            for transcript in transcript_split:
                for content in content_search:
                    if content in transcript.lower():
                        s, t = formatter(string=transcript, detour=DEVIATION)
                        yt_link = f"https://www.youtube.com/watch?v={video_id}"
                        msg = f"Text: {s}\nTimecode: {t}\nID: {yt_link}\n"
                        instances_found.append(msg)
                        if output_file: # outputs file to file if user wants it
                            output_result(msg, output_file)
        except TranscriptsDisabled or NoTranscriptFound:
            pass

        print('\n---\n\nDone!')


if __name__ == "__main__":
    clear()
    title("YouTube Transcript Searcher - github.com/oliver748")
    channel_ids, content_search, output_file = setup()
    channels = channel_identifier(channel_ids)
    videos_list = fetch_videos(channels)
    fetch_instances(videos_list)
