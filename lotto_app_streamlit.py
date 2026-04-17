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
    /* 1. 웹사이트의 느낌을 지우고 앱처럼 전체 너비 활용 */
    .block-container {
        max-width: 100% !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        padding-top: 1rem !important;
        padding-bottom: 1rem !important;
    }

    /* 2. 제목과 텍스트 크기를 모바일에 맞게 축소 */
    h1 {
        font-size: 1.5rem !important;
        text-align: center;
    }
    .stMarkdown p {
        font-size: 0.9rem !important;
        margin-bottom: -15px !important; /* 라벨과 공 사이 밀착 */
        padding-left: 5px;
    }

    /* 3. [핵심] 공들을 가로로 옹기종기 모으기 (모바일 강제 정렬) */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        justify-content: flex-start !important; /* 왼쪽으로 정렬 */
        gap: 2px !important; /* 공 사이의 미세한 간격 */
        width: 100% !important;
    }
    
    /* 4. 각 컬럼의 너비를 공 크기에 딱 맞게 고정 */
    [data-testid="column"] {
        flex: 0 0 auto !important;
        width: 40px !important; /* 공 크기 34px + 여백 6px */
        min-width: 40px !important;
    }

    /* 5. 버튼을 화면 너비에 꽉 차게 */
    .stButton button {
        width: 100% !important;
        border-radius: 10px !important;
        height: 3rem !important;
    }

    /* 6. 불필요한 위쪽 여백(헤더) 제거 */
    header {
        visibility: hidden;
    }
    #MainMenu {
        visibility: hidden;
    }
    footer {
        visibility: hidden;
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
st.title(" 🍀 민우동행 행운의 LOTTO 🍀 ")
st.write(f"현재 시간: {current_time}")
st.write("---")

# 번호 생성 버튼
if st.button("✨ 행운의 번호 생성하기", type="primary", use_container_width=True):
    # st.balloons() # 축하 효과
    
    for label in ['A', 'B', 'C', 'D', 'E']:
        nums = generate_true_random_lotto()
        
        # 가로 한 줄에 라벨과 공 표시
        st.write(f"**{label}   자  동**")
        cols = st.columns(6)
        
        for i, n in enumerate(nums):
            color = get_color(n)
            # 모바일 최적화 사이즈(34px) 적용
            cols[i].markdown(f"""
                <div style="
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
        st.write("") # 줄 간격

st.write("---")
st.caption("본 프로그램은 기계적 무작위성 알고리즘을 사용합니다.")
