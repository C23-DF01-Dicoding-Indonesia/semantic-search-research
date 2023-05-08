from transformers import DPRContextEncoder, DPRContextEncoderTokenizer
import json
import os
from pyprojroot.here import here



def create_embedding_vector_modules(model, tokenizer):

    folder = here("data")
    file = os.path.join(folder, "modules_partition.json")
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        for i, each in enumerate(data):
            sentence = f'{each["title"]}. {each["content_only_text"]}'
            input_ids = tokenizer(sentence, return_tensors="pt").input_ids
            each["embedding_vector"] = model(input_ids).pooler_output.tolist()[0]
            print(f"Done {i+1} out of {len(data)}")
    with open(here("data_with_vector/modules_partition_with_vector.json"), "w", encoding="utf-8") as f:
        json.dump(data, f)


def create_embedding_vector_video(model, tokenizer):
    file = here("data/video_partition.json")
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
        for i, each in enumerate(data):
            sentence = each["caption"]
            input_ids = tokenizer(sentence, return_tensors="pt").input_ids
            each["embedding_vector"] = model(input_ids).pooler_output.tolist()[0]
            print(f"Done {i+1} out of {len(data)}")
    with open(here("data_with_vector/video_partition_with_vector.json"), "w", encoding="utf-8") as f:
        json.dump(data, f)

    



if __name__ == "__main__":
    tokenizer= DPRContextEncoderTokenizer.from_pretrained('firqaaa/indo-dpr-ctx_encoder-multiset-base')
    model = DPRContextEncoder.from_pretrained('firqaaa/indo-dpr-ctx_encoder-multiset-base')
    create_embedding_vector_modules(model, tokenizer)
    create_embedding_vector_video(model, tokenizer)

