# import secrets
# import time

# def generate_true_random_lotto():
#     # 1. 시스템의 암호학적 난수 생성기를 사용하여 씨앗값 생성
#     # 2. 미세한 시간값(나노초 단위)을 더해 무작위성 강화
#     seed_base = int(time.time() * 1000000)
    
#     # 3. 1~45번 공 리스트 생성
#     balls = list(range(1, 46))
    
#     # 4. 공을 '실제로 섞는 것처럼' 수백 번 셔플
#     # seed_base에 따라 섞는 횟수가 매번 달라짐
#     for _ in range(seed_base % 1000):
#         secrets.SystemRandom().shuffle(balls)
        
#     # 5. 최종적으로 6개 추출 (중복 없이)
#     result = []
#     for _ in range(6):
#         pick = secrets.SystemRandom().choice(balls)
#         balls.remove(pick)
#         result.append(pick)
        
#     return sorted(result)

# # --- 5개 세트(한 장) 출력 부분 ---
# print(f"{'='*35}")
# print(f"    🍀 무작위 로또 추천 🍀")
# print(f"{'='*35}")

# for label in ['A', 'B', 'C', 'D', 'E']:
#     # 매 게임마다 새로운 무작위성을 부여하여 생성
#     lotto_numbers = generate_true_random_lotto()
    
#     # 시각적으로 보기 좋게 포맷팅 (01, 05 등의 형식)
#     formatted_nums = "  ".join(f"{num:02}" for num in lotto_numbers)
#     print(f" {label} 자 동  {formatted_nums}")

# print(f"{'='*35}")
# print(f" 생성 일시: {time.strftime('%Y-%m-%d %H:%M:%S')}")





# import streamlit as st
# import secrets
# import time

# # 기계적 무작위성 로직
# def generate_lotto():
#     seed_base = int(time.time() * 1000000)
#     balls = list(range(1, 46))
#     for _ in range(seed_base % 1000):
#         secrets.SystemRandom().shuffle(balls)
#     result = []
#     for _ in range(6):
#         pick = secrets.SystemRandom().choice(balls)
#         balls.remove(pick)
#         result.append(pick)
#     return sorted(result)

# # 웹 화면 구성
# st.title("🍀 인생한방 무작위 로또 🍀")
# st.write("나노초 단위 시간 동기화 시스템 가동 중")

# if st.button("번호 5게임 생성하기", type="primary"):
#     for label in ['A', 'B', 'C', 'D', 'E']:
#         nums = generate_lotto()
#         # 공 색깔 대신 가독성 좋은 텍스트 박스로 표시
#         st.subheader(f"자 동 {label}")
#         cols = st.columns(6)
#         for i, n in enumerate(nums):
#             cols[i].info(f"**{n}**")
#     st.success(f"생성 일시: {time.strftime('%Y-%m-%d %H:%M:%S')}")















# =======================Version 3 ======================

import tkinter as tk
import secrets
import time

def generate_true_random_lotto():
    """기계적 무작위성을 가미한 번호 추출 로직"""
    seed_base = int(time.time() * 1000000)
    balls = list(range(1, 46))
    
    # 셔플 과정 시뮬레이션
    for _ in range(seed_base % 1000):
        secrets.SystemRandom().shuffle(balls)
        
    result = []
    for _ in range(6):
        pick = secrets.SystemRandom().choice(balls)
        balls.remove(pick)
        result.append(pick)
    return sorted(result)

def get_color(n):
    """번호 대역별 로또 공 색상 반환"""
    if n <= 10: return "#fbc400" # 노랑
    if n <= 20: return "#69c8f2" # 파랑
    if n <= 30: return "#ff7272" # 빨강
    if n <= 40: return "#aaaaaa" # 회색
    return "#b0d840"            # 녹색

def draw_lotto():
    """화면의 모든 칸을 지우고 새로 번호를 생성하여 그림"""
    canvas.delete("all") # 기존 그림 삭제
    
    for i, label in enumerate(['A', 'B', 'C', 'D', 'E']):
        y_offset = 50 + (i * 60) # 각 게임별 세로 위치
        
        # 게임 라벨 (A, B, C, D, E)
        canvas.create_text(40, y_offset, text=f"{label} 자 동", font=("맑은 고딕", 12, "bold"))
        
        # 번호 생성 및 공 그리기
        numbers = generate_true_random_lotto()
        for j, num in enumerate(numbers):
            x_offset = 110 + (j * 50)
            color = get_color(num)
            
            # 원(공) 그리기
            canvas.create_oval(x_offset-18, y_offset-18, x_offset+18, y_offset+18, 
                               fill=color, outline="white", width=2)
            # 숫자 적기
            canvas.create_text(x_offset, y_offset, text=str(num), 
                               fill="white" if num > 10 else "black", font=("Consolas", 11, "bold"))

# --- 메인 윈도우 설정 ---
root = tk.Tk()
root.title(" 민우동행 로또 추첨 프로그램 ")
root.geometry("450x650")
root.configure(bg="#f8f9fa")

# 제목
title = tk.Label(root, text="🍀 민우동행 행운의 LOTTO 🍀", font=("맑은 고딕", 21, "bold"), bg="#f8f9fa", fg="#333")
title.pack(pady=10)

# 그림이 그려질 영역 (캔버스)
canvas = tk.Canvas(root, width=420, height=350, bg="white", highlightthickness=0)
canvas.pack(pady=5)

# 하단 버튼
btn = tk.Button(root, text="번호 생성하기", command=draw_lotto, 
                width=20, height=2, bg="#333", fg="white", 
                font=("맑은 고딕", 14, "bold"), cursor="hand2")
btn.pack(pady=15)

date = tk.Label(root, text=f"생성 일시 : {time.strftime('%Y-%m-%d %H:%M:%S')} ", font=("맑은 고딕", 13, "bold"),bg="#f8f9fa", fg="#333" )
date.pack(pady=10)

# 처음 실행 시 바로 번호 한 세트 보여주기
draw_lotto()

root.mainloop()
