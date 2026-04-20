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
    .stApp {
        background-color: white !important;
    }  

    /* 전체 요소 박스 모델 고정 */
    *, *:before, *:after {
        box-sizing: border-box !important;
    }

    /* 메인 컨테이너 패딩 조절 (타이틀 가려짐 방지) */
    .block-container {
        padding: 3rem 0.5rem 1rem 0.5rem !important;
    }

    /* 타이틀 스타일 */
    .main-title {
        text-align: center;
        font-size: 1.6rem; /* 모바일 맞춤 크기 */
        font-weight: 800;
        # color: #2E7D32;
        color: #000000;
        margin-bottom: 10px;
    }

    /* 로또 행(Row) 컨테이너 최적화 */
    [data-testid="stHorizontalBlock"] {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 0px !important; /* 미세한 간격 */
        width: 20% !important;
        max-width: 500px !important; /* 가로 모드 시 너무 퍼지지 않게 제한 */
        margin: 0 auto !important;
        # overflow: visible !important;
    }
    
    /* 각 컬럼 너비 강제 조정 */
    [data-testid="column"] {
        flex: 1 1 0% !important; /* 👈 남은 공간을 균등하게 배분 */
        min-width: 0 !important; /* 👈 좁은 화면에서 스스로 줄어들게 허용 */
        padding: 0 !important;
        margin: 0 !important;
        text-align: center !important;
    }
    
    /* 라벨 칸 (A 자동 등) */
    [data-testid="column"]:nth-child(1) {
        flex: 0 0 1px !important; /* 라벨에 필요한 최소 너비 고정 */
        color: #000000;
    }
    
    /* 공이 들어가는 나머지 칸들 */
    [data-testid="column"]:not(:nth-child(1)) {
        flex: 1 1 0% !important; /* 남은 공간을 정확히 1/6씩 배분 */
    }
            
    /* 스피너(로딩) 텍스트 색상 및 스타일 강제 지정 */
    div[data-testid="stMarkdownContainer"] p {
        color: #000000 !important;
    }

    /* 스피너 아이콘 옆의 텍스트 정밀 타겟팅 */
    .stElementContainer div[role="status"] {
        color: #000000 !important;
        font-weight: bold !important;
        font-size: 20px;
        font-weight:bold;
        text-align: center;
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
        color : #000000;
        font-size: 29px;   /* 원하는 크기로 조절 (20px~28px 추천) */
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
    # 첫 번째 대기 메시지
    with st.spinner('과연'):
        time.sleep(2.0) # 0.5초보다 조금 더 길게 주면 긴장감이 생깁니다.

    with st.spinner('당신의 행운의 추첨번호는...?'):
        time.sleep(2.0) # 0.5초보다 조금 더 길게 주면 긴장감이 생깁니다.
        
    # 두 번째 대기 메시지 (with 문을 새로 열거나 내부에서 텍스트를 보여줌)
    with st.spinner('자!'):
        time.sleep(2.0)
    with st.spinner('공개 합니다 !!'):
        time.sleep(2.0)
    


    # 이후에 번호 생성 로직(for 문)이 오면 됩니다.
    st.balloons() # 공개 직후 효과 추가
    
    for label in ['A', 'B', 'C', 'D', 'E']:
        nums = generate_true_random_lotto()
        
        # 1. 컬럼 구성 변경: 첫 칸은 라벨용(가로폭 60px), 나머지 6개는 공용(각 40px)
        # 비율을 직접 조절하기 위해 숫자를 포함한 리스트 사용
        cols = st.columns([1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]) 
        
        # 2. 첫 번째 칸에 라벨 배치 (수직 중앙 정렬을 위해 padding-top 추가)
        cols[0].markdown(f"<div style='padding-top:8px; font-weight:bold; font-size:14px; color: #000000;'>{label} 자동</div>", unsafe_allow_html=True)
        
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
st.markdown("<p style='color: #333333; font-size: 0.8rem; opacity: 0.8; text-align: center;'>본 프로그램은 기계적 무작위성 알고리즘을 사용합니다.</p>", unsafe_allow_html=True)
