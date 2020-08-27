
import argparse
from video_image_downloader import VideoImageDownloader

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='A tool to download frames of videos')
    parser.add_argument("--output_dir", help="Where to save the images")
    parser.add_argument("--url", help="url of video")
    parser.add_argument("--start_timestamp", help="Where to start in video")
    parser.add_argument("--stop_timestamp", help="Where to stop in video")

    args = parser.parse_args()

    with VideoImageDownloader(args.url, args.output_dir, args.start_timestamp, args.stop_timestamp) as video:
        video.process()

    print("Finished!")
