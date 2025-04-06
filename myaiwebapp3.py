import streamlit as st
import GT
import cv2
from stability_ai import text2image

api_key = "AIzaSyCMhLs7vX1h9laRoJDvIwj0_WiwoATwsIM"
engine_id = "stable-diffusion-v1-6"
filename_save = "image_out.jpg"

st.title("สร้างภาพจากข้อความ")

# รับ prompt จากผู้ใช้
prompt_th = st.text_input("ป้อน prompt ภาษาไทย:")

# ตัวเลือกสไตล์ภาพ
ch = st.selectbox("เลือกรูปแบบ", (
    "watercolor painting",
    "cartoon line drawing",
    "flat cartoon illustration",
    "sticker",
    "3d rendering",
    "kid crayon drawing"))

# เมื่อกดปุ่ม
if st.button("สร้างภาพ"):
    if prompt_th.strip() == "":
        st.warning("กรุณาป้อนข้อความก่อนสร้างภาพ")
    else:
        try:
            # แปลข้อความเป็นอังกฤษ
            prompt_en = GT.translate(prompt_th, 'th', 'en')
            final_prompt = prompt_en + " , " + ch
            st.text(f"Prompt ภาษาอังกฤษ: {final_prompt}")

            # สร้างภาพ
            with st.spinner("กำลังสร้างภาพ..."):
                text2image(api_key, engine_id, final_prompt, filename_save)

            # โหลดและแสดงภาพ
            img = cv2.imread(filename_save)
            if img is not None:
                st.image(img, channels="BGR")
            else:
                st.error("ไม่สามารถโหลดภาพที่สร้างได้")
        except Exception as e:
            st.error(f"เกิดข้อผิดพลาด: {e}")






    



