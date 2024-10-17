# Arcaea-beautify

## 专案描述

- 自动化美化 Arcaea 的脚本。把你要修改的图档、音效放在 `Modification/` 资料夹中，脚本会自动解包并将 `assets` 内的图档、音效替换成 `Modification/` 内的资源并重新打包、签名。
- 此脚本只供安卓用户使用。
- 此脚本有两种模式可执行，第一种是针对个人使用，第二种是针对有录手元需求的玩家。执行第二种模式的话将不会动到游戏进行画面以及结算画面的任何素材。

<img src="https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/demo.png"/>


## 免责声明

- 改包相关内容涉及 Lowiro 的利益与服务条款。
- 本专案仅用于个人逆向工程技术研究与学习，作者不承担此专案所带来的一切附属责任。
- 请勿将此专案内容用于商业或非法用途，使用此专案代表您将为自己的全部行为负责。

## 系统需求

- 作业系统：`Ubuntu 20.04`（`Windows` 使用者可以使用 `WSL`）
- Shell：`bash` 以及 `fish`
- Dependencies：`python3`、`apktool`、`zipalign`、`default-jdk`、`default-jre`、`apksigner`

## 使用方法

1. 下载这个 Repository
2. 准备好一份你要修改的 Arcaea APK，放在这个 Repository 底下，注意必须是最新版本。以 `Arcaea-5.10.apk` 为例：

 ![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/ls.png)

3. 修改 `please_run_this_script_before_running_modify.py.sh` 的权限并执行，自动装好所有需要的工具。
 ```bash
 chmod +x please_run_this_script_before_running_modify.py.sh
 ./please_run_this_script_before_running_modify.py.sh
 ```
 ![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/please_run_this_script_before_running_modify.py.png)

4. 执行 `modify.py`，开始修改 `apk`。
 ```bash
 python3 modify.py Arcaea-5.10.apk Modifications/
 ```
 ![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/run_modify.png)
 如果你有录手元需求，不希望动到游戏进行画面以及结算画面，请加一个参数 `public`：
 ```bash
 python3 modify.py Arcaea-5.10.apk Modifications/ public
 ```
 ![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/run_modify_public.png)

5. 执行过程中，`keytool` 会要你输入签名资讯：

 - `Enter keystore password:` 请输入 `123456`
 - `Re-enter new password:` 请再输入一次 `123456`
 - 个人资讯全部直接按 `Enter` 跳过不输入
 - `Is CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown correct?` 请输入 `yes`

 ![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/apksigner.png)

6. 完成。


## 警告

1. 放入 `Modification/` 资料夹的素材档案名称、资料夹路径必须与 `assets/` 内欲替换之素材对应。
2. 请不要修改 `assets/songs` 内的任何素材，Arcaea 对于该资料夹有使用杂凑函数保护，修改的话你将无法启动游戏。
3. 修改游戏进行时的背景、轨道颜色、音符样式、打击特效属于作弊行为，此脚本针对这些素材有保护，无法修改这些素材。

## 素材来源

- `Modifications/startup/1080/bg.jpg`：https://twitter.com/Refish10086/status/1740695545755427027
- 一些音效：来自 Phigros，以及旧版 Arcaea
- `Modifications/img/1080/_*.png`：Rotaeno 部分曲绘、cg
- `Modifications/img/1080/bg_select_light.jpg`：Juvenile (by technoplanet) 曲绘
- `Modifications/img/1080/bg_select_dark.jpg`：Juvenile (by technoplanet) 曲绘
- `Modifications/img/scenery/scenery_bg_default.png`：Juvenile (by technoplanet) 曲绘
- `Modifications/img/bg_colorless.jpg`：Arcaea cg
- `Modifications/img/bg_byd_light.jpg`：Arcaea cg
- `Modifications/img/bg_byd_dark.jpg`：Arcaea cg
