# 翻譯者指南

## 最短流程

1. 在 DSW 看到英文或不合適的繁體中文。
2. 開啟「英文漏翻」或「翻譯修正」Issue。
3. 貼上畫面、原文與建議譯文。
4. 維護者分類成 `overrides` 或 `extras`。
5. CI 產生 audit 與 preview；翻譯者直接看實際畫面確認。

## 為什麼不要求直接改 PO

PO 同時包含來源字串、譯文、context、plural 與 placeholder，手動編輯容易破壞格式。
本 repo 把 Issue 當成一般翻譯者的正式貢獻入口；PO 是建置格式，不是參與門檻。

## 用詞原則

- 優先遵循 `glossary/zh-Hant.csv`。
- 保留產品名、縮寫與程式識別字。
- `%s`、`{name}`、`${value}` 等 placeholder 不可刪除或改名。
- 同一個動作盡量使用一致的動詞；情境不明時附上截圖，不要只憑英文猜測。

