# DSW UI 繁體中文補翻

這個 repo 專門補足 DSW 官方 Weblate 尚未翻譯、或 depositar 實際介面仍顯示英文的
文字。一般翻譯者不需要使用 Git、編輯 PO，也不需要接觸工具 repo。

:::{admonition} 發現漏翻時，直接填 Issue
:class: tip

- [回報英文漏翻](https://github.com/ThreeMonth03/dsw-ui-locales-zh_Hant/issues/new?template=missing-translation.yml)
- [修正現有翻譯](https://github.com/ThreeMonth03/dsw-ui-locales-zh_Hant/issues/new?template=translation-correction.yml)

請提供 DSW 版本、畫面位置、完整英文原文與截圖；建議譯文可以留空討論。
:::

```{toctree}
:maxdepth: 2
:hidden:

translator-guide
version-policy
maintainer-guide
```

## 貢獻流程

1. 翻譯者用 Issue 回報英文或不自然的譯文。
2. 維護者判斷字串屬於官方翻譯的暫時補譯，或官方 POT 尚未收錄的 UI 文字。
3. CI 檢查 gettext 結構、placeholder、locale build 與 package。
4. 一次性 DSW preview 產生實際介面截圖，讓翻譯者直接確認結果。
5. 確認後發布 immutable installer image；production 不需要 fork DSW frontend。

完整說明見 {doc}`translator-guide`；preview 的畫面與判讀方式見
[DSW Locale Tool 的 preview 文件](https://www.threemonth03.com/dsw-locale-tool/preview.html)。

## 支援版本

DSW 4.29、4.30、4.31、4.32 都接受回報與補翻。每個 minor version 使用獨立的
`sync/vX.Y` branch，避免不同版本的來源字串彼此污染。Weblate 將舊 project 鎖定，
不代表本 repo 停止維護該版本；詳見 {doc}`version-policy`。

## 與官方翻譯的關係

官方 `ds-wizard/wizard-locales` 是唯讀 baseline；本 repo 只保存仍有必要的差異。
官方日後補上相同譯文時，本地 override 會被移除。適合所有 DSW 使用者的修正仍應
回饋官方 Weblate，這裡不是另一套 Weblate。
