import cv2
import pafy


class VideoImageDownloader:
    """
     A wrapper around cv2 so you can use contextmanager
     for better resource management

     Usage:
        with VideoImageDownloader(args.url, args.output_dir, args.start_timestamp, args.stop_timestamp) as video:
            video.process()

    """

    def __init__(self,  url, output_dir, start_timestamp, stop_timestamp):
        self.output_dir = output_dir
        self.url = url
        self.start_timestamp = start_timestamp
        self.stop_timestamps = stop_timestamp


    def __enter__(self):
        """
            Used by contextmanager
            Creates the video capture object from opencv
        """

        video = pafy.new(self.url).getbest(preftype="mp4")
        self.video_capture = cv2.VideoCapture(video.url)
        return self


    def __exit__(self, exc_type, exc_val, exc_tb):
        """
            Clean up
        """

        self.video_capture.release()

        # unsure of the exact behaviour of this, potentially move it out later
        cv2.destroyAllWindows()

    def process(self):
        """
            Loop through the entire video and save each frame
        """

        if not self.video_capture.isOpened():
            raise Exception(f"Unable to open the video from {self.url}")

        counter = 0
        while (True):
            ret, frame = self.video_capture.read()

            if ret:
                # TODO handle error for writes 
                cv2.imwrite(f'{self.output_dir}/frame_{counter}.jpg', frame)
            else:
                break

            # if q is pressed
            if cv2.waitKey(20) & 0xFF == ord('q'):
                break

            counter +=1
