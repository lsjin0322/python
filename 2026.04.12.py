import flet as ft
import random
from datetime import datetime

# -----------------------------
# DB
# -----------------------------
items = [
    "비누", "치약", "샴푸", "린스", "바디워시", "폼클렌징", "칫솔", "수건",
    "휴지", "물티슈", "세탁세제", "섬유유연제", "주방세제", "수세미", "고무장갑",
    "쌀", "라면", "햇반", "생수", "우유", "계란", "두부", "콩나물", "시금치",
    "양파", "감자", "고구마", "사과", "바나나", "오렌지", "귤", "토마토",
    "김치", "된장", "고추장", "간장", "식용유", "참기름", "소금", "설탕",
    "커피", "차", "과자", "빵", "젤리", "초콜릿", "음료수", "맥주", "소주",
    "고기(돼지고기)", "고기(소고기)", "닭고기", "생선", "오징어", "새우", "게",
    "쌀국수", "파스타", "잼", "버터", "치즈", "요거트", "아이스크림", "통조림",
    "냉동만두", "어묵", "햄", "소시지", "김", "미역", "다시마", "멸치",
    "밀가루", "부침가루", "튀김가루", "빵가루", "식초", "소스", "향신료",
    "양초", "성냥", "건전지", "전구", "쓰레기봉투", "지퍼백", "호일", "랩"
]

products = {
    i: {"price": random.randint(1000, 8000), "stock": random.randint(5, 20)}
    for i in items
}

cart = {}

# -----------------------------
# 날짜
# -----------------------------
today = datetime.now().strftime("%Y.%m.%d")

# -----------------------------
# 할인
# -----------------------------
discount_items = random.sample(items, 5)
discount = {i: random.randint(10, 50) for i in discount_items}

# -----------------------------
# 매출
# -----------------------------
monthly = 0
yearly = 0


