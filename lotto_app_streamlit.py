import streamlit as st
import secrets
import time
import pytz # 타임존 라이브러리 추가

# 한국 타임존 설정
KST = pytz.timezone('Asia/Seoul')

# 1. 현재 한국 시간 가져오기
now_kst = datetime.now(KST)
current_time = now_kst.strftime('%Y-%m-%d %H:%M:%S')



# 1. 페이지 설정 (제목 및 모바일 레이아웃)
st.set_page_config(page_title="민우동행 로또", page_icon="🍀", layout="centered")

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
st.write(f"현재 시간 : {current_time}")
st.write("---")

# 번호 생성 버튼
if st.button("✨ 행운의 번호 생성하기", type="primary", use_container_width=True):
    # st.balloons() # 축하 효과
    
    for label in ['A', 'B', 'C', 'D', 'E']:
        nums = generate_true_random_lotto()
        
        # 가로 한 줄에 라벨과 공 표시
        st.write(f"**{label} 자 동**")
        cols = st.columns(6)
        
        for i, n in enumerate(nums):
            color = get_color(n)
            # 모바일에서 예쁘게 보이는 공 디자인 (HTML/CSS)
            cols[i].markdown(f"""
                <div style="
                    background-color: {color};
                    color: {'black' if n <= 10 else 'white'};
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 16px;
                    font-weight: bold;
                    margin: auto;
                    box-shadow: 1px 1px 3px rgba(0,0,0,0.2);
                ">{n}</div>
                """, unsafe_allow_html=True)
        st.write("") # 간격 조절

st.write("---")
st.caption("본 프로그램은 기계적 무작위성 알고리즘을 사용합니다.")
