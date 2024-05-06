import os
import shutil
import xmltodict
#کلاس های موجود در فایل های ما
Class = {"0": 0, "1": 1, "2": 2,"3": 3, "4": 4, "5": 5,"6": 6, "7": 7, "8": 8,"9": 9, "الف": 10, "ب": 12,"پ": 13, "ت": 14, "ث": 15,"ج": 16, "چ": 17, "ح": 18,
       "خ": 19, "د": 20, "ذ": 21,"ر": 22, "ز": 23, "ژ (معلولین و جانبازان)": 24,"س": 25, "ش": 26, "ص": 27,"ض": 28, "ط": 29, "ظ": 30,"ع": 31, "غ": 32, "ف": 33,"ق": 34, "ک": 35, "گ": 36,
       "ل": 37, "م": 38, "ن": 39,"و": 40, "ه‍": 41, "ی": 42}

#پوشه دیتای ورودی
images = 'E:/plate/train/x'
#پوشه خروجی
output_pass = 'E:/plate/train2/'

contents = os.listdir(images)
temp = []

for img in contents:
    temp = f'E:/plate/train/x/{img}'
    if 'xml' in temp:
        with open(temp, encoding='utf-8') as xml_file:
            xml_data = xml_file.read()

            dict_data = xmltodict.parse(xml_data)

            for item in dict_data['annotation']['object']:
                for i in Class.keys():
                    if item['name'] == i:
                        item['name'] = Class[i]

            txt_filename = f'{output_pass}' + os.path.splitext(img)[0] + '.txt'
            txt_filepath = os.path.join(txt_filename)
            with open(txt_filepath, 'w', encoding='utf-8') as txt_file:
                for item in dict_data['annotation']['object']:
                    for i in Class.keys():
                        if item['name'] == i:
                            item['name'] = str(Class[i])
                    txt_file.write(
                        f"{item['name']} {float(item['bndbox']['xmin'])} {float(item['bndbox']['ymin'])} {float(item['bndbox']['xmax'])} {float(item['bndbox']['ymax'])}\n")

    elif 'jpg' in temp:
        shutil.copy(temp, output_pass)











