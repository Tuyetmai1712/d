import streamlit as st
import time
import random

# Page configuration
st.set_page_config(page_title="DLP4 RPG", layout="centered")

# Custom CSS for an RPG school theme
st.markdown("""
<style>
body {
    background-color: #f0f8ff;
    color: #333333;
    font-family: 'Courier New', monospace;
}
h1, h2, h3 {
    font-family: 'Courier New', monospace;
}
button {
    background-color: #8b4513;
    color: #ffffff;
}
</style>
""", unsafe_allow_html=True)

# Typewriter effect
def typewriter(text):
    placeholder = st.empty()
    displayed = ""
    for char in text:
        displayed += char
        placeholder.markdown(f"<p style='font-family: monospace; font-size:20px'>{displayed}</p>", unsafe_allow_html=True)
        time.sleep(0.02)

# Animal icons with learning-themed descriptions
animals = [
    ("🐢", "Bạn bền bỉ như rùa, từng bước vững vàng hoàn thành deadline."),
    ("🐶", "Bạn trung thành như chó, luôn sẵn sàng hỗ trợ đồng đội làm questionnaires."),
    ("🐱", "Bạn linh hoạt như mèo, thích khám phá mọi Class Days."),
    ("🦊", "Bạn khéo léo như cáo, biết cách hướng dẫn các bạn trong Class Days."),
    ("🐼", "Bạn dễ thương như gấu trúc, tạo không khí thoải mái khi thảo luận nhóm questionnaires."),
    ("🐵", "Bạn tinh nghịch như khỉ, mang đến nhiều ý tưởng sáng tạo cho làm questionnaires."),
    ("🦁", "Bạn dũng cảm như sư tử, luôn dẫn đầu khi tham gia bài tập nhóm questionnaires.")
]

# Staff selection mapping
staff_options = {
    4: {
        "Nguyễn Thị Thu Hà (Yoogi)": 7,
        "Nguyễn Thu Hương": 8,
        "Trịnh Thị Phương Uyên": 9,
        "Phan Mai Ngọc Linh": 10,
        "Trần Lê Khánh Chi": 11,
        "Lê Phương Nhi": 12,
        "Đỗ Lê Ngọc Minh": 13,
        "Đỗ Hoàng Gia Huy": 14,
        "Trần Triệu Vy": 15,
        "Phạm Nguyễn Thu Hà": 16,
        "Hoàng Bích Phượng": 17,
        "Trịnh Hoàng Nhật Lệ": 18,
        "Nguyễn Thị Thùy Trang": 19,
        "Hán Ngọc Bảo Trân": 20,
        "Nguyễn Đức Dương": 21,
        "Trần Anh Đức": 22,
        "Lý Hạnh Linh": 23,
        "Nguyễn Thị Khánh Linh": 24
    },
    5: {
        "Hoàng Thị Thảo Anh": 25,
        "Tá Mai Linh": 26,
        "Đỗ Minh Châu": 27,
        "Lê Chí Nam": 28,
        "Nguyễn Việt Anh": 29,
        "Đỗ Phương Anh": 30,
        "Trần Hoàng Thắng": 31,
        "Nguyễn Thảo Đan": 32,
        "Trần Thanh An": 33,
        "Nguyễn Tùng Lâm": 34,
        "Phạm Hà Phương": 35
    },
    6: {
        "Anh Trần Chí Trung": 36,
        "Đoàn Hoa Hạ": 37,
        "Phạm Tuyết Mai": 38,
        "Mai Minh Quân": 39
    }
}

