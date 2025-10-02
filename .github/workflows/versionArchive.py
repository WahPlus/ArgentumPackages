import json
import os

os.chdir("/home/runner/work/ArgentumPackages/ArgentumPackages/")

agConfig = json.load(open("./ag2.json"))

for package in agConfig:
  if not os.path.isdir("./" + package + "-versions/"):
    os.mkdir("./" + package + "-versions/")
  versionsSaved = []
  for dirPath, dirNames, fileNames in os.walk("./" + package + "-versions/"):
    versionsSaved.extend(dirNames)
    break
    if agConfig[package]["version"] not in versionsSaved:
      print("Stinky!")
