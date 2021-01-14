# Anime Filter
### Nhóm:
* Dương Lê Tường Khang 18520882
* Bùi Đào Gia Huy 18520818
* Lã Trường Hải 18520698
## Hiệu ứng xây dựng trên OpenCV(file: anime_filter_bilateral.py)
Hướng dẫn sử dụng:

    python anime_filter_bilateral.py "image path"
  
 ## Hiệu ứng xây dựng trên mô hình animeGAN
 
 Tạo thư mục img:
  
    !mkdir img
 Tải ảnh vào thư mục img hoặc download:
  
    !mkdir img
    %cd 'img'
    !wget https://i.pinimg.com/originals/c2/a2/b7/c2a2b72d1e852146b3d539115c85f0fe.jpg
    %cd ..
Chuyển ảnh sang phong cách anime

    !python test.py --checkpoint_dir checkpoint/generator_Hayao_weight --test_dir /content/AnimeGAN/img --style_name H
