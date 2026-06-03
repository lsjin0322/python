# 🧮 수식 계산기

> 스택(Stack) 자료구조를 직접 구현해 만든 후위표기식 기반 수식 계산기

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)
![Flet](https://img.shields.io/badge/Flet-UI-C0604A?style=flat-square)
![Algorithm](https://img.shields.io/badge/Algorithm-Stack-5A7A62?style=flat-square)

---

## 📌 프로젝트 소개

`eval()` 같은 내장 함수를 사용하지 않고, **스택 자료구조**를 직접 구현해 수식을 계산하는 계산기입니다.

중위 표기식(`3 + 4 * 2`)을 후위 표기식(`3 4 2 * +`)으로 변환한 뒤 계산하는 과정을 직접 코드로 구현했습니다.  
UI는 Flet으로 레트로 감성의 계산기 디자인으로 구현했습니다.

---

## ✨ 주요 기능

| 기능 | 설명 |
|------|------|
| ➕➖✖️➗ **사칙연산** | 덧셈, 뺄셈, 곱셈, 나눗셈 |
| **괄호 연산** | `(`, `)` 를 포함한 복잡한 수식 계산 |
| **백스페이스** | 마지막 입력 한 글자 삭제 |
| **C 초기화** | 전체 수식 초기화 |
| **소수점** | 실수 계산 지원 |
| ⚠️ **오류 처리** | 0으로 나누기, 잘못된 수식 오류 메시지 표시 |

---

## 🗂️ 파일 구조

```
calculator_app/
├── app.py     # Flet UI (계산기 화면)
├── calc.py    # 중위→후위 변환 & 후위 계산 로직
└── stack.py   # ArrayStack 클래스 직접 구현
```

---

## 🧠 알고리즘 설명

### 1단계 — 중위 표기식 → 후위 표기식 변환

스택을 이용한 **Shunting-yard 알고리즘** 적용

```
입력:  3 + 4 * 2
출력:  3 4 2 * +
```

- 숫자 → 출력 큐에 바로 추가
- 연산자 → 우선순위 비교 후 스택에 push
- `)` → 스택에서 `(` 나올 때까지 pop

### 2단계 — 후위 표기식 계산

```
후위:  3 4 2 * +
 └─ 3 push
 └─ 4 push
 └─ 2 push
 └─ * → 4 * 2 = 8 push
 └─ + → 3 + 8 = 11 ✓
```

### 연산자 우선순위

| 연산자 | 우선순위 |
|--------|----------|
| `+` `-` | 1 |
| `*` `/` | 2 |

---

## 🚀 실행 방법

### 1. 의존성 설치

```bash
pip install flet
```

### 2. 실행

```bash
python app.py
```

---

## 🎨 디자인 컨셉

빈티지 전자계산기 감성의 **테라코타 + 세이지 그린 웜톤 테마**

| 역할 | 색상 |
|------|------|
| 배경 | `#E8E0D5` 크림 베이지 |
| 숫자 버튼 | `#F0EAE2` 오프화이트 |
| 연산자 버튼 | `#D4E4D6` 세이지 그린 |
| `=` / `C` 버튼 | `#C0604A` 테라코타 |
| 텍스트 | `#3D3530` 다크 브라운 |

---
## 미리보기 
<img width="478" height="662" alt="스크린샷 2026-06-03 145713" src="https://github.com/user-attachments/assets/f96546aa-6250-4c02-9ce4-fc105a4f8e7e" />

---

## 📚 사용 기술

- **Python 3.10+**
- **Flet** — Python 기반 UI 프레임워크
- **ArrayStack** — 직접 구현한 스택 클래스 (`stack.py`)
- **Shunting-yard 알고리즘** — 중위 → 후위 표기식 변환

---

## 🔗 관련 프로젝트

> 함께 진행한 다른 프로젝트들입니다.

- [Pixel Maze Quest](../MazeQuest_DFS) — DFS 알고리즘 시각화
- [버킷리스트 앱](../bucket_app) — FastAPI + Flet CRUD 앱
- [자료구조 구현](../자료구조) — 리스트, 스택, 집합 ADT 직접 구현
