# Arcaea-beautify

## Description

- A script to automate the beautification of Arcaea. Place the image and sound files you want to modify in the `Modifications/` folder, and the script will automatically unpack, replace the resources in `assets` with those in `Modifications/`, and repack and sign the files.
- This script is intended for Android users only.
- There are two modes available:
  - The first is for personal use.
  - The second is for players who need to record gameplay. If you run the second mode, it will not alter any assets in the gameplay or results screens.

<img src="https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/demo.png"/>

## Disclaimer

- Modifying packages may involve Lowiro's rights and terms of service.
- This project is for personal reverse engineering research and learning only; the author accepts no liability for any consequences arising from this project.
- Do not use this project's contents for commercial or illegal purposes; by using this project, you take full responsibility for your actions.

## Requirements

- Operating System: `Ubuntu 20.04` (Windows users can use `WSL`)
- Shell: `bash` and `fish`
- Dependencies: `python3`, `apktool`, `zipalign`, `default-jdk`, `default-jre`, `apksigner`

## Usage

1. Download this Repository.
2. Prepare the Arcaea APK you want to modify and place it under this Repository. Make sure it is the latest version. For example, `Arcaea-5.10.apk`:

    ![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/ls.png)

3. Change the permissions of `please_run_this_script_before_running_modify.py.sh` and execute it to automatically install all required tools.
    ```bash
    chmod +x please_run_this_script_before_running_modify.py.sh
    ./please_run_this_script_before_running_modify.py.sh
    ```
    ![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/please_run_this_script_before_running_modify.py.png)

4. Run `modify.py` to start modifying the APK.
    ```bash
    python3 modify.py Arcaea-5.10.apk Modifications/
    ```
    ![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/run_modify.png)
    If you need to record gameplay and do not want to modify the gameplay or results screens, add a parameter `public`:
    ```bash
    python3 modify.py Arcaea-5.10.apk Modifications/ public
    ```
    ![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/run_modify_public.png)

5. During the execution, `keytool` will ask you to enter signing information:

    - `Enter keystore password:` Please enter `123456`
    - `Re-enter new password:` Please enter `123456` again
    - Press `Enter` to skip entering personal information
    - `Is CN=Unknown, OU=Unknown, O=Unknown, L=Unknown, ST=Unknown, C=Unknown correct?` Please enter `yes`
       
    ![image](https://github.com/Penguin-71630/Arcaea-beautify/blob/main/Demo/apksigner.png)

6. Done.

## Warning

1. The file names and folder paths of the resource files placed in the `Modification/` folder must correspond to the assets you wish to replace in `assets/`.
2. Do not modify any materials within `assets/songs`, as Arcaea uses a hash function for protection in that folder. Modifying them may prevent the game from starting.
3. Modifying the background, track colors, note styles, or hit effects during gameplay is considered cheating. This script protects these assets and does not allow modifications.

## Credits

- `Modifications/startup/1080/bg.jpg`: https://twitter.com/Refish10086/status/1740695545755427027
- Some sound effects: from Phigros and older versions of Arcaea
- `Modifications/img/1080/_*.png`: Part of Rotaeno's artwork and CG
- `Modifications/img/1080/bg_select_light.jpg`: Artwork from Juvenile (by technoplanet)
- `Modifications/img/1080/bg_select_dark.jpg`: Artwork from Juvenile (by technoplanet)
- `Modifications/img/scenery/scenery_bg_default.png`: Artwork from Juvenile (by technoplanet)
- `Modifications/img/bg_colorless.jpg`: Arcaea CG
- `Modifications/img/bg_byd_light.jpg`: Arcaea CG
- `Modifications/img/bg_byd_dark.jpg`: Arcaea CG

