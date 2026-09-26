"""Build one editable LaTeX source from the three verified Markdown reports."""
from pathlib import Path
import re
import shutil
import zipfile
from markdown_it import MarkdownIt

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'latex_report_revised'
OUT.mkdir(exist_ok=True)
(OUT/'figures').mkdir(exist_ok=True)
parser=MarkdownIt('commonmark').enable('table')
special={'\\':r'\textbackslash{}','{':r'\{','}':r'\}','$':r'\$','&':r'\&','#':r'\#','%':r'\%','_':r'\_','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
symbols={'≥':r'\ensuremath{\geq}','≤':r'\ensuremath{\leq}','→':r'\ensuremath{\to}','−':'-',
         '×':r'\ensuremath{\times}','·':r'\ensuremath{\cdot}','∶':r'\ensuremath{:}',
         '‖':r'\ensuremath{\Vert}','θ':r'\ensuremath{\theta}','₁':r'\ensuremath{_1}',
         '₂':r'\ensuremath{_2}','ₘ':r'\ensuremath{_m}','…':r'\ldots{}','–':'--','—':'---'}
def esc(s):
    out=[]
    for i,c in enumerate(s):
        out.append(symbols.get(c,special.get(c,c)))
        if c in '/_' or (c=='.' and i+1<len(s) and s[i+1].isascii() and s[i+1].isalpha()):
            out.append(r'\allowbreak{}')
    return ''.join(out)

def inline(children):
    out=[]
    for t in children or []:
        if t.type=='text':out.append(esc(t.content))
        elif t.type=='code_inline':
            out.append(r'\texttt{'+esc(t.content)+'}' if '\\' in t.content or '{' in t.content else r'\nolinkurl{'+t.content+'}')
        elif t.type=='strong_open':out.append(r'\textbf{')
        elif t.type=='strong_close':out.append('}')
        elif t.type=='em_open':out.append(r'\emph{')
        elif t.type=='em_close':out.append('}')
        elif t.type=='link_open':out.append(r'\href{'+t.attrGet('href').replace('%',r'\%')+'}{')
        elif t.type=='link_close':out.append('}')
        elif t.type in ['softbreak','hardbreak']:out.append(' ')
        elif t.type=='image':
            source=ROOT/t.attrGet('src');target=OUT/'figures'/source.name
            shutil.copy2(source,target)
            out.append('\n'+r'\begin{center}\begin{minipage}{\linewidth}\centering'+'\n'+r'\includegraphics[width=\linewidth]{figures/'+source.name+'}\n'+r'\captionof{figure}{'+esc(t.content)+'}\n'+r'\end{minipage}\end{center}'+'\n')
        else:raise ValueError('Unhandled inline token '+t.type)
    return ''.join(out)

def formula_override(text):
    if text.startswith('令词表为 V，'):
        return r'''令词表为 $V$，$n(d,j)$ 表示词 $j$ 在文档 $d$ 中出现的次数。两种表示定义为
\begin{align}
x^{\mathrm{binary}}_{d,j}&=\mathbf{1}[n(d,j)>0],\\
x^{\mathrm{count}}_{d,j}&=n(d,j).
\end{align}
例如词表为 [team, win, market]，文本“team team win”分别得到 $[1,1,0]$ 与 $[2,1,0]$。'''
    if text.startswith('Accuracy=预测正确数/'):
        return r'''评价指标定义为
\begin{align}
\mathrm{Accuracy}&=\frac{\text{预测正确的样本数}}{\text{总样本数}},\\
P_k&=\frac{TP_k}{TP_k+FP_k},\qquad R_k=\frac{TP_k}{TP_k+FN_k},\\
F_{1,k}&=\frac{2TP_k}{2TP_k+FP_k+FN_k},\\
\mathrm{Macro\text{-}F1}&=\frac{1}{3}\sum_{k=1}^{3}F_{1,k}.
\end{align}
Macro-F1 是三个类别 F1 的算术平均，而不是先平均 Precision 和 Recall 再求 F1。'''
    if text.startswith('设文档中具有词向量的 token 序列为'):
        return r'''设文档中具有词向量的 token 序列为 $w_1,\ldots,w_m$，文档表示为
\begin{equation}
\boldsymbol h_d=\frac{1}{m}\sum_{i=1}^{m}\boldsymbol v(w_i),\qquad
\boldsymbol x_d=\frac{\boldsymbol h_d}{\lVert\boldsymbol h_d\rVert_2}.
\end{equation}
重复出现的词重复参与求和，未登录词忽略；若整篇无已知词则用零向量。
分类器为 liblinear、L2 正则、OvR LR，\nolinkurl{max_iter=2000}，不使用类别权重。
$C$ 网格为 $0.01,0.1,1,10,100$，分数相同时选较小 $C$。'''
    return None

def render_table(tokens,context):
    rows=[];row=[]
    for t in tokens:
        if t.type=='tr_open':row=[]
        elif t.type=='inline':row.append((inline(t.children),t.content))
        elif t.type=='tr_close':rows.append(row)
    n=len(rows[0]);assert all(len(r)==n for r in rows)
    # Column widths adapt to text-heavy evidence cells and compact metric columns.
    def length(s):return sum(2 if ord(c)>255 else 1 for c in s)
    weights=[]
    for i in range(n):
        sizes=sorted(length(row[i][1])for row in rows)
        typical=sizes[int((len(sizes)-1)*.75)]
        weights.append(max(10,min(70,typical))**.65)
    total=sum(weights)
    specs=''.join(r'>{\raggedright\arraybackslash}p{\dimexpr '+f'{w/total:.5f}'+r'\linewidth-'+f'{2*n*w/total:.5f}'+r'\tabcolsep\relax}'for w in weights)
    header=' & '.join(r'\textbf{'+c[0]+'}'for c in rows[0])+r' \\'
    body='\n'.join(' & '.join(c[0]for c in row)+r' \\'for row in rows[1:])
    return '\n'.join([r'\begin{center}\begin{minipage}{\linewidth}\small',r'\setlength{\tabcolsep}{4pt}',r'\renewcommand{\arraystretch}{1.22}',r'\captionof{table}{'+esc(context)+'}',r'\begin{tabular}{'+specs+'}',r'\toprule',header,r'\midrule',body,r'\bottomrule',r'\end{tabular}',r'\end{minipage}\end{center}'])

def convert(path,index):
    source=path.read_text(encoding='utf-8')
    source=source.replace('T2 为 Word2Vec，T3 为 BERT，不属于本次实验。','T2 为 Word2Vec，T3 为 BERT，分别在后续两节讨论。')
    source=source.replace('T2 运行说明见 T2_实验报告.md。','T2 运行说明见第 2 节的复现部分。')
    tokens=parser.parse(source)
    out=[];i=0;context='实验结果'
    while i<len(tokens):
        t=tokens[i]
        if t.type=='heading_open':
            level=int(t.tag[1]);text=tokens[i+1].content
            text=re.sub(r'^\d+(?:\.\d+)*\.?\s*','',text)
            if level==1:
                title=text
                out.append(r'\clearpage\section{'+esc(title)+'}')
            else:
                context=text
                cmd='subsection'if level==2 else 'subsubsection'
                out.append(chr(92)+cmd+'{'+esc(text)+'}')
            i+=3;continue
        if t.type=='paragraph_open':
            contents=tokens[i+1]
            replacement=None
            out.append(replacement if replacement else inline(contents.children))
            out.append('');i+=3;continue
        if t.type=='table_open':
            j=i+1
            while tokens[j].type!='table_close':j+=1
            out.append(render_table(tokens[i:j+1],context));i=j+1;continue
        if t.type=='fence':
            if t.info.strip()=='latex':out.append(t.content if t.content.lstrip().startswith(r'\begin{') else '\\[\n'+t.content+'\\]\n')
            else:out.append(r'\par\noindent\begin{minipage}{\linewidth}'+'\n'+r'\begin{Verbatim}[breaklines=true,breakanywhere=true,fontsize=\small,frame=single,framesep=3mm]'+'\n'+t.content+r'\end{Verbatim}'+'\n'+r'\end{minipage}\par')
        elif t.type in ['bullet_list_open','ordered_list_open']:out.append(r'\begin{itemize}'if t.type=='bullet_list_open'else r'\begin{enumerate}')
        elif t.type in ['bullet_list_close','ordered_list_close']:out.append(r'\end{itemize}'if t.type=='bullet_list_close'else r'\end{enumerate}')
        elif t.type=='list_item_open':out.append(r'\item ')
        elif t.type=='list_item_close':pass
        else:raise ValueError('Unhandled block '+t.type)
        i+=1
    return '\n'.join(out)

preamble=r'''% !TeX program = xelatex
% UTF-8. Compile twice with XeLaTeX. Figures are in the figures/ directory.
% Edit the author information below; experimental data are from completed runs.
\documentclass[UTF8,a4paper,11pt,fontset=fandol]{ctexart}
\usepackage[left=24mm,right=24mm,top=25mm,bottom=25mm,headheight=15pt]{geometry}
\usepackage{amsmath,amssymb,graphicx,booktabs,longtable,array}
\usepackage{fancyhdr,lastpage,xcolor,enumitem,fvextra,needspace,caption}
\usepackage{xurl}
\usepackage[unicode,colorlinks=true,linkcolor=blue!45!black,urlcolor=blue!55!black]{hyperref}
\captionsetup{hypcap=false}
\hypersetup{pdftitle={自然语言处理作业1：NYT新闻分类实验报告},pdfauthor={马传志}}
\setlength{\parskip}{0.35em}
\setlength{\emergencystretch}{3em}
\setlength{\LTpre}{0.5em}
\setlength{\LTpost}{0.6em}
\setcounter{tocdepth}{2}
\setlist{nosep,leftmargin=2em}
\ctexset{section={format=\Large\bfseries},subsection={format=\large\bfseries},subsubsection={format=\normalsize\bfseries}}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{\small 自然语言处理作业 1}
\fancyhead[R]{\small NYT 新闻分类实验}
\fancyfoot[C]{\small 第 \thepage\ 页，共 \pageref*{LastPage} 页}
\title{\textbf{自然语言处理作业 1}\\[0.4em]\Large NYT 新闻分类：文本表示、性能与误差分析}
\author{姓名：马传志\qquad 学号：2411788}
\date{}
\begin{document}
\maketitle
\begin{abstract}
本实验依据正式作业要求，在同一 NYT 数据划分上比较二值词袋、计数词袋、GloVe、
AG News 与 NYT 训练的 Word2Vec，以及输入长度为64、微调3轮的 BERT。
所有传统表示均使用逻辑回归，模型参数只按验证集选择。
实验不仅报告 Accuracy 与 Macro-F1，也从类别混淆、语料覆盖、正则化、
逐样本错误与输入预算对照解释性能差异。
全文计数词袋的测试 Macro-F1 为96.79\%，规定的 BERT-64 为93.95\%；
而仅使用相同开头内容的计数词袋为91.33\%。
这一结果提示：表示能力与可见文本范围共同影响分类效果，不能仅凭模型规模判定优劣。
补充实验与规定实验明确区分，历史512长度结果不替代规定结果。
\end{abstract}
\noindent\textbf{关键词：}新闻分类；词袋模型；逻辑回归；Word2Vec；BERT；误差分析
\tableofcontents
'''
