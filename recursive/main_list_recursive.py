import os
import json
import pandas

# neden sade bir şekilde çözülemez ?
# file_list = os.listdir("/Users/mehmetbilen/Code")
# for i in file_list:
#     new_files = os.listdir(i)
#     for j in new_files:
#         new_new_files = os.listdir(j)
#         for k in new_new_files... 

def browse_files(start_path, filter):
    file_list = os.listdir(start_path)
    founded = {}
    for file_path in file_list:
        full_path = os.path.join(start_path,file_path)

        if os.path.isfile(full_path):
            if filter in full_path:
                founded[file_path] = "File"
        if os.path.isdir(full_path):
            founded[file_path] = browse_files(full_path,filter)
    return founded
        


result = browse_files("/Users/mehmetbilen/Code",".docx")
with open("file_structure.json","w") as dosya:
    json.dump(result, dosya)


pass

# Ödev : 
# 1 - Sonuçların json'a kaydedilmesi
# 2 - Structured bir yapı kurulması
# 3 - filtreleme opsiyonu