import os
import sys
import time
import pyfiglet
from colorama import Fore, Style, init
from yt_dlp import YoutubeDL

# Initialize colorama
init(autoreset=True)

def print_banner():
    """Display a banner with ASCII art."""
    banner = pyfiglet.figlet_format("DWD")
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + "save any media")
    print(Fore.MAGENTA + "=" * 50)

def loading_effect():
    """Simulate a loading effect."""
    print(Fore.GREEN + "Preparing the downloader", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print("\n")

def download_video(url, output_folder="downloads"):
    """
    Download a video from the given URL using yt-dlp.

    Args:
        url (str): The URL of the video to download.
        output_folder (str): Folder to save the downloaded video.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    options = {
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'format': 'best',  # Download the best quality video
    }

    with YoutubeDL(options) as ydl:
        try:
            print(Fore.BLUE + "Downloading video...")
            ydl.download([url])
            print(Fore.GREEN + f"Video downloaded successfully to '{output_folder}'")
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

def main():
    print_banner()
    loading_effect()

    while True:
        print(Fore.CYAN + "Type 'exit' to quit.")
        url = input(Fore.YELLOW + "Enter video URL: ").strip()
        if url.lower() == "exit":
            print(Fore.RED + "Exiting the downloader. Goodbye!")
            sys.exit()

        output_folder = input(Fore.YELLOW + "Enter output folder (default: 'downloads'): ").strip() or "downloads"
        download_video(url, output_folder)

if __name__ == "__main__":
    main()