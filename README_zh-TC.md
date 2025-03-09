**繁體中文** [簡體中文󠄁](https://github.com/haydenwong7bm/ClasswizDisplayExt/tree/main/README_zh-SC.md) [EN](https://github.com/haydenwong7bm/ClasswizDisplayExt/tree/main)

# CASIO ClassWiz 屏幕顯示字體 Ext

**來自卡西歐計算器屏幕上的像素字體！**

![ClassWizDisplay](readme_assets/ClassWizDisplay.svg)

## 語言支持

✅ 英語、德語、捷克語、匈牙利語、波蘭語、斯洛伐克語、法語、西班牙語、加泰羅尼亞語、巴斯克語、葡萄牙語、越南語、俄語<br>
🟨 日語假名<br>
❌ 希臘語、阿拉伯語、漢語拼音<br>

## 字符集支持

✅ ASCII（[Wenti-D#2](https://github.com/Wenti-D/ClasswizDisplayExt/issues/2)）<br>
✅ ISO/IEC 8859-1（🟨 Windows-1252）<br>
🟨 ISO/IEC 8859-2<br>
🟨 ISO/IEC 8859-3<br>
🟨 ISO/IEC 8859-4<br>
🟨 ISO/IEC 8859-5<br>
❌ ISO/IEC 8859-6<br>
❌ ISO/IEC 8859-7<br>
❌ ISO/IEC 8859-8（沒計畫支持）<br>
🟨 ISO/IEC 8859-9<br>
🟨 ISO/IEC 8859-10<br>
❌ ISO/IEC 8859-11<br>
🟨 ISO/IEC 8859-13<br>
🟨 ISO/IEC 8859-14<br>
🟨 ISO/IEC 8859-15<br>
🟨 ISO/IEC 8859-16

## 使用方法

字體分爲四部分：X Display、X Math、CW Display 與 CW Math。X版爲襯線體，CW版爲無襯線體。Display版用作普通文本，提供 OTF、TTF 與 WOFF2 格式；Math版由 OpenType MATH 表強力驅動，用作數學公式輸入，僅提供 OTF 格式。

所有版本的字體打包可以到 [Release 頁面](https://github.com/haydenwong7bm/ClasswizDisplayExt/releases)獲取。

本文只是關於字體的一個粗略說明，而壓縮包內除字體外還有自述文件（`README.pdf` 之類的文檔）。

如果覺得本項目對你有幫助，不妨點一下頁面右上角的 ☆。

## 構建字體

字體源文件以[FontForge](https://fontforge.org/)源文件格式提供，是一個擴展名爲 `.sfd` 的文件。欲編輯、構建字體，請下載 FontForge。構建字體，可通過 FontForge 使用`build.py`構建。

~~然而 `.sfd` 文件是其實是文本，所以你用記事本修改也不是不行。~~

## 貢獻與反饋

「ClassWiz Display Ext」系列均以 SIL 開源字體許可 1.1 版（SIL Open Font License 1.1）協議授權，詳情請查看 `OFL.txt` 文件，若想編輯、再發布字體，請務必遵守許可協議。如有任何問題或建議，請開啓一個議題（issue）。