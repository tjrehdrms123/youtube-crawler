from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import time

import warnings
warnings.filterwarnings('ignore')

# Chrome 드라이버를 설치하고 생성
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# YouTube 동영상 URL 배열: 원하는 유튜브 링크 넣어서 사용
youtube_urls = [
# "https://www.youtube.com/watch?v=SacqsPMhOBI&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=1",
# "https://www.youtube.com/watch?v=e5FGR2X526Q&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=2",
# "https://www.youtube.com/watch?v=2ExT3oHCVZI&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=3",
# "https://www.youtube.com/watch?v=IvsI1qds8c0&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=4",
# "https://www.youtube.com/watch?v=Mn1p0RMYcrQ&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=5",
"https://www.youtube.com/watch?v=AeJk9Du2BnU&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=6",
"https://www.youtube.com/watch?v=qKSvyTUQZ6w&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=8",
"https://www.youtube.com/watch?v=07oyDj9xQvs&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=9",
"https://www.youtube.com/watch?v=COS8_UFIBzI&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=10",
"https://www.youtube.com/watch?v=RSXFkJnxEvs&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=11", 
"https://www.youtube.com/watch?v=XuG8eu0osOM&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=12", 
"https://www.youtube.com/watch?v=vdt23uc5Ymw&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=13", 
"https://www.youtube.com/watch?v=hCRapAa_zdI&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=14", 
"https://www.youtube.com/watch?v=BmQ4zECZyvY&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=15", 
"https://www.youtube.com/watch?v=UFrwLnmE2R0&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=17", 
"https://www.youtube.com/watch?v=6oPLscD6LyA&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=25", 
"https://www.youtube.com/watch?v=U45600MlJjA&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=27",
"https://www.youtube.com/watch?v=JlpJjB3HkYk&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=28", 
"https://www.youtube.com/watch?v=P4-x5Me0guM&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=61", 
"https://www.youtube.com/watch?v=A2GbgaLiVIk&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=62", 
"https://www.youtube.com/watch?v=qpm4dGc2NI0&list=PLFIYUdSkjiCAuWe006VqSTFfaE7rgIHNy&index=64", 
]

for youtube_url in youtube_urls:
    driver.get(youtube_url)  # 링크 열기

    driver.implicitly_wait(5)

    time.sleep(3)

    driver.execute_script('window.scrollTo(0, 800)')  # 한번 스크롤
    time.sleep(3)

    last_height = driver.execute_script('return document.documentElement.scrollHeight')  # 스크롤 전체 높이

    id_final = []  # 초기화 위치 변경
    comment_final = []  # 초기화 위치 변경
    like_final = []  # 초기화 위치 변경

    while True:
        driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')  # 스크롤 다운
        time.sleep(1.5)

        new_height = driver.execute_script('return document.documentElement.scrollHeight')  # 스크롤 다운 후 스크롤 높이

        if new_height == last_height:  # 댓글 마지막 페이지면 while문 벗어남
            break

        last_height = new_height
        time.sleep(1.5)

        try:
            driver.find_element_by_css_selector('#dismiss-button > a').click()  # 유튜브 1달 무료 팝업 닫기
        except:
            pass

    # WebDriverWait를 사용하여 댓글이 로딩될 때까지 기다림
    comments_loaded = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'yt-formatted-string#content-text'))
    )

    # 댓글 크롤링
    html_source = driver.page_source
    soup = BeautifulSoup(html_source, 'html.parser')

    id_list = soup.select('a#author-text>yt-formatted-string.ytd-comment-renderer')  # 글쓴이 리스트
    comment_list = soup.select('yt-formatted-string#content-text')  # comment 리스트
    like_list = soup.select('div#toolbar>#vote-count-middle')  # like 리스트

    # 좋아요 천 단위 일때 1천으로 나와서 숫자형으로 변환하는 함수
    def convert_likes(temp_like):
        if '천' in temp_like:
            temp_like = temp_like.replace('천', '')
            temp_like = float(temp_like) * 1000
        return int(temp_like)

    # 기존 코드
    for i in range(len(comment_list)):
        temp_like = like_list[i].text
        temp_like = temp_like.replace('\n', '').replace('\t', '').replace('\r', '').strip()
        converted_like = convert_likes(temp_like)
        # 좋아요 50개 이상인 데이터만 추출
        if converted_like >= 50:
            like_final.append(converted_like)  # 좋아요

            temp_id = id_list[i].text
            temp_id = temp_id.replace('\n', '').replace('\t', '').replace(' ', '').strip()
            id_final.append(temp_id)  # 댓글 작성자

            temp_comment = comment_list[i].text
            temp_comment = temp_comment.replace('\n', '').replace('\t', '').replace('\r', '').strip()
            comment_final.append(temp_comment)  # 댓글 내용

    # DataFrame 만들기(list -> dictionary -> dataframe)
    # list -> dictionary
    youtube_dic = {"아이디": id_final, "댓글 내용": comment_final, "좋아요 갯수": like_final}
    # dictionary -> dataframe
    youtube_pd = pd.DataFrame(youtube_dic)

    # URL에서 index 값을 추출하여 파일명으로 사용
    index = int(youtube_url.split('&index=')[-1])
    # DataFrame을 엑셀 파일로 내보내기
    youtube_pd.to_excel(f"h_{index}.xlsx", index=False)

# WebDriver 종료
driver.quit()
