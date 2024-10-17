# Arcaea-beautify

## Description

自動化美化 Arcaea 的腳本。把你要修改的圖檔、音效放在 `Modification/` 資料夾中，腳本會自動解包並將 `assets` 內的圖檔、音效替換成 `Modification/` 內的資源並重新打包、簽名。

此腳本只供安卓用戶使用。

此腳本有兩種模式可執行，第一種是針對個人使用，第二種是針對有錄手元需求的玩家。執行第二種模式的話將不會動到遊戲進行畫面以及結算畫面的任何素材。

<img src="https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/demo.png"/>


## Disclaimer

- 改包相關內容涉及 Lowiro 的利益與服務條款。
- 本專案僅用於個人逆向工程技術研究與學習，作者不承擔此專案所帶來的一切附屬責任。
- 請勿將此專案內容用於商業或非法用途，使用此專案代表您將為自己的全部行為負責。

## Requirements

- 作業系統：`Ubuntu 20.04`（`Windows` 使用者可以使用 `WSL`）
- Shell：`bash` 以及 `fish`
- Dependencies：`python3`、`apktool`、`zipalign`、`default-jdk`、`default-jre`、`apksigner`

## Usage

1. 下載這個 Repository
2. 準備好一份你要修改的 Arcaea APK，放在這個 Repository 底下，注意必須是最新版本。以 `Arcaea-5.10.apk` 為例：

	![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/ls.png)

3. 修改 `please_run_this_script_before_running_modify.py.sh` 的權限並執行，自動裝好所有需要的工具。
	```bash
	chmod +x please_run_this_script_before_running_modify.py.sh
	./please_run_this_script_before_running_modify.py.sh
	```
 	![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/please_run_this_script_before_running_modify.py.png)

4. 執行 `modify.py`，開始修改 `apk`。
	```bash
	python3 modify.py Arcaea-5.10.apk Modifications/
	```
 	![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/run_modify.png)
	如果你有錄手元需求，不希望動到遊戲進行畫面以及結算畫面，請加一個參數 `public`：
	```bash
	python3 modify.py Arcaea-5.10.apk Modifications/ public
	```
	![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/run_modify_public.png)

5. 執行過程中，`apksigner` 會要你輸入簽名資訊：

    - `Enter keystore password:` 請輸入 `123456`
    - `Re-enter new password:` 請再輸入一次 `123456`
    - 個人資訊全部直接按 `Enter` 跳過不輸入
    - `Is CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown correct?` 請輸入 `yes`
   	
	![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/apksigner.png)

6. 完成。


## Warning

1. 放入 `Modification/` 資料夾的素材檔案名稱、資料夾路徑必須與 `assets/` 內欲替換之素材對應。
2. 請不要修改 `assets/songs` 內的任何素材，Arcaea 對於該資料夾有使用雜湊函數保護，修改的話你將無法啟動遊戲。
3. 修改遊戲進行時的背景、軌道顏色、音符樣式、打擊特效屬於作弊行為，此腳本針對這些素材有保護，無法修改這些素材。

## Credits

- `Modifications/startup/1080/bg.jpg`：https://twitter.com/Refish10086/status/1740695545755427027
- 一些音效：來自 Phigros，以及舊版 Arcaea
- `Modifications/img/1080/_*.png`：Rotaeno 部分曲繪、cg
- `Modifications/img/1080/bg_select_light.jpg`：Juvenile (by technoplanet) 曲繪
- `Modifications/img/1080/bg_select_dark.jpg`：Juvenile (by technoplanet) 曲繪
- `Modifications/img/scenery/scenery_bg_default.png`：Juvenile (by technoplanet) 曲繪
- `Modifications/img/bg_colorless.jpg`：Arcaea cg
- `Modifications/img/bg_byd_light.jpg`：Arcaea cg
- `Modifications/img/bg_byd_dark.jpg`：Arcaea cg

