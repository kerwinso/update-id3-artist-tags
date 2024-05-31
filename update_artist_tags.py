import os
from mutagen.easyid3 import EasyID3


def update_artist_field(file_path):
    try:
        # Load the MP3 file
        audio = EasyID3(file_path)
        # Check if the Artist field exists
        if 'artist' in audio:
            original_artist = audio['artist'][0]
            updated_artist = original_artist.replace('HCL', 'HCC')
            if original_artist != updated_artist:
                audio['artist'] = updated_artist
                audio.save()
                print(f"Updated Artist for {file_path}: '{original_artist}' -> '{updated_artist}'")
            if not original_artist.startswith('HC'):
                print(f"Metadata needs manual update for {file_path}")
        else:
            print(f"No artist metadata found in {file_path}")
    except Exception as e:
        print(f"Error updating {file_path}: {e}")


def update_artist_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.mp3'):
                file_path = os.path.join(root, file)
                update_artist_field(file_path)


if __name__ == '__main__':
    target_directory = '/Users/kerwin/Desktop/HCL to HCC'
    update_artist_in_directory(target_directory)
