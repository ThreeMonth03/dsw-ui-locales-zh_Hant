# DSW 版本政策

## Branch 對應

| Branch | 用途 | 是否含翻譯檔 |
| --- | --- | --- |
| `main` | 設定、政策、詞彙表、Issue 入口 | 否 |
| `sync/v4.29` | DSW 4.29 維護線 | 是 |
| `sync/v4.30` | DSW 4.30 維護線 | 是 |
| `sync/v4.31` | DSW 4.31 維護線 | 是 |
| `sync/v4.32` | DSW 4.32 active 線 | 是 |

維護範圍以 DSW 官方 Weblate projects 清單為準，不綁定任何 production 現在使用的
版本。每個 minor version 獨立同步官方同名 branch，不把某版 PO 直接覆蓋到另一版。

## 狀態

- `active`：Weblate project 未鎖定，持續同步、補翻、preview 與發版。
- `maintenance`：Weblate project locked；仍可同步、補翻、preview 與發版。
- `retired`：Weblate 已不再列出該 project；凍結但保留歷史 branch 與 artifacts。

狀態與 package version 由 `translation-config.yml` 管理。locale 內容有任何 release
變更時必須增加 `locale_version`，避免 DSW 誤認為仍是同一份 package。

Tool repo 的 `Check Weblate version alignment` workflow 每週核對 Weblate、設定與
`sync/vX.Y` branches。少一個版本、branch，或 lifecycle state 不一致時會留下報告並
使 workflow 失敗。

## 升版

Weblate 新增 DSW minor version 時：

1. 在 `main` 的設定新增版本並標示狀態。
2. 從 `main` 建立新的 `sync/vX.Y`。
3. 同步官方 baseline。
4. 只移植 audit 證明仍存在的 overrides/extras，不整包複製舊版。
5. 通過 audit、package 與 preview 後才供 production 使用。
