---
layout: post
title: Windows 实用技巧汇总
categories: Windows
description: 平时使用 Windows 时总结的一些实用的小技巧。
keywords: Windows
---

**目录**

* TOC
{:toc}

### Win7 不按 Shift，右键显示 "在此处打开命令窗口 (W)"

<img src="/images/posts/windows/rclick.png" alt="Windows Skills" />

图上的这条右键命令一般在 Win7 下是需要 Shift + 右键在弹出菜单里才能看到的，怎么省掉这个 Shift，直接就能出来呢？

先说方法：

将如下代码保存为 .reg 文件然后执行即可。

```
Windows Registry Editor Version 5.00

[HKEY_CLASSES_ROOT\Directory\shell\cmd]
"Extended"=-

[HKEY_CLASSES_ROOT\Drive\shell\cmd]
"Extended"=-

[HKEY_CLASSES_ROOT\LibraryFolder\background\shell]
@="none"

[HKEY_CLASSES_ROOT\LibraryFolder\background\shell\cmd]
@="@shell32.dll,-8506"
"NoWorkingDirectory"=""
