import requests

BASE_URL = "https://api.mangadex.org/"

def getManga(title):
    if (title != ""):
        try: 
            r = requests.get(f"{BASE_URL}manga?title={title}")
            
            mangaData = r.json()
            
            return mangaData
            
        except Exception as e: 
            print(f"An error occured: {e}")


def getChapters(id):
    try:
        r = requests.get(f"{BASE_URL}/manga/{id}/feed")

        chapters = []
        
        for chapter in r.json()["data"]:
            lang = chapter["attributes"]["translatedLanguage"]
            if lang == "pt-br" or lang:
                chapters.append(chapter["id"])
            
        return chapters
    
    except Exception as e:
        print(f"An error occured: {e}")