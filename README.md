# DSW UI 繁體中文補翻

這個 repo 補足 DSW 官方 Weblate／`wizard-locales` 尚未涵蓋、或在 depositar
實際介面仍顯示英文的文字。它不取代官方翻譯；官方既有成果會持續同步，本 repo
只保存必要的差異。

## 我要回報漏翻

不需要會 Git、gettext 或 Python。請直接建立以下其中一種 Issue：

- [回報英文漏翻](../../issues/new?template=missing-translation.yml)
- [修正現有翻譯](../../issues/new?template=translation-correction.yml)

請貼上英文原文、出現位置與 DSW 版本；若能附畫面與建議譯文，會更容易重現。
維護者會把內容放入正確版本並由工具檢查。

完整的回報範例、CI 畫面預覽與成果確認方式見
[DSW UI 繁體中文補翻指南](https://threemonth03.github.io/dsw-locale-tool/)。

## 內容如何分層

- `upstream/`：從官方 `ds-wizard/wizard-locales` 同步，禁止人工編輯。
- `overrides/`：官方 POT 有該字串，但本地需要補譯或暫時覆蓋。
- `extras/`：實際 UI 出現、但官方 POT 尚未收錄的字串。
- `glossary/`：跨版本共用詞彙。

`main` 只管理政策與版本設定；實際翻譯位於 `sync/v4.31`、`sync/v4.32` 等版本
branch。完整規則見 [版本政策](docs/version-policy.md)。

## 維護原則

1. 優先使用 Weblate 的官方翻譯。
2. 本地只保存差異，不複製整份翻譯作為人工維護來源。
3. `extras` 一旦進入官方 POT，便移到 `overrides` 或直接採用上游。
4. production 只使用經過 audit 與官方 packager 打包的 artifact。
