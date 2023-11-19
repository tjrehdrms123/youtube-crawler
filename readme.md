# 유튜브 크롤러 <img src="./logo.png" align=left width="100" alt="Nest Logo" />

> 유튜브 댓글 중 좋아요 50개가 넘는 댓글 분석을 통해 가치관과 태도의 차이를 보기 위해 진행 했습니다.

<br/>

# 🌿 사용 스택

### Languages

![python](https://img.shields.io/badge/python-007ACC?style=for-the-badge&logo=python&logoColor=white)

<br/>

# 🐈 시작 가이드

Application을 실행하기 위해 필요합니다.

- Mac OS
- Python v3.11.6
- Pip3 v23.3.1

## Installation

```bash
$ git clone git@github.com:tjrehdrms123/youtube-crawler.git
$ cd youtube-crawler
$ pip3 install selenium webdriver_manager beautifulsoup4 pandas #패키지 설치
$ brew install --cask chromedriver #크롬 드라이버 설치
$ pip3 install webdriver_manager #드라이버 버전관리
$ python3 app.py #크롤러 실행
```

### Install Error

`WebDriver.**init**() got an unexpected keyword argument 'service'` 에러가 발생한다면 selenium 버전 문제로 버전 업데이트를 진행해야 됩니다.

```bash
pip3 install --upgrade selenium
```

</br>

# 📢 해결한 이슈 & 알게된 것

- [https://ddingmin00.tistory.com/entry/mac-m1-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%A7%81-Selenium-Chromedriver-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0](https://ddingmin00.tistory.com/entry/mac-m1-%EC%9B%B9-%ED%81%AC%EB%A1%A4%EB%A7%81-Selenium-Chromedriver-%EC%84%A4%EC%B9%98%ED%95%98%EA%B8%B0)
- [https://velog.io/@parkeu/youtubecomment](https://velog.io/@parkeu/youtubecomment)
