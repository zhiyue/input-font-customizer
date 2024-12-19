# Input Font 自定义工具

这是一个用于自定义 Input 字体的 Python 工具。通过这个工具，你可以自定义 Input 字体的多个特性，包括行高、字符样式等。

## 关于脚本来源

本工具中的 `inputCustomize.py` 脚本改编自 [Input 字体官方网站](https://input.djr.com/download/) 提供的压缩包中的原始脚本。原始脚本仅支持 Python 2，我们对其进行了以下改进：

1. 升级支持 Python 3
2. 增加了多个预设字体样式的配置
3. 优化了代码结构和注释
4. 添加了更多使用示例

## 前置要求

- Python 3.x
- fonttools 库（TTX）

## 安装

1. 克隆此仓库：
```bash
git clone [repository-url]
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 使用方法

基本用法：
```bash
python Scripts/inputCustomize.py [INPUT] [--dest=OUTPUT] [OPTIONS]
```

- 如果不指定 INPUT，工具会处理当前目录下的所有字体文件
- 如果不指定 OUTPUT，工具会覆盖原始文件

### 可用选项

#### 基础选项
- `--help`, `-h`: 显示帮助信息
- `--dest=<路径>`: 指定输出目录
- `--lineHeight=<数值>`: 设置字体行高的倍数
- `--suffix=<字符串>`: 为字体名称添加后缀（不能包含空格）
- `--preset=<style>`: 使用预定义的字体样式，可用值：
  - `andale`: Andale Mono 风格
  - `anonymous`: Anonymous Pro 风格
  - `consolas`: Consolas 风格
  - `dejavu`: Deja Vu / Menlo 风格
  - `envy`: Envy Code R 风格
  - `fira`: Fira Mono 风格
  - `liberation`: Liberation Mono 风格
  - `monaco`: Monaco 风格
  - `pragmata`: Pragmata Pro 风格
  - `sourcecode`: Source Code Pro 风格

#### 字符样式选项
- `--a=ss`: 将默认的双层 'a' 替换为单层 'a'
- `--g=ss`: 将默认的双层 'g' 替换为单层 'g'
- `--i=serif`: 修改 'i' 的样式，可选值：
  - `serifs`: 衬线样式
  - `serifs_round`: 圆形衬线样式
  - `topserif`: 顶部衬线样式
- `--l=serif`: 修改 'l' 的样式，可选值：
  - `serifs`: 衬线样式
  - `serifs_round`: 圆形衬线样式
  - `topserif`: 顶部衬线样式
- `--zero=slash`: 修改数字 '0' 的样式：
  - `slash`: 使用斜线零
  - `nodot`: 使用无点零
- `--asterisk=height`: 将上标星号替换为中高度星号
- `--braces=straight`: 使用直线型大括号替换默认的曲线型大括号

#### 字体族选项
- `--fourStyleFamily`: 将四个输入的字体文件组织为一个字体族（需要按顺序提供四个字体文件）

### 使用示例

1. 基本样式修改：
```bash
python Scripts/inputCustomize.py Input-Regular.ttf --lineHeight=1.5 --a=ss --g=ss --zero=slash
```

2. 使用预设样式：
```bash
python Scripts/inputCustomize.py Input-Regular.ttf --preset=consolas --suffix=Custom
```

3. 使用预设样式创建完整字体族：
```bash
python Scripts/inputCustomize.py \
    Input-Regular.ttf \
    Input-Italic.ttf \
    Input-Bold.ttf \
    Input-BoldItalic.ttf \
    --preset=monaco \
    --suffix=Monaco \
    --fourStyleFamily
```

4. 预设样式基础上添加自定义修改：
```bash
python Scripts/inputCustomize.py Input-Regular.ttf \
    --preset=consolas \
    --lineHeight=1.2 \
    --a=ss \
    --suffix=Custom
```

5. 处理当前目录下所有字体：
```bash
cd /path/to/fonts
python /path/to/inputCustomize.py --preset=fira --suffix=Custom
```

## 注意事项

1. 此工具专门设计用于 Input 字体系列，不适用于其他字体
2. 使用 `--fourStyleFamily` 选项时，需要按照以下顺序提供字体文件：
   - Regular（常规）
   - Italic（斜体）
   - Bold（粗体）
   - Bold Italic（粗斜体）
3. 建议在修改字体前备份原始文件
4. 如果使用 `--dest` 参数，请确保目标目录已存在

## 预设样式生成命令

以下是生成各种预设样式的具体命令示例。每个命令都基于 Input 字体的默认特性进行定制化修改。

### 1. Andale Mono 风格
```bash
python Scripts/inputCustomize.py Input-Regular.ttf --preset=andale
```

### 2. Anonymous Pro 风格
```bash
python Scripts/inputCustomize.py Input-Regular.ttf --preset=anonymous
```

### 3. Consolas 风格
```bash
python Scripts/inputCustomize.py Input-Regular.ttf --preset=consolas
```

### 4. Deja Vu / Menlo 风格
```bash
python Scripts/inputCustomize.py Input-Regular.ttf --preset=dejavu
```

### 5. Envy Code R 风格
```bash
python Scripts/inputCustomize.py Input-Regular.ttf --preset=envy
```

### 6. Fira Mono 风格
```bash
python Scripts/inputCustomize.py Input-Regular.ttf --preset=fira
```

### 7. Liberation Mono 风格
```bash
python Scripts/inputCustomize.py Input-Regular.ttf --preset=liberation
```

### 8. Monaco 风格
```bash
python Scripts/inputCustomize.py Input-Regular.ttf --preset=monaco
```

### 9. Pragmata Pro 风格
```bash
python Scripts/inputCustomize.py Input-Regular.ttf --preset=pragmata
```

### 10. Source Code Pro 风格
```bash
python Scripts/inputCustomize.py Input-Regular.ttf --preset=sourcecode
```

### 预设样式参数对照表

以下是每个预设样式包含的具体参数配置，供参考：

1. **Andale Mono** (`--preset=andale`)
   - `--i=topserif`
   - `--l=serifs`
   - `--braces=straight`

2. **Anonymous Pro** (`--preset=anonymous`)
   - `--g=ss`
   - `--i=serif`
   - `--l=serif`
   - `--zero=slash`
   - `--asterisk=height`
   - `--braces=straight`

3. **Consolas** (`--preset=consolas`)
   - `--i=serif`
   - `--l=serif`
   - `--zero=slash`
   - `--braces=straight`

4. **Deja Vu / Menlo** (`--preset=dejavu`)
   - `--g=ss`
   - `--i=serif`
   - `--l=serifs_round`
   - `--zero=slash`
   - `--asterisk=height`
   - `--braces=straight`

5. **Envy Code R** (`--preset=envy`)
   - `--g=ss`
   - `--i=topserif`
   - `--l=topserif`
   - `--zero=slash`

6. **Fira Mono** (`--preset=fira`)
   - `--i=serif`
   - `--l=serifs_round`
   - `--braces=straight`

7. **Liberation Mono** (`--preset=liberation`)
   - `--g=ss`
   - `--i=serif`
   - `--l=serif`
   - `--braces=straight`

8. **Monaco** (`--preset=monaco`)
   - `--a=ss`
   - `--g=ss`
   - `--i=serifs`
   - `--l=serifs`
   - `--zero=slash`

9. **Pragmata Pro** (`--preset=pragmata`)
   - `--i=serif`
   - `--l=serif`
   - `--asterisk=height`
   - `--braces=straight`

10. **Source Code Pro** (`--preset=sourcecode`)
    - `--i=topserif`
    - `--l=serifs_round`
    - `--asterisk=height`
    - `--braces=straight`

### 创建预设样式的完整字体族

要创建完整的字体族（包含常规、斜体、粗体和粗斜体），请使用以下格式：

```bash
python Scripts/inputCustomize.py \
    Input-Regular.ttf \
    Input-Italic.ttf \
    Input-Bold.ttf \
    Input-BoldItalic.ttf \
    --preset=<style> \
    --fourStyleFamily \
    [其他可选参数]
```

例如，创建 Consolas 风格的完整字体族：

```bash
python Scripts/inputCustomize.py \
    Input-Regular.ttf \
    Input-Italic.ttf \
    Input-Bold.ttf \
    Input-BoldItalic.ttf \
    --preset=consolas \
    --fourStyleFamily \
    --suffix=Consolas
```