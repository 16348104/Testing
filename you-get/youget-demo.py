import sys
from you_get import common as you_get #导入you-get库

# 设置下载目录mac
directory = '/Users/xdx/Downloads/pdf/'
#需要下载的视频地址,部分网址不能用
url = 'https://www.bilibili.com/video/BV1Vt411579n?from=search&seid=17215681599528404474'
#sys传递参数执行下载，就像在命令行一样；‘-o’后面跟保存目录。
sys.argv = ['you-get', '-o', directory, url]
you_get.main()
