import streamlit as st
import random
import time

st.set_page_config(page_title="Surprise Box 🎁", layout="centered")

# 🎨 Custom CSS
st.markdown("""
    <style>
    .stApp { text-align: center; background: linear-gradient(120deg, #f9d6eb, #d6f9f0); }
    .big-title { font-size: 36px; font-weight: bold; color: #ff2e63; }
    .box {
        font-size: 22px;
        background: white;
        padding: 20px;
        border-radius: 20px;
        display: inline-block;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        margin-top: 20px;
        max-width: 600px;
    }
    button {
        border-radius: 12px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 📝 User input
user_name = st.text_input("Your Name 💖:")

# 😂 Jokes (15+)
jokes =  [
    "👩‍🏫 Teacher: Tum late kyu aaye?\n😅 Pappu: Sir, board pe likha tha 'School Ahead, Go Slow'...\n🤣 to main dheere aaya!",
    "👩 Wife: Suno ji, main mar gayi to kya karoge?\n😅 Husband: Main bhi pagal ho jaunga… shaadi kar lunga!",
    "😂 Santa: Doctor sahab, mujhe bhoolne ki bimaari hai!\n👨‍⚕️ Doctor: Kab se?\n😅 Santa: Kab se kya?",
    "😆 Pappu: Sir, mera dimaag computer jaisa hai!\n👨‍🏫 Teacher: Kaunsa Windows?\n😅 Pappu: Nahi sir, hamesha 'Hang' ho jata hai!",
    "👮 Police: Tumne seat belt kyun nahi pehni?\n😅 Driver: Sir, main to destiny pe believe karta hoon!",
    "🤣 Husband: Tum mujhe chhod ke chali gayi to main kya karunga?\n😅 Wife: Phir tumne kya karna hai, main to khush ho jaungi!",
    "😂 Teacher: Batao, AC ka full form?\n😅 Student: Aayi Chutti!",
    "🤣 Santa: Ek ladki ne mujhe apna number diya...\n😅 Banta: Kya baat hai!\nSanta: Lekin usne bola tha 'Emergency ke liye'!",
    "😅 Pappu: Papa mujhe bike chahiye!\n👨 Papa: Paise nahi hai beta.\n😅 Pappu: To ped pe paise uga do!",
    "😂 Biwi: Tum mujhe kahan le jaoge shaadi ke baad?\n😅 Pati: Jahan tum chaho!\n😂 Biwi: To chalo mummy ke ghar hi rahte hain!",
    "🤣 Student: Sir, mera pen kho gaya.\n👨‍🏫 Teacher: To tumhe punishment milegi.\n😅 Student: Lekin sir, pen to 'Pilot' tha, to woh ud gaya!",
    "😂 Santa: Train late kyu hai?\n👮 Guard: Engine mobile charge kar raha hai!",
    "🤣 Pappu: Sir, light gayi to kya karna chahiye?\n👨‍🏫 Teacher: Candles jalani chahiye.\n🤣 Pappu: Lekin sir, cake kahan se laun?",
    "😅 Wife: Tum mujhe kab surprise doge?\n😄 Husband: Jab tum phone silent pe rakhogi!",
    "🤣 Teacher: Homework kyu nahi kiya?\n😅 Student: Sir, wifi slow tha!",
    "😂 Pappu: Mujhe neend nahi aa rahi!\n🤣 Dost: Mobile side me rakh aur aankh bandh kar!",
    "😆 Boyfriend: Tum mujhe kab shaadi karogi?\n😅 Girlfriend: Jab tum mujhe battery ka backup doge!",
    "🤣 Santa: Mere phone mein balance khatam ho gaya!\n😅 Banta: Kya karun?\nSanta: Recharge kar de, dosti nibha!",
    "😂 Teacher: Sooraj kaha se nikalta hai?\n😅 Student: Neighbor ke ghar se!",
    "🤣 Biwi: Tum mujhe khush kyun nahi rakhte?\n😅 Pati: Khud try kyun nahi karti?",
    "😂 Pappu: Papa mujhe girlfriend chahiye!\n😡 Papa: Maar khayega?\n🤣 Pappu: Ji, wahi to girlfriend ka kaam hai!",
    "😅 Santa: Mujhe English nahi aati!\n🤣 Banta: Toh WhatsApp pe likhta kyu hai!",
    "🤣 Husband: Tum kitna pyar karte ho?\n😅 Husband: Jab tak wifi chal raha ho!",
    "😂 Teacher: Computer ka baap kaun?\n😅 Student: Data!",
    "🤣 Friend: Exam me kaisa likha?\n😅 Dost: Pen hi chal raha tha, dimaag off tha!",
    "😂 Wife: Aaj khana kaisa tha?\n😅 Husband: Taste Google pe search karna padega!",
    "🤣 Santa: Main exercise karta hu.\n😅 Banta: Kaunsi?\n😂 Santa: Phone charge karte waqt plug lagana!",
    "😅 Student: Sir, mera dimaag bandh ho jata hai!\n👨‍🏫 Teacher: To chalu karke kaam kar!",
    "😂 Pappu: Mumma, mera test achha gaya!\n👩 Mumma: Kaise pata?\n😅 Pappu: Marks to abhi aayenge, par main khush hoon!",
    "🤣 Wife: Tum mujhse kitna pyar karte ho?\n😅 Husband: Google se zyada… woh mere liye search karta hai!",
    "😂 Santa: Mere ghar ka wifi slow hai!\n😅 Banta: To router ko chai pila do!",
    "🤣 Teacher: Tumhara favorite subject kaunsa hai?\n😅 Student: Break time!",
    "😂 Pappu: Maa, main kal hero banunga!\n👩 Maa: Kaise?\n😅 Pappu: Movie dekh kar!",
    "🤣 Husband: Tumhara birthday kya chahiye?\n😅 Wife: Bas tumhara time chahiye!\n😂 Husband: To tum mujhe silent mode me daal do!",
    "😅 Santa: Mere paas itna kaam hai!\n🤣 Banta: To list bana lo.\n😅 Santa: List bhi kal karunga, aaj to relax!",
    "😂 Teacher: Tumhara naam aur roll no. bolo.\n😅 Student: Sir, roll no. bhool gaya… naam type kar do!",
    "🤣 Pappu: Sir, mera homework doge?\n👨‍🏫 Teacher: Homework to tumne de diya, ab duplikate banana mushkil hai!",
    "😂 Wife: Tum mujhe khush kaise rakhte ho?\n😅 Husband: Bas khaana khila kar, sab theek ho jata hai!",
    "🤣 Santa: Main jald amir banunga!\n😅 Banta: Kaise?\n😂 Santa: Lottery ticket kharid kar… sapne me!",
    "😅 Doctor: Aapko kitni neend chahiye?\n🤣 Patient: Sir, Friday se Sunday tak full!",
    "😂 Pappu: Papa, mujhe cricket khelna hai!\n👨 Papa: Accha, par homework pehle.\n😅 Pappu: Papa cricket bhi homework me count hoga?",
    "🤣 Teacher: Aaj tumne kitna padha?\n😅 Student: Sir, aankhon se dekha to padha maana!",
    "😂 Wife: Tum mujhe jaldi se phone mil jaoge?\n😅 Husband: Haan, alarm laga do!",
    "🤣 Santa: Mere ghar me chhota fridge hai!\n😅 Banta: Kya rakha hai?\n😂 Santa: Sirf dreams!",
    "😅 Pappu: School me sab boring hai!\n🤣 Teacher: Toh tum khud interesting bano!",
    "😂 Husband: Tumhara favourite color kya hai?\n😅 Wife: Jo mera shopping bag match kare!",
    "🤣 Student: Sir, internet band ho gaya!\n😅 Teacher: Toh tum bhi break le lo!"
]
# 💖 Compliments
compliments =  [
    "✨ Tumhari smile pure room ko roshan kar deti hai!",
    "🌸 Tumhara dil bahut hi saaf aur sundar hai.",
    "💎 Tum ek rare diamond ki tarah ho, priceless!",
    "🌞 Tumhari energy sabko khush kar deti hai.",
    "🌹 Tumhari baaton me ek alag hi mithaas hai.",
    "🌟 Tum hamesha positive vibes laate ho.",
    "💖 Tumhara style sabse alag aur classy hai.",
    "🎶 Tumhari awaaz dil ko sukoon deti hai.",
    "🌈 Tumhare aas paas sab kuch colorful lagta hai.",
    "🔥 Tumhari confidence sabse alag hai.",
    "💎 Tumhari soch bahut hi unique hai.",
    "🌸 Tumhare dost bahut lucky hain tumhe paake.",
    "🌞 Tum din ka sabse bright hissa ho.",
    "🌹 Tumhe dekh kar lagta hai zindagi sundar hai.",
    "✨ Tum ek chhoti si duniya ho jo sabko pyaari lagti hai.",
    "🌟 Tumhari aankhen sach me chamakti hui taare hain.",
    "💖 Tumhare saath waqt udkar nikal jaata hai.",
    "🌈 Tumhare ideas bahut creative hote hain.",
    "🎶 Tum ek perfect melody jaisi ho.",
    "🌸 Tumhari kindness sabse badi strength hai."
]


# 🔮 Fortunes
fortunes = [
    "🍀 Tumhare liye ek naya moka aane wala hai.",
    "🌟 Jaldi hi tumhari mehnat rang layegi.",
    "💰 Aane wale dinon me paisa aur sukh dono milenge.",
    "🌸 Tumhari life me ek naya dost shamil hone wala hai.",
    "🔥 Tumhari passion tumhe safalta tak le jayegi.",
    "🌞 Tumhe ek aisa surprise milega jo tumhe khushi dega.",
    "🎯 Tumhara focus tumhe goal tak pahunchayega.",
    "🌈 Tumhari life me ek nayi beginning hone wali hai.",
    "💖 Tumhe jaldi hi apno ka pyaar aur support milega.",
    "🌹 Tumhara din aaj bahut lucky hoga.",
    "🌟 Tumhari soch tumhe naye raaste dikhayegi.",
    "✨ Tumhara ek sapna jaldi pura hoga.",
    "🎉 Tumhe khushiyon ki baarish milegi.",
    "🍀 Tumhari kismat tumhare saath hai.",
    "🔥 Tum ek naye safar par nikalne wale ho.",
    "🌸 Tumhe ek acchi khabar sunne ko milegi.",
    "🌞 Tumhari life me ek bada positive change aane wala hai.",
    "💎 Tumhara hard work waste nahi jaayega.",
    "🌈 Tumhari smile kisi aur ki life badal degi.",
    "🎯 Tum apne goals ko easily achieve kar loge."
]

# 🙌 Blessings
blessings = [
    "🙏 Bhagwan tumhe sada khush rakhe.",
    "🌸 Tumhari zindagi me hamesha sukh-shanti rahe.",
    "🌟 Tumhari mehnat hamesha rang laye.",
    "💖 Tumhe hamesha apno ka pyaar mile.",
    "🌈 Tumhari life hamesha colorful aur khushiyon se bhari ho.",
    "✨ Tumhara har din ek nayi umeed laye.",
    "🎉 Tumhe sada safalta aur khushi mile.",
    "🍀 Tumhari kismat hamesha chamakti rahe.",
    "🌞 Tumhari zindagi suraj ki roshni ki tarah roshan ho.",
    "🌹 Tumhara dil hamesha pyaar se bhara rahe.",
    "🔥 Tumhare raaste me kabhi andhera na ho.",
    "🌸 Tumhari family hamesha khush rahe.",
    "🌟 Tumhe sada sehat aur sukoon mile.",
    "💎 Tumhe hamesha acchi soch aur accha saath mile.",
    "🌈 Tumhari zindagi me kabhi kamee na ho.",
    "🎶 Tumhe hamesha sukoon aur chain mile.",
    "🌞 Tumhari rooh hamesha shanti me rahe.",
    "🌹 Tumhara har sapna pura ho.",
    "✨ Tumhe hamesha naye mauke milte rahe.",
    "🙏 Tumhari muskaan kabhi na mile."
]

# 🎲 Surprise Mix
def get_surprise():
    all_messages = jokes + compliments + fortunes + blessings
    return random.choice(all_messages)

# ⌨️ Typing animation
def type_text(text):
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(f"<div class='box'>{full_text}</div>", unsafe_allow_html=True)
        time.sleep(0.02)

# 🎁 Title
st.markdown("<div class='big-title'>🎁 Surprise Box</div>", unsafe_allow_html=True)

if user_name:
    st.success(f"नमस्ते {user_name}! चलो देखते हैं तुम्हारे लिए क्या मजेदार है 🎉")

    # Tabs
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["😂 Jokes", "💖 Compliments", "🔮 Fortunes", "🙌 Blessings", "🎲 Surprise Mix"])

    with tab1:
        if st.button("😂 Joke सुनो"):
            type_text(random.choice(jokes))

    with tab2:
        if st.button("💖 Compliment लो"):
            type_text(random.choice(compliments))

    with tab3:
        if st.button("🔮 Lucky Fortune"):
            type_text(random.choice(fortunes))

    with tab4:
        if st.button("🙌 Blessing लो"):
            type_text(random.choice(blessings))

    with tab5:
        if st.button("🎲 Surprise Mix"):
            st.balloons()
            type_text(get_surprise())
