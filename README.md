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
| 搜索/门户 | [百度](./blob/main/archives/baidu/baidu.md)、搜狗、360搜索、搜狐、夸克 |
| 社交/社区 | 微博、知乎、V2EX、虎扑、豆瓣、AcFun |
| 新闻资讯 | 今日头条、澎湃新闻、新京报、网易新闻、腾讯新闻、人民网、南方周末、CCTV新闻 |
| 科技 | CSDN、GitHub、IT之家 |
| 视频/娱乐 | 哔哩哔哩、抖音、梨视频 |
| 其他 | 少数派、懂球帝、国家地理、历史上的今天、360doc |

## 更新日志

- **2026-03-22**: 优化脚本：请求超时+重试、精确去重、URL编码统一
- **2025-01-10**: 重写 API，支持 30 个平台
- **2024-10-18**: 切换到自建 API
- **2023-12-16**: 教书先生 API 恢复
- **2023-12-15**: 开始自建 API → [api-for-hot-search-golang](https://github.com/iiecho1/api-for-hot-search-golang)
- **2023-10-22**: 按天归档，去重，改为每小时执行
- **2023-08-16**: 项目启动
