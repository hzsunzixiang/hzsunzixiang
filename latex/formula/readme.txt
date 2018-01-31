
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
