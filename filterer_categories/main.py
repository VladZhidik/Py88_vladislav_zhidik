import json

with open('/home/vladislav/PycharmProjects/pythonProject1/categories.json', 'r') as f:
    data = json.load(f)

    for i in data["Table"]:
        try:
            for j in i["Child"]:
                for a in j["Child"]:
                    if 'Child' in a:
                        with open('/home/vladislav/PycharmProjects/pythonProject1/filtered_categories.json', 'a') as f_w:
                            json.dump(a['Child'], f_w, ensure_ascii=False, indent=1)
                    else:
                        with open('/home/vladislav/PycharmProjects/pythonProject1/filtered_categories.json', 'a') as f_w:
                            json.dump(a, f_w, ensure_ascii=False, indent=1)
        except KeyError:
            with open('/home/vladislav/PycharmProjects/pythonProject1/filtered_categories.json', 'a') as f_w:
                json.dump(i, f_w, ensure_ascii=False, indent=1)
