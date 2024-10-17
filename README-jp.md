# Arcaea-beautify

## 説明

- Arcaeaの美化を自動化するスクリプトです。変更したい画像や音声ファイルを`Modifications/`フォルダに置くと、スクリプトが自動的に解凍し、`assets`内のリソースを`Modifications/`内のものに置き換え、再パッケージ化と署名を行います。
- このスクリプトはAndroidユーザー専用です。
- 利用可能なモードは2つあります：
  - 1つ目は個人使用向けです。
  - 2つ目はゲームプレイを録画する必要があるプレイヤー向けです。2つ目のモードを実行すると、ゲームプレイや結果画面のアセットは変更されません。

<img src="https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/demo.png"/>

## 免責事項

- パッケージの変更はLowiroの権利と利用規約に関わる場合があります。
- このプロジェクトは個人のリバースエンジニアリング研究および学習のみを目的としており、著者はこのプロジェクトに起因するいかなる結果についても責任を負いません。
- このプロジェクトの内容を商業的または違法な目的で使用しないでください。このプロジェクトを使用することで、あなたは自分の行動に対して全責任を負うことになります。

## 要件

- オペレーティングシステム：`Ubuntu 20.04`（Windowsユーザーは`WSL`を使用できます）
- シェル：`bash`と`fish`
- 依存関係：`python3`、`apktool`、`zipalign`、`default-jdk`、`default-jre`、`apksigner`

## 使用方法

1. このリポジトリをダウンロードします。
2. 変更したいArcaeaのAPKを用意し、このリポジトリの下に置きます。最新バージョンであることを確認してください。例えば、`Arcaea-5.10.apk`:

    ![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/ls.png)

3. `please_run_this_script_before_running_modify.py.sh`の権限を変更し、自動的に必要なツールをインストールします。
    ```bash
    chmod +x please_run_this_script_before_running_modify.py.sh
    ./please_run_this_script_before_running_modify.py.sh
    ```
    ![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/please_run_this_script_before_running_modify.py.png)

4. `modify.py`を実行してAPKの変更を開始します。
    ```bash
    python3 modify.py Arcaea-5.10.apk Modifications/
    ```
    ![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/run_modify.png)
    ゲームプレイを録画する必要があり、ゲームプレイや結果画面を変更したくない場合は、パラメータ`public`を追加します：
    ```bash
    python3 modify.py Arcaea-5.10.apk Modifications/ public
    ```
    ![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/run_modify_public.png)

5. 実行中に、`keytool`が署名情報の入力を求めてきます：

    - `Enter keystore password:` `123456`を入力してください
    - `Re-enter new password:` `123456`をもう一度入力してください
    - 個人情報の入力をスキップするには`Enter`を押します
    - `Is CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown correct?`には`yes`と入力してください
       
    ![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/apksigner.png)

6. 完了です。

## 警告

1. `Modification/`フォルダに置かれたリソースファイルのファイル名とフォルダパスは、`assets/`内の変更したいアセットに対応している必要があります。
2. `assets/songs`内の素材は変更しないでください。Arcaeaはそのフォルダに対してハッシュ関数による保護を使用しています。変更するとゲームが起動しなくなる可能性があります。
3. ゲームプレイ中の背景、トラックカラー、ノートスタイル、またはヒットエフェクトの変更は不正行為と見なされます。このスクリプトはこれらのアセットを保護し、変更を許可しません。

## クレジット

- `Modifications/startup/1080/bg.jpg`: https://twitter.com/Refish10086/status/1740695545755427027
- 一部の効果音：Phigrosおよび旧バージョンのArcaeaから
- `Modifications/img/1080/_*.png`: Rotaenoの一部のアートワークおよびCG
- `Modifications/img/1080/bg_select_light.jpg`: Juvenile (by technoplanet) のアートワーク
- `Modifications/img/1080/bg_select_dark.jpg`: Juvenile (by technoplanet) のアートワーク
- `Modifications/img/scenery/scenery_bg_default.png`: Juvenile (by technoplanet) のアートワーク
- `Modifications/img/bg_colorless.jpg`: ArcaeaのCG
- `Modifications/img/bg_byd_light.jpg`: ArcaeaのCG
- `Modifications/img/bg_byd_dark.jpg`: ArcaeaのCG
