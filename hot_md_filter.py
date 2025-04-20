import requests
import time
import os
import shutil
from urllib.parse import quote

def get_api_data(url):
    """从 API 获取数据"""
    try:
        response = requests.get(url)
        response.raise_for_status()  # 检查 HTTP 状态码
        return response.json()  # 返回 JSON 数据
    except requests.exceptions.RequestException as e:
        print(f"请求 API 时发生错误: {e}")
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

def process_api_data(api_data, base_path):
    """处理 API 数据并保存到 Markdown 文件"""
    if not api_data or 'obj' not in api_data:
        print("API 数据无效或缺失 'obj' 字段")
        return

    current_date = time.strftime("%Y-%m-%d", time.localtime())
    year, month, day = current_date.split("-")

    for key, items in api_data['obj'].items():
        if not items:  # 如果 items 为 None 或空列表，跳过
            print(f"键 '{key}' 的数据为空，跳过处理")
            continue

        # 提取标题和链接
        titles = [item.get("title") for item in items if item.get("title")]
        hrefs = [item.get("url") for item in items if item.get("url")]

        if not titles or not hrefs:
            print(f"键 '{key}' 的数据缺失标题或链接，跳过处理")
            continue

        # 创建目录
        archive_path = os.path.join(base_path, 'archives', key, year, month)
        ensure_directory_exists(archive_path)

        # 文件路径
        markdown_file = os.path.join(archive_path, f'{current_date}.md')
        root_file = os.path.join(base_path, 'archives', key, f'{key}.md')

        # 读取现有内容
        existing_content = read_markdown(markdown_file)

        # 写入新内容
        if not existing_content:
            write_markdown(markdown_file, f"## {key} \n### {current_date}\n\n")

        new_content = ""
        for title, href in zip(titles, hrefs):
            print("title",title, "href:",href)
            if title not in existing_content:
                # 对 href 进行 URL 编码，避免 Markdown 将%20重新渲染为空格。（主要针对微博）
                encoded_href = quote(href, safe=":/=?")
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