# Full Scene contents
scenes = {
    1: [
        "Chào mừng bạn đến với DAV Leadership Programme – Summer Course 2025",
        "Một hành trình mới sắp bắt đầu, chúc bạn chân cứng đá mềm",
        "Mình là Phạm Tuyết Mai",
        "Mai trong Hoa Mai 🌸",
        "Tuyết trong Bông Tuyết ❄️",
        "Phạm là họ bố..........................",
        "Mình sẽ là Instructor đi cùng với bạn hết hành trình DLP4 này",
        "Cảm Ơn Vì Đã Đến"
    ],
    7: [
        "Tên: Nguyễn Thị Thu Hà (Yoogi)",
        "Ngày sinh: 19/11",
        "Cung hoàng đạo: Bọ Cạp",
        "Đặc điểm nhận dạng: Luôn bốc cháy, dâng hiến cả con tim",
        "Link FB: https://www.facebook.com/ha.yoongie.7/",
        "Lời chào đầu: Mình là Yoogie, mình thấy mình rất hài hước, mình thích được mang những câu joke vui vẻ đến với mọi người. Mình cung nước (Bọ Cạp) nên nhìn ngoài nhưng bên trong mềm nhũn."
    ],
    8: [
        "Tên: Nguyễn Thu Hương",
        "Ngày sinh: 11/07",
        "Cung hoàng đạo: Cự Giải",
        "Đặc điểm nhận dạng: Thích lượn nhờ phố cổ Hà Nội, ăn 1 lúc 2 suất",
        "Link FB: https://www.facebook.com/nguyenthuhuong1107",
        "Lời chào đầu: Bonjour, chao xìn cả nhà yêu của kem!!! Em/mình/chị là Thu Hương, or Hương 2 suất cơm (dù giờ tới mình vẫn chưa nhận được suất thứ 2!)"
    ],
    9: [
        "Tên: Trịnh Thị Phương Uyên",
        "Ngày sinh: 19/12",
        "Cung hoàng đạo: Nhân Mã",
        "Đặc điểm nhận dạng: Thích đi xe bus, là nhân vật trong một câu chuyện cổ tích",
        "Link FB: https://www.facebook.com/profile.php?id=100018092570083",
        "Lời chào đầu: Hi mọi ngừi, mình là Uyên Trịnh. Uyên trong Uyên Trịnh và Trịnh trong Uyên Trịnh. Rất vui khi cuối cùng đã được chung VUCA với mọi ngườii. VUCA trong Vui vẻ - Ung dung - Chân thành - An nhiên 😘"
    ],
    10: [
        "Tên: Phan Mai Ngọc Linh",
        "Ngày sinh: 09/01",
        "Cung hoàng đạo: Ma Kết",
        "Đặc điểm nhận dạng: Luôn đúng giờ, tìm thấy bình yên khi ngồi trước biển.",
        "Link FB: https://www.facebook.com/phan.maingoclinh0901",
        "Lời chào đầu: Chào chúng ta, mình là.........à mình là Ngọc Linh, mình vừa mới ngủ gật. Đêm nào ngủ mình cũng mơ về DLP..."
    ],
    11: [
        "Tên: Trần Lê Khánh Chi",
        "Ngày sinh: 06/09",
        "Cung hoàng đạo: Xử Nữ",
        "Đặc điểm nhận dạng: Thực hành lãnh đạo liên tục trên nền tảng điện tử",
        "Link FB: https://www.facebook.com/khanhchi.tranle",
        "Lời chào đầu: ."
    ],
    12: [
        "Tên: Lê Phương Nhi",
        "Ngày sinh: 07/12",
        "Cung hoàng đạo: Nhân Mã",
        "Đặc điểm nhận dạng: Không bao giờ được nằm trên giường khi đi bonding nhưng luôn là người ngồi lại cuối cùng với nồi lẩu",
        "Link FB: https://www.facebook.com/nhikan14723",
        "Lời chào đầu: Chào cả nhà, mình là Nhi, đệm Phương, họ Lê. Thông tin chi tiết hồi sau sẽ rõ. Welcome cả nhà đến với DLP4 và rất vui vì được đồng hành cùng mọi người trong quãng thời gian sắp tới. (*icon pháo hoa*)"
    ],
    13: [
        "Tên: Đỗ Lê Ngọc Minh",
        "Ngày sinh: 23/08",
        "Cung hoàng đạo: Xử Nữ",
        "Đặc điểm nhận dạng: Cứng cáp, vững vàng, thích đọc truyện, viết lách vẽ vời.",
        "Link FB: https://www.facebook.com/profile.php?id=100047347188105&mibextid=LQQJ4d",
        "Lời chào đầu: hihelloannyeongminhlangocminhcungsutunhinmathoicangnmathraminhbinhthuong"
    ],
    14: [
        "Tên: Đỗ Hoàng Gia Huy",
        "Ngày sinh: 28/12",
        "Cung hoàng đạo: Ma Kết",
        "Đặc điểm nhận dạng: Thích hiphop nên hay bị 'lộn ruột', nấu ăn rất ngon nhưng chỉ đứng sau giật dây",
        "Link FB: https://www.facebook.com/profile.php?id=100072990672246&mibextid=LQQJ4d",
        "Lời chào đầu: Hí chúng ta, mình là Jerry... đúng hơn là Gia Huy. Trải qua VUCA tinh thần lẫn thể chất, mình sẽ luôn có mặt để giúp đỡ (miễn là bạn muốn)."
    ],
    15: [
        "Tên: Trần Triệu Vy",
        "Ngày sinh: 12/10",
        "Cung hoàng đạo: Thiên Bình",
        "Đặc điểm nhận dạng: Từng đẩy 1 nam sinh bay 2m, có kinh nghiệm kết nối cảm xúc với người máy, cẩn thận bị brain rot khi tiếp xúc",
        "Link FB: https://www.facebook.com/trieuvy.tran.92560",
        "Lời chào đầu: Chào cả nhà, mình là Triệu Vy, thi trượt bằng lái xe 3 lần. Trượt ở đoạn đi thẳng nhưng vòng số 8 mình rất lụa. Ai cần hướng dẫn thì inbox nhé 🚕🚗🚌"
    ],
    16: [
        "Tên: Phạm Nguyễn Thu Hà",
        "Ngày sinh: 31/07",
        "Cung hoàng đạo: Sư Tử",
        "Đặc điểm nhận dạng: Mother material, cảnh báo nhiều tình cảm đang tiến về phía bạn",
        "Link FB: https://www.facebook.com/thuha.phamnguyen.9",
        "Lời chào đầu: Hi cả nhà, mình là Thu Hà, mình hay cười phà phà..."
    ],
    17: [
        "Tên: Hoàng Bích Phượng",
        "Ngày sinh: 12/03",
        "Cung hoàng đạo: Song Ngư",
        "Đặc điểm nhận dạng: 安 (An)",
        "Link FB: https://www.facebook.com/hoang.b.phuong.31?mibextid=ZbWKwL",
        "Lời chào đầu: Chào cả nhà, mình là Phượng. Ai nói gì cũng tin, hehe"
    ],
    18: [
        "Tên: Trịnh Hoàng Nhật Lệ",
        "Ngày sinh: 10/08",
        "Cung hoàng đạo: Sư Tử",
        "Đặc điểm nhận dạng: Giọt nước mắt rơi lúc hoàng hôn ở Nhật Bản vì cười quá nhiều",
        "Link FB: https://www.facebook.com/nhatle.trinhhoang",
        "Lời chào đầu: Mình là Japan Cry. Dù có Japan nhưng mình thích xem, nghe, đọc phim và show truyền hình Việt Nam"
    ],
    19: [
        "Tên: Nguyễn Thị Thùy Trang",
        "Ngày sinh: 28/09",
        "Cung hoàng đạo:Thiên Bình",
        "Đặc điểm nhận dạng: Nhẹ nhàng vững vàng, kiềm được mọi cơn sóng cứng đầu nhất.",
        "Link FB: https://www.facebook.com/trangs.thuys.9619",
        "Lời chào đầu: 67 104 195... (nội dung mã hóa như kịch bản)"
    ],
    20: [
        "Tên: Hán Ngọc Bảo Trân",
        "Ngày sinh: 02/07",
        "Cung hoàng đạo:Cự Giải",
        "Đặc điểm nhận dạng: Mới chuyển hộ khẩu lên núi và có view nhà nhìn ra thác - thác Bản Joke.",
        "Link FB: fb.com/han.ngocbaotran.35",
        "Lời chào đầu: Mình là Trân, dân tộc Kinh, quê Yên Bái, uống nước suối, ăn rau rừng và cưỡi ngựa đi học…"
    ],
    21: [
        "Tên: Nguyễn Đức Dương",
        "Ngày sinh: 17/09",
        "Cung hoàng đạo: Xử Nữ",
        "Đặc điểm nhận dạng:Cởi mở, tươi sáng và thích mời bạn tới chơi nhà",
        "Link FB: https://www.facebook.com/mr.scheherazade",
        "Lời chào đầu: Xin chào DLP-er đời mới! Mình là Dương – cố cũ quay lại với vai trò TA... Let's gooo 💥🔥"
    ],
    22: [
        "Tên: Trần Anh Đức",
        "Ngày sinh: 28/5",
        "Cung hoàng đạo:Song Tử",
        "Đặc điểm nhận dạng:Thích ăn và uống",
        "Link FB: https://www.facebook.com/felix.tran.810706/",
        "Lời chào đầu:Chào các đồng chí, mình là Đức..."
    ],
    23: [
        "Tên: Lý Hạnh Linh",
        "Ngày sinh: 03/08",
        "Cung hoàng đạo:Sư Tử",
        "Đặc điểm nhận dạng:Mẹ của 3 bé mèo, thích thách thức lãnh đạo",
        "Link FB: https://www.facebook.com/hanhlinh.ly",
        "Lời chào đầu:Eoseo wa, DLP-neun cheoeumiji? Welcome lần đầu với DLP!"
    ],
    24: [
        "Tên: Nguyễn Thị Khánh Linh",
        "Ngày sinh: 12/11",
        "Cung hoàng đạo:Bọ Cạp",
        "Đặc điểm nhận dạng:Thích che ô đi dưới mưa tại Paris",
        "Link FB: https://www.facebook.com/khanh.linh.nguyenn.2024",
        "Lời chào đầu:Chào mọi người, mình là Khánh Linh..."
    ],
    25: [
        "Tên: Hoàng Thị Thảo Anh",
        "Ngày sinh:6/2",
        "Cung hoàng đạo:Bảo Bình",
        "Đặc điểm nhận dạng:Công tắc bật nước mắt của DLPer, dịu dàng suốt 4 mùa",
        "Link FB: https://www.facebook.com/thaoanh.cht",
        "Lời chào đầu:Xin chào quý vị học viên đang theo dõi “DLP4 - một chốn yên bình”..."
    ],
    26: [
        "Tên: Tá Mai Linh",
        "Ngày sinh:28/7",
        "Cung hoàng đạo:Sư Tử",
        "Đặc điểm nhận dạng:Cô gái được nhiều người thực hành lãnh đạo..."
    ],
    27: [
        "Tên: Đỗ Minh Châu",
        "Ngày sinh:9/3",
        "Cung hoàng đạo:Song Ngư",
        "Đặc điểm nhận dạng:Từng được thuê về DLP để take note...",
        "Link FB: https://www.facebook.com/timon.bumba.1466",
        "Lời chào đầu:Xin chào chúng taa, mình là Châu Đỗ..."
    ],
    28: [
        "Tên: Lê Chí Nam",
        "Ngày sinh:23/7",
        "Cung hoàng đạo:Sư Tử",
        "Đặc điểm nhận dạng:Là người máy học về cảm xúc",
        "Link FB: https://www.facebook.com/chinam.le.1422",
        "Lời chào đầu:Xin chào, mình là Chí Nam – Personal AI Assistant..."
    ],
    29: [
        "Tên: Nguyễn Việt Anh",
        "Ngày sinh:28/8",
        "Cung hoàng đạo:Xử Nữ",
        "Đặc điểm nhận dạng:Nấu ăn rất ngon, ôm mềm như gấu...",
        "Link FB: https://www.facebook.com/nvanh003",
        "Lời chào đầu:4368e1baaf63206b68c3b46e672…"
    ],
    30: [
        "Tên: Đỗ Phương Anh",
        "Ngày sinh:5/7",
        "Cung hoàng đạo:Cự Giải",
        "Đặc điểm nhận dạng:Miss DAV 2026, bonding liên tục 3 ngày ko tẩy trang",
        "Link FB: https://www.facebook.com/hnagnouhp.05",
        "Lời chào đầu:."
    ],
    31: [
        "Tên: Trần Hoàng Thắng",
        "Ngày sinh:26/4",
        "Cung hoàng đạo:Kim Ngưu",
        "Đặc điểm nhận dạng:Ca sĩ miền Tây nuốt mic mọi bài",
        "Link FB: https://www.facebook.com/thangquang.or.winnie",
        "Lời chào đầu:Hi cả nhà, mình là Thắng..."
    ],
    32: [
        "Tên: Nguyễn Thảo Đan",
        "Ngày sinh:27/6",
        "Cung hoàng đạo:Cự Giải",
        "Đặc điểm nhận dạng:Đừng bao giờ hỏi xin meme...",
        "Link FB: https://www.facebook.com/thaodannguyen.2706",
        "Lời chào đầu:Chào cả nhà..."
    ],
    33: [
        "Tên: Trần Thanh An",
        "Ngày sinh:6/4",
        "Cung hoàng đạo:Bạch Dương",
        "Đặc điểm nhận dạng:Phù thủy mạnh nhất DLP",
        "Link FB: https://www.facebook.com/thaanhhannn?mibextid=LQQJ4d",
        "Lời chào đầu:Chào mọi người..."
    ],
    34: [
        "Tên: Nguyễn Tùng Lâm",
        "Ngày sinh:23/6",
        "Cung hoàng đạo:Cự Giải",
        "Đặc điểm nhận dạng:Chưa ngán thách thức",
        "Link FB: https://www.facebook.com/justmalng",
        "Lời chào đầu:Sawadeekaa..."
    ],
    35: [
        "Tên: Phạm Hà Phương",
        "Ngày sinh:11/9",
        "Cung hoàng đạo:Xử Nữ",
        "Đặc điểm nhận dạng:90% bay trên cung trăng",
        "Link FB: https://www.facebook.com/congchualizcute",
        "Lời chào đầu:Xin chào..."
    ],
    36: [...],
    37: [...],
    38: [...],
    39: [...]
}

