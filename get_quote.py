import requests
import re
import pyttsx3

def get_bible(user_input):
    pattern = r"Quote me Book of (\w+(?: \w+)*) Chapter (\d+) and Verse (\d+)"
    match = re.match(pattern, user_input)

    if not match:
        return "Invalid input. Please use the format: 'Quote me Book of [Book Name] Chapter [Number] and Verse [Number]'."

    book, chapter, verse = match.groups()
    url = f"https://bible-api.com/{book.replace(' ', '+')}+{chapter}:{verse}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        verse_text = data['verses'][0]['text']
        return f"{data['reference']}: {verse_text}"
    else:
        return "Verse not found."

def speak_text(text):
    engine = pyttsx3.init(driverName='sapi5')
    engine.say(text)
    engine.runAndWait()

user_input = "Quote me Book of John Chapter 3 and Verse 16"
bible_quote = get_bible(user_input)
print(bible_quote)

if "Verse not found" not in bible_quote:
    speak_text(bible_quote)
