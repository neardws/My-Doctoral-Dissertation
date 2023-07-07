# 车载信息物理融合系统建模与优化关键技术研究

> Research on Key Techniques for Modeling and Optimization of Vehicular Cyber-Physical Systems

## 特性🔥

* 本项目是本人的重庆大学博士学位论文，理论上硕士和本科也可使用
* 使用 LaTeX 编写，Mom再也不用担心我的博士论文排版（大雾）
* 支持《**重庆大学博士、硕士学位论文格式标准（2023年修订）**》格式要求

## 目录🔎

* [中文摘要](#中文摘要)
* [Abstract](#Abstract)
* [论文目录](#论文目录)
* [编译运行](#编译运行)
* [使用指南](#使用指南)
* [引用本学位论文](#引用本学位论文)
* [致谢](#致谢)

## 中文摘要🀄

随着感知模式、通讯技术和计算范式的发展，传统汽车正朝着智能化、网联化和协同化方向迅速演进。以智能网联汽车为抓手，车联网驱动的智能交通系统（Intelligent Transportation System, ITS）有望实现更安全、高效和可持续发展的交通运输。车载信息物理融合系统（Vehicular Cyber-Physical System, VCPS）是实现ITS应用的基础和关键。然而，车联网高异构、高动态和分布式等特征以及ITS应用的多元化需求给VCPS的实现带来了巨大挑战。首先，面向车联网高动态物理环境，创新的服务架构和高效的数据感知与质量评估模型是VCPS的架构基础和驱动核心。其次，面向车联网分布式异构节点资源，先进的任务调度与资源分配策略是进一步优化VCPS服务质量的技术支撑。再次，面向智能交通系统多元应用需求，创新的服务质量与系统开销均衡策略是实现高质量、低成本和可扩展VCPS的理论保障。最后，面向动态复杂车联网环境，原型系统的设计和实现是针对VCPS必要的验证手段。因此，从架构融合与系统建模、协同资源优化、质量-开销均衡，以及原型系统实现四个方面，对车载信息物理融合系统进行了理论、技术和系统上的协同创新。主要创新成果包括：

1️⃣ **基于分层车联网架构的车载信息物理融合系统建模**。
首先，设计了分层车联网服务架构，其融合了软件定义网络和移动边缘计算范式，并最大化逻辑集中控制与边缘分布式服务的协同效应。在此基础上，提出了分布式感知与多源信息融合场景，其中边缘节点融合感知信息并构建逻辑视图。其次，建立了基于多类M/G/1优先队列的信息排队模型，并针对多源信息需求对车载信息物理融合质量进行建模，设计了 Age of View 指标来定量评估视图质量，并形式化定义了VCPS质量最大化问题。再次，提出了基于差分奖励的多智能体深度强化学习（Multi-Agent Difference-Reward-based Deep Reinforcement Learning, MADR）算法，通过确定信息感知频率、上传优先级，以及车与基础设施通信（Vehicle-to-Infrastructure, V2I）带宽，以实现VCPS质量最大化。最后，构建了仿真实验模型并进行了性能评估，证明了 MADR 算法的优越性。

2️⃣ **面向车载信息物理融合的通信与计算资源协同优化**。
首先，提出了协同通信与计算卸载场景，其中边缘节点协同调度通信与计算资源来实现VCPS实时任务处理。其次，考虑非正交多址接入（Non-Orthogonal Multiple Access, NOMA）车联网中同一边缘内与不同边缘间的干扰，并建立了V2I传输模型。形式化定义了协同资源优化问题，旨在最大化服务率。再次，提出了基于博弈理论的多智能体深度强化学习（Multi-Agent Game-Theoretic Deep Reinforcement Learning, MAGT）算法，将原问题分解为任务卸载和资源分配两个子问题，其中，任务卸载子问题建模为严格势博弈并实现纳什均衡，资源分配子问题分解为两个独立凸优化问题，并分别利用基于梯度的迭代方法和KKT条件得到最优解，以实现异构资源协同优化。最后，构建了仿真实验模型并进行了性能评估，证明了 MAGT 算法的优越性。

3️⃣ **面向车载信息物理融合的质量-开销均衡优化**。
首先，提出了协同感知与 V2I 上传场景，其中车辆进行协同感知与上传，而边缘节点在构建视图时会同时考虑视图质量与开销。其次，考虑边缘视图中多源信息的及时性和一致性，建立了VCPS质量模型。同时，考虑到视图信息冗余度、感知开销以及传输开销，建立了VCPS开销模型。在此基础上，形式化定义了双目标优化问题，以最大化VCPS质量和最小化VCPS开销。再次，提出了基于多目标的多智能体深度强化学习（Multi-Agent Multi-Objective Deep Reinforcement Learning, MAMO）算法，其中系统奖励包含VCPS质量和VCPS利润，并通过决斗评论家网络基于状态价值和动作优势来评估智能体动作，以实现质量-开销均衡。最后，构建了仿真实验模型并进行了性能评估，证明了 MAMO 算法的优越性。

4️⃣ **面向车载信息物理融合的超视距碰撞预警原型系统设计与实现**。
首先，提出了超视距（None-Light-of-Sight, NLOS）碰撞预警场景，其中交叉路口的车辆由于视线遮挡而具有潜在碰撞风险。其次，提出了基于车载信息物理融合系统优化的碰撞预警（Vehicular Cyber-Physical System Optimization based Collision Warning, VOCW）算法，建立了V2I 应用层传输时延拟合模型，设计了数据包丢失检测机制，通过丢包检测与时延补偿实现更加实时准确的逻辑视图以提高碰撞预警系统性能。再次，构建了仿真实验模型并进行了性能评估，证明了 VOCW 算法的优越性。最后，搭建了基于车载终端和路侧设备的硬件在环试验平台，并进一步在真实的车联网环境中实现了超视距碰撞预警原型系统，并验证了所提系统的可行性与有效性。

## Abstract🔠

With the development of sensing patterns, communication technologies, and computing paradigms, traditional vehicles are rapidly evolving towards intelligence, networking, and collaboration. By leveraging intelligent connected vehicles as the starting point, the intelligent transportation system (ITS) driven by vehicle-to-everything (V2X) communications is expected to achieve safer, more efficient, and sustainable transportation. The vehicular cyber-physical system (VCPS) is the foundation and key to implement ITS applications. However, the implementation of VCPS faces significant challenges due to the highly heterogeneous, dynamic, and distributed nature of vehicular networks, along with the diverse requirements of ITS applications. First, an innovative service architecture and efficient data sensing and quality evaluation models tailored to the highly heterogeneous and dynamic physical environment of vehicular networks are the architecture foundation and driving force of VCPS. Second, advanced task scheduling and resource allocation towards distributed heterogeneous resources in vehicular networks is the technical support for further optimizing the quality of VCPS services. Third, a novel equilibrium strategy for system quality and cost towards the diversified application demands of ITS is the theoretical guarantee for achieving high-quality, low-cost, and scalable VCPS. Finally, the design and implementation of a prototype system towards the real-world dynamical vehicular network environment is a necessary verification method for VCPS. Therefore, this thesis focuses on the theoretical, technological and systematic innovations of the VCPS from four aspects: architecture integration and system modeling, collaborative resource optimization, quality-cost tradeoff, and prototype system implementation. The main innovative contributions are as follows:

1️⃣ **Vehicular cyber-physical fusion modeling based on vehicular hierarchical architecture**. First, this thesis designs a hierarchical service architecture that integrates software defined network and mobile edge computing paradigms to maximize their synergistic effects. Based on this, distributed sensing and heterogeneous information fusion scenarios are proposed, where edge nodes fuse sensing information and construct logical views. Second, this thesis establishes an information queuing model based on multi-class M/G/1 priority queues and models the quality of VCPS for various requirements of heterogeneous information. Specifically, the Age of View metric is designed to quantitatively evaluate the quality of views, and the VCPS quality maximization problem is formulated. Third, a multi-agent difference-reward-based deep reinforcement learning (MADR) algorithm is proposed to achieve VCPS quality maximization. The system state includes vehicle sensing information, edge cached information, and view requirements. The action space of the vehicle includes information sensing frequencies and uploading priorities, while the edge node allocates vehicle-to-infrastructure (V2I) bandwidth according to vehicular predicted trajectories and view requirements. Finally, this thesis constructs a simulation model and gives a comprehensive performance evaluation, which conclusively demonstrates the superiority of the MADR algorithm.

2️⃣ **Cooperative optimization for communication and computing resources in vehicular cyber-physical fusion**. First, this thesis proposes a collaborative communication and computing offloading scenario, where edge nodes collaborate to schedule communication and computing resources to achieve real-time task processing for VCPS. Second, this thesis considers intra-edge and inter-edge interferences in non-orthogonal multiple access (NOMA)-based vehicular networks, and establishes a V2I transmission model. The cooperative resource optimization (CRO) problem is formulated to maximize the service ratio for VCPS tasks. Third, a multi-agent game-theoretic deep reinforcement learning (MAGT) algorithm is proposed to achieve cooperative optimization for heterogeneous resources. Specifically, the CRO problem is decomposed into two subproblems, i.e., task offloading and resource allocation. The task offloading subproblem is modeled as an exact potential game and the Nash equilibrium is achieved by the MAGT algorithm. The resource allocation subproblem is decomposed into two independent convex optimization problems and solved by gradient-based iteration methods and KKT conditions, respectively. Finally, this thesis builds the simulation model and gives a comprehensive performance evaluation, which conclusively demonstrates the superiority of the MAGT algorithm.

3️⃣ **Quality-cost tradeoff optimization for vehicular cyber-physical fusion**. First, this thesis proposes a collaborative sensing and V2I uploading scenario, in which vehicles perform collaborative sensing and uploading, and edge nodes take into account both the quality and cost of the view when constructing it. Second, this thesis considers the timeliness and consistency of heterogeneous information in logical views and establishes a VCPS quality model. Meanwhile, considering the redundancy of view information, sensing cost, and transmission cost, a VCPS cost model is established. On this basis, a bi-objective optimization problem is formulated to maximize VCPS quality and minimize VCPS cost. Third, a multi-agent multi-objective deep reinforcement learning (MAMO) algorithm is proposed to achieve quality-cost tradeoff. Specifically, the system reward is a one-dimensional vector containing VCPS quality and VCPS profit. The thesis also proposes a dueling critic network to evaluate agent actions based on state-value and action-advantage. Finally, this thesis constructs a simulation model and gives a comprehensive performance evaluation, demonstrating the superiority of the MAMO algorithm.

4️⃣ **Design and implementation of a non-line-of-sight collision warning prototype system**. First, this thesis introduces a none-line-of-sight (NLOS) collision warning scenario, where vehicles at a crossroads have potential collision risks due to line-of-sight obstructions. Second, this thesis proposes an application-layer V2I communication delay fitting model and a packet loss detection mechanism, and proposes a vehicular cyber-physical system optimization based collision warning (VOCW) algorithm that achieves real-time and accurate logical view construction via packet loss detection and delay compensation to further improve system performance. Third, this thesis constructs a simulation model and conducts performance evaluation to prove the superiority of the VOCW algorithm. Finally, this thesis builds a hardware-in-the-loop test platform based on onboard units and roadside units and further implements a prototype system for NLOS collision warning in a real-world vehicle network environment, verifying the feasibility and effectiveness of the proposed system.

## 论文目录📖

* 1 绪论
  * 1.1 引言
  * 1.2 研究背景
  * 1.3 国内外研究现状
  * 1.4 研究目标与研究内容
  * 1.5 论文的特色与创新之处
  * 1.6 论文的组织架构
* 2 基于分层车联网架构的车载信息物理融合系统建模
  * 2.1 引言
  * 2.2 分层车联网架构设计
  * 2.3 分布式感知与多源信息融合场景
  * 2.4 车载信息物理融合质量指标设计
  * 2.5 基于差分奖励的多智能体强化学习算法设计
  * 2.6 实验设置与结果分析
  * 2.7 本章小结
* 3 面向车载信息物理融合的通信与计算资源协同优化
  * 3.1 引言
  * 3.2 协同通信与计算卸载场景
  * 3.3 协同资源优化问题定义
  * 3.4 基于博弈理论的多智能体强化学习算法设计
  * 3.5 实验设置与结果分析
  * 3.6 本章小结
* 4 面向车载信息物理融合的质量-开销均衡优化
  * 4.1 引言
  * 4.2 协同感知与V2I上传场景
  * 4.3 车载信息物理融合质量/开销模型
  * 4.4 质量-开销均衡问题定义
  * 4.5 基于多目标的多智能体强化学习算法设计
  * 4.6 实验设置与结果分析
  * 4.7 本章小结
* 5 超视距碰撞预警原型系统设计与实现
  * 5.1 引言
  * 5.2 超视距碰撞预警场景
  * 5.3 基于车载信息物理融合系统优化的碰撞预警算法
  * 5.4 实验设置与结果分析
  * 5.5 原型系统实现
  * 5.6 本章小结
* 6 总结与展望

## 编译运行🚆

- 本项目的 LaTeX 主文件为 [/main.tex](https://github.com/neardws/My-Doctoral-Dissertation/blob/master/main.tex)
- 可使用常见Latex编译软件，例如，macOS 平台中的 Texifier
- Tex 编译器为 XeLaTex
- 本人使用的环境
  - MacBook Pro 14-inch，2021  
  - macOS 14.0 Beta
  - Texifier 1.9.21
- 本项目编译出的 PDF 不包含中英文题名页以及独创性声明和使用授权书

![](https://github.com/neardws/My-Doctoral-Dissertation/blob/master/doc/example.jpg)


## 使用指南🛠

### 特别说明

如果有同学希望利用本项目来加快学位论文的撰写过程，那么非常欢迎，但是需要接受本项目的免责声明。

> 本项目已尽最大努力满足《重庆大学博士、硕士学位论文格式标准（2023年修订）》格式要求，但是仅凭我一人之力，肯定无法面面俱到，因此
> - 凡是利用本项目进行学位论文撰写的，对于学位论文的格式要求是否满足概不保证
> - 凡是利用本项目作为模版所生成的PDF进行学位申请产生的任何问题（包括但不限于格式问题），本项目概不负责
> - 本项目对于重庆大学2023年后的学位论文格式概不支持，如果想支持2023年之后的要求（如果有的话），请自己动手修改

如果接受以上免责声明，下面按照学位论文的不同组成部分依次介绍

### 中英文题名页

本项目生成的PDF中**不包含**中英文题名页，中英文题名页的原始文档为 [/doc/cover.doc](https://github.com/neardws/My-Doctoral-Dissertation/blob/master/doc/cover.doc)

**注意**：最终提交电子版本中 中文题名页 和 英文题名页 后都需要加一页空白页

### 独创性声明和使用授权书

本项目生成的PDF中**不包含**授权书，其文档在 [/doc/独创性声明学位论文版权使用授权书-普通.doc](https://github.com/neardws/My-Doctoral-Dissertation/blob/master/doc/独创性声明学位论文版权使用授权书-普通.doc)

也可设置用扫描页代替：
```LaTeX
% 原创声明和授权说明书，可选：用扫描页替换
\cquauthpage[authscan.pdf] 
```

当然，本项目提供的授权书是2023年所提交的版本，如果与现在的授权书有差异，请以现在的授权书格式为准。

### 中英文摘要和关键词

如需修改中文摘要，请更改：
```LaTeX
\begin{cabstract}	% 中文摘要
    % 中文摘要具体内容
\end{cabstract}
```

如需修改英文摘要，请更改：
```LaTeX
\begin{eabstract}	% 英文摘要
    % 英文摘要具体内容
\end{cabstract}
```

其中，`\circled{1}`可输出相应包含数字的圆圈符号，如①

中文关键词和英文关键词修改如下：

```LaTeX
% 中文关键词，请使用英文逗号分隔：
\ckeywords{车联网,信息物理融合系统,车载边缘计算,优化算法,多智能体深度强化学习}

% 英文关键词，请使用英文逗号分隔，关键词内可以空格：
\ekeywords{Vehicular Networks, Cyber-Physical Systems, Vehicular Edge Computing, Optimization Algorithm, Multi-Agent Deep Reinforcement Learning
}
```

### 目录

目录为根据 LaTeX 中正文中的章节（chapter，section，subsection）自动生成，但是默认的格式不能满足学位论文要求，因此，目录格式进行过额外的调整：
```LaTeX
% 目录格式设置
\usepackage{tocloft}
% 设置一级标题的字体样式
\renewcommand{\cftchapfont}{\bfseries\zihao{4}}
% 设置二级标题的字体样式
\renewcommand{\cftsecfont}{\bfseries\zihao{5}}
\renewcommand{\cftsecindent}{12bp}
% 设置三级标题的字体样式和缩进
\renewcommand{\cftsubsecfont}{\zihao{5}}
\renewcommand{\cftsubsecindent}{25bp}
% 设置章标题的编号宽度
\setlength{\cftchapnumwidth}{0em} 
% 设置章标题的编号和标题之间的间距
\renewcommand{\cftchapaftersnum}{\hspace{1em}} 
% 设置二级标题的编号宽度
\setlength{\cftsecnumwidth}{0em} 
% 设置二级标题的编号和标题之间的间距
\renewcommand{\cftsecaftersnum}{\hspace{1em}} 
% 设置三级标题的编号宽度
\setlength{\cftsubsecnumwidth}{0em} 
% 设置三级标题的编号和标题之间的间距
\renewcommand{\cftsubsecaftersnum}{\hspace{1em}} 
% 设置页码字体
\renewcommand{\cftchappagefont}{\normalfont}
\renewcommand{\cftsecpagefont}{\normalfont}
\renewcommand{\cftsubsecpagefont}{\normalfont}
```

### 插图和表格索引

插图和表格索引均为根据正文中的插图和表格自动生成，通过以下语句将其加入：

```LaTeX
%% 插图索引，可选，如不用可注释掉
\clearpage
\phantomsection  
\addcontentsline{toc}{chapter}{插图索引}    % 将插图索引添加至目录中，其中toc 表示table of content
\listoffigures    % 显示插图索引
%% 表格索引，可选，同上
\clearpage
\phantomsection  
\addcontentsline{toc}{chapter}{表格索引}
\listoftables
```

其格式的修改语句如下：

```LaTeX
\usepackage{titletoc} % 引入 titletoc 宏包

\titlecontents{figure}
  [0pt] % 左边距
  {\fontsize{10.5}{15}图~\selectfont\parskip0pt\parindent0pt} % 字体设置和行距
  {\thecontentslabel\enspace} % 编号
  {}
  {\titlerule*[0.3pc]{.}\contentspage}
  
\titlecontents{table}
  [0pt] % 左边距
  {\fontsize{10.5}{15}表~\selectfont\parskip0pt\parindent0pt} % 字体设置和行距
  {\thecontentslabel\enspace} % 编号
  {}
  {\titlerule*[0.3pc]{.}\contentspage}
  
% 消除章节之间的间距
\newcommand{\removelofgap}{\addtocontents{lof}{\vspace{-10pt}}}
\newcommand{\removelotgap}{\addtocontents{lot}{\vspace{-10pt}}}

\usepackage{tocloft}
% 设置 listoffigures 和 listoftables 标题字体为三号黑体
\renewcommand{\cftloftitlefont}{\centering\CJKfontspec{SimHei}\fontsize{16}{20}\selectfont\hspace*{\fill}}
\renewcommand{\cftlottitlefont}{\centering\CJKfontspec{SimHei}\fontsize{16}{20}\selectfont\hspace*{\fill}}

% 在 listoffigures 和 listoftables 标题前后各空一行
\renewcommand{\cftbeforeloftitleskip}{\baselineskip} % 标题前空一行
\renewcommand{\cftafterloftitleskip}{\baselineskip} % 标题后空一行
\renewcommand{\cftbeforelottitleskip}{\baselineskip} % 标题前空一行
\renewcommand{\cftafterlottitleskip}{\baselineskip} % 标题后空一行

```

### 符号和缩略语对照表

- 符号对照表的内容在 [/content/denotation.tex](https://github.com/neardws/My-Doctoral-Dissertation/blob/master/contents/denotation.tex)
- 缩略语对照表的内容在 [/contents/abbreviate.tex](https://github.com/neardws/My-Doctoral-Dissertation/blob/master/contents/abbreviate.tex)

```LaTeX
%% 符号对照表，可选
\clearpage
\phantomsection 
\addcontentsline{toc}{chapter}{主要符号对照表}
\input{contents/denotation}
%% 缩略语对照表，可选
\clearpage
\phantomsection 
\addcontentsline{toc}{chapter}{缩略语对照表}
\input{contents/abbreviate}
```

由于缩略语不一定初次就能整理完毕，而每次添加新缩略语后还需要根据字典顺序进行重新插入，这非常地麻烦。因此，本项目提供了一个Python脚本，其可以方便地对缩略语对照表中的内容进行排序，并生成排序后的tex文件。

该脚本位于 [/contents/abbreviate_sort.py](https://github.com/neardws/My-Doctoral-Dissertation/blob/master/contents/abbreviate_sort.py)，如需运行，请修改main函数中的file_path和output_path。

```Python
def main():
    file_path = "abbreviate.tex"    # 缩略语对照表原始文件位置
    original_contents = read_file(file_path)

    sorted_items = sort_items(extract_items(original_contents))
    sorted_contents = generate_sorted_content(sorted_items, original_contents)

    output_path = "abbreviate sorted.tex"   # 排序后输出的文件位置
    write_file(output_path, sorted_contents)
```

### 正文

正文部分主要包含以序号为索引的章节，例如绪论等。

```LaTeX
\include{contents/introduction}   % 对应 第一章 绪论
\include{contents/architecture}
\include{contents/resource}
\include{contents/qos}
\include{contents/system}
\include{contents/conclusion}
%\include{contents/yourFreeChoise}
```

各章节的tex文件均位于 [/contents/](https://github.com/neardws/My-Doctoral-Dissertation/tree/master/contents)，例如，第一章绪论的文件位于 [contents/introduction.tex](https://github.com/neardws/My-Doctoral-Dissertation/tree/master/contents/introduction.tex)

```LaTex
\chapter[\hspace{0pt}绪\hskip\ccwd{}论]{{\CJKfontspec{SimHei}\zihao{3}\hspace{-5pt}绪\hskip\ccwd{}论}}
\section[\hspace{-2pt}引言]{{\CJKfontspec{SimHei}\zihao{-3} \hspace{-8pt}引言}}\label{section 1-1}
\section[\hspace{-2pt}研究背景]{{\CJKfontspec{SimHei}\zihao{-3} \hspace{-8pt}研究背景}}\label{section 1-2}
\section[\hspace{-2pt}国内外研究现状]{{\CJKfontspec{SimHei}\zihao{-3} \hspace{-8pt}国内外研究现状}}\label{section 1-3}
\subsection[\hspace{-2pt}车联网服务架构研究与现状]{{\CJKfontspec{SimHei}\zihao{4} \hspace{-8pt}车联网服务架构研究与现状}}
\subsection[\hspace{-2pt}车载信息物理融合系统建模研究与现状]{{\CJKfontspec{SimHei}\zihao{4} \hspace{-8pt}车载信息物理融合系统建模研究与现状}}
\subsection[\hspace{-2pt}车联网资源分配与任务卸载研究与现状]{{\CJKfontspec{SimHei}\zihao{4} \hspace{-8pt}车联网资源分配与任务卸载研究与现状}}
\subsection[\hspace{-2pt}车载信息物理融合质量/开销优化研究与现状]{{\CJKfontspec{SimHei}\zihao{4} \hspace{-8pt}车载信息物理融合质量/开销优化研究与现状}}
\subsection[\hspace{-2pt}智能交通系统安全相关应用研究与现状]{{\CJKfontspec{SimHei}\zihao{4} \hspace{-8pt}智能交通系统安全相关应用研究与现状}}
\section[\hspace{-2pt}研究目标与研究内容]{{\CJKfontspec{SimHei}\zihao{-3} \hspace{-8pt}研究目标与研究内容}}\label{section 1-4}
\subsection[\hspace{-2pt}研究目标]{{\CJKfontspec{SimHei}\zihao{4} \hspace{-8pt}研究目标}}
\subsection[\hspace{-2pt}研究内容]{{\CJKfontspec{SimHei}\zihao{4} \hspace{-8pt}研究内容}}
\section[\hspace{-2pt}论文的特色与创新之处]{{\CJKfontspec{SimHei}\zihao{-3} \hspace{-8pt}论文的特色与创新之处}}\label{section 1-6}
\section[\hspace{-2pt}论文的组织结构]{{\CJKfontspec{SimHei}\zihao{-3} \hspace{-8pt}论文的组织结构}}\label{section 1-7}
```

各章节中最多包含 chapter、section、subsection 三个层级，对于不同层级，其格式要求略有不同，但其实都类似，下面以引言为例：

```LaTeX
\section[\hspace{-2pt}引言]{{\CJKfontspec{SimHei}\zihao{-3} \hspace{-8pt}引言}}\label{section 1-1}

% 第一步分解
\section[]()  % [] 表示索引格式，（）表示实际显示格式，当索引格式与实际显示格式有区别时，可采用这种形式

% [] 括号中内容
\hspace{-2pt}引言  % \hspace{-2pt} 表示水平缩进 -2 pt，即向前移动 2 pt

% () 括号中内容
{\CJKfontspec{SimHei}\zihao{-3} \hspace{-8pt}引言}
% \CJKfontspec{SimHei} 表示 使用 SimHei 字体
% \zihao{-3} 字号为 小三号
```

### 插图和表格

- 图片样例

```LaTeX
\begin{figure}[h]   % h 表示图片显示位置为当前插入位置
	\centering        % 居中
	\captionsetup{font={small, stretch=1.312}}    % 设置标题格式
    \includegraphics[width=1\columnwidth]{Fig1-1-V2X.pdf}    % 设置图片宽度为占满一栏
	\bicaption[车联网演进方向]{车联网演进方向}[Evolution direction of the Internet of Vehicles]{Evolution direction of the Internet of Vehicles}   % 分别为图片的中英文标题
	\label{fig 1-1}  % 图片标签
\end{figure}
```

- 表格样例

```LaTex
\begin{table}[h]\small    % 设置表格字体为5号
\setstretch{1.245}        % 设置具有指定弹力的橡皮长度（原行宽的1.2倍）
\captionsetup{font={small, stretch=1.512}}
\centering
\bicaption{不同场景的交通特征}{Traffic characteristics of each scenario}    % 中英文标题
\resizebox{\columnwidth}{!}{%
\begin{tabular}[t]{cccccccc}
\toprule
场景&轨迹&ADT (s)&VDT&AVN&VVN&AVS (m/s)&VVS\\
\midrule
1&718&198.3&123.8&474.6&11.6&5.22&2.61\\
2&359&173.7&124.1&207.9&3.93&7.30&3.16\\
3&206&145.5&114.7&99.9&7.65&8.06&3.70\\
\bottomrule
\end{tabular}}
\label{table 2-1}
\end{table} 
```

### 参考文献

学位论文参考文献需要满足GB/T 7714—2015 《信息与文献 参考文献著录规则》要求，因此直接使用 [GB/T 7714—2015 BibTeX Style](https://github.com/zepinglee/gbt7714-bibtex-style) 即可，在这里也感谢该项目贡献者们！

```LaTex
% 参考文献
\bibliographystyle{gbt7714-numerical}  
\bibliography{ref/refs}
```

本项目的参考文献是使用的顺序编码制，如果有其他需要，也可以参考 [GB/T 7714—2015 BibTeX Style](https://github.com/zepinglee/gbt7714-bibtex-style) 项目。

以下列出不同类型的参考文献所需要的信息，注意不要有缺失情况，否则会出现例如[s1..sn]的类似输出。

- 期刊
```bibtex
@article{agiwal2016next,
 author = {Agiwal, Mamta and Roy, Abhishek and Saxena, Navrati},
 journal = {IEEE Communications Surveys \& Tutorials},
 number = {3},
 pages = {1617--1655},
 publisher = {IEEE},
 title = {{Next generation 5G wireless networks: A comprehensive survey}},
 volume = {18},
 year = {2016}
}
```
- 会议
```bibtex
@inproceedings{dai2021asynchronous,
 address = {Virtual Conference},
 author = {Dai, Penglin and Hu, Kaiwen and Wu, Xiao and others},
 pages={1-10},
 booktitle = {Proceedings of IEEE International Conference on Computer Communications (INFOCOM)},
 publisher = {IEEE},
 title = {{Asynchronous deep reinforcement learning for data-driven task offloading in MEC-empowered vehicular networks}},
 year = {2021}
}
```
- 书籍
```bibtex
@book{cheng2021feng,
 address = {北京},
 author = {{陈山枝, 胡金玲, 赵丽, 等}},
 publisher = {人民邮电出版社},
 title = {{蜂窝车联网（C-V2X）}},
 year = {2021}
}
```

### 附录

附录文件位于 [\contents\appendix.tex](https://github.com/neardws/My-Doctoral-Dissertation/blob/master/contents/appendix.tex)，其中最后一部分必须为学位论文数据集

```LaTeX
\newpage
\section[\hspace{-2pt}学位论文数据集]{{\CJKfontspec{SimHei}\zihao{-3} \hspace{-8pt}学位论文数据集}}

\begin{table}[h]
\resizebox{\columnwidth}{!}{%
\begin{tabular}{|cllcclclcl|}
\hline
\multicolumn{4}{|c|}{\heiti{关键词}}             & \multicolumn{2}{c|}{\heiti{密级}}   & \multicolumn{4}{c|}{\heiti{中图分类号}}                                    \\ \hline
\multicolumn{4}{|c|}{\begin{tabular}[c]{@{}c@{}}车载信息物理融合系统;\\异构车联网; 车载边缘计算;\\资源优化; 多智能体深度强化学习\end{tabular}} & \multicolumn{2}{c|}{公开} & \multicolumn{4}{c|}{TP} \\ \hline
\multicolumn{3}{|c|}{\heiti{学位授予单位名称}} & \multicolumn{3}{c|}{\heiti{学位授予单位代码}}    & \multicolumn{2}{c|}{\heiti{学位类别}}  & \multicolumn{2}{c|}{\heiti{学位级别}}        \\ \hline
\multicolumn{3}{|c|}{\secretize{重庆大学}}     & \multicolumn{3}{c|}{\secretize{10611}}       & \multicolumn{2}{c|}{学术学位}  & \multicolumn{2}{c|}{博士}          \\ \hline
\multicolumn{4}{|c|}{\heiti{论文题名}}            & \multicolumn{2}{c|}{\heiti{并列题名}} & \multicolumn{4}{c|}{\heiti{论文语种}}                                     \\ \hline
\multicolumn{4}{|c|}{\begin{tabular}[c]{@{}c@{}}车载信息物理融合系统建模与优化关键技术研究\end{tabular}}               & \multicolumn{2}{c|}{无}   & \multicolumn{4}{c|}{中文} \\ \hline
\multicolumn{3}{|c|}{\heiti{作者姓名}}     & \multicolumn{3}{c|}{\secretize{许新操}}         & \multicolumn{2}{c|}{\heiti{学号}}    & \multicolumn{2}{c|}{\secretize{20191401452}} \\ \hline
\multicolumn{6}{|c|}{\heiti{培养单位名称}}                                      & \multicolumn{4}{c|}{\heiti{培养单位代码}}                                   \\ \hline
\multicolumn{6}{|c|}{\secretize{重庆大学}}                                        & \multicolumn{4}{c|}{\secretize{10611}}                                    \\ \hline
\multicolumn{3}{|c|}{\heiti{学科专业}}     & \multicolumn{3}{c|}{\heiti{研究方向}}        & \multicolumn{2}{c|}{\heiti{学制}}    & \multicolumn{2}{c|}{\heiti{学位授予年}}       \\ \hline
\multicolumn{3}{|c|}{计算机科学与技术} & \multicolumn{3}{c|}{车联网}         & \multicolumn{2}{c|}{4年}     & \multicolumn{2}{c|}{\secretize{2023年}}        \\ \hline
\multicolumn{3}{|c|}{\heiti{论文提交日期}}   & \multicolumn{3}{c|}{\secretize{2023年6月}}     & \multicolumn{2}{c|}{\heiti{论文总页数}} & \multicolumn{2}{c|}{\pageref{LastPage}}         \\ \hline
\multicolumn{3}{|c|}{\heiti{导师姓名}}     & \multicolumn{3}{c|}{\secretize{刘凯}}          & \multicolumn{2}{c|}{\heiti{职称}}    & \multicolumn{2}{c|}{教授}          \\ \hline
\multicolumn{6}{|c|}{\heiti{答辩委员会主席}}                                     & \multicolumn{4}{c|}{\secretize{雒江涛}}                                      \\ \hline
\multicolumn{10}{|c|}{\heiti{\begin{tabular}[c]{@{}c@{}} 电子版论文提交格式\\ 文本（\checkmark） 图像（） 视频（）音频（）多媒体（）其他（）\end{tabular}}}                              \\ \hline
\end{tabular}%
}
\end{table}
```

### 致谢

致谢中主要需要注意落款的格式：

```LaTeX
\vfill
\begin{flushright}
{\CJKfontspec{STXingkai} \Large 许新操} \hspace*{3.5em}
\\  \hspace*{\fill} \\
{二〇二三年五月\hspace*{1em}于重庆}
\end{flushright}
```

## 引用本学位论文📄

如果本学位论文或者本项目对你有所帮助，请引用本学位论文如下：

```bibtex
@phdthesis{xu2023research,
  author = {许新操},
  title = {车载信息物理融合系统建模与优化关键技术研究},
  school = {重庆大学},
  year = {2023},
  type = {PhD thesis}
}

@phdthesis{xu2023research,
  author = {Xincao Xu},
  title = {Research on Key Techniques for Modeling and Optimization of Vehicular Cyber-Physical Systems},
  school = {Chongqing University},
  year = {2023},
  type = {PhD thesis}
}
```

## 致谢🙏

本项目是基于 https://github.com/nanmu42/CQUThesis ，感谢各位贡献者！

也感谢在本人进行学位论文撰写、校对过程中提供无私帮助的人们！

本学位论文虽然经过了预答辩、盲审、答辩等诸多流程，但是可能无法避免仍存在一些本人暂未发现的问题。我之所以将我的学位论文在GitHub上公开，一来是想帮助各位更快地完成学位论文撰写，尽量少花费精力在论文格式上，二来也希望各位在使用本项目时，如果发现了本论文中有问题，也欢迎各位提交 issue！

世界因你们更美好！
