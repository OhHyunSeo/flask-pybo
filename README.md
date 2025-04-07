# 🧩 Flask Pybo - Q&A 게시판 프로젝트

[![Python Version](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Framework-Flask-green.svg)](https://flask.palletsprojects.com/)

## 🔍 소개

**Flask Pybo**는 Flask 웹 프레임워크를 기반으로 만든 간단한 Q&A 게시판 웹 애플리케이션입니다.  
질문과 답변을 주고받는 구조로 게시글 작성, 조회, 수정, 삭제 기능을 포함하며 사용자 인증 기능도 제공합니다.

---

## 🛠️ 주요 기능

- 질문 / 답변 등록, 수정, 삭제 (CRUD)
- 사용자 회원가입 및 로그인
- 게시글 페이징, 필터링
- 사용자 정의 필터 및 템플릿 구성
- 환경별 설정 지원 (개발/운영)

---

## 📁 프로젝트 구조

```
📁 flask-pybo-master/
│
├── 📁 config/                         # 환경설정 관련 모듈
│   ├── __init__.py
│   ├── default.py                    # 기본 설정
│   ├── development.py                # 개발 환경 설정
│   └── production.py                 # 운영 환경 설정
│
├── 📄 config.py                      # 설정 진입점
│
├── 📁 pybo/                          # 메인 애플리케이션 모듈
│   ├── __init__.py                   # Flask 앱 초기화
│   ├── filter.py                     # 사용자 정의 필터
│   ├── forms.py                      # WTForms 폼 정의
│   ├── models.py                     # SQLAlchemy 모델 정의
│   ├── 📁 static/                    # 정적 자원
│   ├── 📁 templates/                 # Jinja2 템플릿
│   └── 📁 views/                     # 라우팅 블루프린트
```

---

## 🚀 실행 방법

### 1. 환경 설정

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. 환경 변수 설정 (예시)

```bash
export FLASK_APP=pybo
export FLASK_ENV=development
```

### 3. 데이터베이스 초기화

```bash
flask db init
flask db migrate
flask db upgrade
```

### 4. 서버 실행

```bash
flask run
```

---

## 🔒 기능 요약

| 기능              | 설명                              |
|-------------------|-----------------------------------|
| 회원가입/로그인   | 사용자 인증 및 세션 처리           |
| 질문 등록/수정    | 질문 CRUD                          |
| 답변 작성/삭제    | 특정 질문에 대한 답변 기능         |
| 템플릿 구성        | base.html로 구성된 페이지 레이아웃 |
| 정적 자원 분리     | Bootstrap 기반 스타일 적용         |

---

## 🙌 기여 방법

1. 이 저장소를 포크합니다.
2. 새 브랜치를 생성합니다: `git checkout -b feature/새기능`
3. 변경사항을 커밋합니다: `git commit -m "Add 새기능"`
4. 브랜치에 푸시합니다: `git push origin feature/새기능`
5. Pull Request를 생성합니다.
