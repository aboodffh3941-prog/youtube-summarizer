import streamlit as st
import pypdf
import google.generativeai as genai

st.set_page_config(page_title="AI PDF & CV Analyzer", page_icon="📂", layout="centered")

st.title("📂 منصة تحليل وتلخيص ملفات الـ PDF والسير الذاتية بالذكاء الاصطناعي 🧠")
st.write("ارفع أي ملف (كتاب، مذكرة دراسية، أو سيرة ذاتية CV) ودع الذكاء الاصطناعي يحلله لك بدقة فائقة!")

# 🔐 ضع المفتاح الذي نسخته بين القوسين بالأسفل بدلاً من الكلمة المكتوبة
# تأكد من إبقاء علامات التنصيص موجودة مثل: "AIzaSy..."
GEMINI_API_KEY = "حط_المفتاح_اللي_نسخته_هنا"

if GEMINI_API_KEY == "حط_المفتاح_اللي_نسخته_هنا":
    st.warning("⚠️ مبرمج عبدالإله: فضلاً قم بوضع مفتاح الـ API الخاص بك داخل الكود ليشتغل الموقع بشكل حقيقي.")
    st.stop()

# إعداد الاتصال بجوجل جيميناي الحقيقي
genai.configure(api_key=GEMINI_API_KEY)

# زر رفع الملفات من الجهاز
uploaded_file = st.file_uploader("📤 اسحب وأفلت ملف PDF هنا:", type=["pdf"])

if uploaded_file is not None:
    st.success("🎯 تم رفع الملف بنجاح! جاري تحضيره للتحليل...")
    
    if st.button("🚀 ابدأ التحليل الاحترافي العميق"):
        with st.spinner("🧠 جاري قراءة نصوص الـ PDF وتحليلها عبر ذكاء Gemini الخارق..."):
            try:
                # 1. قراءة النص من ملف الـ PDF المرفوع برمجياً
                reader = pypdf.PdfReader(uploaded_file)
                full_text = ""
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        full_text += text + "\n"
                
                if len(full_text).strip() == 0:
                    st.error("❌ عذراً، لم نتمكن من استخراج نص من هذا الملف. تأكد أنه ليس ملفاً يحتوي على صور فقط.")
                    st.stop()
                
                # 2. إعداد ذكاء Gemini وتحليل النص بالكامل
                model = genai.GenerativeModel('gemini-1.5-flash')
                
                prompt = f"""
                أنت خبير ومحلل نصوص محترف. قم بقراءة وتحليل النص التالي المستخرج من ملف PDF بدقة فائقة:
                
                {full_text}
                
                بناءً على محتوى النص، إذا كان الملف (سيرة ذاتية CV) قم بعمل الآتي باللغة العربية:
                1. استخراج المهارات والخبرات الفعالية والتعليم.
                2. إعطاء تقييم منطقي للمرشح ونقاط القوة والضعف لديه.
                3. تقديم نصيحة ذهبية لتطوير سيرته الذاتية.
                
                أما إذا كان الملف (كتاب، مذكرة دراسية، أو مقال طويل) قم بعمل الآتي باللغة العربية:
                1. صياغة خلاصة تنفيذية ذكية وشاملة ومجردة من الهلوسة.
                2. كتابة أهم الأفكار الرئيسية على شكل نقاط واضحة.
                3. ابتكار 5 أسئلة ذكية ومتوقعة للاختبار أو المراجعة بناءً على هذا النص مع إجاباتها النموذجية.
                
                اجعل التنسيق جميلاً ومنظماً ومريحاً للقراءة.
                """
                
                response = model.generate_content(prompt)
                
                # 3. عرض النتيجة الفخمة للمستخدم
                st.markdown("---")
                st.subheader("📊 تقرير التحليل والتلخيص الذكي الحقيقي:")
                st.write(response.text)
                st.balloons()
                
            except Exception as e:
                st.error(f"⚠️ حدث خطأ أثناء التحليل. تأكد من أن مفتاح الـ API صحيخ.")
                
st.markdown("---")
st.caption("تم التطوير بكل حب بواسطة المبرمج عبدالإله 👑")
