import os
import shutil
import xmltodict
#کلاس های موجود در فایل های ما
Class = {"0": 0, "1": 1, "2": 2,"3": 3, "4": 4, "5": 5,"6": 6, "7": 7, "8": 8,"9": 9, "الف": 10, "ب": 11,"پ": 12, "ت": 13, "ث": 14,"ج": 15,
       "د": 16, "ز": 17, "ژ (معلولین و جانبازان)": 18,"س": 19, "ش": 20, "ص": 21, "ط": 22,
       "ع": 23, "ف": 24,"ق": 25,"ل": 26, "م": 27, "ن": 28,"و": 29, "ه‍": 30, "ی": 31}



#پوشه دیتای ورودی
images = 'E:/plate/not/test/test'



contents = os.listdir(images)
temp = []

for img in contents:
    temp = f'E:/plate/not/test/test/{img}'
    if 'xml' in temp:
        # پوشه خروجی لیبل ها 
        output_pass = 'E:/plate/yolo_plate_data/test/labels/'
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
        #پوشه خروجی تصاویر
        output_pass = 'E:/plate/yolo_plate_data/test/images/'
        shutil.copy(temp, output_pass)











