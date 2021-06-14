import json
import os 
from os import path
import urllib.request


def download_tracks(previews):
    for key in previews:
        if key == 'schubert':
            id = 0
            audio_dir = "./"+ key + "/"
            print(audio_dir)
            if not path.exists(audio_dir):
                os.mkdir(audio_dir)
            for p in previews[key]:
                id += 1
                preview = urllib.request.urlretrieve(p, audio_dir + "{0:0=3d}".format(id) + '.mp3')

if __name__ == "__main__":

    preview_file = "./previews.json"
    with open(preview_file, 'r') as p: 
        previews = json.load(p)
    download_tracks(previews)