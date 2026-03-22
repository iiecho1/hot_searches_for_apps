# 热搜归档

[![auto_get_hot](https://github.com/iiecho1/hot_searches_for_apps/actions/workflows/auto.yaml/badge.svg)](https://github.com/iiecho1/hot_searches_for_apps/actions/workflows/auto.yaml)

定时获取 30 个平台的热搜数据，按天归档为 Markdown 文件。从 2023 年 8 月 16 日开始运行。

## 数据来源

热搜接口由 [api-for-hot-search-golang](https://github.com/iiecho1/api-for-hot-search-golang) 提供，每小时自动拉取一次。

## 文件结构

```
archives/
  微博/
    微博.md          ← 最新一天的热搜（快捷查看）
    2026/
      03/
        2026-03-22.md  ← 每日归档
```

每条热搜格式：`+ [标题](链接)`

## 支持平台（30个）

| 分类 | 平台 |
|:--|:--|
| 搜索/门户 | [百度](./archives/百度/百度.md)、[搜狗](./archives/搜狗/搜狗.md)、[360搜索](./archives/360搜索/360搜索.md)、[搜狐](./archives/搜狐/搜狐.md)、[夸克](./archives/夸克/夸克.md) |
| 社交/社区 | [微博](./archives/微博/微博.md)、[知乎](./archives/知乎/知乎.md)、[V2EX](./archives/V2EX/V2EX.md)、[虎扑](./archives/虎扑/虎扑.md)、[豆瓣](./archives/豆瓣/豆瓣.md)、[AcFun](./archives/AcFun/AcFun.md) |
| 新闻资讯 | [今日头条](./archives/今日头条/今日头条.md)、[澎湃新闻](./archives/澎湃新闻/澎湃新闻.md)、[新京报](./archives/新京报/新京报.md)、[网易新闻](./archives/网易新闻/网易新闻.md)、[腾讯新闻](./archives/腾讯新闻/腾讯新闻.md)、[人民网](./archives/人民网/人民网.md)、[南方周末](./archives/南方周末/南方周末.md)、[CCTV新闻](./archives/CCTV新闻/CCTV新闻.md) |
| 科技 | [CSDN](./archives/CSDN/CSDN.md)、[GitHub](./archives/GitHub/GitHub.md)、[IT之家](./archives/IT之家/IT之家.md) |
| 视频/娱乐 | [哔哩哔哩](./archives/哔哩哔哩/哔哩哔哩.md)、[抖音](./archives/抖音/抖音.md)、[梨视频](./archives/梨视频/梨视频.md) |
| 其他 | [少数派](./archives/少数派/少数派.md)、[懂球帝](./archives/懂球帝/懂球帝.md)、[国家地理](./archives/国家地理/国家地理.md)、[历史上的今天](./archives/历史上的今天/历史上的今天.md)、[360doc](./archives/360doc/360doc.md) |

## 更新日志

- **2026-03-22**: 优化脚本：请求超时+重试、精确去重、URL编码统一
- **2025-01-10**: 重写 API，支持 30 个平台
- **2024-10-18**: 切换到自建 API
- **2023-12-16**: 教书先生 API 恢复
- **2023-12-15**: 开始自建 API → [api-for-hot-search-golang](https://github.com/iiecho1/api-for-hot-search-golang)
- **2023-10-22**: 按天归档，去重，改为每小时执行
- **2023-08-16**: 项目启动
