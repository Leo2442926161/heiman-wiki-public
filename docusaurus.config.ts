import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: '海曼科技 Wiki',
  tagline: '用匠心守护安全，让科技温暖生活',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://heiman-wiki.github.io',
  baseUrl: '/heiman-wiki-public/',

  organizationName: 'heiman-wiki',
  projectName: 'heiman-wiki',

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'zh-Hans',
    locales: ['zh-Hans'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          onInlineTags: 'warn',
          onInlineAuthors: 'warn',
          onUntruncatedBlogPosts: 'warn',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    image: 'img/heiman-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: '海曼科技',
      logo: {
        alt: '海曼科技 Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: '文档中心',
        },
        {to: '/blog', label: '博客', position: 'left'},
        {
          href: 'https://www.heiman.com.cn',
          label: '官网',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: '文档',
          items: [
            {
              label: '企业介绍',
              to: '/docs/intro',
            },
            {
              label: '产品中心',
              to: '/docs/tutorial-basics/create-a-page',
            },
          ],
        },
        {
          title: '产品与方案',
          items: [
            {
              label: '智慧消防',
              href: 'https://www.heiman.com.cn/product/?type=list&classid=3',
            },
            {
              label: '智慧燃气',
              href: 'https://www.heiman.com.cn/product/?type=list&classid=4',
            },
            {
              label: '智慧养老',
              href: 'https://www.heiman.com.cn/product/?type=list&classid=34',
            },
          ],
        },
        {
          title: '更多',
          items: [
            {
              label: '博客',
              to: '/blog',
            },
            {
              label: '联系我们',
              href: 'https://www.heiman.com.cn/contactus/',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} 深圳市海曼科技股份有限公司`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
