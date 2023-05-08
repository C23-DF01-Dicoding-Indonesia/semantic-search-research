# for each file in data_with_vector folder convert to jsonl and save in data_with_vector_jsonl folder

for file in data_with_vector/*.json
do
    echo "Converting $file to jsonl"
    jq -c '.[]' $file > data_with_vector_jsonl/$(basename $file .json).jsonl
done