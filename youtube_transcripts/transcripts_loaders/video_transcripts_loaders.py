from langchain_community.document_loaders import YoutubeLoader
from langchain_community.document_loaders.youtube import TranscriptFormat

def load_youtube_transcripts():
    try:
        # Load the transcript of a YouTube video
        yt_loader = YoutubeLoader(video_id="sVcwVQRHIc8", language=["en"], translation="en",
                                  transcript_format=TranscriptFormat.TEXT)

        # Get the transcript
        transcript = yt_loader.load()

        if transcript and len(transcript) > 0:
            return transcript

    except ImportError as ie:
        print(f"Import error: {ie}")
    except ValueError as ve:
        print(f"Value error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



__all__ = [load_youtube_transcripts]
