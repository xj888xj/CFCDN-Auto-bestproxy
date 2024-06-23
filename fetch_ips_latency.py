import requests
import re

# 配置多个网址
urls = [
    "https://cf.090227.xyz/",
    "https://stock.hostmonit.com/CloudFlareYes",
    "https://ip.164746.xyz/",
    "https://monitor.gacjie.cn/page/cloudflare/ipv4.html",
    "https://345673.xyz/#"
]

# 目标延迟阈值
DELAY_THRESHOLD_MS = 200

# 结果存储列表
result_ips = set()

# 正则表达式模式匹配
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

# 获取网页内容并筛选数据
for url in urls:
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            content = response.text
            matches = pattern.findall(content)
            for ip in matches:
                result_ips.add(f"{ip}#{url}")
    except Exception as e:
        print(f"Error fetching data from {url}: {e}")

# 将结果写入到txt文件中
with open("ips_latency.txt", "w") as file:
    for ip_line in result_ips:
        file.write(ip_line + "\n")

print("数据已写入 ips_latency.txt 文件")