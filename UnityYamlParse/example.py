from unityparser import UnityDocument

# Loading and modifying a config file with a single YAML document
# project_settings_file = 'TestUIBindingViewLua.prefab'
# doc = UnityDocument.load_yaml(project_settings_file)
# ProjectSettings = doc.entry
# ProjectSettings.scriptingDefineSymbols[1] += ';CUSTOM_DEFINE'
# ProjectSettings.scriptingDefineSymbols[7] = ProjectSettings.scriptingDefineSymbols[1]
# doc.dump_yaml()

# You can also load YAML files with multiple documents and filter for a single or multiple entries
hero_prefab_file = 'TestUIBindingViewLua.prefab'
doc = UnityDocument.load_yaml(hero_prefab_file)
# print(doc.entries)
# print(doc.entry)

entries = doc.filter(class_names=('MonoBehaviour',), attributes=('BindItems',))
for entry in entries:
    # print(entry.BindItems)
    for item in entry.BindItems:
        print(item.__root)
    break
