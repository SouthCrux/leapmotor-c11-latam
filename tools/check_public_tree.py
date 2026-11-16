"""Conservative public-tree check; no network, no vehicle access, no secret values printed."""
import re
import struct
from pathlib import Path

P = Path(__file__).resolve().parents[1]
FORBIDDEN = {'.apk', '.dex', '.so', '.sqlite', '.db', '.pcap', '.pcapng', '.pem', '.key', '.p12', '.jks', '.heic', '.jpg', '.jpeg'}
TEXT = {'.md', '.json', '.java', '.py', '.S', '.txt'}
RULES = {
    'VIN-shaped identifier': re.compile(r'\b[A-HJ-NPR-Z0-9]{17}\b'),
    'personal absolute path': re.compile('/' + 'Users' + r'/[^/\s]+/|C:\\' + 'Users' + r'\\[^\\\s]+'),
    'private geographic coordinate': re.compile(r'(?<!\w)-(?:3[0-9]|5[0-9])\.\d{4,}'),
    'activation payload': re.compile('LPA' + r':1\$\S+'),
    'access token': re.compile(r'\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b'),
    'phone-shaped personal number': re.compile(r'(?<!\d)\+(?:34|598)\d{8,13}(?!\d)'),
}


def png_metadata(path):
    data = path.read_bytes()
    if not data.startswith(b'\x89PNG\r\n\x1a\n'):
        return True
    pos = 8
    while pos + 12 <= len(data):
        size = struct.unpack('>I', data[pos:pos+4])[0]
        kind = data[pos+4:pos+8]
        if kind in {b'eXIf', b'tEXt', b'zTXt', b'iTXt'}:
            return True
        pos += size + 12
    return False


def main():
    findings = []
    count = 0
    for f in sorted(P.rglob('*')):
        rel = f.relative_to(P)
        if any(part in {'.git', 'build', '__pycache__'} for part in rel.parts) or not f.is_file():
            continue
        count += 1
        if f.is_symlink():
            findings.append((str(rel), 'symlink'))
        if f.suffix.lower() in FORBIDDEN:
            findings.append((str(rel), 'excluded binary/private-data type'))
        if f.suffix.lower() == '.png' and png_metadata(f):
            findings.append((str(rel), 'image metadata or invalid PNG'))
        if f.suffix in TEXT or f.name in {'LICENSE', '.gitignore'}:
            text = f.read_text(encoding='utf-8')
            for rule, pattern in RULES.items():
                if pattern.search(text):
                    findings.append((str(rel), rule))
    for filename, rule in findings:
        print(filename + ': ' + rule)
    if findings:
        raise SystemExit('Public-tree check failed; inspect locally before publishing')
    print('PASS:', count, 'public files checked; still review images and Git history manually')


if __name__ == '__main__':
    main()
