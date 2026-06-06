# 海曼科技 Wiki

海曼科技官方知识库，基于 [Docusaurus](https://docusaurus.io/) 构建的现代化多语言静态站点。

## 支持的语言

| 语言 | 代码 |
|------|------|
| 中文 | `zh-Hans` (默认) |
| English | `en` |
| Français | `fr` |
| Deutsch | `de` |
| Español | `es` |
| Italiano | `it` |
| Português | `pt` |
| Русский | `ru` |
| Nederlands | `nl` |
| Polski | `pl` |
| Svenska | `sv` |
| Türkçe | `tr` |
| 日本語 | `ja` |
| 한국어 | `ko` |

## 安装

```bash
npm install
```

## 本地开发

```bash
npm run start
```

启动本地开发服务器，默认访问 http://localhost:3000/heiman-wiki-public/

指定语言启动：

```bash
npm run start -- --locale en
```

## 构建

```bash
npm run build
```

构建所有语言版本的静态文件，输出到 `build` 目录。

仅构建特定语言：

```bash
npm run build -- --locale en
```

## 维护指南

### 文档内容

- 中文文档：直接编辑 `docs/` 和 `blog/` 目录下的文件
- 英文及其他语言翻译：编辑 `i18n/<locale>/docusaurus-plugin-content-docs/current/` 和 `i18n/<locale>/docusaurus-plugin-content-blog/` 下的对应文件
- 导航栏/页脚等 UI 文本翻译：编辑 `i18n/<locale>/code.json`
- `_category_.json` 中的 `label` 和 `description` 也需要同步翻译

## 部署

### GitHub Pages (自动)

推送至 `main` 分支后，GitHub Actions 会自动构建并部署到 GitHub Pages。

### 手动部署

```bash
npm run build
```

将 `build` 目录部署到任意静态托管服务。
