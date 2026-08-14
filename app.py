import streamlit as st
import sympy as sp

st.set_page_config(
    page_title="AI 수학 선생님",
    page_icon="📚",
    layout="centered"
)

st.markdown("""
<style>

.block-container {
    max-width: 600px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.main-title {
    text-align: center;
    font-size: 32px;
    font-weight: 700;
    margin-bottom: 8px;
}

.subtitle {
    text-align: center;
    font-size: 16px;
    margin-bottom: 30px;
}

.section-box {
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #eeeeee;
    margin-top: 15px;
    margin-bottom: 15px;
}

.button-text {
    text-align: center;
    font-size: 18px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="main-title"> 📚 AI 수학 선생님</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">사진 한 장으로 시작하는 수학 문제 풀이</div>',
    unsafe_allow_html=True
)
# -------------------------
# 1. 문제 사진 업로드
# -------------------------

st.markdown(
    '<div class="section-box">'
    '<div class="button-text">🖼️ 사진 업로드</div>'
    '</div>',
    unsafe_allow_html=True
)

st.write("휴대폰이나 컴퓨터에 저장된 문제 사진을 선택해주세요!")

photo = st.file_uploader(
    "사진 선택하기",
    type=["jpg", "jpeg", "png"]
)

if photo:
    st.success("사진이 성공적으로 입력되었습니다!")
    st.image(photo, caption="입력한 문제")

st.markdown(
    '<div class="section-box">'
    '<div class="button-text">📷 문제 촬영</div>'
    '</div>',
    unsafe_allow_html=True
)

camera_photo = st.camera_input("카메라로 문제를 촬영하세요")

if camera_photo:
    st.success("사진이 성공적으로 촬영되었습니다!")
    st.image(camera_photo, caption="촬영한 문제")

st.divider()

st.subheader("📚 문제 유형을 선택하세요")

problem_type = st.selectbox(
    "문제 유형",
    ["이차방정식", "일차방정식", "일차부등식"]
)

# -------------------------
# 2. 문제 직접 입력
# -------------------------

st.subheader("문제 직접 입력")

if problem_type == "이차방정식":

    a = st.number_input(
        "x²의 계수",
        value=1,
        step=1
    )

    b = st.number_input(
        "x의 계수",
        value=-7,
        step=1
    )

    c = st.number_input(
        "상수항",
        value=12,
        step=1
    )

elif problem_type == "일차방정식":

    a = st.number_input(
        "x의 계수",
        value=2,
        step=1
    )

    d = st.number_input(
        "상수항",
        value=5,
        step=1
    )

    e = st.number_input(
        "오른쪽 값",
        value=13,
        step=1
    )

elif problem_type == "일차부등식":

    a = st.number_input(
        "x의 계수",
        value=2,
        step=1
    )

    d = st.number_input(
        "상수항",
        value=3,
        step=1
    )

    e = st.number_input(
        "오른쪽 값",
        value=7,
        step=1
    )

    inequality = st.selectbox(
        "부등호",
        [">", "<", ">=", "<="]
    )

# -------------------------
# 3. 문제 풀이
# -------------------------

if st.button("문제 풀기"):

    # -------------------------
    # 일차방정식
    # -------------------------
    if problem_type == "일차방정식":

        st.divider()
        st.subheader("📖 풀이 과정")

        # ax + d = e
        # ax = e - d
        # x = (e - d) / a

        if a == 0:
            st.error("x의 계수는 0이 될 수 없습니다.")

        else:
            result = round((e - d) / a, 2)

            st.write(
                "①",
                f"{a}x + {d} = {e}"
            )

            st.write(
                "②",
                f"{a}x = {e - d}"
            )

            st.write(
                "→ 양변에서",
                d,
                "를 빼었습니다."
            )

            st.write(
                "③",
                f"x = {e - d} ÷ {a}"
            )

            st.write(
                "④",
                f"x = {result}"
            )

            st.success(
                f"정답: x = {result}"
            )

   # -------------------------
    # 일차부등식
    # -------------------------
    elif problem_type == "일차부등식":

        st.divider()
        st.subheader("📖 풀이 과정")

        # ax + d > e
        # ax > e - d

        new_value = e - d

        st.write(
            "①",
            f"{a}x + {d} {inequality} {e}"
        )

        st.write(
            "②",
            f"{a}x {inequality} {new_value}"
        )

        st.write(
            "→ 양변에서",
            d,
            "를 빼었습니다."
        )

        # x의 계수가 양수인 경우
        if a > 0:

            result = new_value / a

            st.write(
                "③",
                f"x {inequality} {result}"
            )

            st.success(
                f"정답: x {inequality} {result}"
            )

        # x의 계수가 음수인 경우
        elif a < 0:

            result = new_value / a

            # 음수로 나누면 부등호 방향이 바뀜
            if inequality == ">":
                new_inequality = "<"
            elif inequality == "<":
                new_inequality = ">"
            elif inequality == ">=":
                new_inequality = "<="
            else:
                new_inequality = ">="

            st.write(
                "③",
                f"x {new_inequality} {result}"
            )

            st.write(
                "→ 음수로 나누었기 때문에 "
                "부등호 방향이 바뀌었습니다."
            )

            st.success(
                f"정답: x {new_inequality} {result}"
            )

        else:
            st.error(
                "x의 계수는 0이 될 수 없습니다."
            )

    # -------------------------
    # 이차방정식
    # -------------------------
    elif problem_type == "이차방정식":

        st.divider()
        st.subheader("📖 풀이 과정")

        # 원래 문제 표시
        st.write(
            f"① {a}x² + ({b})x + ({c}) = 0"
        )

        # 인수분해가 가능한지 확인
        found = False

        if a == 1:

            for m in range(-abs(c), abs(c) + 1):
                for n in range(-abs(c), abs(c) + 1):

                    if m * n == c and m + n == b:

                        found = True

                        # 부호에 맞게 인수 표시
                        if m >= 0:
                            first = f"(x + {m})"
                        else:
                            first = f"(x - {abs(m)})"

                        if n >= 0:
                            second = f"(x + {n})"
                        else:
                            second = f"(x - {abs(n)})"

                        st.write(
                            "② 인수분해를 이용합니다."
                        )

                        st.write(
                            f"   {first}{second} = 0"
                        )

                        st.write(
                            f"③ {first} = 0 또는 {second} = 0"
                        )

                        st.write(
                            f"④ x = {-m} 또는 x = {-n}"
                        )

                        st.success(
                            f"정답: x = {-m} 또는 x = {-n}"
                        )

                        break

                if found:
                    break

        # 인수분해가 되지 않는 경우
        if not found:

            st.write(
                "② 인수분해가 어려우므로 근의 공식을 이용합니다."
            )

            # 판별식 계산
            discriminant = pow(b, 2) - 4 * a * c

            st.write(
                "③ 인수분해가 어려운 경우에는 근의 공식을 사용합니다."
                )

            st.write(
                "근의 공식에 사용하기 위해 먼저 판별식을 계산합니다."
                )

            st.write(
                "판별식: D = b² - 4ac"
                )

            st.write(
                f"D = ({b})² - 4 × ({a}) × ({c})"
                )

            st.write(
                f"D = {pow(b, 2)} - {4 * a * c}"
                )
            
            st.write(
                f"D = {discriminant}"
                )
            
            if discriminant > 0:

                x1 = sp.simplify(
                    (-b + sp.sqrt(discriminant)) / (2 * a)
                )

                x2 = sp.simplify(
                    (-b - sp.sqrt(discriminant)) / (2 * a)
                )

                st.write(
                    "④ 근의 공식에 대입합니다."
                )

                st.write(
                    "x = (-b ± √(b² - 4ac)) / 2a"
                )

                st.write("⑤ 근의 공식의 계산 결과:")

                answer1 = sp.latex(x1, order="none")
                answer2 = sp.latex(x2, order="none")

                st.success(
                    f"**정답**  \n\n"
                    f"$x = {answer1}$  또는  $x = {answer2}$"
                )

                    
            elif discriminant == 0:

                x = -b / (2 * a)
                x = round(x, 2)

                st.write(
                    "④ 근의 공식에 대입합니다."
                )

                st.write(
                    f"⑤ x = {x}"
                )

                st.success(
                    f"정답: x = {x}"
                )

            else:

                st.write(
                    "④ 판별식이 0보다 작으므로 "
                    "실수 범위에서는 해가 없습니다."
                )

                st.info(
                    "정답: 실수 범위에서 해가 없습니다."
                )

# -------------------------
# 4. 질문 기능
# -------------------------

st.divider()

st.subheader("💬 모르는 부분을 질문해보세요!")

question = st.text_input(
    "궁금한 내용을 입력하세요",
    placeholder="예: 왜 여기서 인수분해를 해요?"
)

if question:
    st.write(f"질문: {question}")

    if "왜 근의 공식" in question:

        st.success(
            """
            **왜 근의 공식을 사용하나요?**

            이차방정식은 인수분해를 이용하면
            비교적 쉽게 풀 수 있습니다.

            하지만 모든 이차방정식이
            간단하게 인수분해되는 것은 아닙니다.

            따라서 인수분해가 어렵거나
            인수분해가 되지 않는 경우에는
            대부분의 이차방정식에 적용할 수 있는
            근의 공식을 이용하여 해를 구합니다.

            즉,

            인수분해 가능 → 인수분해 이용

            인수분해가 어려움 → 근의 공식 이용
            """
            )
        
    elif "근의 공식" in question:

        st.success(
            """
            **근의 공식이란?**

            이차방정식의 해를 구할 때 사용하는 공식이에요.

            이차방정식

            ax² + bx + c = 0

            에서 a, b, c의 값을 공식에 넣으면
            x의 값을 구할 수 있어요.
 
            근의 공식은

            x = (-b ± √(b² - 4ac)) / 2a

            입니다.

            인수분해가 어렵거나 인수분해하기 힘든
            이차방정식을 풀 때 사용할 수 있어요.
            """
        )

    elif "인수분해" in question:
        st.success(
            """
            **인수분해란?**

            하나의 식을 여러 개의 식의 곱으로 나타내는 방법이에요.

            예를 들어,

            x² - 7x + 12

            를

            (x - 3)(x - 4)

            로 나타낼 수 있어요.
            """
        )

    elif "판별식" in question:
         st.success(
            """
            **판별식이란?**

            이차방정식의 해가 몇 개인지 판단할 때 사용하는 식이에요.

            판별식은 다음과 같이 계산합니다.

            D = b² - 4ac

            이차방정식 ax² + bx + c = 0에서
            a, b, c의 값을 판별식에 대입합니다.
     
            • D > 0 → 서로 다른 두 개의 실수 해

            • D = 0 → 하나의 실수 해
            
            • D < 0 → 실수 범위에서 해가 없음

            따라서 근의 공식을 사용하기 전에
            판별식을 계산하면 해의 개수를 알 수 있어요.
            """
        )

    else:
        st.info(
            """
            아직 이 질문에 대한 설명 데이터가 없어요.

            다음 단계에서는 AI를 연결해서
            다양한 질문에 답할 수 있도록 만들 예정입니다.
            """
        )

# -------------------------
# 5. 자주 하는 실수
# -------------------------

st.divider()

if st.button("💡 사람들이 많이 하는 실수"):

    st.warning(
        """
        **자주 하는 실수**

        • 부호를 잘못 계산하는 경우

        • 인수분해 과정에서 숫자를 잘못 찾는 경우

        • 방정식을 풀 때 부호를 바꾸는 것을 놓치는 경우

        • 최종 답을 확인하지 않는 경우
        """
    )