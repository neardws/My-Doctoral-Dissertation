# 车载信息物理融合系统建模与优化关键技术研究

重庆大学博士学位论文 `\LaTeX{} 🔥`

支持《**重庆大学博士、硕士学位论文格式标准（2023年修订）**》格式要求

## 目录

- [中文摘要](##中文摘要)
- [Abstract](##Abstract)
- [论文目录](##论文目录)
- [使用指南](##使用指南)
- [引用本学位论文](##引用本学位论文)
- [致谢](##致谢)

## 中文摘要

随着感知模式、通讯技术和计算范式的发展，传统汽车正朝着智能化、网联化和协同化方向迅速演进。以智能网联汽车为抓手，车联网驱动的智能交通系统（Intelligent Transportation System, ITS）有望实现更安全、高效和可持续发展的交通运输。车载信息物理融合系统（Vehicular Cyber-Physical System, VCPS）是实现ITS应用的基础和关键。然而，车联网高异构、高动态和分布式等特征以及ITS应用的多元化需求给VCPS的实现带来了巨大挑战。首先，面向车联网高动态物理环境，创新的服务架构和高效的数据感知与质量评估模型是VCPS的架构基础和驱动核心。其次，面向车联网分布式异构节点资源，先进的任务调度与资源分配策略是进一步优化VCPS服务质量的技术支撑。再次，面向智能交通系统多元应用需求，创新的服务质量与系统开销均衡策略是实现高质量、低成本和可扩展VCPS的理论保障。最后，面向动态复杂车联网环境，原型系统的设计和实现是针对VCPS必要的验证手段。因此，从架构融合与系统建模、协同资源优化、质量-开销均衡，以及原型系统实现四个方面，对车载信息物理融合系统进行了理论、技术和系统上的协同创新。主要创新成果包括：

1️⃣ **基于分层车联网架构的车载信息物理融合系统建模**。
首先，设计了分层车联网服务架构，其融合了软件定义网络和移动边缘计算范式，并最大化逻辑集中控制与边缘分布式服务的协同效应。在此基础上，提出了分布式感知与多源信息融合场景，其中边缘节点融合感知信息并构建逻辑视图。其次，建立了基于多类M/G/1优先队列的信息排队模型，并针对多源信息需求对车载信息物理融合质量进行建模，设计了 Age of View 指标来定量评估视图质量，并形式化定义了VCPS质量最大化问题。再次，提出了基于差分奖励的多智能体深度强化学习（Multi-Agent Difference-Reward-based Deep Reinforcement Learning, MADR）算法，通过确定信息感知频率、上传优先级，以及车与基础设施通信（Vehicle-to-Infrastructure, V2I）带宽，以实现VCPS质量最大化。最后，构建了仿真实验模型并进行了性能评估，证明了 MADR 算法的优越性。

2️⃣ **面向车载信息物理融合的通信与计算资源协同优化**。
首先，提出了协同通信与计算卸载场景，其中边缘节点协同调度通信与计算资源来实现VCPS实时任务处理。其次，考虑非正交多址接入（Non-Orthogonal Multiple Access, NOMA）车联网中同一边缘内与不同边缘间的干扰，并建立了V2I传输模型。形式化定义了协同资源优化问题，旨在最大化服务率。再次，提出了基于博弈理论的多智能体深度强化学习（Multi-Agent Game-Theoretic Deep Reinforcement Learning, MAGT）算法，将原问题分解为任务卸载和资源分配两个子问题，其中，任务卸载子问题建模为严格势博弈并实现纳什均衡，资源分配子问题分解为两个独立凸优化问题，并分别利用基于梯度的迭代方法和KKT条件得到最优解，以实现异构资源协同优化。最后，构建了仿真实验模型并进行了性能评估，证明了 MAGT 算法的优越性。

3️⃣ **面向车载信息物理融合的质量-开销均衡优化**。
首先，提出了协同感知与 V2I 上传场景，其中车辆进行协同感知与上传，而边缘节点在构建视图时会同时考虑视图质量与开销。其次，考虑边缘视图中多源信息的及时性和一致性，建立了VCPS质量模型。同时，考虑到视图信息冗余度、感知开销以及传输开销，建立了VCPS开销模型。在此基础上，形式化定义了双目标优化问题，以最大化VCPS质量和最小化VCPS开销。再次，提出了基于多目标的多智能体深度强化学习（Multi-Agent Multi-Objective Deep Reinforcement Learning, MAMO）算法，其中系统奖励包含VCPS质量和VCPS利润，并通过决斗评论家网络基于状态价值和动作优势来评估智能体动作，以实现质量-开销均衡。最后，构建了仿真实验模型并进行了性能评估，证明了 MAMO 算法的优越性。

4️⃣ **面向车载信息物理融合的超视距碰撞预警原型系统设计与实现**。
首先，提出了超视距（None-Light-of-Sight, NLOS）碰撞预警场景，其中交叉路口的车辆由于视线遮挡而具有潜在碰撞风险。其次，提出了基于车载信息物理融合系统优化的碰撞预警（Vehicular Cyber-Physical System Optimization based Collision Warning, VOCW）算法，建立了V2I 应用层传输时延拟合模型，设计了数据包丢失检测机制，通过丢包检测与时延补偿实现更加实时准确的逻辑视图以提高碰撞预警系统性能。再次，构建了仿真实验模型并进行了性能评估，证明了 VOCW 算法的优越性。最后，搭建了基于车载终端和路侧设备的硬件在环试验平台，并进一步在真实的车联网环境中实现了超视距碰撞预警原型系统，并验证了所提系统的可行性与有效性。

## Abstract

With the development of sensing patterns, communication technologies, and computing paradigms, traditional vehicles are rapidly evolving towards intelligence, networking, and collaboration. By leveraging intelligent connected vehicles as the starting point, the intelligent transportation system (ITS) driven by vehicle-to-everything (V2X) communications is expected to achieve safer, more efficient, and sustainable transportation. The vehicular cyber-physical system (VCPS) is the foundation and key to implement ITS applications. However, the implementation of VCPS faces significant challenges due to the highly heterogeneous, dynamic, and distributed nature of vehicular networks, along with the diverse requirements of ITS applications. First, an innovative service architecture and efficient data sensing and quality evaluation models tailored to the highly heterogeneous and dynamic physical environment of vehicular networks are the architecture foundation and driving force of VCPS. Second, advanced task scheduling and resource allocation towards distributed heterogeneous resources in vehicular networks is the technical support for further optimizing the quality of VCPS services. Third, a novel equilibrium strategy for system quality and cost towards the diversified application demands of ITS is the theoretical guarantee for achieving high-quality, low-cost, and scalable VCPS. Finally, the design and implementation of a prototype system towards the real-world dynamical vehicular network environment is a necessary verification method for VCPS. Therefore, this thesis focuses on the theoretical, technological and systematic innovations of the VCPS from four aspects: architecture integration and system modeling, collaborative resource optimization, quality-cost tradeoff, and prototype system implementation. The main innovative contributions are as follows:

1️⃣ **Vehicular cyber-physical fusion modeling based on vehicular hierarchical architecture**. First, this thesis designs a hierarchical service architecture that integrates software defined network and mobile edge computing paradigms to maximize their synergistic effects. Based on this, distributed sensing and heterogeneous information fusion scenarios are proposed, where edge nodes fuse sensing information and construct logical views. Second, this thesis establishes an information queuing model based on multi-class M/G/1 priority queues and models the quality of VCPS for various requirements of heterogeneous information. Specifically, the Age of View metric is designed to quantitatively evaluate the quality of views, and the VCPS quality maximization problem is formulated. Third, a multi-agent difference-reward-based deep reinforcement learning (MADR) algorithm is proposed to achieve VCPS quality maximization. The system state includes vehicle sensing information, edge cached information, and view requirements. The action space of the vehicle includes information sensing frequencies and uploading priorities, while the edge node allocates vehicle-to-infrastructure (V2I) bandwidth according to vehicular predicted trajectories and view requirements. Finally, this thesis constructs a simulation model and gives a comprehensive performance evaluation, which conclusively demonstrates the superiority of the MADR algorithm.

2️⃣ **Cooperative optimization for communication and computing resources in vehicular cyber-physical fusion**. First, this thesis proposes a collaborative communication and computing offloading scenario, where edge nodes collaborate to schedule communication and computing resources to achieve real-time task processing for VCPS. Second, this thesis considers intra-edge and inter-edge interferences in non-orthogonal multiple access (NOMA)-based vehicular networks, and establishes a V2I transmission model. The cooperative resource optimization (CRO) problem is formulated to maximize the service ratio for VCPS tasks. Third, a multi-agent game-theoretic deep reinforcement learning (MAGT) algorithm is proposed to achieve cooperative optimization for heterogeneous resources. Specifically, the CRO problem is decomposed into two subproblems, i.e., task offloading and resource allocation. The task offloading subproblem is modeled as an exact potential game and the Nash equilibrium is achieved by the MAGT algorithm. The resource allocation subproblem is decomposed into two independent convex optimization problems and solved by gradient-based iteration methods and KKT conditions, respectively. Finally, this thesis builds the simulation model and gives a comprehensive performance evaluation, which conclusively demonstrates the superiority of the MAGT algorithm.

3️⃣ **Quality-cost tradeoff optimization for vehicular cyber-physical fusion**. First, this thesis proposes a collaborative sensing and V2I uploading scenario, in which vehicles perform collaborative sensing and uploading, and edge nodes take into account both the quality and cost of the view when constructing it. Second, this thesis considers the timeliness and consistency of heterogeneous information in logical views and establishes a VCPS quality model. Meanwhile, considering the redundancy of view information, sensing cost, and transmission cost, a VCPS cost model is established. On this basis, a bi-objective optimization problem is formulated to maximize VCPS quality and minimize VCPS cost. Third, a multi-agent multi-objective deep reinforcement learning (MAMO) algorithm is proposed to achieve quality-cost tradeoff. Specifically, the system reward is a one-dimensional vector containing VCPS quality and VCPS profit. The thesis also proposes a dueling critic network to evaluate agent actions based on state-value and action-advantage. Finally, this thesis constructs a simulation model and gives a comprehensive performance evaluation, demonstrating the superiority of the MAMO algorithm.

4️⃣ **Design and implementation of a non-line-of-sight collision warning prototype system**. First, this thesis introduces a none-line-of-sight (NLOS) collision warning scenario, where vehicles at a crossroads have potential collision risks due to line-of-sight obstructions. Second, this thesis proposes an application-layer V2I communication delay fitting model and a packet loss detection mechanism, and proposes a vehicular cyber-physical system optimization based collision warning (VOCW) algorithm that achieves real-time and accurate logical view construction via packet loss detection and delay compensation to further improve system performance. Third, this thesis constructs a simulation model and conducts performance evaluation to prove the superiority of the VOCW algorithm. Finally, this thesis builds a hardware-in-the-loop test platform based on onboard units and roadside units and further implements a prototype system for NLOS collision warning in a real-world vehicle network environment, verifying the feasibility and effectiveness of the proposed system.

## 论文目录

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

## 使用指南

TBD

## 引用本学位论文

如果本学位论文或者本项目对你有所帮助，请引用本论文如下：

```bibtex
TBD
```

## 致谢

本项目是基于 https://github.com/nanmu42/CQUThesis ，感谢各位贡献者！

也感谢在本人进行学位论文撰写、校对过程中提供无私帮助的人们！

世界因你们更美好！
