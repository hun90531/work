import urllib.request
from bs4 import BeautifulSoup
import os.path


# 유저 아이디 기반 푼 문제 번호 가져오기
def get_problem_num(id):    
    url = home + '/user/' + id

    data = urllib.request.urlopen(url)
    soup = BeautifulSoup(data, 'html.parser')

    problem_num = soup.find_all('div', class_='panel-body')
    problem_num = problem_num[0].text.split('\n')[1:-1]
    
    return problem_num


# id1이 풀었는데 id2가 풀지 않은 문제
def filter_by_number(id1, id2):
    id1 = set(id1)
    id2 = set(id2)
    res = id1 - id2
    res = list(res)

    return res


# 전체 문제를 관리하는 파일에 문제 정보 새로 입력
def save_problem_info(id, problem_num):
    check = input('all.txt 데이터 날아갈 수 있는데 진짜로? [y / n] ')
    
    if check != 'y':
        return '취소했습니다.'

    problem_info = [] # 추가 저장할 문제 리스트

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


    return 'all.txt 파일에 데이터를 모두 저장했습니다.'
    

# 전체 문제 정보 업데이트
def update_problem_solving(problem_num):
    all = get_all_problem() # 전체 문제 정보
    
    all_num = [i.split()[0] for i in all]

    search_problem = list(set(problem_num) - set(all_num))

    index = 0
    for p in search_problem:
        url = home + '/problem/' + p

        data = urllib.request.urlopen(url)
        soup = BeautifulSoup(data, 'html.parser')

        name = soup.find('span', id='problem_title')
        search_problem[index] = search_problem[index] + ' ' + name.text
        index = index + 1

    all = sorted(all + search_problem)
    
    print(all, len(all))
    print(len(search_problem))
    with open('problem_info/all.txt', 'w', encoding='utf-8') as f:
        for p in all:
            f.write('%s\n' %p)


    return 'all.txt 파일에 업데이트를 완료했습니다.'


# 전체 문제 불러오기
def get_all_problem():
    all_problem_db = [] # 전체 문제
    all_problem_num = [] # 전체 문제에 대한 번호

    # 기존의 문제 정보 가져오기
    with open('problem_info/all.txt', 'r', encoding='utf-8') as f:
        for line in f:
            all_problem_db.append(line[:-1])

    return all_problem_db


home = 'https://www.acmicpc.net'
user = 'rkdwl960'

with open('work_helper.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line.replace('\n',''))

select = int(input('\n원하는 기능을 선택하세요. '))

if select == 1:
    pass

elif select == 2:
    pass
nums = get_problem_num(user)
# print(save_problem_info(user, nums))
print(len(get_all_problem()))
# print(update_problem_solving(nums))