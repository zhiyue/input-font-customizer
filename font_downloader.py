import os
import requests
from tqdm import tqdm
import json

class InputFontDownloader:
    def __init__(self):
        self.download_dir = "downloads"
        self.base_url = "https://input.djr.com/build/"
        self._create_download_directory()
        # 定义预设样式及其对应的参数
        self.style_presets = {
            "Input defaults": {
                "preset": "default",
                "data-list": "0,0,0,0,0,0,0",  # 从HTML的data-list属性获取
                "a": "0", "g": "0", "i": "0", "l": "0",
                "zero": "0", "asterisk": "0", "braces": "0"
            },
            "Andale Mono style": {
                "preset": "andale",
                "data-list": "0,0,1,2,0,0,1",
                "a": "0", "g": "0", "i": "1", "l": "2",
                "zero": "0", "asterisk": "0", "braces": "1"
            },
            "Anonymous Pro style": {
                "preset": "anonymous",
                "data-list": "0,1,3,3,1,1,1",
                "a": "0", "g": "1", "i": "3", "l": "3",
                "zero": "1", "asterisk": "1", "braces": "1"
            },
            "Consolas style": {
                "preset": "consolas",
                "data-list": "0,0,3,3,1,0,1",
                "a": "0", "g": "0", "i": "3", "l": "3",
                "zero": "1", "asterisk": "0", "braces": "1"
            },
            "Deja Vu / Menlo style": {
                "preset": "dejavu",
                "data-list": "0,1,3,4,1,1,1",
                "a": "0", "g": "1", "i": "3", "l": "4",
                "zero": "1", "asterisk": "1", "braces": "1"
            },
            "Envy Code R style": {
                "preset": "envy",
                "data-list": "0,1,1,1,1,0,0",
                "a": "0", "g": "1", "i": "1", "l": "1",
                "zero": "1", "asterisk": "0", "braces": "0"
            },
            "Fira Mono style": {
                "preset": "fira",
                "data-list": "0,0,3,4,0,0,1",
                "a": "0", "g": "0", "i": "3", "l": "4",
                "zero": "0", "asterisk": "0", "braces": "1"
            },
            "Liberation Mono style": {
                "preset": "liberation",
                "data-list": "0,1,3,3,0,0,1",
                "a": "0", "g": "1", "i": "3", "l": "3",
                "zero": "0", "asterisk": "0", "braces": "1"
            },
            "Monaco style": {
                "preset": "monaco",
                "data-list": "1,1,2,2,1,0,0",
                "a": "1", "g": "1", "i": "2", "l": "2",
                "zero": "1", "asterisk": "0", "braces": "0"
            },
            "Pragmata Pro style": {
                "preset": "pragmata",
                "data-list": "0,0,3,3,0,1,1",
                "a": "0", "g": "0", "i": "3", "l": "3",
                "zero": "0", "asterisk": "1", "braces": "1"
            },
            "Source Code Pro style": {
                "preset": "sourcecode",
                "data-list": "0,0,1,4,0,1,1",
                "a": "0", "g": "0", "i": "1", "l": "4",
                "zero": "0", "asterisk": "1", "braces": "1"
            }
        }

    def _create_download_directory(self):
        """创建下载目录"""
        if not os.path.exists(self.download_dir):
            os.makedirs(self.download_dir)

    def _generate_filename(self, style_name, style_params):
        """
        生成文件名
        :param style_name: 样���名称
        :param style_params: 样式参数
        :return: 格式化的文件名
        """
        # 使用预设名称作为主要标识
        preset_name = style_params["preset"].lower()

        # 直接返回简化的文件名格式
        return f"Input-{preset_name}.zip"

    def _generate_download_url(self, style_params):
        """
        生成完整的下载URL及其参数
        :param style_params: 样式参数
        :return: 完整的URL字符串
        """
        # 参数值映射
        param_mappings = {
            "a": {"0": "0", "1": "ss"},  # ss01
            "g": {"0": "0", "1": "ss"},  # ss02
            "i": {
                "0": "0",
                "1": "topserif",  # ss03
                "2": "serifs",    # ss05
                "3": "serif",     # ss07
                "4": "serifs_round"  # ss09
            },
            "l": {
                "0": "0",
                "1": "topserif",  # ss04
                "2": "serifs",    # ss06
                "3": "serif",     # ss08
                "4": "serifs_round"  # ss10
            },
            "zero": {
                "0": "0",
                "1": "slash",
                "2": "nodot"  # ss13
            },
            "asterisk": {
                "0": "0",
                "1": "height"  # ss11
            },
            "braces": {
                "0": "0",
                "1": "straight"  # ss12
            }
        }

        # 转换参数值
        converted_params = {}
        for param, value in style_params.items():
            if param in param_mappings:
                converted_params[param] = param_mappings[param].get(value, "0")

        # 构建请求参数
        params = {
            "fontSelection": "whole",    # 下载完整字体包
            "line-height": "1.2",        # 行高
            "accept": "I do",            # 接受许可
            "email": "",                 # 可选的邮箱地址
            "preset": style_params["preset"],
            "a": converted_params.get("a", "0"),
            "g": converted_params.get("g", "0"),
            "i": converted_params.get("i", "0"),
            "l": converted_params.get("l", "0"),
            "zero": converted_params.get("zero", "0"),
            "asterisk": converted_params.get("asterisk", "0"),
            "braces": converted_params.get("braces", "0")
        }

        # 构建URL
        url = self.base_url
        query_string = "&".join([f"{k}={v}" for k, v in params.items()])
        full_url = f"{url}?{query_string}"
        return full_url

    def download_input_font(self, style_name):
        """
        下载Input字体
        :param style_name: 字体样式名称
        """
        try:
            # 获取预设样式的参数
            style_params = self.style_presets[style_name]

            # 生成并显示下载URL
            download_url = self._generate_download_url(style_params)
            print(f"\n下载URL: {download_url}")

            print(f"\n正在请求下载 {style_name}...")

            # 发送下载请求
            response = requests.get(
                download_url,
                stream=True,
                headers={
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
                }
            )
            response.raise_for_status()

            # 生成描述性文件名
            filename = self._generate_filename(style_name, style_params)
            save_path = os.path.join(self.download_dir, filename)

            # 获取文件大小
            total_size = int(response.headers.get('content-length', 0))

            # 下载文件并显示进度条
            with open(save_path, 'wb') as file, \
                 tqdm(
                    desc=filename,
                    total=total_size,
                    unit='iB',
                    unit_scale=True,
                    unit_divisor=1024,
                ) as progress_bar:
                    for data in response.iter_content(chunk_size=1024):
                        size = file.write(data)
                        progress_bar.update(size)

            print(f"✓ {style_name} 已成功下载到: {save_path}")
            return True

        except requests.exceptions.RequestException as e:
            print(f"× {style_name} 下载失败: {str(e)}")
            return False

    def download_all_styles(self):
        """下载所有可用的字体样式"""
        print(f"准备下载 {len(self.style_presets)} 种字体样式...")

        success_count = 0
        failed_styles = []

        for style in self.style_presets.keys():
            if self.download_input_font(style):
                success_count += 1
            else:
                failed_styles.append(style)

        print("\n下载总结:")
        print(f"成功: {success_count}/{len(self.style_presets)}")
        if failed_styles:
            print("失败的样式:")
            for style in failed_styles:
                print(f"- {style}")

def main():
    downloader = InputFontDownloader()

    print("开始下载所有Input字体样式...")
    downloader.download_all_styles()

if __name__ == "__main__":
    main()