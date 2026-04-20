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
        /* 1. 기본 박스 모델 설정 및 전체 폭 확보 */
        *, *:before, *:after {
            box-sizing: border-box !important;
        }
    
        .block-container {
            padding: 5rem 0.5rem 1rem 0.5rem !important;
            max-width: 100% !important; /* 전체 가로 폭 사용 */
        }
    
        /* 2. 메인 타이틀 (반응형 폰트) */
        .main-title {
            text-align: center;
            font-size: clamp(1.2rem, 5vw, 1.8rem); /* 화면 폭에 따라 폰트 크기 자동 조절 */
            font-weight: 800;
            color: #2E7D32;
            margin-bottom: 20px;
        }
    
        /* 3. 로또 행 컨테이너 (가장 중요) */
        [data-testid="stHorizontalBlock"] {
            display: flex !important;
            flex-direction: row !important;
            flex-wrap: nowrap !important; /* 줄바꿈 절대 방지 */
            align-items: center !important;
            justify-content: center !important; /* 세로 화면에서도 중앙 정렬 */
            width: 100% !important; /* 화면을 가득 채움 */
            max-width: 600px !important; /* 가로 모드 시 너무 퍼지는 것 방지 */
            margin: 0 auto !important;
            gap: 0px !important;
        }
        
        /* 4. 컬럼 유연성 확보 (세로 화면 스크롤 방지의 핵심) */
        [data-testid="column"] {
            padding: 0 !important;
            margin: 0 !important;
            min-width: 0 !important; /* 최소 너비 제한을 풀어야 화면 내에 수축함 */
            flex: 1 1 auto !important;
        }
        
        /* 라벨 칸 (A 자동 등) - 비율로 설정 */
        [data-testid="column"]:nth-child(1) {
            flex: 0 0 15% !important; /* 화면의 15%만 차지 */
            min-width: 45px !important; /* 글자가 깨지지 않을 최소치 */
        }
        
        /* 공 칸 - 나머지 공간을 정확히 나눔 */
        [data-testid="column"]:not(:nth-child(1)) {
            flex: 1 1 0% !important;
        }
    
        /* 5. 공 디자인 (반응형 크기) */
        /* 고정 px 대신 화면 폭(vw) 단위를 섞어 씁니다 */
        .lotto-ball {
            background-color: var(--ball-color);
            width: 8.2vw !important;  /* 화면 폭의 약 8% 크기 */
            height: 8.2vw !important;
            max-width: 36px !important; /* 가로 모드 시 너무 커짐 방지 */
            max-height: 36px !important;
            min-width: 28px !important; /* 너무 작아짐 방지 */
            min-height: 28px !important;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: clamp(10px, 2.5vw, 14px); /* 숫자 크기 자동 조절 */
            font-weight: bold;
            margin: 3px auto;
            box-shadow: 1px 1px 2px rgba(0,0,0,0.15);
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
        cols = st.columns([1, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]) 
        
        # 2. 첫 번째 칸에 라벨 배치 (수직 중앙 정렬을 위해 padding-top 추가)
        cols[0].markdown(f"<div style='padding-top:8px; font-weight:bold; font-size:14px;'>{label} 자동</div>", unsafe_allow_html=True)
        
        # 3. 나머지 칸에 공 배치
        for i, n in enumerate(nums):
            color = get_color(n)
            cols[i+1].markdown(f"""
                <div class="lotto-ball" style="
                    background-color: {color};
                    color: {'black' if n <= 10 else 'white'};
                ">{n}</div>
                """, unsafe_allow_html=True)
        st.write("") # 줄 간격 조절용


st.write("---")
st.caption("본 프로그램은 기계적 무작위성 알고리즘을 사용합니다.")
