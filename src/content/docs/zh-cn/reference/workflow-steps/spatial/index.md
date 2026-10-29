---
title: 地理空间步骤
description: PlaidCloud 的全部地理空间工作流步骤——导入空间文件、缓冲、匹配、测量和构建几何，完整覆盖 Alteryx 空间工具。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/spatial/index.md
---

读取、构建、转换和匹配几何的工作流步骤。它们与[几何表达式](/zh-cn/reference/workflow-steps/spatial/spatial-sql-recipes/)一起，
覆盖了 Alteryx 的整个空间工具集——逐个工具的对应关系请参阅
[Alteryx 转换矩阵](/zh-cn/reference/alteryx-conversion-matrix/)。

## 几何为 WKT

所有空间步骤都以 **WKT**（well-known text，已知文本）格式在普通文本列中读写几何。无需声明特殊的几何类型，步骤之间也无需转换：
[空间文件导入](/zh-cn/reference/workflow-steps/spatial/spatial-file-import/)生成的几何列，
可直接用于 [Spatial Buffer 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-buffer/)、
[空间匹配](/zh-cn/reference/workflow-steps/spatial/spatial-match/)或 SQL 表达式，顺序不限。

## 两种执行路径

每个步骤都通过能给出正确结果的最简单路径运行。

| 路径 | 在此运行的内容 | 原因 |
|---|---|---|
| **SQL**——在数据库中 | 查找最近点、匹配，以及[几何表达式](/zh-cn/reference/workflow-steps/spatial/spatial-sql-recipes/) | 谓词联接和列表达式随表规模扩展；没有行离开数据仓库 |
| **工作流引擎**——Shapely 和 GDAL | 所有对几何进行重塑的操作 | 缓冲、平滑和融合无法用数据库 SQL 表达 |

路径无需您选择；每种步骤类型只有一种路径。在评估作业规模时，这一区别很重要：
SQL 路径的步骤随数据仓库扩展，引擎路径的步骤随工作流 Pod 扩展。

## 加载和写入几何

- [空间文件导入](/zh-cn/reference/workflow-steps/spatial/spatial-file-import/)——读取 MapInfo `.TAB`、ESRI `.shp`、`.kml` 或 `.geojson` 文件及其附属文件
- [空间文件导出](/zh-cn/reference/workflow-steps/spatial/spatial-file-export/)——将 WKT 几何及其属性写入 shapefile、GeoJSON、GeoPackage、KML、GML 或 MapInfo 文件
- [Geometry in SQL 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-sql-recipes/)——根据经度/纬度列构建点

## 匹配和测量

- [Spatial Find Nearest 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-find-nearest/)——一个表中与另一个表的每一行最接近的 N 行，并给出距离
- [空间匹配](/zh-cn/reference/workflow-steps/spatial/spatial-match/)——配对几何相交、位于其内或包含的行
- [Spatial Match (Intersect / Unmatched) 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-match-executor/)——同样的匹配，但输出重叠几何或未匹配的行
- [Spatial Info 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-info/)——面积、长度、质心和外接矩形，按大地测量方式计算
- [空间重新投影](/zh-cn/reference/workflow-steps/spatial/spatial-reproject/)——将几何从一个坐标参考系转换到另一个

## 重塑几何

- [Spatial Buffer 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-buffer/)——将每个几何按固定距离向外扩展
- [Spatial Trade Area 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-trade-area/)——以真实世界单位确定大小的同心缓冲区
- [Spatial Generalize 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-generalize/)——按容差简化
- [Spatial Smooth 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-smooth/)——按指定遍数平滑
- [空间处理](/zh-cn/reference/workflow-steps/spatial/spatial-process/)——对两个几何列求相交、合并或裁剪

## 构建和拆分

- [Spatial Poly-Build 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-poly-build/)——为每组点构建多边形或凸包
- [Spatial Poly-Split 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-poly-split/)——每个顶点、组成多边形或孔洞各一行
- [空间合并](/zh-cn/reference/workflow-steps/spatial/spatial-combine/)——将每组的几何融合为一个
- [Spatial Centroid 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-centroid/)——添加每个几何的中心点
- [Spatial Point to Line 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-point-to-line/)——将每组的点连成一条线
- [Spatial Line to Polygon 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-line-to-polygon/)——将每条线闭合为多边形
- [Spatial Make Grid 步骤](/zh-cn/reference/workflow-steps/spatial/spatial-make-grid/)——将一个范围切分为方形单元

## 表达式参考

- [几何函数（Lakehouse v1）](/zh-cn/reference/expressions/lakehouse-v1/09-geometry-functions/)——`ST_*` 系列
- [地理函数（Lakehouse v1）](/zh-cn/reference/expressions/lakehouse-v1/09-geo-functions/)——H3 六边形索引和 geohash
- [空间函数（Lakehouse v2）](/zh-cn/reference/expressions/lakehouse-v2/17-spatial-functions/)

## 相关内容

- [地理空间分析](/zh-cn/guides/workflows/geospatial-analytics/)——从源文件到发布地图的完整示例路径
- [迁移空间 Alteryx 工作流](/zh-cn/guides/workflows/migrate-spatial-alteryx-workflows/)
- [Report Map 步骤](/zh-cn/reference/workflow-steps/reports/report-map/)——将几何渲染到报表中
- [打包宏步骤](/zh-cn/reference/workflow-steps/macros/)——Heat Map 和 Pie Wedge Trade Area
