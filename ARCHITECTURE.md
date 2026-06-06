# 文档架构约定

## 目录结构

```
docs/
├── intro.md                         # 海曼简介（页面）
├── about.md                         # 关于我们（页面）
├── 生态平台/                         # 每平台一个子目录
│   ├── _category_.json
│   ├── home assistant/
│   │   ├── index.md                 # 集成指南
│   │   ├── 自动化示例.md
│   │   ├── 使用技巧.md
│   │   └── 仪表盘.md (仅HA)
│   ├── Zigbee2mqtt/
│   │   ├── index.md
│   │   ├── 自动化示例.md
│   │   └── 使用技巧.md
│   └── ...
├── 无线协议/
│   ├── _category_.json
│   ├── Matter/
│   │   ├── index.md                 # 协议概述
│   │   ├── 支持型号列表.md
│   │   ├── 技术参数.md
│   │   ├── HS1SA-M 智能烟雾报警器（Matter）/   # 每型号一个子目录
│   │   │   ├── index.md             # 型号详情
│   │   │   └── 版本历史.md
│   │   └── ...
│   ├── Zigbee/
│   │   ├── index.md
│   │   ├── 支持型号列表.md
│   │   ├── 技术参数.md
│   │   ├── HS1SA-E/
│   │   └── ...
│   └── ...
└── 产品类型/
    ├── _category_.json
    ├── 烟雾传感器/
    │   ├── index.md                 # 产品概述
    │   ├── 型号对比.md
    │   ├── 安装指南.md
    │   └── 版本历史.md
    └── ...
```

## 关键规则

1. **无线协议**下每个型号是一个 **子目录**（而非 .md 文件），内含 `index.md` + `版本历史.md`
2. **产品类型**引用协议型号时，链接到 `../../无线协议/Zigbee/{型号名}/index.md`
3. **生态平台**引用协议时，链接到 `../../无线协议/Zigbee/index.md`
4. 每个类别目录下有 `_category_.json` 控制排序
5. 所有层级使用 `sidebar_position` 控制 sidebar 顺序
6. 未发布文章使用 frontmatter `draft: true` 隐藏

## 版本历史

- 无线协议型号的版本历史放在该型号子目录下的 `版本历史.md`
- 产品类型的版本历史放在产品类型目录下的 `版本历史.md`（已删除，暂不保留）
- 格式：`## vX.Y.Z（YYYY-MM-DD）` + 变更列表

## 国际化

- 源文件在 `docs/`（中文）
- 英文翻译在 `i18n/en/docusaurus-plugin-content-docs/current/`
- 其他语言空目录，自动 fallback 到中文
- 目录结构必须完全镜像 docs/
