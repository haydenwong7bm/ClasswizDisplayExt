[繁體中文](https://github.com/haydenwong7bm/ClasswizDisplayExt/tree/main/README_zh-TC.md) **简体中文󠄁** [EN](https://github.com/haydenwong7bm/ClasswizDisplayExt/tree/main)

# CASIO ClassWiz 屏幕显示字体 Ext

**来自CASIO ClassWiz计算器屏幕上的像素字体！**

![ClassWizDisplay](readme_assets/ClassWizDisplay.svg)

## 语言支持

（根据当前字体源文件）

✅ 英语、德语、捷克语、匈牙利语、波兰语、斯洛伐克语、法语、西班牙语、加泰罗尼亚语、巴斯克語、葡萄牙语、越南语、俄语、汉语拼音<br>
🟨 日语假名<br>
❌ 希腊语、阿拉伯语、台语白话字<br>

## 字符集支持

（根据当前字体源文件）

✅ ASCII（[Wenti-D#2](https://github.com/Wenti-D/ClasswizDisplayExt/issues/2)）<br>
✅ ISO/IEC 8859-1（🟨 Windows-1252）<br>
🟨 ISO/IEC 8859-2<br>
🟨 ISO/IEC 8859-3<br>
🟨 ISO/IEC 8859-4<br>
🟨 ISO/IEC 8859-5<br>
❌ ISO/IEC 8859-6<br>
❌ ISO/IEC 8859-7<br>
❌ ISO/IEC 8859-8（没计画支持）<br>
🟨 ISO/IEC 8859-9<br>
🟨 ISO/IEC 8859-10<br>
❌ ISO/IEC 8859-11<br>
🟨 ISO/IEC 8859-13<br>
🟨 ISO/IEC 8859-14<br>
🟨 ISO/IEC 8859-15<br>
🟨 ISO/IEC 8859-16

## 使用方法

字体分为四部分：X Display、X Math、CW Display 与 CW Math。X版为衬线体，CW版为无衬线体。Display版用作普通文本，提供 OTF、TTF 与 WOFF2 格式；Math版由 OpenType MATH 表强力驱动，用作数学公式输入，仅提供 OTF 格式。

所有版本的字体打包可以到 [Release 页面](https://github.com/haydenwong7bm/ClasswizDisplayExt/releases)获取。

本文只是关于字体的一个粗略说明，而**压缩包内除字体外还有自述文件（`README.pdf` 之类的文档），使用前请一定、务必、绝对要认真、仔细、用心阅读！**

如果觉得本项目对你有帮助，不妨点一下页面右上角的 ☆。

## 构建字体

字体源文件以[FontForge](https://fontforge.org/)源文件格式提供，是一个扩展名为 `.sfd` 的文件。欲编辑、构建字体，请下载 FontForge。构建字体，可通过 FontForge 使用`build.py`构建。

~~然而 `.sfd` 文件是其实是文本，所以你用记事本修改也不是不行。~~

## 贡献与反馈

「ClassWiz Display Ext」系列均以 SIL 开源字体许可 1.1 版（SIL Open Font License 1.1）协议授权，详情请查看 `OFL.txt` 文件，若想编辑、再发布字体，请务必遵守许可协议。如有任何问题或建议，请开启一个议题（issue）。