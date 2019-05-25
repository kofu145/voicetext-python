# voicetext-python
A Python API wrapper for the Japanese text to speech service voicetext (https://cloud.voicetext.jp/webapi)

## How to use:

First, you'll have to get an API_KEY from: https://cloud.voicetext.jp/webapi/api_keys/new

In your code, create a voice_text object:
```
tts = voicetext(API_KEY="MY_API_KEY", text="こんにちは")
```

Then, you can call two methods:
```get_tts_file``` creates a WAV file (will be different if you specified a file_format) 
```write_tts_to``` writes to a specified file

## Examples:
When you're playing sound directly:
```
from voicetext import *
from io import BytesIO

audio = "こんにちは"
my_file = BytesIO()
tts = voice_text(API_KEY="YOUR_API_KEY", text=audio)
tts.write_tts_to(my_file)
# Load my_file, and then use a library to play it (there are many you can use, such as pygame's mixer)
```
When you're creating a file and playing sound from it:
```
from voicetext import *

audio = "こんにちは"
tts = voice_text(API_KEY="YOUR_API_KEY", text=audio)
tts.get_tts_file("audio.wav")
# Now there will be an "audio.wav" file in the working directory, use a library to play it
```
