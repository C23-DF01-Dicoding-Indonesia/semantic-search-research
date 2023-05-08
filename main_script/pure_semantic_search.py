import typesense
from transformers import DPRContextEncoder, DPRContextEncoderTokenizer



def connect_typesense():
    client = typesense.Client({
        'nodes': [{
            'host': 'localhost',  # For Typesense Cloud use xxx.a1.typesense.net
            'port': '8108',       # For Typesense Cloud use 443
            'protocol': 'http'    # For Typesense Cloud use https
        }],
        'api_key': 'xyzy', # For Typesense Cloud use the API key obtained from the dashboard
    })
    return client


def search(client, model, tokenizer):
    which_collection = input("Search in modules or video? (m/v) ")
    collection =""
    if which_collection == "m":
        collection = "modules"
    elif which_collection == "v":
        collection = "video"
    v_query = input("Enter query: ")
    input_ids = tokenizer(v_query, return_tensors="pt")["input_ids"]
    outputs = model(input_ids).pooler_output.tolist()[0]
    top_k = int(input("Enter top k: "))
    search_requests = {
        "searches": [
            {
                "collection": collection,
                "q": '*',
                "vector_query": f"embedding_vector:({outputs})",
                "per_page": top_k,
            }
        ]
    }
    common_params = {}

    search_result = client.multi_search.perform(search_requests, common_params)
    
    if which_collection == "m":
        print("Search result for modules")
        for result in search_result['results'][0]['hits']:
            # create result folder and find relevant modules in content_modules
            print(result['document']['title'])
            print(result['document']['content_only_text'])
            print(result['document']['modules_id'])
            print("====================================")

    elif which_collection == "v":
        print("Search result for video")
        for result in search_result['results'][0]['hits']:
            # create result folder and find relevant modules in content_modules
            print(result['document']['caption'])
            print(result['document']['video_with_time_start'])
            print(result['document']['modules_id'])
            print("====================================")




def search_full_text(client):
    which_collection = input("Search in modules or video? (m/v) ")
    collection =""
    if which_collection == "m":
        collection = "modules"
        query_by = "content_only_text"
    elif which_collection == "v":
        collection = "video"
        query_by = "caption"
    
    v_query = input("Enter query: ")
    top_k = int(input("Enter top k: "))
    search_params = {
        "q": v_query,
        "query_by": query_by,
        "per_page": top_k,
    }
    search_result = client.collections[collection].documents.search(search_params)

    if which_collection == "m":
        print("Search result for modules")
        for result in search_result['hits']:
            # create result folder and find relevant modules in content_modules
            print(result["document"]['title'])
            print(result["document"]['content_only_text'])
            print(result["document"]['modules_id'])
            print("====================================")

    elif which_collection == "v":
        print("Search result for video")
        for result in search_result['hits']:
            # create result folder and find relevant modules in content_modules
            print(result["document"]['caption'])
            print(result["document"]['video_with_time_start'])
            print(result["document"]['modules_id'])
            print("====================================")





if __name__ == "__main__":
    client = connect_typesense()
    search_again = True
    tokenizer= DPRContextEncoderTokenizer.from_pretrained('firqaaa/indo-dpr-ctx_encoder-multiset-base')
    model = DPRContextEncoder.from_pretrained('firqaaa/indo-dpr-ctx_encoder-multiset-base')
    while search_again:
        search_type = input("Semantic search or full text search? (s/f) ")

        if search_type == "s":
            search(client, model,tokenizer)
        elif search_type == "f":
            search_full_text(client)
        search_again = input("Search again? (y/n) ") == "y"


    
