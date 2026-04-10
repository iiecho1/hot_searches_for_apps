import requests
import time
import os
import shutil
from urllib.parse import quote

MAX_RETRIES = 3
RETRY_DELAY = 3  # 秒
REQUEST_TIMEOUT = 30  # 秒

def get_api_data(url, retries=MAX_RETRIES):
    """从 API 获取数据，带重试"""
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=REQUEST_TIMEOUT)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"请求 API 失败 (第 {attempt}/{retries} 次): {e}")
            if attempt < retries:
                time.sleep(RETRY_DELAY * attempt)
    return None

def read_markdown(file_path):
    """读取 Markdown 文件内容"""
    if not os.path.exists(file_path):
        return ""
    with open(file_path, mode='r', encoding='utf-8') as file:
        return file.read()

def write_markdown(file_path, content):
    """写入 Markdown 文件内容"""
    with open(file_path, mode='a', encoding='utf-8') as file:
        file.write(content)

def ensure_directory_exists(path):
    """确保目录存在，如果不存在则创建"""
    os.makedirs(path, exist_ok=True)

def extract_existing_titles(existing_content):
    """从已有内容中提取所有标题，用于精确去重"""
    titles = set()
    for line in existing_content.split('\n'):
        if line.startswith('+ ['):
            # 提取 [+ [title](url)] 中的 title
            end = line.find('](')
            if end > 3:
                titles.add(line[3:end])
    return titles

def process_api_data(api_data, base_path):
    """处理 API 数据并保存到 Markdown 文件"""
    if not api_data or 'obj' not in api_data:
        print("API 数据无效或缺失 'obj' 字段")
        return

    current_date = time.strftime("%Y-%m-%d", time.localtime())
    year, month, day = current_date.split("-")

    for key, items in api_data['obj'].items():
        if not items:
            print(f"键 '{key}' 的数据为空，跳过处理")
            continue

        titles = [item.get("title") for item in items if item.get("title")]
        hrefs = [item.get("url") for item in items if item.get("url")]

        if not titles or not hrefs:
            print(f"键 '{key}' 的数据缺失标题或链接，跳过处理")
            continue

        if len(titles) != len(hrefs):
            print(f"键 '{key}' 的标题({len(titles)})和链接({len(hrefs)})数量不一致，取较短的")

        # 创建目录
        archive_path = os.path.join(base_path, 'archives', key, year, month)
        ensure_directory_exists(archive_path)

        # 文件路径
        markdown_file = os.path.join(archive_path, f'{current_date}.md')
        root_file = os.path.join(base_path, 'archives', key, f'{key}.md')

        # 读取现有内容并提取已有标题（精确去重）
        existing_content = read_markdown(markdown_file)
        existing_titles = extract_existing_titles(existing_content)

        # 写入新内容
        if not existing_content:
            write_markdown(markdown_file, f"## {key} \n### {current_date}\n\n")

        new_content = ""
        for title, href in zip(titles, hrefs):
            print("title", title, "href:", href)
            if title in existing_titles:
                continue
            existing_titles.add(title)  # 防止同批次内重复
            encoded_href = quote(href, safe=":/=?&@#%")
            new_content += f"+ [{title}]({encoded_href})\n\n"

        if new_content:
            write_markdown(markdown_file, new_content)
            print(f"数据已成功保存到 {markdown_file}")

        # 复制文件到根目录
        shutil.copyfile(markdown_file, root_file)
        print(f"文件已复制到 {root_file}")

if __name__ == "__main__":
    # 从环境变量获取 API URL
    api_url = os.getenv("API_URL")
    if not api_url:
        print("未设置 API_URL 环境变量")
        exit(1)

    # 获取 API 数据
    api_data = get_api_data(api_url)
    if not api_data:
        print("无法获取 API 数据")
        exit(1)

    # 处理 API 数据
    base_path = os.path.dirname(os.path.abspath(__file__))
    process_api_data(api_data, base_path)
