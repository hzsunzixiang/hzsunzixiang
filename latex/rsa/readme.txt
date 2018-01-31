
中文暂时可以了 以后再研究其他方式


步骤
在debian下安装
1. 安装latex 
 sudo aptitude  -y install  texlive texlive-*.noarch


2. 安装中文字体cjk
    https://tex.stackexchange.com/questions/125843/how-to-install-cjk-font-to-ubuntu-latex
    sudo apt-get install latex-cjk-all



3.然后用这个帖子里里面说的试验一下  成功的
http://forum.ubuntu.org.cn/viewtopic.php?f=35&t=458674

\documentclass{book}
\usepackage{CJKutf8}
 
\begin{document}
\begin{CJK}{UTF8}{gbsn}
 可以输入中文
\end{CJK}
\end{document}



http://blog.csdn.net/bensnake/article/details/43279329


另外这里也有说明


        建议安装latex-cjk-all以获取完整支持。
        
        Linux下的中文字体，对于Ubuntu来说有现成的。因此，只要第一步正常安装完毕，就可以用下面的测试文件进行测试。
        
        [html] view plain copy
        \documentclass{article}  
        \usepackage{CJKutf8}  
        \begin{document}  
        \begin{CJK}{UTF8}{gkai}  
        这是一个楷体中文测试，处理简体字。  
        \end{CJK}  
        \begin{CJK}{UTF8}{gbsn}  
        这是一个宋体中文测试，处理简体字。  
        \end{CJK}  
        \begin{CJK}{UTF8}{bkai}  
        這是一個big5編碼的楷體中文測試，處理繁體文字。  
        \end{CJK}  
        \begin{CJK}{UTF8}{bsmi}  
        這是一個个big5編碼的明體中文測試，處理繁體文字。  
        \end{CJK}  
        \end{document}  


// 这篇文章也不错
http://evoupsight.com/blog/2016/07/11/latex-vim-pratice/


好久没有更新blog了，又得开始啦，不然传不习乎都忘记了。这里主要记录下vim下配置latex的一些经过，整个过程还是比较快可以上手的。 这里没有去手动下载安装texlive2015，而是采取直接apt安装。
sudo apt-get install texlive texlive-math-extra texlive-latex-base texlive-latex-extra texlive-latex-recommended texlive-pictures texlive-science latex-beamer texlive-base texlive-bibtex-extra
当然也可以下载完整的latexlive-full，但比较占用磁盘空间。

sudo apt-get install texlive-full latex-beamer
由于磁盘空间充裕，为避免可能出现的各种麻烦，我选择了后者的完整安装。 安装完后，继续安装CJK的相关软件包（仅仅为了获取中文支持）：

sudo apt-get install latex-cjk-chinese ttf-arphic-* hbf-*
然后做测试，将下面的文件保存为helloworld.tex

\documentclass{article}
\usepackage{CJKutf8}
\begin{document}
\begin{CJK}{UTF8}{gkai}
这是一个楷体中文测试，处理简体字。
\end{CJK}
\begin{CJK}{UTF8}{gbsn}
这是一个宋体中文测试，处理简体字。
\end{CJK}
\begin{CJK}{UTF8}{bkai}
這是一個big5編碼的楷體中文測試，處理繁體文字。
\end{CJK}
\begin{CJK}{UTF8}{bsmi}
這是一個个big5編碼的明體中文測試，處理繁體文字。
\end{CJK}
\end{document}
然后运行pdflatex helloworld.tex，正常的话应该就可以看到生成的能正确显示中文的pdf格式文件了。 安装evince，这是用来查看pdf文件的。

sudo apt-get install evince
查看pdf

evince helloworld.pdf
Alt text

接下来就可以装字体了

sudo apt-get install fontforge
这样是不够的，还需要一堆windows的字体，宋体、仿宋、黑体等,这里提供下载：

SimSun.ttc

simhei.ttf

simkai.ttf

TimesNewRoman.ttf

STXingkai.ttf

simfang.ttf

sudo cp simsun.ttc simhei.ttf simkai.ttf TimesNewRoman.ttf STXingkai.ttf simfang.ttf /usr/share/fonts
cd /usr/share/fonts
sudo chmod 644 simsun.ttc simhei.ttf simkai.ttf TimesNewRoman.ttf STXingkai.ttf simfang.ttf
sudo mkfontscale && sudo mkfontdir
sudo fc-cache -fsv
然后还是找不到某些字体，需要hack一下latexlive的配置文件

locate ctex-xecjk-winfonts.def | xargs sudo vim
修改其中的[SIMKAI.TTF]为KaiTi_GB2312
修改其中的[SIMFANG.TTF]为FangSong_GB2312
接下来就可以开始latex中文写作之旅了!

后记
这里还没有考虑繁体中文的配置，还有vim的preview pdf插件没有测试成功，以后补上。
