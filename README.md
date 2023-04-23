# Action_Magisk_PATCHE

这是一个用来修补 boot.img / init_boot.img 的 Github Action 项目

## Usage

Fork 本仓库，在 Action 界面内选择 “直接修补boot 或者是 从ROM提取boot并修补”，然后点击 “Run workflow”，填入 ROM/boot 下载直链，等待完成。

**如果遇到 “403 资源访问受限”，请去 Settings-Actions-General-Workflow permissions,将它调整至 “Read and write permissions”**

**从ROM提取boot并修补仅支持卡刷包**

## Others

依赖于 [Firmware_extractor](https://github.com/ShivamKumarJha/Firmware_extractora)

感谢 [BootIMGExtractAction](https://github.com/tosasitill/BootIMGExtractAction)
