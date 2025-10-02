import streamlit as st

# --------------------------------------------------------------------------
# 중요: 이 파일을 저장할 때 반드시 'UTF-8' 인코딩으로 저장해주세요.
# (대부분의 코드 에디터는 기본값이 UTF-8 입니다.)
# --------------------------------------------------------------------------


# 페이지 기본 설정
st.set_page_config(
    page_title="중학도형 총정리",
    page_icon="✔️",
    layout="centered"
)

# --- 각 주제별 내용 함수 (가장 안정적인 방식으로 재구성) ---

def show_parallel_lines():
    st.header("✔️ 평행선의 성질")
    st.markdown("---")
    
    st.subheader("1. 기본 용어 정의")
    st.write("🔹 **평행선**: 한 평면 위에서 서로 만나지 않는 두 직선입니다.")
    st.write("🔹 **동위각**: 서로 같은 위치에 있는 각의 쌍을 말합니다.")
    st.write("🔹 **엇각**: 서로 엇갈린 위치에 있는 각의 쌍을 말합니다.")
    st.write("🔹 **동측내각**: 같은 쪽에 있는 안쪽 각의 쌍을 말합니다.")
    st.markdown("---")

    st.subheader("2. 평행선의 핵심 성질")
    st.markdown("두 직선이 **서로 평행하다면**, 다음 성질이 항상 성립합니다.")
    st.success("1. 동위각의 크기는 서로 같다.")
    st.success("2. 엇각의 크기는 서로 같다.")
    st.success("3. 동측내각의 크기의 합은 180°이다.")
    st.markdown("---")
    
    st.subheader("3. 평행선이 되기 위한 조건")
    st.markdown("반대로, 아래 조건 중 하나라도 만족하면 두 직선은 **서로 평행**합니다.")
    st.info("1. 동위각의 크기가 서로 같을 때")
    st.info("2. 엇각의 크기가 서로 같을 때")
    st.info("3. 동측내각의 크기의 합이 180°일 때")


def show_similarity():
    st.header("✔️ 삼각형의 닮음")
    st.markdown("---")

    st.subheader("1. 닮음의 정의")
    st.write("🔹 **닮음**: 한 도형을 일정한 비율로 확대 또는 축소하여 다른 도형과 완전히 포갤 수 있는 관계입니다.")
    st.write("🔹 **닮음비**: 서로 닮은 두 도형에서 대응하는 변의 길이의 비입니다.")
    st.write("🔹 **성질**: 닮은 도형끼리는 대응하는 각의 크기가 각각 같고, 대응변의 길이의 비(닮음비)는 일정합니다.")
    st.markdown("---")
    
    st.subheader("2. 삼각형의 닮음 조건")
    st.markdown("두 삼각형은 다음 세 조건 중 하나만 만족하면 서로 닮음입니다.")
    st.success("1. SSS 닮음: 세 쌍의 대응변의 길이의 비가 모두 같을 때")
    st.success("2. SAS 닮음: 두 쌍의 대응변의 길이의 비가 같고, 그 끼인각의 크기가 같을 때")
    st.success("3. AA 닮음: 두 쌍의 대응각의 크기가 각각 같을 때")
    st.markdown("---")

    st.subheader("3. 직각삼각형의 닮음 활용")
    st.markdown(r"직각삼각의 꼭짓점 A($\angle A=90^\circ$)에서 빗변 BC에 수선의 발 H를 내리면, 다음 공식들이 성립합니다.")
    st.info("첫 번째 공식")
    st.latex(r"\overline{AB}^2 = \overline{BH} \times \overline{BC}")
    st.info("두 번째 공식")
    st.latex(r"\overline{AC}^2 = \overline{CH} \times \overline{CB}")
    st.info("세 번째 공식")
    st.latex(r"\overline{AH}^2 = \overline{BH} \times \overline{CH}")
    st.info("넓이 공식 (소 공식)")
    st.latex(r"\overline{AB} \times \overline{AC} = \overline{BC} \times \overline{AH}")

def show_area_bisector():
    st.header("✔️ 넓이의 비와 각의 이등분선")
    st.markdown("---")

    st.subheader("1. 높이가 같은 두 삼각형의 넓이의 비")
    st.markdown("**높이가 같은** 두 삼각형이 있을 때, 두 삼각형의 **넓이의 비**는 **밑변의 길이의 비**와 같습니다.")
    st.success("넓이의 비 = 밑변의 길이의 비")
    st.write("🔹 활용: 삼각형의 한 중선(꼭짓점과 대변의 중점을 이은 선)은 그 삼각형의 넓이를 정확히 이등분합니다.")
    st.markdown("---")
    
    st.subheader("2. 삼각형의 각의 이등분선 정리")
    st.markdown(r"$\triangle ABC$에서,")
    
    st.info("내각의 이등분선")
    st.markdown(r"""
    꼭짓점 A의 내각을 이등분하는 선이 변 BC와 만나는 점을 D라고 하면, 다음 비례식이 성립합니다.
    $$
    \overline{AB} : \overline{AC} = \overline{BD} : \overline{CD}
    $$
    """)
    
    st.info("외각의 이등분선")
    st.markdown(r"""
    꼭짓점 A의 외각을 이등분하는 선이 변 BC의 연장선과 만나는 점을 D라고 하면, 다음 비례식이 성립합니다.
    $$
    \overline{AB} : \overline{AC} = \overline{BD} : \overline{CD}
    $$
    """)
    
