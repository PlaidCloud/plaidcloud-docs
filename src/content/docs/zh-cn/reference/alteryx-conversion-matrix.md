---
title: Alteryx 转换矩阵
description: PlaidCloud 如何将 Alteryx 工具转换为原生高级工作流步骤、宏、变量和托管执行器，并附每个工具的支持状态。
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/alteryx-conversion-matrix.md
---

PlaidCloud 将 Alteryx 工作流、应用和宏转换为原生高级工作流。导入器会把每个 Alteryx 工具映射为工作流步骤、宏结构、受控变量、基于文档的文件操作或托管作业执行器，因此转换后的工作流以云原生方式运行，而不是通过模拟运行。

**几乎所有标准 Alteryx 工具都可以完整转换。** 下面按工具列出支持状态：

- **完整**：转换为原生 PlaidCloud 步骤、宏、变量、制品或托管执行器，并运行该工具的功能。大多数工具属于此类。
- **部分**：转换后可运行其常见用法，但该工具的某一种独立*能力模式*尚未实现。这种情况很少见。
- **不支持**：不提供转换，该能力改为以原生方式重建。

外部系统连接器（Salesforce、HTTP、Google Analytics、Cassandra、电子邮件、Hadoop、Spark 等）是**连接而非转换**，参见[连接到外部系统](#连接到外部系统)。

## 工具支持

| Alteryx 工具 | 状态 | PlaidCloud 对应项 | 转换内容 |
| --- | --- | --- | --- |
| Action | 完整 | 变量绑定和条件步骤配置 | 根据转换后的应用输入更新下游步骤设置。 |
| Analytic App interface (`.yxwz`) | 部分 | 已发布的 Panel 应用“App Runner”前端 | 应用的 `<Questions>` 布局会被具体化为一个可用的 Panel 应用，用于收集用户输入并驱动转换后的工作流，并在转换过程中自动发布（没有输入控件的应用会被跳过）。常见的问题类型，包括文本、数值（Numeric Up Down）、日期、复选框、单选按钮、下拉列表、列表框、树、文件浏览和文件夹浏览，都会变为 App Runner 控件。其值未绑定到任何工作流变量的问题会显示可见的提示，而不是悄悄收集一个无效值；较少见的问题类型会被标记待审核，而不会具体化。参见[使用转换后的 Alteryx 应用](/zh-cn/guides/workflows/use-converted-alteryx-apps/#app-runner-前端)。 |
| Append Fields | 完整 | 追加字段转换 | 将一个数据流中的字段追加到另一个数据流。 |
| Auto Field | 完整 | 自动字段大小转换 | 保留推断出的字段大小。 |
| AutoML | 完整 | [ML：训练模型](/zh-cn/reference/workflow-steps/machine-learning/ml-train/) | 将模型方法、目标和候选算法的选择合并为一个 ML Train 步骤，与 Classification 和 Regression 相同。AutoML 不会记录哪个候选算法在 Alteryx 运行时实际获胜，因此转换时会选择第一个被勾选且 ML Train 支持的算法，并注明所做选择。请将转换后的 AutoML 步骤与您自己的 Alteryx 结果进行比较。 |
| Barcode | 完整 | 条形码执行器 | 按配置的码制读取或写入条形码。 |
| Batch Macro | 部分 | 按控制锚点表展开的宏 | 调用方针对其控制输入的每条记录运行一次整个宏，并在每次运行时绑定内部的控制参数，包括调用方重命名为显示标签的控制参数（仅当只有一个参数参与时），以及根据变量重写 Select 字段列表的 `UpdateRawXml` Action。对于无法安全重现每次运行取值的情形，会按名称失败关闭，而不会错误地转换：重写 Select 字段列表以外内容的 `UpdateRawXml`，以及用变量替换 Filter 整个表达式的 Action（其每次运行的原始语法会被错误求值）。 |
| Browse | 完整 | Browse / 直通 | 保留以供检查，无运行时开销。 |
| Buffer | 完整 | [Spatial Buffer 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-buffer/) | 将每个几何图形按固定距离扩展。 |
| Build Features | 部分 | [Build Features 步骤](/zh-cn/reference/workflow-steps/tables/table-build-features/) | 转换算术和交互基元、日期部分提取、显式阈值分箱、z 分数和最小-最大缩放，以及独热编码。跨表聚合（跨 Manage Relationships 选项卡的 Deep Feature Synthesis）、PCA、目标编码和数据驱动的自动分箱没有对应实现，每一项都会在转换报告中按名称标记，而不会被悄悄丢弃。 |
| Calgary Cross Count | 完整 | [Calgary 数据库](/zh-cn/guides/workflows/migrate-alteryx-workflows/#calgary-数据库)聚合 | 对已建立索引的字段分组，并统计每个自定义字段的命名值数量。 |
| Calgary Cross Count Append | 完整 | [Calgary Cross Count Append](/zh-cn/guides/workflows/migrate-alteryx-workflows/#calgary-join-和-cross-count-append) | 将每条输入记录与值索引匹配，然后统计其匹配到的数据库记录数。 |
| Calgary Input | 完整 | [Calgary 数据库](/zh-cn/guides/workflows/migrate-alteryx-workflows/#calgary-数据库)输入 | 读取数据库，并将其保存的查询作为筛选器应用。 |
| Calgary Join | 完整 | [Calgary Join](/zh-cn/guides/workflows/migrate-alteryx-workflows/#calgary-join-和-cross-count-append) | 将每条记录与数据库上的值索引匹配，保留匹配到的记录。 |
| Calgary Loader | 完整 | [Calgary 数据库](/zh-cn/guides/workflows/migrate-alteryx-workflows/#calgary-数据库)写入器 | 写入每个 Calgary 读取器所绑定的替身表。 |
| Centroid | 完整 | Centroid 执行器操作 | 将每个几何图形缩减为其中心点，并追加为 `Centroid` 列。 |
| Check Box | 完整 | 受控工作流变量 | 将应用的复选框选择转换为受控输入。 |
| Classification | 完整 | [ML：训练模型](/zh-cn/reference/workflow-steps/machine-learning/ml-train/) | 将 Assisted Modeling 链合并为一个 ML Train 步骤，包含其算法、目标、特征和超参数。 |
| Comment / Annotation / Link | 完整 | 画布注释 | 保留为工作流上下文。 |
| Condition | 完整 | 步骤条件 | 根据表达式触发警告、错误或分支。 |
| Control Parameter | 完整 | 宏控制参数 | 映射为 PlaidCloud 宏参数。 |
| Convex Hull | 完整 | Convex Hull 执行器操作 | 构建包围每个几何图形的最小凸多边形，并追加为 `ConvexHull` 列。 |
| Create Points | 完整 | 带 `geom_point` 的 [Table Extract 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-sql-recipes/) | 在 SQL 中根据经度/纬度列构建点几何。 |
| Create Samples | 完整 | Table Extract 步骤，每个输出一个 | 按配置的百分比将输入拆分为 Estimation、Validation 和 Holdout。 |
| Cross Tab | 完整 | 透视 / 交叉表转换 | 将行透视为列，涵盖所有聚合方法和派生合计。 |
| Data Cleansing | 完整 | 数据清理转换 | 清理空白、空值、标点和大小写。 |
| Date | 完整 | 工作流变量（日期） | 为步骤和条件输出 ISO 日期值。 |
| DateTime | 完整 | 日期/时间转换 | 转换日期和时间的解析与格式化。 |
| Detour | 完整 | 条件分支路由 | 将路由选择转换为 DAG 条件。 |
| Detour End | 完整 | 条件分支合并 | 重新汇合按条件选择的分支。 |
| Directory | 完整 | 文档目录列表 | 列出文档路径中的文件。 |
| Distance | 完整 | 带 `ST_DISTANCE_SPHERE` 的 [Table Extract 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-sql-recipes/) | 在 SQL 中计算大地点到点的距离和方位角。 |
| Download | 完整 | 针对 REST 连接的 [REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/)步骤 | 下载外部数据或制品；运行前需为转换后的步骤分配一个 REST 连接。 |
| Drop Down | 完整 | 受控工作流变量 | 将应用的下拉列表选择转换为受控输入。 |
| Dynamic Input | 部分 | 动态文档输入 | 在运行时解析文件模式和由变量驱动的输入。当上游 Filter 通过精确匹配将工作表固定为单一名称时，Excel *ReadList*（从 Directory 工具列出的每个工作簿中读取一个工作表，然后合并）会转换为文件夹通配符的工作表读取。由 Contains、不等式或 OR 筛选器选定的工作表，或跨多个工作表的读取，会被拒绝，以免读错工作表。 |
| Dynamic Rename | 完整 | 动态重命名转换 | 根据元数据或规则重命名字段。 |
| Dynamic Replace | 完整 | 动态替换转换 | 应用来自第二个数据流的替换规则。 |
| Dynamic Select | 完整 | 动态字段选择转换 | 按类型、名称或规则选择字段。 |
| Error | 完整 | 步骤条件（错误） | 将配置的错误行为转换为步骤条件。 |
| Feature Types | 完整 | [ML：训练模型](/zh-cn/reference/workflow-steps/machine-learning/ml-train/)特征配置 | 将每个字段所分配的模型角色带入合并后的 ML Train 步骤。 |
| File Browse | 完整 | 受控文档文件变量 | 让用户为转换后的应用运行选择文件。 |
| Filter | 完整 | 筛选器转换 | 按表达式将记录拆分为真和假两条路径。 |
| Fit | 完整 | [ML：训练模型](/zh-cn/reference/workflow-steps/machine-learning/ml-train/) | 并入合并后的 ML Train 步骤。 |
| Folder Browse | 完整 | 受控文档文件夹变量 | 让用户为转换后的应用运行选择文件夹。 |
| Formatted Excel output into a styled template | 部分 | 支持模板的 Excel 写入器（多工作表使用 [Export to Excel Sheets 步骤](/zh-cn/reference/workflow-steps/export/export-to-excel-sheets/)） | 写入带样式的模板时会保留模板的格式，包括值、数字格式、字体、填充、边框、合并单元格和列宽，并带入命名的工作表和区域。这既适用于单个工作表，也适用于将多个输出组装到同一工作簿的不同工作表中，并在一次处理中全部填充，因此各工作表不再互相覆盖。有一种情况仍为部分：包含数据透视表或图表的模板，在写入其工作表时会丢弃这些对象。普通（无样式）Excel 输出为完整，参见 Output Data。 |
| Formula | 完整 | 公式转换 | 将字段表达式转换为 PlaidCloud 表达式或 SQL。 |
| Fuzzy Match | 完整 | 模糊匹配执行器 | 基于键、阈值和候选项审核进行匹配。 |
| Generalize | 完整 | [Spatial Generalize 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-generalize/) | 在保持拓扑的前提下，将几何图形简化到指定容差。 |
| HTML | 完整 | 报表文本 / HTML 制品 | 将内容保留为报表或制品输出。 |
| Image Processing | 完整 | 图像转换执行器 | 按画布顺序应用灰度、缩放、裁剪和旋转。 |
| Image Profile | 完整 | 图像概要执行器 | 报告尺寸、模式、格式、通道和亮度统计。 |
| Image to Text | 完整 | OCR 执行器 | 通过托管 OCR 从图像中提取文本。 |
| Input Data | 完整 | 基于文档的文件输入 | 将 `.yxdb`、`.dbf`、Excel 和固定宽度 `.flat` 源文件加载到工作流数据中。 |
| Insights | 完整 | 仪表板 / 制品输出 | 创建云原生的审阅制品。 |
| Interactive Chart | 完整 | 图表制品 | 根据转换后的数据创建图表制品。 |
| Join | 完整 | 联接转换 | 基于单字段或多字段键，或按位置，生成联接、仅左侧和仅右侧三个数据流。 |
| Join Multiple | 完整 | 多重联接转换 | 联接多个输入数据流。 |
| Key/Value Pairs | 完整 | [Text: NLP AI](/zh-cn/reference/workflow-steps/text-documents/nlp-ai/)（keyvalue 任务） | 通过基于 LLM 的 NLP AI 步骤从文本列中提取键/值对，可选候选键以及模糊或精确匹配。 |
| Line To Polygon | 完整 | Line To Polygon 执行器操作 | 将每条线闭合为多边形环，并追加为 `Polygon` 列。 |
| List Box | 完整 | 受控工作流变量 | 将应用的列表选择转换为受控输入。 |
| 位置优化器 | 部分 | [位置优化器](/zh-cn/reference/workflow-steps/optimization/location-optimizer/) | 将线性距离最小化的情形（选择 K 个站点，使到需求点的总距离或加权距离最小）转换为原生的 p-median MIP 步骤。引力核评分、定制评分宏或任何其他候选搜索目标仍会被拒绝，参见[迁移 Alteryx 工作流](/zh-cn/guides/workflows/migrate-alteryx-workflows/#转换后工作流中的宏)。 |
| Macro calls | 完整 | 宏调用 | 导入已知的宏源，并将宏调用映射为 PlaidCloud 宏步骤。 |
| Macro Input / Macro Output | 完整 | 宏输入 / 输出端口 | 直接映射为 PlaidCloud 宏端口。 |
| 生成网格 | 完整 | [Spatial Make Grid 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-make-grid/) | 将一个范围划分为方形单元，每个单元一行。 |
| Map | 完整 | 地图制品 | 创建 PlaidCloud 地图制品。 |
| Map Input | 完整 | [空间文件导入](/zh-cn/reference/workflow-steps/spatial/spatial-file-import/) | 读取 MapInfo、ESRI、KML 和 GeoJSON 文件及其附属文件。 |
| Master Selector | 部分 | 受控工作流变量和条件步骤可见性 | 将该工具针对界面元素的显示/隐藏可见性条件转换为条件步骤可见性。以尽力而为的方式转换所选内容运行哪个子工作流；针对实际租户应用的验证仍在进行中，因此在生产环境依赖之前，请先审核所选的运行目标。 |
| Message | 完整 | 步骤条件（消息） | 根据条件发出工作流警告、消息或错误。 |
| Modeling | 完整 | [ML：训练模型](/zh-cn/reference/workflow-steps/machine-learning/ml-train/) | 与管道的模型选择一起合并到 ML Train 步骤中。 |
| Multi-Field Formula | 完整 | 多字段公式转换 | 将公式应用于所选的多个字段。 |
| Multi-Row Formula | 完整 | 窗口 / 行感知公式转换 | 将相对行的逻辑转换为窗口行为，按分组依据分区。 |
| Named Entity Recognition (NER) | 完整 | [Text: NLP AI](/zh-cn/reference/workflow-steps/text-documents/nlp-ai/)（ner 任务） | 通过基于 LLM 的 NLP AI 步骤从文本列中提取实体（人员、组织、地点、日期、数量，或自定义类型列表）。 |
| Numeric Up Down | 完整 | 受控数值变量 | 将应用的数值输入转换为带类型的变量。 |
| Output Data | 完整 | 文档 / 表输出 | 将输出写入文档或 PlaidCloud 表，包括 Parquet 和 Avro 文件；`.yxdb`、`.hyper` 和 `.dbf` 输出会写为 Parquet。 |
| Overlay | 完整 | [空间处理](/zh-cn/reference/workflow-steps/spatial/spatial-process/) | 对两个几何列求交集、并集或切割。 |
| PDF Input | 完整 | PDF 提取执行器 | 从 PDF 中提取文本或表。 |
| Point To Line | 完整 | Point To Line 执行器操作 | 将每组的点串联为每组一条 `SequenceLine`，按序列字段排序。 |
| Poly-Build | 完整 | [Spatial Poly-Build 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-poly-build/) | 为每组点构建多边形或凸包。 |
| Poly-Split | 完整 | [Spatial Poly-Split 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-poly-split/) | 每个顶点、组成多边形或孔洞一行。 |
| Portfolio Composer (Text / Table / Image / Layout / Render) | 完整 | 报表制品 | 将报表内容、布局和渲染转换为 PlaidCloud 报表输出。 |
| POS Tagger | 完整 | [Text: NLP AI](/zh-cn/reference/workflow-steps/text-documents/nlp-ai/)（pos 任务） | 通过基于 LLM 的 NLP AI 步骤标注文本列中每个词元的词性。 |
| Predict | 完整 | [ML：评分](/zh-cn/reference/workflow-steps/machine-learning/ml-score/) | 使用已训练的模型表对数据评分，并追加预测列。 |
| Radio Button | 完整 | 受控工作流变量 | 将应用的单选选择转换为受控输入。 |
| Random % Sample | 完整 | Table Extract（随机） | 返回所请求的确切记录数或百分比。 |
| Record ID | 完整 | 行标识符转换 | 按配置的类型和起始值添加确定性的记录标识符，每组重新开始。 |
| Redistribute | 完整 | Redistribute 执行器操作 | 按重叠面积将某个度量从一组地理区域重新分配到另一组，并追加为 `Redistributed` 列。 |
| RegEx | 完整 | 正则表达式转换 | 解析、匹配或替换文本。 |
| Regression | 完整 | [ML：训练模型](/zh-cn/reference/workflow-steps/machine-learning/ml-train/) | 将 Assisted Modeling 链合并为一个 ML Train 步骤。 |
| Report Map | 完整 | 地图报表制品 | 生成云原生的地图/报表制品。 |
| Run Command | 部分 | 针对 REST 连接的 [REST 请求](/zh-cn/reference/workflow-steps/general/rest-request/)步骤（仅限 `curl`/`wget`） | 将 `curl` 或 `wget` 命令行转换为 REST 请求步骤。解释器和脚本命令（`cscript`、PowerShell、Python 等）、Excel-COM 自动化、文件系统操作，以及不透明或会启动工作流的命令，会按名称标记待人工审核，而不会自动转换。 |
| Sample | 完整 | 抽样转换 | 按数量、百分比或分组保留记录。 |
| Select | 完整 | 选择和架构投影步骤 | 选择、重命名、重新排序和重新设置字段类型。 |
| Smooth | 完整 | [Spatial Smooth 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-smooth/) | 经过若干轮次平滑每个几何图形。 |
| Sort | 完整 | 排序转换 | 按配置的字段和方向对记录排序。 |
| Spatial Info | 完整 | [Spatial Info 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-info/) | 以大地测量方式给出面积、长度、质心和边界矩形。 |
| 空间匹配 | 完整 | [空间匹配](/zh-cn/reference/workflow-steps/spatial/spatial-match/) / [Spatial Match (Intersect / Unmatched) 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-match-executor/) | 转换所有关系，包括 Within、Contains、Intersects、Touches、Crosses、Overlaps 和 Centroid-In，在数据库或工作流引擎中匹配。 |
| 空间处理 | 完整 | [空间处理](/zh-cn/reference/workflow-steps/spatial/spatial-process/) | 对几何列求交集、并集或切割。 |
| Summarize | 完整 | 聚合转换 | 分组并聚合：求和、计数、平均值、最小值、最大值、中位数、众数、标准差、方差和去重计数。 |
| Tab | 完整 | 应用选项卡分组 | 保留为转换后的应用结构。 |
| Test | 完整 | 步骤条件 | 将测试断言转换为步骤条件。 |
| Text Box | 完整 | 受控文本变量 | 将应用的文本输入转换为带类型的变量。 |
| Text Input | 完整 | 内联表输入 | 为工作流创建内联数据。 |
| Text Pre-processing | 完整 | NLP 预处理执行器 | 对文本进行规范化和预处理。 |
| Text Summary | 完整 | [Text: NLP AI](/zh-cn/reference/workflow-steps/text-documents/nlp-ai/)（summary 任务） | 通过基于 LLM 的 NLP AI 步骤，将文本列摘要为配置的最大句数。 |
| Text To Columns | 完整 | 拆分列转换 | 将文本拆分为字段或行。 |
| Tile | 完整 | 分块 / 分组转换 | 按配置的规则分配分块组。 |
| Tool Container | 完整 | 画布容器 / 执行组 | 保留为工作流组织结构。 |
| Topic Modeling | 完整 | 主题建模执行器 | 通过托管 NLP 运行主题建模。 |
| Transformation | 完整 | 转换步骤 | 将转换逻辑转换为 PlaidCloud 表达式或 SQL。 |
| Transpose | 完整 | 逆透视转换 | 将列转换为行，形成名称/值对。 |
| Tree | 完整 | 受控工作流变量 | 将应用的树选择转换为受控输入。 |
| Union | 完整 | 合并转换 | 按名称、位置或配置的规则合并数据流。 |
| Unique | 完整 | 唯一 / 重复拆分转换 | 将首次出现的唯一记录与重复记录分开。 |
| Visual Layout | 完整 | 画布布局元数据 | 保留为设计上下文。 |
| Word Cloud | 完整 | 文本可视化制品 | 根据文本分析创建可视化制品。 |
| XML 解析 | 完整 | XML 解析转换 | 将 XML 字段提取到工作流数据中。 |
| Zero-shot Text Classification | 完整 | [Text: NLP AI](/zh-cn/reference/workflow-steps/text-documents/nlp-ai/)（zeroshot 任务） | 通过基于 LLM 的 NLP AI 步骤，针对每行的候选标签列表对文本列分类，支持单标签或多标签。 |
| 查找最近点 | 完整 | [Spatial Find Nearest 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-find-nearest/) | 按距离排序的最近邻联接，包括直线距离，以及通过 PlaidCloud 自托管路由引擎实现的驾车时间最近（按路网上的分钟数排序）。驾车时间功能按工作区启用。 |
| 商圈 | 完整 | [Spatial Trade Area 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-trade-area/) | 以真实世界单位确定大小的同心缓冲区，包括固定半径商圈，以及通过自托管路由引擎实现的驾车时间商圈（路网上的分钟数）。驾车时间功能按工作区启用。 |
| Image Template | 完整 | Image Template 执行器操作 | 手动模式会将图像裁剪为您在模板上绘制的每个区域。自动模式使用开放标准的版面模型为您检测页面区域，并为每个区域输出一行，每行带有其检测到的边界和置信度供审核；模型无法可靠识别的页面会按名称标记，而不会被裁剪。开放标准的检测结果可能与 Alteryx 自己的不同，请审核检测到的区域，或使用手动模式以获得精确控制。 |
| Image Recognition | 完整 | 图像识别执行器 | 在工作流中训练图像分类器，并就地对新图像评分，无需外部账户，数据也不会离开 PlaidCloud。分类器是重新训练的，而不是从 Alteryx 复制的，因此结果是忠实的近似而非逐位一致，且训练在 CPU 上运行。按工作区启用。 |
| Geocoder | 完整 | 自托管地理编码器 | 针对 PlaidCloud 自有的地理编码器，将地址地理编码为坐标，并将坐标反向地理编码为地址，无需外部账户，数据也不会离开 PlaidCloud。按工作区启用。 |

界面控件（下拉列表、列表框、复选框、文本/数值/日期输入、文件和文件夹选择器）、画布对象（注释、链接、容器）以及宏端口，都会转换为原生的受控变量或画布对象。Alteryx 应用的完整界面布局，即 `.yxwz` 文件的 `<Questions>` 定义，也会被具体化为已发布的 Panel 应用“App Runner”前端，因此转换应用会生成一个可用的输入表单，它收集相同的值并驱动转换后的工作流，而不仅仅是单个受控变量。参见上方的 Analytic App interface 行和[使用转换后的 Alteryx 应用](/zh-cn/guides/workflows/use-converted-alteryx-apps/#app-runner-前端)。

**关于 Excel 输出的说明。** 普通的新工作簿（以默认格式写入数据）可完整转换。写入*带样式的模板*（填充命名的工作表和区域并保留其格式）则支持单个工作表，以及将多个输出组装到同一工作簿的不同工作表中（[Export to Excel Sheets 步骤](/zh-cn/reference/workflow-steps/export/export-to-excel-sheets/)会一次性填充所有工作表）。包含数据透视表或图表的模板在写入其工作表时会丢弃这些对象；由 Run Command 驱动的工作表级文件操作（Excel COM/VBS）会按名称标记待人工审核，而不会自动转换。

## 空间工具覆盖范围

Alteryx **Spatial** 工具面板中的每个工具都有对应的 PlaidCloud 路径，而且每条路径都是您也可以手动构建的步骤，转换只是一种便利，而非唯一途径。完整参考请参阅[地理空间步骤](/zh-cn/reference/workflow-steps/spatial/)，它们如何配合使用请参阅[地理空间分析](/zh-cn/guides/workflows/geospatial-analytics/)。

| Alteryx 空间工具 | PlaidCloud 路径 | 运行位置 |
| --- | --- | --- |
| Buffer | [Spatial Buffer 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-buffer/) | 工作流引擎 |
| Centroid | Centroid 执行器操作 | 工作流引擎 |
| Convex Hull | Convex Hull 执行器操作 | 工作流引擎 |
| Create Points | [Table Extract 表达式](/zh-cn/reference/workflow-steps/spatial/spatial-sql-recipes/) | 数据库 |
| Distance | [Table Extract 表达式](/zh-cn/reference/workflow-steps/spatial/spatial-sql-recipes/) | 数据库 |
| 查找最近点 | [Spatial Find Nearest 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-find-nearest/) | 数据库；驾车时间使用路由服务 |
| Generalize | [Spatial Generalize 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-generalize/) | 工作流引擎 |
| Heat Map | [Heat Map (macro)](/zh-cn/reference/workflow-steps/macros/macro-heat-map/) | 工作流引擎 |
| Line To Polygon | Line To Polygon 执行器操作 | 工作流引擎 |
| 生成网格 | [Spatial Make Grid 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-make-grid/) | 工作流引擎 |
| Point To Line | Point To Line 执行器操作 | 工作流引擎 |
| Poly-Build | [Spatial Poly-Build 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-poly-build/) | 工作流引擎 |
| Poly-Split | [Spatial Poly-Split 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-poly-split/) | 工作流引擎 |
| Redistribute | Redistribute 执行器操作 | 工作流引擎 |
| Smooth | [Spatial Smooth 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-smooth/) | 工作流引擎 |
| Spatial Info | [Spatial Info 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-info/) | 工作流引擎 |
| 空间匹配 | [空间匹配](/zh-cn/reference/workflow-steps/spatial/spatial-match/) | 数据库 |
| 空间匹配：交集对象、Unmatched | [Spatial Match (Intersect / Unmatched) 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-match-executor/) | 工作流引擎 |
| 空间处理 | [空间处理](/zh-cn/reference/workflow-steps/spatial/spatial-process/) | 工作流引擎 |
| 商圈（固定半径 + 驾车时间） | [Spatial Trade Area 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-trade-area/) | 工作流引擎；驾车时间使用路由服务 |
| Pie Wedge Trade Area | [Pie Wedge Trade Area (macro)](/zh-cn/reference/workflow-steps/macros/macro-pie-wedge-trade-area/) | 工作流引擎 |
| 空间文件输入 | [空间文件导入](/zh-cn/reference/workflow-steps/spatial/spatial-file-import/) | 工作流引擎 |
| Summarize：SpatialObjCombine、SpatialObjConvexHull | [空间合并](/zh-cn/reference/workflow-steps/spatial/spatial-combine/) | 工作流引擎 |
| Report Map | [Report Map 步骤](/zh-cn/reference/workflow-steps/reports/report-map/) | 工作流引擎 |

**驾车时间商圈和最近点：** 商圈的驾车时间环和查找最近点的驾车时间排序运行在 PlaidCloud 自托管的路由引擎上（路网等时线和行程时间矩阵），而不是托管的第三方 API，因此起点坐标不会离开平台。驾车时间功能按工作区启用。路由和驾车时间区域使用 OpenStreetMap 数据，© OpenStreetMap contributors，依据[开放数据库许可证（ODbL）](https://www.openstreetmap.org/copyright)提供。

### 已知的空间前提条件

空间工具本身可以转换；以下是对输入的前提条件。

- **`.geo` GeoFile 格式。** Alteryx 专有的二进制 GeoFile 没有开放的读取器，因此导入此类文件时会失败关闭，而不是在运行时崩溃。请在 Alteryx 中将该图层重新导出为标准空间格式（shapefile 或 GeoJSON），然后导入该文件；其他空间格式不受影响。参见[迁移空间 Alteryx 工作流](/zh-cn/guides/workflows/migrate-spatial-alteryx-workflows/#打包空间输入)。
- **Peano key 的 Spatial Info 度量。** Peano key 是 Alteryx 专有的空间索引，没有公开规范，因此请求它的 Spatial Info 会跳过该列，并在说明中指出。其他所有 Spatial Info 度量，包括面积、长度、质心、边界矩形、对象类型、部分和点的数量以及端点，均可转换。
- **投影坐标的 Create Points。** Create Points 可直接转换浮点型和整数型（×1,000,000）经纬度坐标。已处于投影坐标系的坐标需要先在上游重新投影为 WGS84 经纬度，因为工作流不会记录它们使用的是哪种投影。

## Calgary 工具覆盖范围

Alteryx 的 Calgary 数据库（`.cydb`）是 PlaidCloud 无法打开的专有索引存储。转换时会把每个 Calgary 数据库视为一张普通 PlaidCloud 表，命名为 `calgary_<database name>`，因此围绕它构建的工具会作为普通表操作进行转换，而不是直接拒绝。有关替身表的工作方式，参见 [Calgary 数据库](/zh-cn/guides/workflows/migrate-alteryx-workflows/#calgary-数据库)；有关索引匹配工具，参见 [Calgary Join 和 Cross Count Append](/zh-cn/guides/workflows/migrate-alteryx-workflows/#calgary-join-和-cross-count-append)。

| Alteryx Calgary 工具 | PlaidCloud 路径 | 转换内容 |
| --- | --- | --- |
| Calgary Loader | 写入 `calgary_<database>` 的 Table Extract | 是，前提是已为数据库命名且其至少存储一个数据字段。 |
| Calgary Input | 读取 `calgary_<database>` 的动态文档输入，并以保存的查询作为筛选器 | 是，包括由 Or 构建或包裹在 Not 中的查询，以及 contains 或 starts-with 筛选器（重建为 SQL LIKE）。对空间查找查询，以及 Skip Records/Max Records 限制，会拒绝转换。 |
| Calgary Input (Count Only) / Calgary Cross Count | 针对 `calgary_<database>` 的聚合转换 | 是，包括由 Or 构建或包裹在 Not 中的分桶。对跨多个自定义字段的交叉，以及未指定统计列的仅计数读取，会拒绝转换。 |
| Calgary Join | 动态文档输入，将其输入的每条记录与 `calgary_<database>` 匹配 | 当传入字段是与值索引匹配的普通值时，包括 Count Only 模式（统计每条输入记录匹配到的数据库记录数，未匹配到任何记录的记录计为零）。当字段为空间类型（请重建为 Spatial Match）或其类型未解析时，以及对范围索引或接有未匹配输出的 Join、未指定匹配字段的 Join、输入未连接任何内容的 Join，会拒绝转换。 |
| Calgary Cross Count Append | 动态文档输入，匹配每条记录，然后对 `calgary_<database>` 进行计数联接 | 当传入字段是与值索引匹配的普通值时：它会按每条输入记录统计匹配到的数据库记录数，未匹配到任何记录的记录计为零。对空间或未解析的索引（请重建为 Spatial Match）、自定义值交叉计数网格、范围索引，以及未指定字段的匹配，会拒绝转换。 |

### 已知的 Calgary 前提条件

其中大多数是对输入的前提条件，而非转换限制。

- **空间索引匹配需要重建为 Spatial Match。** 针对空间索引匹配的 Calgary Join 或 Cross Count Append 会拒绝转换，并指出替身表名称：工作流记录了索引的名称，但没有记录它保存的是普通值还是空间几何，而值匹配（等值联接）和空间匹配（点在多边形内）是不同的操作。请将数据库导出为表，并将匹配重建为 Join（值索引）或 Spatial Match（空间索引）。
- **受 Skip Records 或 Max Records 限制的读取需要明确的排序。** 导出的替身表不带记录顺序，因此如果需要按位置取前 N 条或后 N 条记录，请在导出时添加排序列。
- **必须先加载人口统计或参考数据库。** 在数据库加载之前执行 Calgary 读取会停止，并指出需要构建的表。`.cydb` 文件本身没有开放的读取器，因此请在 Alteryx 中重新导出它（使用 Calgary Input 连接到写出 CSV 或 Parquet 的 Output Data 工具），然后将其作为指定名称的表导入，参见[无法读取的 .cydb（Calgary）数据库](/zh-cn/guides/workflows/troubleshoot-alteryx-imports/#无法读取的-cydb-calgary-数据库)。Alteryx 随附的授权人口统计和参考 `.cydb` 文件（Experian、Census 等）通常属于这种情况：没有任何转换器可以重现这些第三方数据，因此请自带获得授权的参考数据，并将其加载到指定名称的表中，与 Geocoder 的参考数据相同。
- **不存储任何数据字段的 Calgary Loader 无法转换**，因为它所写入的表将没有列。
- **自定义值交叉计数网格暂不支持转换。** 单个普通交叉计数字段可以转换，它会按每条输入记录统计匹配的数据库记录数；但*命名*自定义值的网格会为每个值追加一个计数列，而 Alteryx 既没有说明会有多少列，也没有说明它们如何命名。已列入未来版本计划，待获得参考导出以逆向推导列约定。

值、范围、contains 和 starts-with 查询都会转换为筛选器；只有空间查找查询（一种在列级别没有对应项的索引操作）不会。

## 连接到外部系统

Alteryx 的连接器端点（Salesforce、HTTP、Google Analytics、Cassandra、电子邮件、Hadoop 和 Spark，两个方向均包括）不会转换，因为 PlaidCloud 通过连接而不是画布上的工具来访问这些系统。每一个都会按名称拒绝转换，并说明该工作应放在何处：

| Alteryx 工具 | 在 PlaidCloud 中的去向 |
| --- | --- |
| Salesforce Input / Output | **Salesforce** 连接 |
| Anaplan | **Anaplan** 连接 |
| HTTP Input | 针对 **REST** 连接的 **REST 请求**步骤 |
| Google Analytics Input | 使用 Google Analytics tap 的**导入：Singer 源** |
| Cassandra Input | 使用 Cassandra tap 的**导入：Singer 源** |
| Email Input | 使用 GMail tap 的**导入：Singer 源** |
| Hadoop Input / Output | 通过 Hive、Impala 或 Presto 连接的**导入：SQL** / **导出：SQL** |
| Spark Input / Output | 通过 Databricks 连接的**导入：SQL** / **导出：SQL** |

其中四个完全没有写入路径。PlaidCloud 读取 Google Analytics 和 Cassandra，但从不向它们写入，因此 Google Analytics Output 或 Cassandra Output 工具会改为向受支持目标的**导出：SQL**。电子邮件同样不是数据目标：**通知：电子邮件**会向人员发送通知，因此 Email Output 工具会变为一个导出步骤加一个单独的通知。**Anaplan** 连接同样是只读的：它可读取已保存的视图、运行预先存在的导出操作，或将列表加载到 PlaidCloud 维度中，但没有任何 PlaidCloud 步骤可以写回 Anaplan。

## 验证转换后的工作流

对于生产工作流，请将转换后的输出与可信的 Alteryx 输出进行验证。PlaidCloud 的验证侧重于架构、行数和行值，除非工作流依赖行顺序，否则不考虑行顺序。专门的操作（空间、模糊匹配、OCR、NLP、报表）通过托管作业执行器运行，使工作流保持云原生；机器学习管道会转换为原生的 [ML：训练模型](/zh-cn/reference/workflow-steps/machine-learning/ml-train/)和 [ML：评分](/zh-cn/reference/workflow-steps/machine-learning/ml-score/)步骤。端到端的导入和验证指南请参阅[迁移 Alteryx 工作流](/zh-cn/guides/workflows/migrate-alteryx-workflows/)。
