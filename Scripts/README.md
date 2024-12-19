# Scripts 目录

此目录包含用于自定义 Input 字体的核心脚本。

## 脚本来源说明

本目录中的 `inputCustomize.py` 脚本改编自 [Input 字体官方网站](https://input.djr.com/download/) 提供的压缩包中的原始脚本。我们对原始脚本进行了以下改进：

1. 将代码从 Python 2 升级到 Python 3
2. 增加了多个预设字体样式的配置
3. 优化了代码结构和注释
4. 添加了更详细的使用示例和文档

## 文件说明

### inputCustomize.py

这是主要的字体自定义脚本，用于修改 Input 字体的各种特性。

#### 功能概述

- 修改字体行高
- 自定义字符样式
- 创建字体族
- 添加字体名称后缀

#### 依赖文件

脚本依赖以下模板文件（用于字体族功能）：
- `_template_Regular.txt`
- `_template_Italic.txt`
- `_template_Bold.txt`
- `_template_BoldItalic.txt`

这些模板文件包含了创建字体族所需的基本配置。

#### 字符修改对照表

脚本支持修改以下字符的样式：

1. **字母 'a'**
   - 默认：双层 'a'
   - 可选：单层 'a' (`--a=ss`)

2. **字母 'g'**
   - 默认：双层 'g'
   - 可选：单层 'g' (`--g=ss`)

3. **字母 'i'**
   - 默认：无衬线
   - 可选样式：
     - 衬线 (`--i=serifs`)
     - 圆形衬线 (`--i=serifs_round`)
     - 顶部衬线 (`--i=topserif`)

4. **字母 'l'**
   - 默认：无衬线
   - 可选样式：
     - 衬线 (`--l=serifs`)
     - 圆形衬线 (`--l=serifs_round`)
     - 顶部衬线 (`--l=topserif`)

5. **数字 '0'**
   - 默认：点零
   - 可选样式：
     - 斜线零 (`--zero=slash`)
     - 无点零 (`--zero=nodot`)

6. **星号 '*'**
   - 默认：上标位置
   - 可选：中高度位置 (`--asterisk=height`)

7. **大括号 '{}'**
   - 默认：曲线型
   - 可选：直线型 (`--braces=straight`)

#### 使用示例

1. 修改单个字符：
```bash
python inputCustomize.py Input-Regular.ttf --a=ss
```

2. 组合多个修改：
```bash
python inputCustomize.py Input-Regular.ttf --a=ss --g=ss --i=serifs --zero=slash
```

3. 调整行高并添加后缀：
```bash
python inputCustomize.py Input-Regular.ttf --lineHeight=1.2 --suffix=Custom
```

4. 创建完整字体族：
```bash
python inputCustomize.py \
    Input-Regular.ttf \
    Input-Italic.ttf \
    Input-Bold.ttf \
    Input-BoldItalic.ttf \
    --fourStyleFamily
```

#### 技术细节

脚本通过以下方式修改字体：

1. **行高调整**
   - 修改 OS/2 表和 hhea 表中的度量值
   - 使用倍数方式计算新的行高

2. **字符替换**
   - 使用字体中预定义的替代字形
   - 通过修改 cmap 表实现字符映射

3. **字体族创建**
   - 使用模板文件定义字体族属性
   - 修改 name 表和 OS/2 表
   - 确保字重值正确设置

#### 注意事项

1. 本修改会直接影响原始字体文件，建议：
   - 在修改前备份原始文件
   - 使用 `--dest` 参数指定输出目录

2. 模板文件必须与脚本位于同一目录

3. 字体族功能要求：
   - 必须提供四个字体文件
   - 文件顺序必须正确（Regular -> Italic -> Bold -> BoldItalic）

#### 预设样式生成命令

以下是生成各种预设样式的具体命令示例。每个命令都基于 Input 字体的默认特性进行定制化修改。

1. **Andale Mono 风格**
```bash
python inputCustomize.py Input-Regular.ttf --i=topserif --l=serifs --braces=straight
```

2. **Anonymous Pro 风格**
```bash
python inputCustomize.py Input-Regular.ttf --g=ss --i=serif --l=serif --zero=slash --asterisk=height --braces=straight
```

3. **Consolas 风格**
```bash
python inputCustomize.py Input-Regular.ttf --i=serif --l=serif --zero=slash --braces=straight
```

4. **Deja Vu / Menlo 风格**
```bash
python inputCustomize.py Input-Regular.ttf --g=ss --i=serif --l=serifs_round --zero=slash --asterisk=height --braces=straight
```

5. **Envy Code R 风格**
```bash
python inputCustomize.py Input-Regular.ttf --g=ss --i=topserif --l=topserif --zero=slash
```

6. **Fira Mono 风格**
```bash
python inputCustomize.py Input-Regular.ttf --i=serif --l=serifs_round --braces=straight
```

7. **Liberation Mono 风格**
```bash
python inputCustomize.py Input-Regular.ttf --g=ss --i=serif --l=serif --braces=straight
```

8. **Monaco 风格**
```bash
python inputCustomize.py Input-Regular.ttf --a=ss --g=ss --i=serifs --l=serifs --zero=slash
```

9. **Pragmata Pro 风格**
```bash
python inputCustomize.py Input-Regular.ttf --i=serif --l=serif --asterisk=height --braces=straight
```

10. **Source Code Pro 风格**
```bash
python inputCustomize.py Input-Regular.ttf --i=topserif --l=serifs_round --asterisk=height --braces=straight
```

注意事项：
1. 以上命令假设您已将字体文件放在脚本同目录下
2. 可以添加 `--dest=/path/to/output` 参数指定输出目录
3. 可以添加 `--suffix=Custom` 参数为生成的字体添加后缀
4. 可以添加 `--lineHeight=1.2` 参数调整行高

要创建完整的字体族（包含常规、斜体、粗体和粗斜体），请使用以下格式：

```bash
python inputCustomize.py \
    Input-Regular.ttf \
    Input-Italic.ttf \
    Input-Bold.ttf \
    Input-BoldItalic.ttf \
    --fourStyleFamily \
    [上述任意风格参数]
```

例如，创建 Consolas 风格的完整字体族：

```bash
python inputCustomize.py \
    Input-Regular.ttf \
    Input-Italic.ttf \
    Input-Bold.ttf \
    Input-BoldItalic.ttf \
    --fourStyleFamily \
    --i=serif \
    --l=serif \
    --zero=slash \
    --braces=straight \
    --suffix=Consolas
```