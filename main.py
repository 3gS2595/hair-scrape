import json
from crawlers.donotresearch import donotresearch
from crawlers.finalhotdesert import finalhotdesert
from crawlers.soloshow import soloshow
from crawlers.undergroundflower import undergroundflower


with open('sample.json') as json_file:
    links = json.load(json_file)
    # Print the type of data variable
    print("Type:", type(links))
    for key in links:
        print(key)

    undergroundflower(links)
    soloshow(links)
    finalhotdesert(links)
    donotresearch(links)


json_object = json.dumps(links, indent=4)
with open("sample.json", "w", encoding="utf-8") as outfile:
    outfile.write(json_object)

with open("data.js", "w", encoding="utf-8") as outfile:
    outfile.write('export const data = [')
    for key in links:
        print(key)
        outfile.write("{\n")
        outfile.write("\"date\": \""+links[key][1]+"\",\n")
        outfile.write("\"title\": \""+links[key][0].replace("\"", "").replace("/", "")+"\",\n")
        outfile.write("\"url\": \""+key+"\",\n")
        outfile.write("},\n")
    outfile.write("]")
