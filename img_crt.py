from PIL import Image, ImageDraw, ImageFont


def list_tasks(text):
    """сортировка тасков по времени через концы строк со временем.
    если нет времени то ставится 12:00 по дефолту"""

    lines = text.split('/')
    task_dict = dict()
    used_nums = set()
    for line in lines:
        if len(line) >= 5:
            if line[-3] != ':':
                line += ' 12:00'
        else:
            line += ' 12:00'

        last_symbs = line[-5:]  # выдёргиваем из строчки время в формате 12:00
        while last_symbs in used_nums:
            line = line[:-1]
            line += str(int(last_symbs[-1]) + 1)
            last_symbs = line[-5:]
        used_nums.add(last_symbs)
        task_time = int(last_symbs[:2] + last_symbs[3:])  # время таска и ключ в словаре для сортировки
        task_dict[task_time] = line

    sorted_dict = dict(sorted(task_dict.items()))
    print(sorted_dict)
    res = ''
    for el in sorted_dict.values():
        res += el + '/'
    return res[:-1]


def img_crt(type_img, text):
    """создание изображения. тип_имг -- для будущего апдейта с разными плашками"""

    lines = list_tasks(text)
    lines = lines.split('/')
    num_lines = len(lines)
    if type_img == 'month':
        main_img = Image.open("img/month.png")
        idraw = ImageDraw.Draw(main_img)
        cur_size = int(203 / (num_lines + 1))
        font = ImageFont.truetype("Inter-V.ttf", size=cur_size)
        x_line = 224
        y_line = 189
        for line in lines:
            idraw.text((x_line, y_line), line.strip(), font=font, fill=(0, 0, 0, 255))
            y_line += cur_size + cur_size / num_lines
    elif type_img == 'day':
        # main_img = Image.open("img/day.png")
        pass
    main_img.save('img/res_month_img.png')


img_crt('month', 'first/second 15:00/6')

# print(list_tasks('first 12:00/sec 10:00'))

# def frame_chsn(day):
#     month_31 = ['январь', 'март', 'май', 'июль', 'август', 'октябрь', 'декабрь']
#     month_30 = ['апрель', 'июнь', 'сентябрь', 'ноябрь']
#     month_28 = ['февраль']
#
