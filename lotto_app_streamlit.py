import streamlit as st
import secrets
import time
from datetime import datetime # 타임 라이브러리 추가
import pytz # 타임존 라이브러리 추가

# 한국 타임존 설정
KST = pytz.timezone('Asia/Seoul')

# 1. 현재 한국 시간 가져오기
now_kst = datetime.now(KST)
current_time = now_kst.strftime('%Y-%m-%d %H:%M:%S')



# 1. 페이지 설정 (제목 및 모바일 레이아웃)
st.set_page_config(page_title="민우동행 로또", page_icon="🍀", layout="centered")

st.markdown("""
    <style>
    /* 1. 전체 컨테이너를 가로로 꽉 채우고 줄바꿈 방지 */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        align-items: center !important; /* 수직 중앙 정렬 */
        justify-content: flex-start !important;
        gap: 0px !important;
        width: 50% !important;
    }
    
    /* 2. 라벨 칸과 공 칸의 너비 최적화 */
    [data-testid="column"] {
        flex: 0 0 auto !important;
        padding: 0 !important;
        margin: 0 !important;
    }
    
    /* 라벨이 들어가는 첫 번째 칸 너비 */
    [data-testid="column"]:nth-child(1) {
        width: 15px !important;
        min-width: 15px !important;
    }
    
    /* 공이 들어가는 나머지 칸들 너비 */
    [data-testid="column"]:not(:nth-child(1)) {
        width: 15px !important;
        min-width: 10px !important;
    }

    /* 3. 모바일 레이아웃 패딩 조절 */
    .block-container {
        padding: 1rem 0.5rem !important;
    }
    </style>
    """, unsafe_allow_html=True)





# 2. 로또 추출 로직 (기계적 무작위성 유지)
def generate_true_random_lotto():
    seed_base = int(time.time() * 1000000)
    balls = list(range(1, 46))
    for _ in range(seed_base % 1000):
        secrets.SystemRandom().shuffle(balls)
    result = []
    for _ in range(6):
        pick = secrets.SystemRandom().choice(balls)
        balls.remove(pick)
        result.append(pick)
    return sorted(result)

def get_color(n):
    """번호별 로또 공 색상 스타일"""
    if n <= 10: return "#fbc400"
    if n <= 20: return "#69c8f2"
    if n <= 30: return "#ff7272"
    if n <= 40: return "#aaaaaa"
    return "#b0d840"

# 3. 화면 UI 구성
st.markdown("""
    <h1 style='
        text-align: center; 
        font-size: 28px;   /* 원하는 크기로 조절 (20px~28px 추천) */
        font-weight: 800; 
        padding-bottom: 10px;
    '>
    🍀 민우동행 행운의 LOTTO 🍀
    </h1>
    """, unsafe_allow_html=True)
st.write(f"현재 시간: {current_time}")
st.write("---")

# 번호 생성 버튼
# ... (상단 로직 동일)

if st.button("✨ 행운의 번호 생성하기", type="primary", use_container_width=True):
    st.spinner()
    
    for label in ['A', 'B', 'C', 'D', 'E']:
        nums = generate_true_random_lotto()
        
        # 1. 컬럼 구성 변경: 첫 칸은 라벨용(가로폭 60px), 나머지 6개는 공용(각 40px)
        # 비율을 직접 조절하기 위해 숫자를 포함한 리스트 사용
        cols = st.columns([1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]) 
        
        # 2. 첫 번째 칸에 라벨 배치 (수직 중앙 정렬을 위해 padding-top 추가)
        cols[0].markdown(f"<div style='padding-top:8px; font-weight:bold; font-size:14px;'>{label} 자동</div>", unsafe_allow_html=True)
        
        # 3. 나머지 칸에 공 배치
        for i, n in enumerate(nums):
            color = get_color(n)
            cols[i+1].markdown(f"""
                <div style="
                    box-sizing: border-box;           
                    background-color: {color};
                    color: {'black' if n <= 10 else 'white'};
                    width: 34px;
                    height: 34px;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 14px;
                    font-weight: bold;
                    margin: 0 auto;
                    box-shadow: 1px 1px 2px rgba(0,0,0,0.15);
                ">{n}</div>
                """, unsafe_allow_html=True)
        st.write("") # 줄 간격 조절용


st.write("---")
st.caption("본 프로그램은 기계적 무작위성 알고리즘을 사용합니다.")
