# 維護者指南

## 自動建立與更新版本 branch

`Maintain locale release lines` 每日呼叫 `dsw-locale-tool` 的 reusable workflow。
新的 Weblate `DSW X.Y` project 只有在 `wizard-locales` 已建立 `vX.Y` branch
後才會加入 config，並從 `main` 建立 `sync/vX.Y`。新 branch 不複製舊版
overrides 或 extras。

排程也會重新同步每個未退役 branch 的 baseline，執行 audit、build 與
package。已有 branch 驗證失敗時不 push；新 branch 可保留鎖定 baseline，但不會
當成可發布成果。失敗會留下 Actions artifact 與 `automation` Issue。

以下指令只用於手動重現：

```console
dsw-locale validate-config translation-config.yml
dsw-locale sync-upstream --config translation-config.yml --version v4.32 --output .
dsw-locale audit --root . --report-dir reports --fail-on placeholders --fail-on structure
```

同步只會覆寫 `upstream/`。產生的內容與 `upstream.lock.yml` 要一起 commit；
build、preview 與 publish 只使用這份已鎖定的 baseline。人工補翻放在：

- `overrides/wizard.po` 或 `overrides/mail.po`
- `extras/wizard.po` 或 `extras/mail.po`

## 核對 Weblate 維護版本

```console
dsw-locale version-report \
  --config translation-config.yml \
  --repository-root . \
  --report-dir reports/versions \
  --fail-on-drift
```

Weblate 未鎖定 project 應為 `active`，locked project 應為 `maintenance`；兩者都要有
`sync/vX.Y` branch。Weblate 不再列出的版本不自動刪除、archive 或改為
`retired`；必須由維護者另外決定。

## Pull Request 驗證

所有以 `sync/vX.Y` 為 base 的 PR 都由 default branch 上的 read-only workflow 驗證。
翻譯 PR 只能修改 `overrides/*.po`、`extras/*.po`、詞彙、README 或 Markdown 文件；不得
修改 `upstream/`、workflow 或管理檔案。需要發新版 locale 時，config 只允許提高該
release line 的 `locale_version`。

Validator 由 `dsw-locale-tool` 提供，依序檢查 PR scope、audit、build 與 package；內容
repo 不保存第二份 Python 或 shell 實作。

## Issue 分流

1. 先確認英文原文與 DSW minor version。
2. 在 `upstream/*.pot` 找得到：放入 `overrides`。
3. POT 找不到、但實際 UI 能重現：放入 `extras`，並保留畫面位置於 extracted comment。
4. 若所有支援版本都會出現，同步更新各版本 branch；不要假設不同 minor 共用相同 msgid。

## 上游同步後清理

Audit 會列出：

- `extras_now_upstream`：字串已進 POT，應移出 `extras`。
- `redundant_overrides`：官方譯文已相同，可刪除本地 override。
- `misplaced_overrides`：POT 找不到，通常應移到 `extras` 或確認字串已被移除。
