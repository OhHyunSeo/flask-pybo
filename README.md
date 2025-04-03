# 📘 Flask Pybo 프로젝트

[![Database: SQLite](https://img.shields.io/badge/Database-SQLite-purple.svg)](https://www.sqlite.org/)
[![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey.svg)](https://flask.palletsprojects.com/)

## 🔍 소개

**Flask Pybo**는 Flask 웹 프레임워크를 기반으로 만든 간단한 Q&A 게시판 예제입니다.  
이 프로젝트는 Flask를 학습하고 실제 웹 애플리케이션을 만들어보려는 개발자를 위한 참고용 프로젝트입니다.

---

## 🛠️ 주요 기능

- 질문 / 답변 등록, 수정, 삭제
- 사용자 회원가입 및 로그인
- 게시글 정렬, 페이징 처리
- 템플릿 기반 UI

---

## 📁 프로젝트 구조

```
📁 flask-pybo-master/
│
├── 📄 config.py                  # 애플리케이션 전반 설정 파일
│
└── 📁 pybo/                      # 메인 애플리케이션 패키지
    ├── 📄 __init__.py            # Flask 앱 생성 및 블루프린트 등록
    ├── 📄 filter.py              # 사용자 정의 필터 등록
    ├── 📄 forms.py               # WTForms 폼 정의
    ├── 📄 models.py              # SQLAlchemy 모델 정의
    │
    ├── 📁 static/                # 정적 파일 (CSS, JS 등)
    │   ├── 📄 bootstrap.min.css
    │   ├── 📄 bootstrap.min.js
    │   └── 📄 style.css
    │
    ├── 📁 templates/             # HTML 템플릿 파일
    │   ├── 📁 answer/            # 답변 관련 템플릿
    │   │   └── 📄 answer_form.html
    │   ├── 📁 auth/              # 인증(회원가입/로그인) 관련 템플릿
    │   │   ├── 📄 login.html
    │   │   └── 📄 signup.html
    │   ├── 📁 question/          # 질문 관련 템플릿
    │   │   ├── 📄 question_detail.html
    │   │   ├── 📄 question_form.html
    │   │   └── 📄 question_list.html
    │   ├── 📄 base.html          # 기본 레이아웃 템플릿
    │   ├── 📄 form_errors.html   # 폼 오류 표시 템플릿
    │   └── 📄 navbar.html        # 내비게이션 바 템플릿
    │
    └── 📁 views/                 # 라우팅 핸들러 (블루프린트)
        ├── 📄 answer_views.py    # 답변 관련 라우트
        ├── 📄 auth_views.py      # 사용자 인증 관련 라우트
        ├── 📄 main_views.py      # 메인 페이지 라우트
        └── 📄 question_views.py  # 질문 관련 라우트

---

## 🚀 시작하기

### 1. 프로젝트 클론

```bash
git clone https://github.com/yourusername/flask-pybo.git
cd flask-pybo
```

### 2. 가상환경 설정

```bash
python -m venv venv
source venv/bin/activate  # 윈도우: venv\Scripts\activate
```

### 3. 필수 패키지 설치

```bash
pip install -r requirements.txt
```

### 4. 데이터베이스 초기화

```bash
flask init-db
```

### 5. 서버 실행

```bash
flask run
```

👉 웹 브라우저에서 `http://127.0.0.1:5000` 로 접속

---

## 🖼️ 실행 화면

> 아래는 실제 실행 화면 예시입니다.  
> 이미지 파일은 `images/` 폴더에 넣고 상대 경로로 연결할 수 있습니다.

![메인 페이지](./images/main_page.png)
![질문 작성](./images/create_question.png)

---

## 👩‍💻 개발 환경

| 항목         | 내용               |
|--------------|--------------------|
| 언어         | Python 3.10 이상    |
| 프레임워크   | Flask 2.x          |
| DB           | SQLite             |
| 템플릿 엔진  | Jinja2             |



