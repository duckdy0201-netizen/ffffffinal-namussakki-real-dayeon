import streamlit as st

st.set_page_config(layout="wide") # 화면을 넓게 쓰기 위한 설정

st.title("🧱 6학년 수학: 쌓기나무 복습하기")
st.subheader("문제를 보고 위에서 본 모양에 알맞은 숫자를 써넣으세요!")

# 화면을 왼쪽(문제)과 오른쪽(입력창)으로 나눕니다.
col1, col2 = st.columns(2)

with col1:
    st.write("### 1. 다음 쌓기나무 모양을 관찰하세요.")
    # 실제 수업용 쌓기나무 이미지 주소를 넣거나 업로드한 사진을 띄울 수 있습니다.
    # 여기서는 예시 이미지를 보여줍니다.
    st.image("https://images.unsplash.com/photo-1606166325683-e6deb697d325683?w=500", 
             caption="교과서 65쪽 2번 모양 예시", use_container_width=True)

with col2:
    st.write("### 2. 위에서 본 모양에 수 쓰기")
    st.write("각 칸을 마우스로 클릭하여 알맞은 숫자를 고르세요.")
    
    # 교과서 수업안에 작성하신 정답 데이터 (3 2 2 / 1 3 2 구조)를 3x3 격자로 배치
    # 예시 정답: 1행(3, 2, 2), 2행(1, 3, 2), 3행(0, 0, 0)
    
    # 3x3 입력 격자 만들기
    r1_c1 = st.selectbox("1행 1열", [0, 1, 2, 3, 4], key="r1c1")
    r1_c2 = st.selectbox("1행 2열", [0, 1, 2, 3, 4], key="r1c2")
    r1_c3 = st.selectbox("1행 3열", [0, 1, 2, 3, 4], key="r1c3")
    
    st.divider() # 구분선
    
    r2_c1 = st.selectbox("2행 1열", [0, 1, 2, 3, 4], key="r2c1")
    r2_c2 = st.selectbox("2행 2열", [0, 1, 2, 3, 4], key="r2c2")
    r2_c3 = st.selectbox("2행 3열", [0, 1, 2, 3, 4], key="r2c3")

# 하단 채점 세션
st.write("")
if st.button("정답 확인하기", type="primary"):
    # 수업안에 적어두신 정답 '3 2 2 / 1 3 2'와 학생이 입력한 값이 일치하는지 비교
    if r1_c1 == 3 and r1_c2 == 2 and r1_c3 == 2 and r2_c1 == 1 and r2_c2 == 3 and r2_c3 == 2:
        st.success("🎉 정답입니다! 아주 정확하게 공간을 분석했네요!")
        st.balloons() # 화면에 풍선이 펑펑 터지는 효과
    else:
        st.error("❌ 정답이 아닙니다. 보이지 않는 뒤쪽에 숨겨진 쌓기나무가 있는지 다시 확인해 보세요!")
