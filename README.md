# CASIO Classwiz 屏幕显示字体 Ext

**来自卡西欧计算器屏幕上的像素字体！**

![ClassWizDisplay](readme_assets/ClassWizDisplay.svg)

## 本人修改内容
- 补回「\」、「\`」（[Wenti-D#2](https://github.com/Wenti-D/ClasswizDisplayFont/issues/2)）
- 增设等宽「\|」：「bar」预设是等宽字图，「bar.ss02」是原来「bar」的字图（[Wenti-D#2](https://github.com/Wenti-D/ClasswizDisplayFont/issues/2)）

### X版：
- 补回CW存在但在此版缺失的「α」（U+03B1）

### CW版：
- 补回X版存在但在此版缺失的「𝛼」（U+1D6FC）
- 补回X版存在但在此版缺失的「Ɖ」（U+0189）

## 食用方法

字体分为四部分：X Display Ext、CW Display Ext、X Math Ext与CW Math Ext。带有「Display」的字体用作普通文本，提供OTF、TTF与WOFF2（自 v3.001 起）格式；带有「Math」的字体由Opentype MATH表强力驱动，用作数学公式输入，仅提供OTF格式。

所有版本的字体打包可以到[Release页面](https://github.com/haydenwong7bm/ClasswizDisplayFont/releases)获取。

本文只是关于字体的一个粗略说明，而**压缩包内除字体外还有自述文件（`README.pdf` 之类的文档），使用前请一定、务必、绝对要认真、仔细、用心阅读！**

如果觉得本项目对你有帮助，不妨点一下页面右上角的 ☆。

## 构建字体

字体源文件以[FontForge](https://fontforge.org/)源文件格式提供，是一个扩展名为 `.sfd` 的文件。欲编辑、构建字体，请下载FontForge。亦可通过FontForge使用`build.py`构建字体。

~~然而 `.sfd` 文件是其实是文本，所以你用记事本修改也不是不行。~~

## 贡献与反馈

「ClassWiz 屏幕显示」系列均以 SIL 开源字体许可 1.1 版（SIL Open Font License 1.1）协议授权，详情请查看 `OFL.txt` 文件，若想编辑、再发布字体，请务必遵守许可协议。如有任何问题或建议，还请开启一个议题（issue）。