def main(page: ft.Page):

    global cart, monthly, yearly

    ORANGE = "#FF6A00"

    page.title = "MART SYSTEM"
    page.bgcolor = "white"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # -----------------------------
    # 🛒 배경 (카트 이모지 느낌)
    # -----------------------------
    bg = ft.Stack(
        expand=True,
        controls=[
            ft.Text(
                "🛒 🛒 🛒 🛒 🛒 🛒 🛒 🛒 🛒 🛒",
                size=60,
                color="#FFF1E6",
            ),
        ],
    )

    # -----------------------------
    # INPUT
    # -----------------------------
    item_input = ft.TextField(label="상품명", width=250)
    qty_input = ft.TextField(label="수량", width=250)
    admin_search = ft.TextField(label="관리자 검색", width=300)

    # -----------------------------
    # UI
    # -----------------------------
    cart_view = ft.Column()
    receipt_view = ft.Column()
    admin_view = ft.Column()
    sales_text = ft.Text(color=ORANGE)
    error_text = ft.Text(color="red")
    total_text = ft.Text("총합: 0원", size=18, color=ORANGE)

    # -----------------------------
    # 가격
    # -----------------------------
    def price(n):
        p = products[n]["price"]
        if n in discount:
            p -= p * discount[n] / 100
        return int(p)

    def total():
        return sum(price(n) * q for n, q in cart.items())

    # -----------------------------
    # 장바구니
    # -----------------------------
    def update():

        cart_view.controls.clear()

        for n, q in cart.items():
            cart_view.controls.append(
                ft.Text(f"{n} x{q} = {price(n)*q}원")
            )

        total_text.value = f"총합: {total()}원"
        page.update()

    # -----------------------------
    # 담기
    # -----------------------------
    def add(e):

        error_text.value = ""

        n = item_input.value.strip()

        if n not in products:
            error_text.value = "잘못 입력하였습니다."
            page.update()
            return

        try:
            q = int(qty_input.value)
        except:
            error_text.value = "잘못 입력하였습니다."
            page.update()
            return

        if q <= 0 or products[n]["stock"] < q:
            error_text.value = "잘못 입력하였습니다."
            page.update()
            return

        cart[n] = cart.get(n, 0) + q

        item_input.value = ""
        qty_input.value = ""

        update()

    # -----------------------------
    # 결제
    # -----------------------------
    def pay(e):

        global monthly, yearly, cart

        t = total()

        for n, q in cart.items():
            products[n]["stock"] -= q

        monthly += t
        yearly += t

        update()
        show_receipt(t)
        update_sales()

    # -----------------------------
    # 영수증
    # -----------------------------
    def show_receipt(t):

        receipt_view.controls.clear()

        receipt_view.controls.append(
            ft.Text("🧾 영수증", size=18, color=ORANGE)
        )

        receipt_view.controls.append(ft.Text(f"총 결제: {t}원"))
        receipt_view.controls.append(ft.Text("다음 결제를 진행하시겠습니까?"))

        def yes(e):
            global cart
            cart.clear()
            receipt_view.controls.clear()
            update()
            page.update()

        def no(e):
            page.update()

        receipt_view.controls.append(
            ft.Row([
                ft.ElevatedButton("네", bgcolor=ORANGE, color="white", on_click=yes),
                ft.ElevatedButton("아니오", on_click=no)
            ], alignment=ft.MainAxisAlignment.CENTER)
        )

        page.update()

    # -----------------------------
    # 관리자
    # -----------------------------
    def update_admin(e=None):

        admin_view.controls.clear()

        key = admin_search.value.strip()

        if not key:
            admin_view.controls.append(ft.Text("검색 후 표시됩니다"))
            page.update()
            return

        for n, v in products.items():
            if key in n:
                admin_view.controls.append(
                    ft.Text(f"{n} | 재고:{v['stock']} | {v['price']}원")
                )

        page.update()

    # -----------------------------
    # 매출
    # -----------------------------
    def update_sales():
        sales_text.value = f"월매출: {monthly}원 / 연매출: {yearly}원"
        page.update()

    # -----------------------------
    # 할인
    # -----------------------------
    discount_box = ft.Column()

    def update_discount():

        discount_box.controls.clear()

        discount_box.controls.append(
            ft.Text("📢 할인 정보", color=ORANGE)
        )

        discount_box.controls.append(ft.Text(f"날짜: {today}"))

        for n, r in discount.items():
            discount_box.controls.append(
                ft.Text(f"{n} - {r}%", color=ORANGE)
            )

        page.update()

    # -----------------------------
    # 버튼
    # -----------------------------
    add_btn = ft.ElevatedButton("담기", bgcolor=ORANGE, color="white", on_click=add)
    pay_btn = ft.ElevatedButton("결제", bgcolor=ORANGE, color="white", on_click=pay)

    # -----------------------------
    # UI 레이아웃
    # -----------------------------
    page.add(

        bg,  # 🛒 배경

        ft.Container(
            content=ft.Column(
                [

                    ft.Text("🛒 MART SYSTEM", size=22, color=ORANGE),

                    ft.Row(
                        [
                            ft.Column([
                                ft.Text("🔎 상품 입력", color=ORANGE),
                                item_input,
                                qty_input,
                                ft.Row([add_btn, pay_btn])
                            ]),

                            ft.Container(width=30),

                            discount_box
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    ),

                    error_text,

                    ft.Divider(),

                    ft.Text("🛒 장바구니", color=ORANGE),
                    cart_view,
                    total_text,

                    ft.Divider(),

                    ft.Text("🧾 영수증", color=ORANGE),
                    receipt_view,

                    ft.Divider(),

                    ft.Text("👨‍💼 관리자", color=ORANGE),
                    admin_search,
                    ft.ElevatedButton("검색", on_click=update_admin, bgcolor=ORANGE, color="white"),
                    admin_view,

                    ft.Divider(),

                    sales_text
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    )

    update_discount()
    update_sales()

ft.app(target=main)