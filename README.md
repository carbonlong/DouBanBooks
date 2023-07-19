# DouBanBooks

## 抓取豆瓣图书top250
使用 python3 + selenium 抓取豆瓣图书top250

### 运行环境要求
本程序使用python版本为3.11.0

### 第三方包要求
pip install selenium==4.9.1
pip install openpyxl==3.1.2

#### 配置Chrome浏览器和对应的驱动
本地安装了chrome浏览器 通过Help > About Google Chrome查看浏览器版本

从[chrome驱动下载地址](https://npm.taobao.org/mirrors/chromedriver/)下载对应版本的chrome驱动程序

把chrome驱动程序保存到非中文文件目录下 以便python程序能正确找到

修改python程序chromedriver_path = './chromedriver.exe'设置正确的chrome驱动程序路径
