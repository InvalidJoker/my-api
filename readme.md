# Invalid API
Hier findest du den Source Code zu meiner Invalid API (früher Gradient API). Diese kann Farbverläufe erstellen ohne etwas dafür zu bezahlen. Die API ist Open Source und kann von jedem verwendet werden. Ich würde mich über einen Credit freuen.

## Setup
1. Installiere dir Python 3.10
2. Installiere dir alle Dependencies mit `pip install -r requirements.txt`
3. Starte die API mit `python main.py`
4. Profitiere von der API

## Example
```py
import aiohttp
import asyncio

width = 1280
height = 30

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    async def main():
        async with aiohttp.ClientSession() as session:
            async with session.post("http://localhost:8080/gradient", json={"colors": ['#FFFFFF', '#00FF00', '#0000FF'], "width": width, "height": height}) as resp:
                if resp.status != 200:
                    print("Error")
                
                img = await resp.read()
                
        with open("test.png", "wb") as f:
            f.write(img)
    
    loop.run_until_complete(main())
```
Viel Spaß 💝