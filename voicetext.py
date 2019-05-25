import requests
url = "https://api.voicetext.jp/v1/tts"

# Errors:
class textVoiceError(Exception):
	"""Error with API request"""
	pass


class fileFormatError(Exception):
	"""Invalid file format"""
	pass


class voice_text:
	def __init__(self, API_KEY, text, speaker="hikari", file_format="wav", emotion="happiness", emotion_level=2, pitch=100, speed=100, volume=100):
		self.API_KEY=API_KEY
		self.payload = {
			"text" : text,
			"speaker" : speaker,
			"format" : file_format,
			"emotion" : emotion,
			"emotion_level" : emotion_level,
			"pitch" : pitch,
			"speed" : speed,
			"volume" : volume
		}

	def get_tts_file(self, filename):
		if filename.endswith((".wav",".mp3",".ogg")):
			pass
		else:
			raise fileFormatError("Not a valid file format!")

		try:
			tts_response = requests.post(url, params=self.payload, auth=(self.API_KEY, ''))
		except requests.exceptions.HTTPError:
			raise textVoiceError("Post request failed!")
		f = open(filename, "wb")
		f.write(tts_response.content)
		f.close()

	def write_tts_to(self, file):

		try:
			tts_response = requests.post(url, params=self.payload, auth=(self.API_KEY, ''))
		except requests.exceptions.HTTPError:
			raise textVoiceError("Post request failed!")

		file.write(tts_response.content)
