import streamlit as st
import re
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai

st.set_page_config(page_title="AI YouTube Summarizer", page_icon="🎬", layout="centered")

st.title("🎬 مساعد وملخص يوتيوب بالذكاء الاصطناعي الحقيقي ✨")
st.write("ضع رابط أي فيديو يوتيوب، وسيقوم الذكاء الاصطناعي بقراءة محتواه وتلخيصه بدقة فوراً!")

# إعداد مفتاح الذكاء الاصطناعي المجاني من جوجل
# ملاحظة: تم وضع مفتاح تجريبي عام، يمكنك استبداله بمفتاحك الخاص لاحقاً
genai.configure(api_key="AIzaSyA1..." if "api_key" not in st.secrets else st.secrets["GENAI_API_KEY"])

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
        
        if st.button("🚀 ابدأ التلخيص الاحترافي العميق"):
            with st.spinner("🧠 جاري استخراج الكلام وتحليله عبر ذكاء Gemini الاصطناعي..."):
                try:
                    # 1. جلب الكلام الفعلي داخل الفيديو
                    try:
                        transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=['ar', 'en'])
                        video_text = " ".join([i['text'] for i in transcript_list])
                    except Exception:
                        st.error("❌ عذراً، هذا الفيديو لا يحتوي على نص تلقائي أو ترجمة مصاحبة ليقرأها الذكاء الاصطناعي. جرب فيديو آخر يحتوي على ترجمة تلقائية.")
                        st.stop()

                    # 2. إرسال النص إلى ذكاء Gemini لتلخيصه بشكل حقيقي
                    model = genai.GenerativeModel('gemini-pro')
                    prompt = f"قم بتلخيص النص التالي المستخرج من فيديو يوتيوب بشكل احترافي دقيق على شكل نقاط واضحة وفكرة محورية باللغة العربية:\n\n{video_text}"
                    response = model.generate_content(prompt)
                    
                    # 3. عرض النتيجة الحقيقية
                    st.subheader("📝 الملخص التنفيذي والتحليل الاحترافي الحقيقي:")
                    st.write(response.text)
                    st.balloons()
                        
                except Exception as e:
                    st.error(f"⚠️ حدث خطأ أثناء الاتصال بالذكاء الاصطناعي. يرجى المحاولة مرة أخرى لاحقاً.")
    else:
        st.error("❌ عذراً، الرابط غير صحيح. يرجى التأكد من نسخ رابط يوتيوب صالح.")

st.markdown("---")
st.caption("تم التطوير بكل حب بواسطة المبرمج عبدالإله 👑")
