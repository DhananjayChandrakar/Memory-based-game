import time, json
import numpy as np
import requests
from PIL import Image
from io import BytesIO


def pattern(x:str, y:int) -> str:
    print(x*y)

pattern("-", 20)
print("Welcome to the memory retention game.")
pattern("-", 20)
print()

print("Each image will pop up on your screen for two seconds.")
print("You've to input after that.")
time.sleep(2)

query = int(input("The number of images you want(1-100): "))

x = np.random.randint(1, 101, query)

images = []
images_count = []

with open("images.json", "r") as file:
    data = json.load(file)

for i in x:
    images.append(data[str(i)]["name"].lower())
    url = data[str(i)]["url"]
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img.show()
    time.sleep(2)
    img.close()

pattern("-", 20)
print("Now it's time to check your memory.")
pattern("-", 20)
print()

for i in range(1, query+1):
    chk = input(f"Name of the {i} image: ")
    if chk.lower() in images:
        images_count.append(chk)
    else:
        pass

pattern("-", 20)
print()

print(f"You got {len(images_count)}/{query} images right.")
