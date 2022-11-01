import pandas as pd
import numpy as np

all_tags = []


def find_tag(tag):
    if len(all_tags) == 0:
        return -1
    for i in range(len(all_tags)):
        if tag == all_tags[i][0]:
            return i
    return -1


def analyze_tag(tag, thumb):
    while True:
        if len(tag) < 2:
            break
        if len(tag) == 2:
            a = find_tag(tag)
            if a == -1:
                all_tags.append([tag, 1, int(thumb)])
            else:
                all_tags[a][1] += 1
                all_tags[a][2] += int(thumb)
            break
        elif tag[2] == '改':
            sub_tag = tag[:3]
            a = find_tag(sub_tag)
            if a == -1:
                all_tags.append([sub_tag, 1, int(thumb)])
            else:
                all_tags[a][1] += 1
                all_tags[a][2] += int(thumb)
            tag = tag[3:]
        else:
            sub_tag = tag[:2]
            a = find_tag(sub_tag)
            if a == -1:
                all_tags.append([sub_tag, 1, int(thumb)])
            else:
                all_tags[a][1] += 1
                all_tags[a][2] += int(thumb)
            tag = tag[2:]


if __name__ == '__main__':
    src_datas = pd.read_csv('1000-Data.csv', encoding='GB18030')
    # print(src_datas)
    tag_col = src_datas['标签']
    thumb_col = src_datas['点赞数量']
    tag_data = list(tag_col)
    thumb_data = list(thumb_col)

    for i in range(len(tag_data)):
        try:
            analyze_tag(tag_data[i], thumb_data[i])
        except TypeError:
            print("line" + str(i) + ' occurred a TypeError')

    with open('tag.txt', 'w') as f:
        for tag in all_tags:
            f.write(tag[0])
            f.write(',')
            f.write(str(round(tag[2]/tag[1])))
            f.write('\n')