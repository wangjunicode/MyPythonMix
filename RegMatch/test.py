
import json
import os
import re
from unittest import result

fold_path = "G:\KiHan\Assets\Resources\UILua\ActCenter"


def create_file(file_path, file_content):
    if os.path.exists(file_path):
        pass
        os.remove(file_path)

    with open(file_path, 'w') as f:
        f.write(file_content)


def get_config(prefab_path):
    # print(prefab_path)
    # prefab_path = 'TestUIBindingViewLua.prefab'
    line = open(prefab_path).read()

    pattern0 = re.compile(
        '''m_Script: {fileID: 11500000, guid: 48d58ada50d7a6c47b06cab3ca877077, type: 3}''')
    result0 = pattern0.findall(line)
    if not result0:
        return

    # print(line)
    pattern1 = re.compile('''- ItemName: (.*)
        ItemType: (.*)
        ItemTargets:
    (.*)\n(.*)\n''')
    result1 = pattern1.findall(line)

    pattern2 = re.compile(
        '''chunkName: (.*)''')
    result2 = pattern2.findall(line)
    if not result2:
        return

    script_path = (result2[0].split('/'))
    script_path = script_path[len(script_path) - 1]

    final_result = []

    for item in result1:
        temp = []
        for _ in item:
            temp.append(_)

        final_result.append(temp)

    for item in final_result:
        if "fileID" in item[3]:
            item[1] = item[1] + "[]"
        item.pop(3)
        item.pop(2)

    data1 = json.dumps(final_result, sort_keys=True,
                       indent=4, separators=(',', ': '))

    # print(data1)
    # print(data2)

    print(prefab_path)
    print(script_path)
    create_file('config/' + script_path + ".json", data1)
    # open("data.json", 'w').write(data2)


def getListOfFiles(dirName):
    listOfFile = os.listdir(dirName)
    allFiles = list()
    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            if entry.endswith(".prefab"):
                allFiles.append(fullPath)

    return allFiles


def main():
    mAllPrefabList = list()
    mAllPrefabList = getListOfFiles(fold_path)
    for item in mAllPrefabList:
        pass
        get_config(item)


if __name__ == '__main__':
    main()
