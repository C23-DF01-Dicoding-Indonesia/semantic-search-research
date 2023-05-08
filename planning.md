 schema  module
{
    "id": "0-116"
    "title": " ",
    content_html: " ", # buat show ke user
    content_md: " ", # search standar
    video : url
}


pecah modulenya jadi banyak bagian
{
    "id": "0-116"
    sub_id: "0-dst"
    "title": " ",
    sub_content_md_text_only: " " 
}

pecah modulenya jadi banyak bagian tapi video.
{
    "id": "0-116" # refer ke module mana
    sub_id: "0-dst" #  kita partisi videonya jadi segment, ini buat penanda segment mana
    "title": " ",  
    video_captions:  " "  #  textnya, bisa pakai speech to text
    time_stamp: " " # in seconds
    video : url+timestamp :D
}





