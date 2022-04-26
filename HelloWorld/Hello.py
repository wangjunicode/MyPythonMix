
import json
import os

def resolveJson(path):
	file = open(path, "rb")
	fileJson = json.load(file)

	return fileJson["trunk_path"], fileJson["branch_path"]


path = "ProjPathConfig.json"

trunk_path, branch_path = resolveJson(path)

print(trunk_path)
print(branch_path)