# 貢獻方式

## 一般翻譯者

請使用 GitHub Issue 表單回報，不必修改任何程式碼或 PO 檔。一次 Issue 以一個
畫面或一組相關字串為原則，並提供：

1. DSW 版本。
2. 畫面網址或操作路徑。
3. 完整英文原文，包含標點與 `%s`、`{name}` 等 placeholder。
4. 建議繁體中文譯文（可以留空讓其他人討論）。
5. 螢幕截圖或重現步驟。

翻譯討論直接留在 Issue。維護者完成 preview 後會貼回結果，再關閉 Issue。

## 熟悉 gettext 的貢獻者

可對對應的 `sync/v<major>.<minor>` branch 提 PR，但只修改：

- `overrides/*.po`
- `extras/*.po`
- `glossary/zh-Hant.csv`
- 說明文件

請勿直接修改 `upstream/`；該目錄每次同步都會被工具覆寫。譯文必須保留英文原文
中的 placeholder。若同一句英文依情境需要不同譯法，請在 PR 或 Issue 說明畫面位置。

PR 會自動驗證變更範圍、gettext 結構、placeholder、locale build 與 package。
`translation-config.yml` 只允許提高該版本的 `locale_version`；其他政策或 automation
變更一律對 `main` 提出，不混入翻譯 PR。

## 授權

送出翻譯即表示同意以本 repo 的 CC BY 4.0 條款提供該內容，讓它能與 DSW
官方 locale 相容並在未來回饋上游。
