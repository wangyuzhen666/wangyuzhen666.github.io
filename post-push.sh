#!/bin/bash

# 获取最近更新的文章（比如获取最近更新的5篇文章）
recent_posts=$(git log -n 5 --pretty=format:%an | awk '/commit/{getline; print}')
domain="https://wangyuzhen666.github.io"  # 替换为你的博客域名
token="FbTpyDkXWgtBj02l"  # 替换为你的百度站长平台的 Token

for post in $recent_posts; do
    full_url="$domain${post}"
    # 使用 curl 发送 POST 请求推送文章更新给百度
    curl -H "Content-Type:text/plain" --data "$full_url" "http://data.zz.baidu.com/urls?site=$domain&token=$token"
done
