import json
from crawlers.donotresearch import donotresearch
from crawlers.finalhotdesert import finalhotdesert
from crawlers.soloshow import soloshow
from crawlers.textcrawler import textcrawler
from crawlers.undergroundflower import undergroundflower


with open('sample.json') as json_file:
    links = json.load(json_file)
    name_list = {}
    site_page_cnt = {}

    undergroundflower(links, name_list, site_page_cnt)
    soloshow(links, name_list, site_page_cnt)
    finalhotdesert(links, name_list, site_page_cnt)
    donotresearch(links, name_list, site_page_cnt)

json_object = json.dumps(links, indent=4)
with open("sample.json", "w", encoding="utf-8") as outfile:
    outfile.write(json_object)

with open("data.js", "w", encoding="utf-8") as outfile:
    outfile.write('export const data = [')
    for key in links:
        # print(key)
        outfile.write("{\n")
        outfile.write("\"date\": \""+links[key][1]+"\",\n")
        outfile.write("\"title\": \""+links[key][0].replace("\"", "").replace("/", "")+"\",\n")
        outfile.write("\"url\": \""+key+"\",\n")
        outfile.write("},\n")
    outfile.write("]")

with open("namesData.js", "w", encoding="utf-8") as outfile:
    outfile.write('export const namesData = [')
    for key in name_list:
        print(key + ": " + str(name_list[key]))
        outfile.write("{\n")
        outfile.write("\"name\": \"" + key + "\",\n")
        outfile.write("\"count\": \"" + str(name_list[key][0]) + "\",\n")
        urls = ""
        for url in name_list[key]:
            urls = urls + ", " + str(url)
        outfile.write("\"urls\": \"" + urls + "\",\n")
        outfile.write("},\n")
    outfile.write("]")

with open("sitesData.js", "w", encoding="utf-8") as outfile:
    outfile.write('export const sitesData = [')
    for key in site_page_cnt:
        print(key + ": " + str(site_page_cnt[key]))
        outfile.write("{\n")
        outfile.write("\"site\": \"" + key + "\",\n")
        outfile.write("\"count\": \"" + str(site_page_cnt[key]) + "\",\n")
        outfile.write("},\n")
    outfile.write("]")