# Initialize scene
if 'scene' not in st.session_state:
    st.session_state.scene = 1

def render_scene():
    sc = st.session_state.scene

    if sc == 1:
        for line in scenes[1]:
            typewriter(line)
        if st.button("Tiếp tục"):
            st.session_state.scene = 2
            st.experimental_rerun()

    elif sc == 2:
        st.write("**Bạn đã sẵn sàng tiến vào hành trình này chưa?**")
        col1, col2 = st.columns(2)
        if col1.button("Tôi rất sẵn sàng") or col2.button("Tôi vẫn rất sẵn sàng"):
            st.session_state.scene = 3
            st.experimental_rerun()
        st.caption("Không tìm thấy nút từ bỏ đâu, đừng cố tìm")

    elif sc == 3:
        st.write("### Cẩm nang bắt đầu kết nối thế giới DLP4 dành cho Học viên mới")
        st.write("Gói tìm hiểu về các Staff")
        col1, col2, col3 = st.columns(3)
        if col1.button("Teaching Assistants"):
            st.session_state.scene = 4
            st.experimental_rerun()
        if col2.button("Teaching Fellows"):
            st.session_state.scene = 5
            st.experimental_rerun()
        if col3.button("Instructors"):
            st.session_state.scene = 6
            st.experimental_rerun()

    elif sc in staff_options:
        for name, nxt in staff_options[sc].items():
            if st.button(name):
                st.session_state.scene = nxt
                st.experimental_rerun()

    elif 7 <= sc <= 39:
        for line in scenes[sc]:
            typewriter(line)
        st.write("---")
        icon, desc = random.choice(animals)
        st.write(f"{icon} **{desc}**")
        col1, col2 = st.columns(2)
        if col1.button("Quay lại trang chủ"):
            st.session_state.scene = 3
            st.experimental_rerun()
        if col2.button("Nạp xong dữ liệu tiếp tục hành trình"):
            st.session_state.scene = 40
            st.experimental_rerun()

    elif sc == 40:
        st.write("## Hành trình DLP4 sắp bắt đầu")
        if st.button("Nhập vai Học viên, tiến vào DLP4"):
            st.session_state.scene = 41
            st.experimental_rerun()

    elif sc == 41:
        st.image("/mnt/data/485876466_122192825162110093_3633968015871958652_n.jpg", use_column_width=True)

    else:
        st.write("Cảnh không hợp lệ.")

if __name__ == "__main__":
    render_scene()
