# DSW 版本政策

## Branch 對應

| Branch | 用途 | 是否含翻譯檔 |
| --- | --- | --- |
| `main` | 設定、政策、詞彙表、Issue 入口 | 否 |
| `sync/v4.31` | DSW 4.31 維護線 | 是 |
| `sync/v4.32` | DSW 4.32 目前使用線 | 是 |

每個 minor version 獨立同步官方同名 branch，不把 4.32 的 PO 直接覆蓋到 4.31。

## 狀態

- `active`：production 或 preview 主要版本，持續收補翻與上游更新。
- `maintenance`：只處理仍在使用環境的必要修正。
- `retired`：停止建置，不接受一般翻譯更新；歷史 branch 保留。

狀態與 package version 由 `translation-config.yml` 管理。locale 內容有任何 release
變更時必須增加 `locale_version`，避免 DSW 誤認為仍是同一份 package。

## 升版

新增 DSW minor version 時：

1. 在 `main` 的設定新增版本並標示狀態。
2. 從 `main` 建立新的 `sync/vX.Y`。
3. 同步官方 baseline。
4. 只移植 audit 證明仍存在的 overrides/extras，不整包複製舊版。
5. 通過 audit、package 與 preview 後才供 production 使用。

