


- 有时候需要make clean然后再编译通过

- pdflatex 运行两次失败,原因是sections标题中有中文  通过删除 rsa_alg.toc 来解决
	但是生成tableofcontents又需要两次 生成toc
	和第三条冲突了
	https://tex.stackexchange.com/questions/78682/table-of-contents-doesnt-get-created
	You need to compile it atleast two times to get the TOC. – user11232 Oct 22 '12 at 15:30
	I just compiled the example document given by you and all worked out fine for me. TOC showed up after the second compilation. – Benedikt Bauer Oct 22 '12 at 15:31

- 用pdflatex 生成tableofcontents 需要运行两次才行

-  这种选项可以规避第二条的问题 pdflatex -interaction nonstopmode
	然后再解决第三条的问题

- 管道符号 打印出来 | 是破折号
		真正的整除符号为 $\mid$


- CJK包
    https://en.wikibooks.org/wiki/LaTeX/Internationalization#Chinese
    gbsn (简体宋体, simplified Chinese)
	gkai (简体楷体, simplified Chinese)
	bsmi (繁體細上海宋體, traditional Chinese)
	bkai (繁體標楷體, traditional Chinese)

	One possible Chinese support is made available thanks to the CJK package collection. If you are using a package manager or a portage tree, the CJK collection is usually in a separate package because of its size (mainly due to fonts).
	Make sure your document is saved using the UTF-8 character encoding. See Special Characters for more details. Put the parts where you want to write chinese characters in a CJK environment.
	\documentclass{article}
	\usepackage{CJK}
	\begin{document}

	\begin{CJK}{UTF8}{gbsn}
	你好
	You can mix latin letters and chinese.
	\end{CJK}

	\end{document}
	The last argument specifies the font. It must fit the desired language, since fonts are different for Chinese, Japanese and Korean. Possible choices for Chinese include:

	gbsn (简体宋体, simplified Chinese)
	gkai (简体楷体, simplified Chinese)
	bsmi (繁體細上海宋體, traditional Chinese)
	bkai (繁體標楷體, traditional Chinese)
    % 下面这两种字不支持
    %\begin{CJK*}{UTF8}{bsmi}
    %\begin{CJK*}{UTF8}{bkai}


