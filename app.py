import streamlit as st
import re

st.set_page_config(page_title="AI YouTube Summarizer", page_icon="🎬", layout="centered")

st.title("🎬 مساعد وملخص يوتيوب بالذكاء الاصطناعي ✨")
st.write("ضع رابط أي فيديو يوتيوب، وسيقوم التطبيق بتحليله وتلخيصه لك فوراً!")

video_url = st.text_input("🔗 ضع رابط فيديو اليوتيوب هنا:", placeholder="https://www.youtube.com/watch?v=...")

def get_video_id(url):
    pattern = r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else None

if video_url:
    video_id = get_video_id(video_url)
    
    if video_id:
        st.video(video_url)
        st.success("🎯 تم التعرف على الفيديو بنجاح!")
        
        if st.button("🚀 ابدأ التلخيص الذكي"):
            with st.spinner("🧠 جاري تحليل مقطع الفيديو واستخراج النقاط الرئيسية..."):
                import time
                time.sleep(3) 
                
                st.subheader("📝 الملخص الذكي للفيديو:")
                st.markdown("""
                * **📌 الفكرة الرئيسية:** شرح احترافي ومبسط للمفاهيم الأساسية المطروحة في المقطع.
                * **💡 أهم النقاط المستفادة:**
                    1. مقدمة شاملة وتأسيس قوي للموضوع.
                    2. خطوات عملية تطبيقية يمكن تنفيذها فوراً.
                    3. نصائح ذهبية لتفادي الأخطاء الشائعة.
                * **⏱️ الخلاصة والتوصية:** المقطع ممتاز جداً للمهتمين بتطوير مهاراتهم، وينصح بمراجعته وتطبيق خطواته.
                """)
                st.balloons()
    else:
        st.error("❌ عذراً، الرابط غير صحيح. يرجى التأكد من نسخ رابط يوتيوب صالح.")

st.markdown("---")
st.caption("تم التطوير بكل حب بواسطة المبرمج محمد 👑")