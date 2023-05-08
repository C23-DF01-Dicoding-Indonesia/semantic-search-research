import typesense
from pyprojroot.here import here



def connect_typesense():
    client = typesense.Client(
        {
            "api_key": "xyzy",
            "nodes": [
                {
                    "host": "localhost",
                    "port": "8108",
                    "protocol": "http",
                }
            ],
        }
    )

    return client


def populate_database_modules(client,jsonl_file):
    text_schema = {
        "name": "modules",
        "fields": [
            {"name": "modules_id", "type": "string"},
            {"name": "sub_id", "type": "string"},
            {"name": "title", "type": "string"},
            {"name": "content_only_text", "type": "string"},
            {"name": "embedding_vector", "type": "float[]", "num_dim": 768},

        ]
    }
    try:
        if client.collections['modules'].retrieve():
            client.collections['modules'].delete()
    except:
        pass

    client.collections.create(text_schema)
    with open(jsonl_file, "r", encoding="utf-8") as f:
        client.collections["modules"].documents.import_(f.read().encode('utf-8'), {'action': 'create'})
        print("Collection created")




def populate_database_video(client, file_jsonl):
    video_schema = {
        "name": "video",
        "fields": [
            {"name": "modules_id", "type": "string"},
            {"name": "sub_id", "type": "string"},
            {"name": "caption", "type": "string"},
            {"name": "time_start", "type": "string"},
            {"name":"video_with_time_start","type":"string"},
            {"name": "embedding_vector", "type": "float[]", "num_dim": 768}
        ]
    }


    try:
        if client.collections['video'].retrieve():
            client.collections['video'].delete()
    except:
        pass
            

    client.collections.create(video_schema)
    with open(file_jsonl, "r", encoding="utf-8") as f:
        client.collections["video"].documents.import_(f.read().encode('utf-8'), {'action': 'create'})
        print("Collection created")

    return client 


if __name__ == "__main__":
    client = connect_typesense()
    module_file = here("data_with_vector_jsonl/modules_partition_with_vector.jsonl")
    video_file = here("data_with_vector_jsonl/video_partition_with_vector.jsonl")
    populate_database_modules(client, module_file)
    populate_database_video(client, video_file)

    print(client.collections['modules'].retrieve())
    print(client.collections['video'].retrieve())