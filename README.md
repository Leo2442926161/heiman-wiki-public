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

启动本地开发服务器（仅默认语言 `zh-Hans`），访问 http://localhost:3000/heiman-wiki-public/

> ⚠️ **注意**：开发模式下一次只能服务一个语言，其他语言的页面会显示 404。这是 Docusaurus 的正常行为。

### 指定语言启动

```bash
npm run start -- --locale en      # 英文
npm run start -- --locale fr      # 法语
npm run start -- --locale de      # 德语
npm run start -- --locale ja      # 日语
# 其他语言同理，locale 代码见上方表格
```

### 本地预览所有语言

构建后使用静态服务器，可访问所有语言：

```bash
npm run build
npm run serve
```

然后访问对应路径，例如：
- http://localhost:3000/heiman-wiki-public/ （中文）
- http://localhost:3000/heiman-wiki-public/en/ （英文）
- http://localhost:3000/heiman-wiki-public/fr/ （法语）
- http://localhost:3000/heiman-wiki-public/de/ （德语）

## 构建

```bash
npm run build
```

构建所有语言版本的静态文件，输出到 `build` 目录。

仅构建特定语言：

```bash
npm run build -- --locale en
```

## 贡献指南

我们欢迎社区贡献！以下是参与方式。

### 📝 贡献文档

#### 通过 GitHub Pull Request

1. Fork 本仓库
2. 修改或新增文档：
   - 中文文档在 `docs/` 和 `blog/` 目录
   - 其他语言在 `i18n/<locale>/` 对应目录
3. 提交 PR，描述你的改动
4. 等待审核合并

#### 通过 GitHub Issues

在 [Issues 页面](https://github.com/Leo2442926161/heiman-wiki-public/issues) 提交文档建议：

- 点击 **"Doc Suggestion"** 模板
- 填写建议内容和相关页面路径
- 提交后我们会评估并处理

### 🐛 报告错误

遇到问题请提交 GitHub Issue：

1. 前往 [Issues 页面](https://github.com/Leo2442926161/heiman-wiki-public/issues/new/choose)
2. 选择 **"Bug Report"** 模板
3. 填写：
   - 出错的页面路径
   - 期望的行为与实际行为
   - 截图（可选）
   - 浏览器和语言版本
4. 提交 Issue

### 💬 文章评论

本站基于 GitHub Discussions 提供评论功能。访问 [Discussions 页面](https://github.com/Leo2442926161/heiman-wiki-public/discussions) 参与讨论。

### 翻译改进

发现翻译不准确或需要改进？欢迎：

- 直接提交 PR 修改 `i18n/<locale>/` 下的文件
- 在 Issue 中选择"翻译改进"类型提交反馈

## 部署

### GitHub Pages (自动)

推送至 `main` 分支后，GitHub Actions 会自动构建并部署到 GitHub Pages。

### 手动部署

```bash
npm run build
```

将 `build` 目录部署到任意静态托管服务。
