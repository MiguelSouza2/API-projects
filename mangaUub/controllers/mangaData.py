import requests

BASE_URL = "https://api.mangadex.org/"

def getManga(title):
    if (title != ""):
        try: 
            r = requests.get(f"{BASE_URL}/manga", params={"title": title, "order[rating]": "desc", "order[followedCount]": "desc"})
            
            mangaData = r.json()
            
            return mangaData
            
        except Exception as e: 
            print(f"An error occured: {e}")


def getChapters(id):
    try:
        r = requests.get(f"{BASE_URL}/manga/{id}/feed", params={"translatedLanguage[]":["pt-br", "en"], "order[chapter]": "asc"})

        chapters = []
        
        for chapter in r.json()["data"]:
            chapters.append([chapter["attributes"]["title"], chapter["id"]])
            
        return chapters
    
    except Exception as e:
        print(f"An error occured: {e}")
        


def getChapterImage(chapter_id):
    try:
        r = requests.get(f"{BASE_URL}/at-home/server/{chapter_id}")
        
        chapter_data = r.json()
        return chapter_data
    
    except Exception as e:
        print(f"An error has occured: {e}")