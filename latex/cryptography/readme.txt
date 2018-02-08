


1. 有时候需要make clean然后再编译通过

2. pdflatex 运行两次失败,原因是sections标题中有中文  通过删除 rsa_alg.toc 来解决
	但是生成tableofcontents又需要两次 生成toc
	和第三条冲突了
	https://tex.stackexchange.com/questions/78682/table-of-contents-doesnt-get-created
	You need to compile it atleast two times to get the TOC. – user11232 Oct 22 '12 at 15:30
	I just compiled the example document given by you and all worked out fine for me. TOC showed up after the second compilation. – Benedikt Bauer Oct 22 '12 at 15:31

3. 用pdflatex 生成tableofcontents 需要运行两次才行

4. 管道符号 打印出来 | 是破折号
		真正的整除符号为 $\mid$

