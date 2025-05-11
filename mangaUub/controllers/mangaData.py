import requests

BASE_URL = "https://api.mangadex.org/"

def getManga(title="", id=""):
    if (title != ""):
        try: 
            r = requests.get(f"{BASE_URL}/manga", params={"title": title, "order[rating]": "desc", "order[followedCount]": "desc", "limit": 10})
            
            mangaData = r.json()
            
            return mangaData
            
        except Exception as e: 
            print(f"An error occured: {e}")
    elif(id != ""):
        try: 
            r = requests.get(f"{BASE_URL}/manga/{id}")
            
            mangaData = r.json()
            
            return mangaData
            
        except Exception as e: 
            print(f"An error occured: {e}")

    else:
        try:
            r = requests.get(f"{BASE_URL}/manga", params={"order[rating]": "desc", "order[followedCount]": "desc", "limit": 5})
            
            mangaData = r.json()
            return mangaData
        
        except Exception as e:
            print(f"An error has occurred: {e}")
            
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
        
        
def getCover(id):
    if id:
        try: 
            r = requests.get(f"{BASE_URL}/cover/{id}")
            
            cover_data = r.json()
            
            
            
            return cover_data
        
        except Exception as e:
            print(f"An error has occurred: {e}")