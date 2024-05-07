import os
import shutil
import xmltodict
from PIL import Image

# کلاس‌های موجود در فایل‌های ما
Class = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "الف": 10, "ب": 11, "پ": 12,
         "ت": 13, "ث": 14, "ج": 15,
         "د": 16, "ز": 17, "ژ (معلولین و جانبازان)": 18, "س": 19, "ش": 20, "ص": 21, "ط": 22, "ع": 23, "ف": 24, "ق": 25,
         "ل": 26, "م": 27, "ن": 28, "و": 29, "ه‍": 30, "ی": 31}

# پوشه دیتای ورودی
input_dir = 'E:/plate/not/train/x'
# پوشه خروجی برای لیبل‌ها
output_labels_dir = 'E:/plate/yolo_plate_data/train/labels'
# پوشه خروجی برای تصاویر
output_images_dir = 'E:/plate/yolo_plate_data/train/images'


# ایجاد پوشه‌های خروجی اگر وجود نداشته باشند
os.makedirs(output_labels_dir, exist_ok=True)
os.makedirs(output_images_dir, exist_ok=True)

contents = os.listdir(input_dir)

for item in contents:
    file_path = os.path.join(input_dir, item)

    if 'jpg' in file_path:
        shutil.copy(file_path, output_images_dir)
        # باز کردن تصویر و استخراج ابعاد
        image = Image.open(file_path)
        image_width, image_height = image.size

    elif 'xml' in file_path:
        with open(file_path, encoding='utf-8') as xml_file:
            xml_data = xml_file.read()

            dict_data = xmltodict.parse(xml_data)

            # ایجاد فایل لیبل با نام متناظر تصویر
            txt_filename = os.path.splitext(item)[0] + '.txt'
            txt_filepath = os.path.join(output_labels_dir, txt_filename)

            with open(txt_filepath, 'w', encoding='utf-8') as txt_file:
                for obj in dict_data['annotation']['object']:
                    class_name = obj['name']
                    xmin = float(obj['bndbox']['xmin'])
                    ymin = float(obj['bndbox']['ymin'])
                    xmax = float(obj['bndbox']['xmax'])
                    ymax = float(obj['bndbox']['ymax'])

                    # محاسبه مرکز و ابعاد bounding box
                    x_center = (xmin + xmax) / 2
                    y_center = (ymin + ymax) / 2
                    box_width = xmax - xmin
                    box_height = ymax - ymin

                    # نرمالایز کردن مختصات
                    x_center_normalized = x_center / image_width
                    y_center_normalized = y_center / image_height
                    box_width_normalized = box_width / image_width
                    box_height_normalized = box_height / image_height

                    # نوشتن مختصات به فایل لیبل
                    txt_file.write(
                        f"{Class[class_name]} {x_center_normalized} {y_center_normalized} {box_width_normalized} {box_height_normalized}\n")

