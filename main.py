import argparse
from pytube import YouTube

def main():
    parser = argparse.ArgumentParser(description="Convert youtube URL to MP4")
    parser.add_argument('-URL', type=str, required=True,
                        help="URL of video to download.")
    parser.add_argument('-dest', type=str, required=True,
                        help="location of saved video.")
    args = parser.parse_args()

    video = YouTube(args.URL)
    itag_highest_resolution = video.streams.filter(file_extension="mp4").get_highest_resolution().itag
    stream = video.streams.get_by_itag(itag_highest_resolution)
    stream.download(output_path=args.dest)





if __name__ == "__main__":
    main()