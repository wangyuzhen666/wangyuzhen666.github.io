---
layout: page
title: About
description: 打码改变世界
keywords: wangyuzhen, 王玉镇
comments: true
menu: 关于
permalink: /about/
---

### 我是 Yoken Wang😎。

2008年出生
🤔

## 联系
Email：  <wangyuzhen831201@163.com>
## BLOG:

<ul>
{% for website in site.data.social %}
<li>{{website.sitename }}：<a href="{{ website.url }}" target="_blank">@{{ website.name }}</a></li>
{% endfor %}
{% if site.url contains 'https://mazhuang.org' %}
<li>
我的CSDN博客<br />
<img style="height:192px;width:192px;border:1px solid lightgrey;" src="{{ site.url }}/assets/images/qrcode.jpg" alt="我的CSDN" />
</li>
{% endif %}
</ul>


## Skill Keywords

{% for skill in site.data.skills %}
### {{ skill.name }}
<div class="btn-inline">
{% for keyword in skill.keywords %}
<button class="btn btn-outline" type="button">{{ keyword }}</button>
{% endfor %}
</div>
{% endfor %}
