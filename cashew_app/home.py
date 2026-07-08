import streamlit as st

def home_page():

    # Background + Box Styles
    st.markdown("""
    <style>
    .stApp {   
        background-image: url("https://png.pngtree.com/thumb_back/fh260/background/20231017/pngtree-top-view-of-cashew-apple-and-cashew-seeds-arranged-on-a-image_13632717.png");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }

    .center-box {
        background: rgba(0, 0, 0, 0.55);
        width: 600px;
        margin: auto;
        margin-top: 140px;
        padding: 50px;
        border-radius: 20px;
        text-align: center;
        color: white;
        backdrop-filter: blur(8px);
    }

    .start-btn {
        background-color: #ffcc00;
        padding: 15px 36px;
        border-radius: 30px;
        font-size: 22px;
        border: none;
        cursor: pointer;
        animation: float 2s infinite ease-in-out;
        font-weight: bold;
    }

    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
    }

    .start-btn:hover {
        background-color: #ffe680;
    }
    
    </style>
    """, unsafe_allow_html=True)

    # UI Box
    st.markdown("""
    <div class="center-box">
        <h1> AI-Driven Cashew Nut Classification</h1>    
    </div>
    """, unsafe_allow_html=True)

    # Center “Get Started”
    st.markdown("""
<style>
.stButton > button {
    background-color: #f7d400 !important;   /* Yellow */
    color: black !important;
    border-radius: 10px;
    padding: 12px 24px;
    font-weight: bold;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

    st.write("")
    st.write("")
    centered = st.columns([3,3,3])
    with centered[1]:
        if st.button(" Get Started", use_container_width=True):
            st.session_state.step = 1
            st.rerun()