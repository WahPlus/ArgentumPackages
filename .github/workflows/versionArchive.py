import json
import os
import shutil

os.chdir("/home/runner/work/ArgentumPackages/ArgentumPackages/")

with open("./ag2.json") as f:
  agConfig = json.load(f)

for package in agConfig:
  if not os.path.isdir("./" + package + "-versions/"):
    os.mkdir("./" + package + "-versions/")
  versionsSaved = []
  for dirPath, dirNames, fileNames in os.walk("./" + package + "-versions/"):
    versionsSaved.extend(dirNames)
    break
  if agConfig[package]["version"] not in versionsSaved:
    currentVersionDir = "./" + package + "-versions"
    with open(currentVersionDir + "/ag2.json", "w") as f:
      json.dump({"package": agConfig[package]}, f, sort_keys=True, indent=4)
    if "directories" in agConfig[package]:
      for i in agConfig[package]["directories"]:
        os.mkdir(os.path.join(currentVersionDir, i))
    if "files" in agConfig[package]:
      for i in agConfig[package]["files"]:
        shutil.copyfile(os.path.join("./", i), os.path.join(currentVersionDir, i))
