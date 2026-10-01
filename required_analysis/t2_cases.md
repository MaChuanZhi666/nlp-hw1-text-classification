# T2 三方错例对比



从三组预测不一致的文章中，事后选取AG单独误判、NYT单独误判、GloVe单独误判各一例，避免只展示某一来源获胜的样本。这些案例用于解释，不能据此估计三组的总体胜率。完整原文、未知词、概率和逐词贡献保存在required_analysis/t2_case_evidence.json。

| row_id/真实类 | 来源 | 预测 | 覆盖率(%) | 类别分差 |
| --- | --- | --- | --- | --- |
| 2849/politics | glove | politics | 99.83 | -3.060 |
| 2849/politics | ag | business | 99.17 | +1.770 |
| 2849/politics | nyt | politics | 99.50 | -0.004 |
| 9704/business | glove | business | 99.89 | -1.295 |
| 9704/business | ag | business | 96.47 | -0.604 |
| 9704/business | nyt | sports | 97.83 | +3.530 |
| 11327/business | glove | sports | 100.00 | +0.588 |
| 11327/business | ag | business | 98.12 | -2.488 |
| 11327/business | nyt | business | 98.74 | -2.175 |

2849的分差为business减politics，另外两篇为sports减business；正值支持此处的错误类别。各模型分别训练，分差尺度不能跨模型解释为统一置信度。对固定平均词向量加线性分类器，可精确分解：

```latex
s_a(d)-s_b(d)=(b_a-b_b)+\sum_{w\in V_d}\frac{c_d(w)}{n_d}(\boldsymbol w_a-\boldsymbol w_b)^\top\boldsymbol e(w).
```

其中n_d为已知token总数，V_d为文档中已知词的集合，重复词由次数c_d(w)计入。分析脚本检查“全部词贡献之和加截距”与实际类别分差一致（误差小于0.0001）。这能定位线性决策的数值来源，但不是删除该词后的因果效果：删除词还会改变平均分母。

### 案例2849：保险产品等级与公共政策混淆

文章介绍医保交易平台、联邦政府公布的保险计划与价格，真实为politics。AG判business，GloVe和NYT正确。三者覆盖率都超过99%，AG仅缺失varieties、comanche、923、optima、064五个各出现一次的token。因此不能简单归因为大量政治词缺失。

在AG模型中，gold出现6次，对business减politics的分差贡献+1.466；premium贡献+0.575，而federal贡献-0.062、government贡献-0.197。原文gold和silver指保险计划等级；固定词向量不会随当前语境改变，平均表示也不保留修饰关系。结合全部词与截距，AG最终分差为+1.770，落入business。这里不能断言gold被内部解释成贵金属，只能确认其数值贡献推向商业类。NYT的分差约-0.004，虽然正确，却非常接近边界，并非同域词向量在此例具有压倒性优势。

### 案例9704：体育题材服务于酒店营销

文章讲万豪借棒球电影推广会员计划，真实为business。GloVe与AG正确，NYT误判sports。AG覆盖率96.47%，低于NYT的97.83%，却分类正确，直接反驳“覆盖率更高就一定分类更好”。AG未知词包括facebook、screenings和multicultural；但核心品牌marriott在三组词表中都存在。

marriott出现24次，在GloVe和AG中对sports减business分别贡献-2.135和-2.088，在NYT中仅为-0.177。NYT的robinson、baseball、league分别贡献+0.805、+0.708、+0.700；所有词与截距合计后分差为+3.530。问题不只是未知词，还涉及已知词向量与分类器共同形成的判别方向。由于三组LR也分别训练，不能把贡献差异全部归因于词向量本身，更不能由这篇反例推出同域训练普遍无效。

### 案例11327：冰球商品的关税报道

文章讨论加拿大取消体育用品进口关税及零售价格，真实为business。GloVe误判sports，AG与NYT正确。GloVe覆盖率100%，没有未知词，说明该错误完全不能用OOV解释。hockey出现13次，对GloVe的sports减business贡献+3.524；tariffs和prices分别贡献-0.155和-0.401，最终分差仍为+0.588。

AG与NYT中的hockey同样推向sports，贡献分别为+3.333和+3.002，但全篇其他词与截距共同使分差降为-2.488和-2.175，得到business。不能只取最大正贡献词就判断模型输出；平均表示加LR依赖的是整篇净证据。此例和9704共同显示，体育实体既可能是报道主旨，也可能只是商业活动的对象，平均池化难以显式区分这两种关系。

三例说明：覆盖率衡量词是否可用，逐词贡献解释当前线性分类器怎样累计证据，二者都不能单独代表篇章理解能力。主结果中NYT的测试点估计最高，但AG与GloVe各自也有正确而NYT错误的样本，因此仍保留三来源差异区间跨零的结论。