def show_circle_tangent():
    st.header("✔️ 원과 접선")
    st.markdown("---")
    
    st.subheader("1. 용어의 정의")
    st.write("🔹 **접선**: 원과 오직 한 점에서 만나는 직선")
    st.write("🔹 **접점**: 원과 접선이 만나는 바로 그 점")
    st.write("🔹 **접한다**: 원과 직선이 한 점에서 만나는 상태")
    st.markdown("---")
    
    st.subheader("2. 원의 접선의 핵심 성질")
    st.success("1. 원의 중심에서 접점을 이은 반지름은 접선과 수직(90°)이다.")
    st.success("2. 원 밖의 한 점에서 원에 그은 두 접선의 길이는 서로 같다.")
    st.markdown("---")
    
    st.subheader("3. 내접원과 외접사각형")
    st.info("삼각형의 내접원")
    st.write("삼각형의 넓이는 내접원의 반지름과 삼각형의 둘레를 이용하여 구할 수 있습니다.")
    st.latex(r"\text{넓이} = \frac{1}{2} \times (\text{내접원 반지름}) \times (\text{삼각형 둘레})")
    
    st.info("원에 외접하는 사각형")
    st.write("원에 외접하는 사각형은 마주보는 두 변의 길이의 합이 서로 같습니다.")
    st.latex(r"(\text{윗변}) + (\text{아랫변}) = (\text{왼쪽 변}) + (\text{오른쪽 변})")

def show_circle_angles():
    st.header("✔️ 원주각과 중심각")
    st.markdown("---")

    st.subheader("1. 용어의 정의")
    st.write("🔹 **중심각**: 원의 중심과 한 호의 양 끝점을 이어서 만든 각")
    st.write("🔹 **원주각**: 원 위의 한 점과 한 호의 양 끝점을 이어서 만든 각")
    st.markdown("---")

    st.subheader("2. 원주각의 핵심 성질")
    st.success("1. 하나의 호에 대한 원주각의 크기는 중심각 크기의 절반(1/2)이다.")
    st.success("2. 같은 호에 대한 원주각의 크기는 모두 같다.")
    st.success("3. 반원에 대한 원주각의 크기는 항상 90°이다.")
    st.markdown("---")

    st.subheader("3. 원에 내접하는 사각형의 성질")
    st.markdown("네 꼭짓점이 모두 한 원 위에 있는 사각형을 말합니다.")
    st.info("1. 마주보는 두 내각(대각)의 크기의 합은 항상 180°이다.")
    st.info("2. 사각형의 한 외각의 크기는 그와 이웃한 내각의 맞은편 각(내대각)의 크기와 같다.")
    
def show_centers():
    st.header("✔️ 외심, 내심, 무게중심")
    st.markdown("---")

    st.subheader("1. 외심 (Circumcenter)")
    st.info("정의: 삼각형의 **세 변의 수직이등분선**의 교점")
    st.write("🔹 **특징**: 외접원(세 꼭짓점을 지나는 원)의 중심입니다.")
    st.write("🔹 **핵심 성질 1**: 외심에서 세 꼭짓점까지의 거리는 모두 같습니다. (외접원의 반지름)")
    st.write("🔹 **핵심 성질 2**: 직각삼각형의 외심은 **빗변의 중점**에 위치합니다.")
    st.markdown("---")

    st.subheader("2. 내심 (Incenter)")
    st.info("정의: 삼각형의 **세 내각의 이등분선**의 교점")
    st.write("🔹 **특징**: 내접원(세 변에 모두 접하는 원)의 중심입니다.")
    st.write("🔹 **핵심 성질 1**: 내심에서 세 변까지의 거리는 모두 같습니다. (내접원의 반지름)")
    st.write("🔹 **핵심 성질 2**: 내심은 항상 삼각형의 내부에 있습니다.")
    st.markdown("---")

    st.subheader("3. 무게중심 (Centroid)")
    st.info("정의: 삼각형의 **세 중선**(꼭짓점과 대변의 중점을 이은 선)의 교점")
    st.write("🔹 **특징**: 삼각형의 균형점(무게의 중심) 역할을 합니다.")
    st.write("🔹 **핵심 성질 1**: 무게중심은 중선의 길이를 꼭짓점으로부터 **2 : 1**로 나눕니다.")
    st.write("🔹 **핵심 성질 2**: 세 개의 중선은 삼각형의 넓이를 정확히 **6등분**합니다.")


# --- 메인 앱 구성 ---

st.title("✔️ 중학도형 핵심 개념 총정리 (안정화 버전)")
st.write("개념이 깨지지 않도록 안정성을 최우선으로 만든 버전입니다. 아래 버튼을 눌러 학습을 시작하세요.")

# session_state 초기화
if 'topic' not in st.session_state:
    st.session_state.topic = None

# 버튼 배치
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("① 평행선의 성질", use_container_width=True): st.session_state.topic = 'parallel'
    if st.button("④ 원과 접선", use_container_width=True): st.session_state.topic = 'tangent'
with col2:
    if st.button("② 삼각형의 닮음", use_container_width=True): st.session_state.topic = 'similarity'
    if st.button("⑤ 원주각과 중심각", use_container_width=True): st.session_state.topic = 'circle_angle'
with col3:
    if st.button("③ 넓이의 비와 각의 이등분선", use_container_width=True): st.session_state.topic = 'area_bisector'
    if st.button("⑥ 외심, 내심, 무게중심", use_container_width=True): st.session_state.topic = 'centers'

st.markdown("---")

# 선택된 주제에 맞는 함수 호출
if st.session_state.topic:
    if st.session_state.topic == 'parallel': show_parallel_lines()
    elif st.session_state.topic == 'similarity': show_similarity()
    elif st.session_state.topic == 'area_bisector': show_area_bisector()
    elif st.session_state.topic == 'tangent': show_circle_tangent()
    elif st.session_state.topic == 'circle_angle': show_circle_angles()
    elif st.session_state.topic == 'centers': show_centers()