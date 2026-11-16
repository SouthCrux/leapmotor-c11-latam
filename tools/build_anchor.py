"""Build only the original cluster-anchor helper. Does not install or contact a vehicle."""
import hashlib
import os
from pathlib import Path
import shutil
import subprocess

P = Path(__file__).resolve().parents[1]


def run(args):
    r = subprocess.run(list(map(str, args)), capture_output=True, text=True)
    if r.returncode:
        raise RuntimeError(r.stdout[-1000:] + r.stderr[-2000:])


def main():
    sdk = Path(os.environ.get('ANDROID_SDK_ROOT', str(Path.home() / 'Library/Android/sdk')))
    java_home = os.environ.get('JAVA_HOME')
    java = Path(java_home) / 'bin/java' if java_home else Path(shutil.which('java') or 'java')
    javac = Path(java_home) / 'bin/javac' if java_home else Path(shutil.which('javac') or 'javac')
    android = sdk / 'platforms/android-36.1/android.jar'
    d8 = sdk / 'build-tools/37.0.0/lib/d8.jar'
    if not android.is_file() or not d8.is_file():
        raise RuntimeError('Android platform 36.1 and build-tools 37.0.0 required; set ANDROID_SDK_ROOT')
    b = P / 'build/anchor'
    for name in ['classes', 'dex']:
        target = b / name
        if target.exists():
            shutil.rmtree(target)
        target.mkdir(parents=True)
    run([javac, '--release', '8', '-encoding', 'UTF-8', '-cp', android,
         '-d', b / 'classes', P / 'src/local/amap/voice/ClusterAnchor.java'])
    run([java, '-cp', d8, 'com.android.tools.r8.D8', '--min-api', '31',
         '--lib', android, '--output', b / 'dex', *sorted((b / 'classes').rglob('*.class'))])
    dex = b / 'dex/classes.dex'
    print('Helper compiled locally. Integration into a compatible OEM runtime is still required.')
    print('SHA256:', hashlib.sha256(dex.read_bytes()).hexdigest())


if __name__ == '__main__':
    main()
