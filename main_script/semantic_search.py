 




def search(model,tokenzier, modules, video):
    query = input("Enter query: ")
    input_ids = tokenizer(query, return_tensors="pt")["input_ids"]
    v_query = model().pooler_output.tolist()[0]
    top_k = int(input("Enter top k: "))





if __name__ == "__main__":
    search_again = True
    tokenizer= DPRContextEncoderTokenizer.from_pretrained('firqaaa/indo-dpr-ctx_encoder-multiset-base')
    model = DPRContextEncoder.from_pretrained('firqaaa/indo-dpr-ctx_encoder-multiset-base')

    with open(here("data_with_vector/modules_partition_with_vector.json"), "r") as f:
        modules = json.load(f)
        #convert to dataframe
        modules = pd.DataFrame(modules)
    with open(here("data_with_vector/video_partition_with_vector.json"), "r") as f:
        video = json.load(f)
        #convert to dataframe
        video = pd.DataFrame(video)

    print("Modules: ", modules.shape)
    print("Video: ", video.shape)
    print(modules.info())
    print(video.info())
          
    while search_again:
        break
        search(model, tokenizer,modules, video)
        search_again = input("Search again? (y/n) ") == "y"