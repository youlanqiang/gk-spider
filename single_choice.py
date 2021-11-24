# coding:utf-8

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests

url = 'http://ks.zjtvu.edu.cn/Business/Online/Exercise/Ajax/OnlineTest.ashx'
cookie = {
    'ASP.NET_SessionId': 'auatinqy5vcgrlht4dqnqmi0'
}

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"
}


def save_question(question_id, row_number, file):
    params = {
        'Method': 'GetQuestion',
        'ChapterID': 4612,
        'QuestionTypeID': 105,
        'RowNumber': row_number,
        'QuestionInnerTypeID': 1,
        'QuestionID': question_id
    }
    # Use a breakpoint in the code line below to debug your script.
    r = requests.get(url=url, cookies=cookie, params=params, headers=header)
    text = r.text.replace('"', '')
    array = text.split('^')
    title = array[0].replace('<p>', '').replace('</p>', '')
    answer = array[2].replace('<span name=\'answer\' >', '').replace('</span></br>', '')
    next_id = array[3]
    print("row_number", row_number)
    print("题目:", title)
    file.write(str(row_number) + " 题目:" + title + '\n')
    print("答案:", answer)
    file.write("答案:" + answer + '\n')
    file.write('\n')
    print("下一题:", next_id)
    if len(next_id) > 0:
        row_number += 1
        save_question(next_id, row_number, file)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file = open('./single_choice.txt', 'w')

    save_question('b9abe2d1-b844-4d54-bd34-399340a006bc', 1, file)


