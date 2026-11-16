# RC1: public status record

Milestone: **2026-11-16**. Installed changes: **2026-11-15**. Platform: Chinese-market 2024 C11 BEV 580 Premium, OEM AMap/AutoNavi 3.30, Android-side navigation integration.

The owner reported that map behavior was working well after restoring the earlier runtime and adding only the isolated instrument-cluster anchor adjustment. This report is the basis for RC1. It is not a comprehensive acceptance test or a compatibility certification.

## Evidence and scope

- Installation checks observed follow enabled, preview disabled and rendering active on the main and cluster map surfaces.
- The isolated cluster adjustment was observed changing the vertical anchor from approximately .70 to .611111: 64 pixels upward in a 720-pixel viewport. Main-screen projection remained unchanged.
- The navigation-mode adjustment from .76 to approximately .671111 follows the same code path but is not separately claimed as comprehensively road-tested.
- The coordinate correction was previously exercised in local OEM SDK tests. Historical testing included startup timing failures; no universal latency or lifecycle guarantee is claimed.
- Existing UI/voice adaptation is partial. This repository does not distribute those entire modules.
- Road behavior was subsequently confirmed by the owner, without a recorded public matrix of every mode, road, reboot or operating condition.
- Project-added traffic, speed-camera warnings and later home-arrival refinements are not active in RC1. Their reintroduction must be isolated and regression-tested.
- No ADAS/NOA activation, autonomous driving, eSIM provisioning or global-account migration is delivered by this public release.

## Exact private installation reference

These are file fingerprints, not vehicle identifiers. They help avoid confusing newer experiments with the working milestone:

| Component | SHA-256 |
|---|---|
| Installed RC1 runtime DEX | `d61bbb452f1e2217edda8b7441114a92824ffc577ec632975912bdb0fef7ac9f` |
| Restored runtime before isolated anchor change | `304666b112d4fe0c543be7f2dc233c29d8855e82cff1fd192588cdfd00ae933e` |
| Corrected private coordinate library | `11d5559c652399e5b9dc1735f081a96b53c8209fff4ab0f5dce7495e97d297e2` |

These files are **not included or downloadable from this public repository**. The public Git commit/tag identifies a documentation and original-source snapshot, not the private installation's complete history or binary bundle.

## Known limits

Only one vehicle/platform is the basis for owner confirmation. Other model years, trims, hardware and firmware remain unvalidated. Full regression tests, cross-country coverage, long-duration operation, lifecycle transitions and language completeness remain open work.

No fresh vehicle access was used to prepare this publication. The public screenshots are earlier development captures with identifying map content removed, not current RC1 screenshots or motion-test evidence.
