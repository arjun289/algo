"""
Basic Video exporting example for factory pattern
"""
from abc import ABC, abstractmethod
import pathlib


################ Video Exporter ######################
class VideoExporter(ABC):
    """
    Basic representation of video exporting codec.
    """

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares video data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the video data to the folder."""


class LosslessVideoExporter(VideoExporter):
    """Lossless video exporting codec."""

    def prepare_export(self, video_data):
        print("Prepare video data for lossless export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in lossless format to {folder}")


class H264BPVideoExporter(VideoExporter):
    """ H.264 video exporting codec with Baseline Profile."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Baseline) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Baseline) format to {folder}")


class H264Hi422PVideoExporter(VideoExporter):
    """ H.264 video exporting codec with Hi422P Profile (10-bit, 4:2:2 chroma sampling) ."""

    def prepare_export(self, video_data):
        print("Preparing video data for H.264 (Hi422P) export.")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting video data in H.264 (Hi422P) format to {folder}")

################## Audio Exporter #######################

class AudioExporter(ABC):
    """Basic representation of audio exporting codec."""

    @abstractmethod
    def prepare_export(self, video_data):
        """Prepares audio data for exporting."""

    @abstractmethod
    def do_export(self, folder: pathlib.Path):
        """Exports the audio data to the folder."""


class AACAudioExporter(AudioExporter):
    """ AAC Audio exporting codec"""

    def prepare_export(self, video_data):
        print("Preparing to export audio AAC export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in AAC format to {folder}")


class WAVAudioExporter(AudioExporter):
    """ WAV Audio exporting codec"""

    def prepare_export(self, video_data):
        print("Preparing to export audio WAV export")

    def do_export(self, folder: pathlib.Path):
        print(f"Exporting audio data in WAV format to {folder}")


#################### Factories ########################

class ExporterFactory(ABC):
    """
    Factory that represents a combination of audio and video codecs.
    The factory doesn't maintain any of the instances it creates.
    """

    @abstractmethod
    def get_video_exporter():
        "Returns a video exporter"

    @abstractmethod
    def get_audio_exporter():
        "Returns an audio exporter"

class FastExporter(ExporterFactory):
    "Factory aimed at providing high speed, low quality export."
    
    def get_video_exporter(self):
        return H264BPVideoExporter()

    def get_audio_exporter(self):
        return AACAudioExporter()

class HighQualityExporter(ExporterFactory):
    """Factory aimed at providing slow speed, high quality export."""

    def get_video_exporter(self):
        return H264Hi422PVideoExporter()

    def get_audio_exporter(self):
        return AACAudioExporter()


class MasterQualityExporter(ExporterFactory):
    """ Default factory aimed at slower speed, master quality export"""

    def get_video_exporter(self):
        return LosslessVideoExporter()

    def get_audio_exporter(self):
        return WAVAudioExporter()


def read_exporter() -> ExporterFactory:

    export_options = {
        "low": FastExporter(),
        "high": HighQualityExporter(),
        "master": MasterQualityExporter()
    }

    while True:
        export_quality = input("Enter desired output quality (low, high, master): ")
        if export_quality in export_options:
            break
        print(f"Unknown output quality option: {export_quality}." )

    return export_options[export_quality]

########### main function ############

def main() -> None:
    exporter = read_exporter()

    video_exporter = exporter.get_video_exporter()
    audio_exporter = exporter.get_audio_exporter()

    # prepare the export
    video_exporter.prepare_export("placeholder_for_video_data")
    audio_exporter.prepare_export("placeholder_for_audio_data")

    # do the export 
    folder = pathlib.Path("./exports")
    video_exporter.do_export(folder)
    audio_exporter.do_export(folder)


if __name__ == "__main__":
    main()
