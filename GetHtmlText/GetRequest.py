# https://lab.uwa4d.com/api/solution/projects/ids?categories[]=Unity&limit=24&skip=120&sort=update_time
import json
import requests


cur_num = 0
per_num = 100

final_res = []

for i in range(1, 70):
    rsp1 = requests.get(
        'https://lab.uwa4d.com/api/solution/projects/ids?categories[]=Unity&limit={num1}&skip{num2}&sort=update_time'.format(num1=per_num, num2=cur_num))

    final_url = 'https://lab.uwa4d.com/api/solution/projects?'
    rsp1Data = json.loads(rsp1.text)
    for item in rsp1Data["ids"]:
        final_url = final_url + 'ids[]=' + item+'&'

    rsp2 = requests.get(final_url)
    rsp2Data = json.loads(rsp2.text)

    for item in rsp2Data["projects"]:
        final_res.append(
            '- [{des}]({link})\n'.format(des=item["descCN"], link=item["project_link"]))

    cur_num = cur_num + per_num


with open("GetHtmlText/1111.md", "w", encoding="utf-8") as f:
    for item in final_res:
        f.write(item)
