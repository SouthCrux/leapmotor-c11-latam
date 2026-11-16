# Roadmap / Hoja de ruta

This describes intended work, not functionality already delivered by RC1.

1. **Protect the baseline.** Reproducible follow tests on both displays, with/without a destination, manual pan and return to follow, route completion, screen recreation and restarts. Document failures as well as passes.
2. **Make contributions reproducible.** Document build assumptions, anonymized test reports, recovery boundaries and firmware compatibility. Improve diagnostic summaries without publishing travel traces.
3. **Improve navigation quality in the pilot region.** Address/POI search, routing/rerouting, speech, lane/maneuver presentation, offline behavior and charger data. Evaluate each capability separately rather than treating a successful route calculation as proof of moving-map follow.
4. **Restore optional features carefully.** Traffic and speed-camera information should return in separate changes only after both-screen follow regression checks. Use suitable sources, provenance, freshness and local validation. No delivery dates or coverage guarantees are set.
5. **Expand throughout LATAM.** Country-by-country data and language work following [COUNTRIES.md](COUNTRIES.md), including Spanish and Portuguese and other community needs. Unsupported countries stay labeled as such until checked.
6. **Map-assisted navigation.** Integrate validated route context, maneuvers, lanes and limits consistently across displays and voice. Explore map-based driving assistance only where hardware/interface compatibility and a suitable validation process exist. RC1 provides no ADAS/NOA or autonomous-driving feature.
7. **Regional usability.** Continue research on local connectivity and the OEM service ecosystem. eSIM/APN provisioning or official server/account migration are research topics, not solved features or promises.

Each step should preserve a recoverable reference. A new feature does not justify accepting a regression in the fundamental moving-map behavior.
