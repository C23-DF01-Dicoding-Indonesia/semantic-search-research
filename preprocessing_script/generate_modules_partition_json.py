from pyprojroot.here import here
import os
import json
import re


def generate_modules_partition_json():
    file_updated_json = here("data/modules_updated.json")
    list_to_create_json = []
     
    with open(file_updated_json, "r", encoding="utf-8") as f:
        data = json.load(f)

        for i, each_module in enumerate(data):
            # partition the content into 500 words each

            text_list = each_module["content_only_text"].split(" ")
            for j,k in enumerate(range(0, len(text_list), 100)):

                

                if k+100 > len(each_module["content_only_text"]):
                    list_to_create_json.append({
                        "modules_id": str(i) ,
                        "sub_id": str(j),
                        "title": each_module["title"],
                        "content_only_text": " ".join(text_list[k:]),
                    })
                else:
                    list_to_create_json.append({
                        "modules_id": str(i),
                        "sub_id": str(j),
                        "title": each_module["title"],

                        "content_only_text": " ".join(text_list[k:k+100]),
                    })

    with open(here("data/modules_partition.json"), "w", encoding="utf-8") as f:
        json.dump(list_to_create_json, f, indent=4, ensure_ascii=False)


        
if __name__ == "__main__":
    generate_modules_partition_json()
