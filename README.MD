# 如果哪天你忘记了努力，我把科比讲给你听

## 效果图
![效果图](https://github.com/juventusryp/bitbar_for_kobe/blob/master/pic.png)

## 描述
一个[bitbar](https://getbitbar.com/)插件，依靠bitbar可以在MacOS上的Menu Bar显示科比的经典语录以及收集了一些科比的文章视屏。

## 使用方法
程序员及电脑折腾者直接看[bitbar](https://getbitbar.com/)官方教程即可  
其他请看下面教程：  
1、下载
```
https://www.lanzous.com/i8xp52d
```
2、在电脑上新建一个文件夹，然后打开bitbar选择它为默认插件目录
3、下载此仓库的kobe.1h.py文件放在上面的文件夹中
4、软件上点击Preferences-Refresh all出现科比语录即成功，结束  
如果未出现继续做下面步骤  
5、在mac上打开终端，输入
```
which python3
```
用编辑器打开下载的py文件，将上面命令返回的东西替换py文件第一行，例如我的是
```
/Users/lovehxy/opt/anaconda3/bin/python3
```
那么我py文件第一行就是
```
#!/Users/lovehxy/opt/anaconda3/bin/python3
```
6、如果未返回任何东西，先自行去安装python3再做上面步骤

## 其它说明
1、科比语录可以按时更换，更换方法：修改文件名中1h即可
```
10s 10秒钟
30m 30分钟
1h  1小时
1d  1天
```
例如想让语录10s换一次，修改文件名为kobe.10s.py刷新软件即可  
2、支持英文语录，编辑器打开py文件，把最后一行修改为：
```
mamba_en()
```
3、可以自行添加语录，还有收藏的文章与视屏，编辑器打开py文件搜索quoations_zh、quoations_en、articles、movies，按照里面的格式添加你喜欢的即可，注意其它代码格式不要动，否则会报错  
4、里面所有内容均来自网络，如果侵权，请联系我，我会第一时间删除  
5、如果你有好的资源或者建议欢迎联系我，我会尽我所能让曼巴精神激励每一个人

                                            致敬 Kobe Bryant



