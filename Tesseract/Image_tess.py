import os
import re
import matplotlib.pyplot as plt
import requests
from fontTools.ttLib import TTFont


def font_css():
    # first_num_dict = [{"code": "uniF43A", "num": 1}, {"code": "uniF387", "num": 3},
    #                   {"code": "uniE27E", "num": 5},{"code": "uniF871", "num": 6},
    #                   {"code": "uniEF9E", "num": 0}, {"code": "uniEEE6", "num": 2},
    #                   {"code": "uniF38C", "num": 8}, {"code": "uniE20B", "num": 9},
    #                   {"code": "uniE7C7", "num": 7},{"code": "uniE5C3", "num": 4}
    #                   ]

    url = "https://maoyan.com/board/1"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    html = response.content.decode("utf-8")

    font_file_name = re.findall(r"//vfile.meituan.net/colorstone/(\w+\.woff)", html)[0]
    font_file = requests.get("http://vfile.meituan.net/colorstone/" + font_file_name)



    # if os.path.exists("fonts/" + font_file_name):
    #     return first_num_dict

    new_num_dict = []

    if not os.path.exists("fonts"):
        os.mkdir("fonts")

    with open("fonts/" + font_file_name, "wb") as f:
        f.write(font_file.content)

    ttfont = TTFont("fonts/" + font_file_name)
    ttfont.saveXML(font_file_name + ".xml")



# str1 = """
# <contour>
#         <pt x="331" y="-40" on="1"/>
#         <pt x="336" y="149" on="1"/>
#         <pt x="13" y="150" on="1"/>
#         <pt x="23" y="223" on="1"/>
#         <pt x="347" y="721" on="1"/>
#         <pt x="421" y="706" on="1"/>
#         <pt x="421" y="222" on="1"/>
#         <pt x="520" y="232" on="1"/>
#         <pt x="520" y="147" on="1"/>
#         <pt x="432" y="149" on="1"/>
#         <pt x="430" y="-21" on="1"/>
#         <pt x="328" y="-18" on="1"/>
#       </contour>
#       <contour>
#         <pt x="331" y="229" on="1"/>
#         <pt x="331" y="552" on="1"/>
#         <pt x="98" y="229" on="1"/>
#         <pt x="331" y="238" on="1"/>
#       </contour>
# """

str1 = """
<contour>
        <pt x="181" y="371" on="1"/>
        <pt x="71" y="412" on="0"/>
        <pt x="71" y="521" on="1"/>
        <pt x="71" y="603" on="0"/>
        <pt x="185" y="710" on="0"/>
        <pt x="378" y="710" on="0"/>
        <pt x="436" y="654" on="1"/>
        <pt x="486" y="596" on="0"/>
        <pt x="508" y="510" on="1"/>
        <pt x="495" y="412" on="0"/>
        <pt x="386" y="371" on="1"/>
        <pt x="454" y="349" on="0"/>
        <pt x="524" y="251" on="0"/>
        <pt x="524" y="184" on="1"/>
        <pt x="524" y="88" on="0"/>
        <pt x="447" y="21" on="1"/>
        <pt x="391" y="-29" on="0"/>
        <pt x="283" y="-54" on="1"/>
        <pt x="174" y="-45" on="0"/>
        <pt x="108" y="25" on="1"/>
        <pt x="42" y="86" on="0"/>
        <pt x="42" y="200" on="1"/>
        <pt x="42" y="257" on="0"/>
        <pt x="114" y="354" on="0"/>
        <pt x="181" y="360" on="1"/>
      </contour>
      <contour>
        <pt x="163" y="524" on="1"/>
        <pt x="163" y="470" on="0"/>
        <pt x="230" y="406" on="0"/>
        <pt x="282" y="412" on="1"/>
        <pt x="336" y="406" on="0"/>
        <pt x="369" y="424" on="1"/>
        <pt x="402" y="470" on="0"/>
        <pt x="402" y="567" on="0"/>
        <pt x="379" y="601" on="1"/>
        <pt x="334" y="640" on="0"/>
        <pt x="283" y="635" on="1"/>
        <pt x="229" y="650" on="0"/>
        <pt x="197" y="603" on="1"/>
        <pt x="163" y="570" on="0"/>
      </contour>
      <contour>
        <pt x="134" y="186" on="1"/>
        <pt x="134" y="146" on="0"/>
        <pt x="169" y="75" on="0"/>
        <pt x="207" y="55" on="1"/>
        <pt x="242" y="35" on="0"/>
        <pt x="284" y="35" on="1"/>
        <pt x="316" y="35" on="0"/>
        <pt x="369" y="57" on="0"/>
        <pt x="390" y="77" on="1"/>
        <pt x="432" y="117" on="0"/>
        <pt x="430" y="248" on="0"/>
        <pt x="346" y="332" on="0"/>
        <pt x="276" y="332" on="1"/>
        <pt x="217" y="332" on="0"/>
        <pt x="134" y="249" on="0"/>
      </contour>"""



x = [int(i) for i in re.findall(r'<pt x="(.*?)" y=', str1)]
y = [int(i) for i in re.findall(r'y="(.*?)" on=', str1)]
plt.plot(x,y)
plt.show()
#     old_font = TTFont("fonts/8683187a80f572f22606110cb63260762292.woff")
#
#     new_font = TTFont("./fonts/" + font_file_name)
#     new_font_unicode_list = new_font.getGlyphOrder()[2:]  # 前两个不是数字对应的编码,去掉
#     for i in range(len(new_font_unicode_list)):
#         news = new_font["glyf"][new_font_unicode_list[i]]
#         for j in range(len(new_font_unicode_list)):
#             olds = old_font["glyf"][first_num_dict[j]["code"]]
#             if news == olds:
#                 num = first_num_dict[j]["num"]
#                 new_num_dict.append({"code": new_font_unicode_list[i].replace("nui", "&#x").lower() + ";","num":num})
#
#     return new_num_dict
#
# if __name__ == '__main__':
#     new_num_dict= font_css()
#     print(new_num_dict)

font_css()