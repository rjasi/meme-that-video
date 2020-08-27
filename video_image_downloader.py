import cv2
import pafy

# wrapper for cv2 so you can use contextmanager
class VideoImageDownloader:
    def __init__(self,  url, output_dir, start_timestamp, stop_timestamp):
        self.output_dir = output_dir
        self.url = url
        self.start_timestamp = start_timestamp
        self.stop_timestamps = stop_timestamp

    def __enter__(self):

        video = pafy.new(self.url).getbest(preftype="mp4")
        self.video_capture = cv2.VideoCapture(video.url)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.video_capture.release()
        cv2.destroyAllWindows()

    def process(self):
        if not self.video_capture.isOpened():
            raise Exception(f"Unable to open the video from {self.url}")

        counter = 0
        while (True):
            ret, frame = self.video_capture.read()

            if ret:
                cv2.imwrite(f'{self.output_dir}/frame_{counter}.jpg', frame)
            else:
                break

            # if q is pressed
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

            counter +=1
