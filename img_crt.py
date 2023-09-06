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
        cur_size = 203 // (num_lines + 1)  # размер шрифта
        for i in range(len(lines)):
            line = lines[i]
            need_len = cur_size // 3
            if need_len >= len(line):
                # без переноса. всё вмещается

                new_line = line + '\n'
            else:
                num_lines += 1
                if (len(line) - need_len) <= 5:
                    # перенос времени

                    new_line = line[:-5].strip() + '\n' + line[-5:].strip() + '\n'
                else:
                    # некрасивый пока что перенос по символам в строчке

                    new_line = line[:-len(line) + need_len].strip() + '\n' + line[-(
                            len(line) - need_len):].strip() + '\n'
                if i == len(lines) - 1:
                    new_line = new_line[:-1]
            lines[i] = new_line
        cur_size = 203 // (num_lines + 1)
        font = ImageFont.truetype("Inter-V.ttf", size=cur_size)
        x_line = 224
        y_line = 189

        res_text = ''.join(lines)
        idraw.text((x_line, y_line), res_text, font=font, fill=(0, 0, 0, 255))  # пишет в ячейку

        # обработка и вывод текста отдельно по строчкам (изначальный вариант).
        # было принято решение внутри одного текста менять строчки, но не разделять их и не выводить отдельно

        # for line in lines:
        #     # print(238 // cur_size)
        #     # if 238 * 2 // cur_size <= len(line):
        #     #     cur_size -= 5
        #     # else:
        #     #     cur_size = int(203 / (num_lines + 1))
        #     #     print(line, 'DONE')
        #     # print(line, cur_size)
        #
        #     need_len = cur_size // 5
        #     print(need_len, len(line))
        #     if need_len <= len(line):
        #         idraw.text((x_line, y_line), line.strip(), font=font, fill=(0, 0, 0, 255))  # пишет в ячейку
        #         y_line += cur_size + cur_size / num_lines  # коорд новой строчки по оси игрек
        #     else:
        #         if (len(line) - need_len) <= 5:
        #             idraw.text((x_line, y_line), line[:5].strip(), font=font, fill=(0, 0, 0, 255))  # пишет в ячейку
        #             y_line += cur_size + cur_size / num_lines  # коорд новой строчки по оси игрек
        #             idraw.text((x_line, y_line), line[-5:].strip(), font=font, fill=(0, 0, 0, 255))  # пишет в ячейку
        #             num_lines += 1
    elif type_img == 'day':
        # main_img = Image.open("img/day.png")
        pass
    main_img.save('img/res_month_img.png')


img_crt('month', 'первое 10:00/дз/обнять алиночку 13:00/мрмяу 13:45')

# print(list_tasks('first 12:00/sec 10:00'))

# def frame_chsn(day):
#     month_31 = ['январь', 'март', 'май', 'июль', 'август', 'октябрь', 'декабрь']
#     month_30 = ['апрель', 'июнь', 'сентябрь', 'ноябрь']
#     month_28 = ['февраль']
#
