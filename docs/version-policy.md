# DSW 版本政策

## Branch 對應

| Branch | 用途 | 是否含翻譯檔 |
| --- | --- | --- |
| `main` | 設定、政策、詞彙表、Issue 入口 | 否 |
| `sync/vX.Y` | 單一 DSW minor line 的 baseline 與本地補翻 | 是 |

維護範圍以 DSW 官方 Weblate projects 清單為準，不綁定任何 production 現在使用的
版本。每個 minor version 獨立同步官方同名 branch，不把某版 PO 直接覆蓋到另一版。

## 狀態

- `active`：Weblate project 未鎖定，持續同步、補翻、preview 與發版。
- `maintenance`：Weblate project locked；仍可同步、補翻、preview 與發版。
- `retired`：維護者明確凍結的版本；仍保留歷史 branch 與 artifacts。

目前 4.29、4.30、4.31、4.32 全部接受翻譯貢獻，任何一條都不得 archive 或設為
`retired`。即使 Weblate project locked，也仍維持完整的本地翻譯流程。Weblate 後來
不再列出某版本時，automation 也不會自動刪除、archive 或退役它。

狀態與 package version 由 `translation-config.yml` 管理。locale 內容有任何 release
變更時必須增加 `locale_version`，避免 DSW 誤認為仍是同一份 package。

`Maintain locale release lines` 每日核對 Weblate、`wizard-locales`、設定與
`sync/vX.Y` branches。它只透過 repo 自己的 `GITHUB_TOKEN` 做一般 fast-forward
push，不使用 PAT、force-push 或常駐服務。

## 升版

Weblate 新增 DSW minor version 時，automation 會：

1. 等待 `wizard-locales` 建立對應 `vX.Y` branch。
2. 在 `main` 的設定新增版本並標示狀態。
3. 從 `main` 建立新的 `sync/vX.Y`。
4. 同步官方 baseline，不整包複製舊版 overrides/extras。
5. 通過 audit、package 與 preview 後才供 production 使用。
