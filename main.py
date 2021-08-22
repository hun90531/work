import urllib.request
from bs4 import BeautifulSoup
import os.path

def get_problem_num(id):    
    # 유저 아이디 기반 푼 문제 번호 가져오기
    url = home + '/user/' + id

    data = urllib.request.urlopen(url)
    soup = BeautifulSoup(data, 'html.parser')

    problem_num = soup.find_all('div', class_='panel-body')
    problem_num = problem_num[0].text.split('\n')[1:-1]
    
    return problem_num


def filter_by_number(id1, id2):
    id1 = set(id1)
    id2 = set(id2)
    res = id1 - id2
    res = list(res)

    return res


def save_problem_info(id, problem_num):
    problem_info = []
    problem_db = []


    # 기존의 문제 정보 가져오기
    with open('problem_info/all.txt', 'r', encoding='utf-8') as f:
        for line in f:
            problem_db.append(line)


    cnt = 1
    for p in problem_num:
        url = home + '/problem/' + p

        data = urllib.request.urlopen(url)
        soup = BeautifulSoup(data, 'html.parser')

        name = soup.find('span', id='problem_title')
        problem_info.append(p + ' ' + name.text)

        print(f'{p} {name.text} ({cnt} / {len(problem_num)})')
        cnt = cnt + 1

    
    
    with open('problem_info/all.txt', 'w', encoding='utf-8') as f:
        for p in problem_info:
            f.write('%s\n' %p)
    

def update_problem_solving(id, problem_num):
    problem_name = []

    with open('problem_info/백준-강지훈.txt', 'w', encoding='utf-8') as f:
        for p in problem_num:
            f.write('%s\n' %p)

    '''for problem in problem_num:
        url = home + '/problem/' + problem

        data = urllib.request.urlopen(url)
        soup = BeautifulSoup(data, 'html.parser')

        name = soup.find('span', id='problem_title')
        
        problem_name.append(name.text)'''
    
    print(problem_name)




home = 'https://www.acmicpc.net'
user = 'rkdwl960'
a = [1,2,4,5,6]
b = [3,4,5,6]
a = set(a)
b = set(b)
print(list(a - b))
# nums = get_problem_num(user)
# save_problem_info(user, nums)
# update_problem_solving('hun90531', nums)