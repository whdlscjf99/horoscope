import random
from datetime import date

import streamlit as st

st.set_page_config(page_title="오늘의 운세", page_icon="🔮")

ZODIACS = ["쥐띠", "소띠", "호랑이띠", "토끼띠", "용띠", "뱀띠",
           "말띠", "양띠", "원숭이띠", "닭띠", "개띠", "돼지띠"]

FORTUNES = [
    "다른 사람의 말에 휩쓸리지 말고 자신의 주관을 뚜렷하게 가지세요.",
    "작은 노력이 뜻밖의 좋은 결과로 돌아오는 날입니다.",
    "오래 미뤄둔 일을 시작하기에 좋은 날입니다.",
    "가까운 사람과의 대화에서 힌트를 얻게 됩니다.",
    "서두르면 실수하기 쉬우니 한 번 더 확인하세요.",
    "새로운 만남이 좋은 인연으로 이어질 수 있습니다.",
    "지출을 줄이고 계획적으로 움직이면 이득을 봅니다.",
    "몸의 신호에 귀 기울이세요. 충분한 휴식이 필요합니다.",
    "뜻밖의 칭찬을 듣게 되는 날입니다. 겸손하게 받아들이세요.",
    "고민하던 문제가 자연스럽게 풀리기 시작합니다.",
]

CLOSINGS = [
    "오늘도 행복하고 즐거운 하루 보내세요!",
    "작은 것에 감사하면 하루가 더 좋아집니다.",
    "웃는 얼굴이 행운을 부릅니다.",
    "저녁에는 좋아하는 음악을 들으며 쉬어보세요.",
]

COLORS = ["빨강", "주황", "노랑", "초록", "파랑", "보라", "하양", "검정"]

st.title("🔮 오늘의 운세 🔮")
st.write("띠를 선택하고 당신의 운세를 확인해 보세요!")

zodiac = st.selectbox("당신의 띠를 선택하세요:", ZODIACS)
st.divider()

if st.button("운세 보기", type="primary"):
    today = date.today()
    # 같은 날, 같은 띠는 항상 같은 운세가 나오도록 시드 고정
    rng = random.Random(f"{today.isoformat()}-{zodiac}")

    st.subheader(f"📅 {today.year}년 {today.month:02d}월 {today.day:02d}일")
    st.markdown(f"#### {zodiac}의 오늘의 운세")
    st.info("✨ " + rng.choice(FORTUNES))
    st.success(rng.choice(CLOSINGS))

    col1, col2 = st.columns(2)
    col1.metric("행운의 숫자", rng.randint(1, 45))
    col2.metric("행운의 색", rng.choice(COLORS))
