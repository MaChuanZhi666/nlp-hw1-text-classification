# 自然语言处理作业一：马传志（2411788）

本仓库包含实验报告、完整代码、课程数据、实验结果与运行说明。**老师可直接打开下方PDF报告、源码和结果文件查看，无需运行程序。后面的运行步骤仅供需要复现实验时使用。**

- **实验报告：[PDF（19页）](NLP_HW1_2411788_report.pdf)**
- **原始数据：[AG CSV](ag.csv) · [NYT CSV](nyt.csv)**
- **可编辑报告：[LaTeX源码](latex_report_revised/main.tex)**
- **实验结果：[统一逐样本预测](required_analysis/all_predictions.csv)**
- **复现方法：见下方环境和运行步骤。**

## 已完成内容

- T1：Binary BoW、Word Frequency，均使用LR；TF-IDF是额外补充，解决文件总述“三种”但只列两种的歧义，不声称老师指定了它。
- T2：glove.6B 100d、AG News训练100d Word2Vec、NYT训练集训练100d Word2Vec，三组均以原始平均向量+LR作为主结果。
- T3：google-bert/bert-base-uncased，max_length=64，完整训练3轮。历史512实验只用于补充对照。
- 六组规定实验均报告Accuracy和Macro-F1；另有混淆矩阵、逐类指标、超参数选择、输入审计、错例、配对bootstrap与局限分析。

## 目录约定

原始数据 `nyt.csv` 与 `ag.csv` 均直接保存在仓库根目录，无需解压或运行恢复程序。**老师查看报告和结果无需执行代码；后面的运行步骤仅供复现实验时使用。**

`t1_results/splits.csv` 是所有方法共用的划分清单。row_id是原CSV从0开始的数据记录索引。NYT先去除72条完全重复记录，再seed=42分层随机划分为9157/1145/1145；原始文件未改动。

`latex_report_revised/main.tex` 可独立编辑；figures子目录必须保留。选择XeLaTeX并编译两次，Overleaf可直接上传该目录。封面已填写姓名与学号。

结果目录内的JSON/CSV为实际运行输出；完整预测含原文，便于逐样本复核。`required_analysis/all_predictions.csv` 对齐了所有模型。下载的大权重、Python虚拟环境和临时文件不在提交包内。

## 环境

实验使用两个环境，不必强行安装成一个环境。

1. 本地CPU：Python 3.13.5，依赖见 `requirements_cpu.txt`，用于T1、T2、补充TF-IDF与报告分析。
2. GPU：Python 3.8.10、PyTorch 2.1.2+cu121、RTX A6000，依赖见 `requirements_gpu.txt`。现有CUDA PyTorch可直接保留，在隔离环境中安装其余包。

本地环境建立示例（Windows）：

```powershell
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements_cpu.txt
```

`bow_head64.py`只用Tokenizer，不需要GPU；若本地已有CPU PyTorch可继续保留。正式BERT训练需CUDA PyTorch；CPU版本不能运行该脚本。Linux GPU环境中的PyTorch应与驱动匹配，本次复现实测组合已列明，不要求改动系统环境。

## 从零训练规定任务

在项目根目录按顺序执行，以下`python`均指对应环境的解释器：

```text
python t1_experiment.py
python t2_experiment.py
python prepare_glove.py
python t2_required.py --models ag nyt glove
python prepare_bert.py
python t3_required.py --batch-size 16 --gradient-accumulation 2 --eval-batch-size 32
```

- T1脚本生成固定划分；后续脚本不再自行划分。若已使用提交包的splits.csv，可直接运行后续实验。
- `t2_experiment.py`生成可复用的NYT Skip-gram向量（也保留历史CBOW）。`t2_required.py`将NYT向量直接平均后重训LR，主结果在`*_raw_mean_predictions.csv`；归一化结果单列为消融，不与原实验混淆。
- GloVe从斯坦福官方ZIP按HTTP Range读取100d成员，并验证ZIP CRC。若网络不支持Range，可手动下载 `https://nlp.stanford.edu/data/glove.6B.zip` 并解压100d文件至`models/glove/`，同时保留提交包中对应的`source.json`。不要换成2024版。
- BERT准备脚本固定revision `86b5e0934494bd15c9632b12f734a8a67f723594`。若在本地下载后传至GPU服务器，应整体复制`models/bert-base-uncased/`。
- GPU服务器只需NYT原数据、划分清单、模型文件、`nlp_common.py`和`t3_required.py`。训练输出为`t3_64_results/`，完成后复制回本地同名目录进行分析。
- BERT保存验证Macro-F1最高的checkpoint；本次选中第3轮。预测前重载该checkpoint。训练/验证日志与配置均已保存。
- 所有LR按验证Macro-F1选C，平分取较小C；测试仅用于最终评价和事后分析，不按测试调参。

## 补充实验与报告重建

```text
python t1_tfidf.py
python bow_head64.py
python t3_experiment.py --batch-size 16 --gradient-accumulation 2 --eval-batch-size 32
python analyze_required.py
python build_required_report.py
```

其中`t3_experiment.py`为历史512头尾输入配置，正式64实验是`t3_required.py`。提交包保留了历史512结果，因此仅重建报告时无需重训512。`analyze_required.py`读取各模型预测，重新核算Accuracy/F1/混淆矩阵并校验数据哈希，固定seed进行3000次配对bootstrap。

最后在`latex_report_revised`目录执行两次：

```text
xelatex -interaction=nonstopmode -halt-on-error main.tex
```

## 结果核对（测试集百分数）

| 正式模型 | Accuracy | Macro-F1 |
|---|---:|---:|
| Binary BoW | 98.60 | 96.85 |
| Word Frequency | 98.69 | 96.79 |
| GloVe 6B 100d均值 | 98.08 | 95.58 |
| AG Word2Vec均值 | 97.90 | 94.99 |
| NYT Word2Vec均值 | 98.34 | 96.04 |
| BERT-64 | 97.12 | 93.95 |

不要将不同小数精度的四舍五入差异视为结果不一致。CPU/GPU及库版本变化可能导致合理微小差异；完整精度见JSON。

## 数据与来源校验

- nyt.csv SHA256：`de12ebe7f41316b798896bf975da840e2998f82393328d375fe5456a14e9eb2d`
- ag.csv SHA256：`06fa7de72a2f1cb41513c35260964518d029ff63ae631a807d3b189fbf246c4b`
- splits.csv SHA256：`4de67b1b482685379c1836ec32c5947ff3e813213473a7a81ee6a44a9d72a281`
- glove.6B.100d.txt SHA256：`95dde4dfd627ab26608d33e76d1195ec059734bd29089ea52cadb08d07c64544`
- BERT来源记录位于`models/bert-base-uncased/source.json`；源代码固定了同一revision。

`requirements_audit/缺项核对与修订.md`记录旧PDF缺项和本轮补齐情况。报告已完成实验内容；最终按老师要求提交包含PDF、完整代码和运行说明的GitHub仓库链接。提交链接：https://github.com/MaChuanZhi666/nlp-hw1-text-classification 。
