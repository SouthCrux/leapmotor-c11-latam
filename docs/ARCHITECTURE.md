# Technical notes

## Keep the original map's follow mechanism

RC1 uses the existing native navigation/map integration. The aim is for the vehicle glyph to remain at its follow anchor while the geographic map moves. A central-screen SDK view and an instrument-cluster SDK view are involved. In the observed OEM build, cluster surface 3 maps to engine 5; those identifiers must not be assumed for another build.

The restored runtime removed subsequent experimental extensions. This isolated a working reference; it did not prove which removed change caused the regression. Do not present the rollback as a demonstrated root-cause attribution to traffic or speed-camera features.

## Coordinate validation

A local investigation reproduced a native message path that accepted a centre only with positive longitude **and** positive latitude. Such a check rejects ordinary coordinates in Uruguay and other southern/western regions.

The retained correction uses finite, nonzero coordinates with absolute longitude below 180 and absolute latitude below 90. It preserves that particular path's zero/sentinel rejection; it is **not** a general-purpose geographic-validity rule, since valid global locations can lie on the equator or prime meridian.

`src/signed-coordinate-guard-aarch64.S` is the original replacement guard fragment used in that investigation. It relies on a specific ARM64 register/stack layout and an external `oem_resume` symbol. It is not standalone, not a patch for arbitrary AMap versions, and not an installer. Full manufacturer libraries, reverse-engineered class dumps and map packages are intentionally absent.

The fragment explains the mechanism so others can examine equivalent paths in their own compatible environments. Porting requires independent analysis and validation of the actual input build. The correction of this one path is not proof that every regional-coordinate path has been fixed.

## Instrument-cluster anchor

`src/local/amap/voice/ClusterAnchor.java` is original project code. It observes the already existing cluster view on the Android main thread. When the view is in follow mode, not preview, uses a 720-pixel viewport and has a recognized OEM projection anchor, it subtracts 64 pixels from that vertical anchor.

The recognized raw anchors are approximately .6667, .70 and .76. The resulting anchor no longer matches a raw value, so subsequent observations do not accumulate the shift. If the OEM reinstates its raw anchor or replaces the view, the adjustment can be applied once again. Unknown/custom anchors are left alone.

The periodic observation is every 1.5 seconds. It does not periodically recenter the map and does not write GPS, map centre, follow mode, pitch, roll or zoom. It only calls the existing projection-anchor setter. It writes a small local status record when applying a shift; that record contains anchor settings, not location coordinates.

The code expects the original OEM application class loader and existing SDK classes. Its startup entry is `ClusterAnchor.start(context)`. Merely compiling or sideloading this helper DEX will not integrate it into the OEM application. The private RC1 runtime added one bootstrap call while preserving its earlier classes. That entire runtime is not redistributed here.

`python3 tools/build_anchor.py` compiles the helper locally when an Android SDK and JDK are available. `python3 tools/check_public_tree.py` checks the public working tree before commits/publication. Neither command contacts a vehicle.
