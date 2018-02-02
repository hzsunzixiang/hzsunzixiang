
中文暂时可以了 以后再研究其他方式


使用 ctex 显示中文

-   安装套件
    https://packages.debian.org/sid/texlive-lang-chinese
    sudo aptitude install texlive-lang-chinese


    sudo aptitude install texlive-full
- msttcorefonts
    https://tex.stackexchange.com/questions/160666/how-can-i-install-a-chinese-font-in-a-ubuntu-13-10-in-a-way-that-xelatex-can-see
	安装一些字体
	sudo aptitude install msttcorefonts
    msttcorefonts 这个包下面有一些字体 但是不全 
    需要从windows下拷贝
- 从window下拷贝字体 到

  sudo mkdir /usr/share/fonts/win/
  sudo cp Fonts/*  /usr/share/fonts/win/
  sudo fc-cache 
  # 注意修改权限 否则无法显示
  sudo chmod 755 -R /usr/share/fonts/win/ 
  sudo fc-list :lang=zh



 参考
  http://bbs.ctex.org/forum.php?mod=viewthread&tid=70874
  看来问题已经解决差不多了，其实字体问题貌似没有那么复杂。但我觉得根本没有必要折腾那么多，字体直接从windows上复制过来，fc-cache之后XeTeX调用（使用字体名）起来几乎没有问题，至今只遇到过一个方正的字体和一个毛泽东字体需要折腾一下。

    http://blog.sina.com.cn/s/blog_85998e380100zfh2.html
    以root身份执行：
    #cp -r /media/Windows/Fonts/* /usr/share/fonts
    #fc-cache
    #fc-list
    sudo chmod 755 /usr/share/fonts/* #此处要注意，文件夹一定要赋予x权限，否则你的系统就会全是框框了。


    http://linux-wiki.cn/wiki/LaTeX%E4%B8%AD%E6%96%87%E6%8E%92%E7%89%88%EF%BC%88%E4%BD%BF%E7%94%A8XeTeX%EF%BC%89
    
    因为复制文件时是以root身份进行的， 复制到目标文件夹下的字体文件其读取的权限设置可能有问题。建议如下设定：
    
    $ sudo chmod 755 /usr/share/fonts/win/*
    此外，有些免费的字体可以下载使用，比如楷体, 细明体。 如果是在ubuntu下，可以直接通过以下命令安装微软的公开免费字体：
    
    $ sudo apt-get install xfonts-wqy ttf-wqy-microhei ttf-wqy-zenhei
    接着,需要更新字体缓存：
    
    $ fc-cache
    为了使整个系统下的用户的字体列缓存都更新，建议使用root权限执行:
    
    $ sudo fc-cache -f -s -v
    使用fc-list查看可用的字体：
    
    $ fc-list
    或者只查看中文的字体
    
    $ fc-list ：lang=zh
    如果能看到想要的中文字体，就可以了。至此，准备工作已经结束。


-  修改配置文件
    如果还不行 就查看配置文件
    http://www.cnblogs.com/xiao-cheng/archive/2012/03/13/2393464.html
    cd ~/texlive/2011/texmf-dist/tex/latex/ctex/fontset/
    sudo cp ctex-xecjk-winfonts.def ctex-xecjk-winfonts.def.bak
    sudo gedit ctex-xecjk-winfonts.def

   真正的位置
   StephenSun@debian-1:~/hzsunzixiang.github.io/latex/ctex$ sudo find / -name "ctex-xecjk-winfonts.def"
   /usr/share/texlive/texmf-dist/tex/latex/ctex/fontset/ctex-xecjk-winfonts.def
   StephenSun@debian-1:~/hzsunzixiang.github.io/lat

