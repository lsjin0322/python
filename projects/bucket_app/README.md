# 👾 2026 버킷리스트 앱

> FastAPI 백엔드와 Flet 프론트엔드로 만든 픽셀 감성 버킷리스트 관리 앱

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Flet](https://img.shields.io/badge/Flet-UI-00FF41?style=flat-square)

---

## 📌 프로젝트 소개

**"한번 사는 인생, 멋있게 살자"**

하고 싶은 것들을 목록으로 관리하는 버킷리스트 앱입니다.  
FastAPI로 REST API 서버를 구축하고, Flet으로 레트로 터미널 감성의 UI를 구현했습니다.  
데이터는 텍스트 파일(`bucketlist.txt`)에 저장됩니다.

---

## ✨ 주요 기능

| 기능 | 설명 |
|------|------|
| ➕ **추가** | 새로운 버킷리스트 항목 추가 |
| ✅ **완료 토글** | 목표 달성 여부 체크 / 해제 |
| ✏️ **수정** | 기존 항목 제목 수정 |
| 🗑️ **삭제** | 항목 삭제 |
| 🔍 **검색** | 키워드로 항목 필터링 |
| 📊 **진행률** | 전체 목표 대비 달성률 프로그레스바 표시 |

---

## 🗂️ 파일 구조

```
bucket_app/
├── main.py          # FastAPI 서버 (REST API)
├── app.py           # Flet 프론트엔드 UI
└── bucketlist.txt   # 데이터 저장 파일
```

---

## 🔌 API 명세

| Method | Endpoint | 설명 |
|--------|----------|------|
| `GET` | `/bucketlist` | 전체 조회 (검색 파라미터 지원) |
| `POST` | `/bucketlist` | 항목 추가 |
| `PUT` | `/bucketlist` | 항목 수정 (제목 or 완료 상태) |
| `DELETE` | `/bucketlist/{id}` | 항목 삭제 |
| `GET` | `/bucketlist/progress` | 진행률 조회 |

---

## 🚀 실행 방법

### 1. 의존성 설치

```bash
pip install fastapi flet httpx uvicorn
```

### 2. FastAPI 서버 실행 (터미널 1)

```bash
uvicorn main:app --reload
```

### 3. Flet 앱 실행 (터미널 2)

```bash
python app.py
```

> 서버(`main.py`)와 앱(`app.py`)을 **동시에** 실행해야 합니다.

---

## 💾 데이터 저장 방식

별도 DB 없이 텍스트 파일에 저장합니다.

```
바다보기|False
수상스키타기|True
하와이에서 서핑하기|False
```

- `|` 구분자로 제목과 완료 여부를 저장
- 항목 삭제 시 ID 자동 재배정

---

## 🎨 디자인 컨셉

레트로 터미널 / 해킹 감성의 **다크 그린 픽셀 테마**

| 역할 | 색상 |
|------|------|
| 배경 | `#0A0A0A` 블랙 |
| 메인 텍스트 | `#00FF41` 네온 그린 |
| 패널 배경 | `#0F1A0F` 다크 그린 |
| 오류 / 삭제 | `#FF4444` 레드 |

---
## 미리보기 
<img width="854" height="747" alt="스크린샷 2026-06-03 143048" src="https://github.com/user-attachments/assets/f11c77c2-1a15-4060-9916-c7a8e8c6e484" />

---

## 📚 사용 기술

- **FastAPI** — REST API 서버
- **Flet** — Python 기반 UI 프레임워크
- **httpx** — 비동기 HTTP 클라이언트
- **Pydantic** — 데이터 모델 검증

---

## 🔗 관련 프로젝트

> 함께 진행한 다른 프로젝트들입니다.

- [Pixel Maze Quest](../MazeQuest_DFS) — DFS 알고리즘 시각화
- [수식 계산기](../calculator_app) — 스택 기반 후위표기식 계산기
- [자료구조 구현](../자료구조) — 리스트, 스택, 집합 ADT 직접 구현
