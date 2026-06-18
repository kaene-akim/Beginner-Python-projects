import os
from pydub import AudioSegment
from pydub.playback import play

music_path = "/home/akim/Testmusic"


# ==========================
# Helper Functions
# ==========================

def show_files():
    files = os.listdir(music_path)

    if not files:
        print("\nNo audio files found.\n")
        return []

    print("\nAvailable files:\n")

    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")

    return files


def choose_song():
    files = show_files()

    if not files:
        return None

    choice = input("\nEnter filename: ")

    if choice not in files:
        print("Song not found.")
        return None

    return choice


# ==========================
# Audio Player
# ==========================

def audio_play():

    choice = choose_song()

    if choice is None:
        return

    full_path = os.path.join(music_path, choice)

    song = AudioSegment.from_file(full_path)

    print(f"\nPlaying: {choice}\n")

    play(song)


# ==========================
# Batch MP3 -> WAV
# ==========================

def mp3_to_wav():

    converted = 0

    for file in os.scandir(music_path):

        if file.name.endswith(".mp3"):

            out_file = os.path.join(
                music_path,
                os.path.splitext(file.name)[0] + ".wav"
            )

            AudioSegment.from_file(file.path).export(
                out_file,
                format="wav"
            )

            print(f"Created {out_file}")

            converted += 1

    print(f"\nConverted {converted} file(s).\n")


# ==========================
# Batch WAV -> MP3
# ==========================

def wav_to_mp3():

    converted = 0

    for file in os.scandir(music_path):

        if file.name.endswith(".wav"):

            out_file = os.path.join(
                music_path,
                os.path.splitext(file.name)[0] + ".mp3"
            )

            AudioSegment.from_file(file.path).export(
                out_file,
                format="mp3"
            )

            print(f"Created {out_file}")

            converted += 1

    print(f"\nConverted {converted} file(s).\n")


# ==========================
# Single MP3 -> WAV
# ==========================

def song_mp3_to_wav():

    choice = choose_song()

    if choice is None:
        return

    if not choice.endswith(".mp3"):
        print("Please choose an MP3 file.")
        return

    full_path = os.path.join(music_path, choice)

    out_file = os.path.join(
        music_path,
        os.path.splitext(choice)[0] + ".wav"
    )

    AudioSegment.from_file(full_path).export(
        out_file,
        format="wav"
    )

    print(f"Created {out_file}")


# ==========================
# Single WAV -> MP3
# ==========================

def song_wav_to_mp3():

    choice = choose_song()

    if choice is None:
        return

    if not choice.endswith(".wav"):
        print("Please choose a WAV file.")
        return

    full_path = os.path.join(music_path, choice)

    out_file = os.path.join(
        music_path,
        os.path.splitext(choice)[0] + ".mp3"
    )

    AudioSegment.from_file(full_path).export(
        out_file,
        format="mp3"
    )

    print(f"Created {out_file}")


# ==========================
# Audio Slicer
# ==========================

def slice_audio():

    choice = choose_song()

    if choice is None:
        return

    start = float(input("Start time (seconds): "))
    end = float(input("End time (seconds): "))

    full_path = os.path.join(music_path, choice)

    song = AudioSegment.from_file(full_path)

    clip = song[int(start * 1000):int(end * 1000)]

    name, ext = os.path.splitext(choice)

    out_file = os.path.join(
        music_path,
        f"{name}_clip{ext}"
    )

    clip.export(
        out_file,
        format=ext[1:]
    )

    print(f"Created {out_file}")


# ==========================
# Menu
# ==========================

while True:

    menu = input(
        "\n"
        + "=" * 35 +
        "\n      AUDIO UTILITY\n"
        + "=" * 35 +
        "\n1. Play Audio"
        "\n2. Batch MP3 -> WAV"
        "\n3. Batch WAV -> MP3"
        "\n4. Single MP3 -> WAV"
        "\n5. Single WAV -> MP3"
        "\n6. Slice Audio"
        "\n7. Show Files"
        "\n8. Quit"
        "\n\nSelect option: "
    )

    if menu == "1":
        audio_play()

    elif menu == "2":
        mp3_to_wav()

    elif menu == "3":
        wav_to_mp3()

    elif menu == "4":
        song_mp3_to_wav()

    elif menu == "5":
        song_wav_to_mp3()

    elif menu == "6":
        slice_audio()

    elif menu == "7":
        show_files()

    elif menu == "8":
        print("\nGoodbye.\n")
        break

    else:
        print("\nInvalid option.\n")