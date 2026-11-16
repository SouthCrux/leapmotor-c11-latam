# Contributing / Cómo contribuir

Start from RC1 and keep changes small. Explain the concrete issue, platform assumptions, resulting behavior, tests performed and remaining limits. Test locally first; community reports from another firmware or country should be labeled as reports until independently validated.

Useful reports contain model year/trim, generic firmware version, country, whether a route was active, what each screen did, and reproducible steps. **Do not include a VIN, registration plate, account, activation code, exact private coordinates, home/work/school destination, trip history, credentials, or an unredacted screenshot/log.** Remove metadata from images too.

Do not upload manufacturer APKs, native libraries, complete firmware, commercial map packages or proprietary decompiled source here. Prefer original code, minimal technical descriptions, references and build-specific fingerprints.

Any navigation change needs checks on both central display and instrument cluster. Record failures and conditions not tested. Stationary checks do not demonstrate behavior while driving. Avoid tests that require the driver to interact with diagnostic tools while driving.

The public repository is not an installer. Changes to a real vehicle require its owner's authorization and an appropriate recovery plan for the actual platform. Reports or requests do not authorize anyone to connect to another person's vehicle or accounts.

Translations should preserve the distinction between the initiating owner's personal account, observed behavior, locally tested code and future research goals. Do not turn a country listed as a target into a claim of existing support.

Run `python3 tools/check_public_tree.py` before preparing a contribution. Automated checks supplement, but do not replace, a manual review of text, images and Git history.
