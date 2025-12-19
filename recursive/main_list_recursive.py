import os

# neden sade bir şekilde çözülemez ?
# file_list = os.listdir("/Users/mehmetbilen/Code")
# for i in file_list:
#     new_files = os.listdir(i)
#     for j in new_files:
#         new_new_files = os.listdir(j)
#         for k in new_new_files... 

def browse_files(start_path):
    file_list = os.listdir(start_path)
    for file_path in file_list:
        full_path = os.path.join(start_path,file_path)
        print("FilePath:",file_path,"\nFullPath:",full_path)
        if os.path.isfile(full_path):
            print(f"{file_path} bir dosyadır.")
        if os.path.isdir(full_path):
            print(f"{file_path} bir dizindir (klasördür).")
            browse_files(full_path)
        print("-"*50)

        


browse_files("/Users/mehmetbilen/Code")
# Ödev : 
# 1 - Sonuçların json'a kaydedilmesi
# 2 - Structured bir yapı kurulması
# 3 - filtreleme opsiyonu