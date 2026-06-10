#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Safe launcher for Transbot scripts.

Purpose:
- Avoid polluted shell environments such as bad LD_PRELOAD/LD_LIBRARY_PATH.
- Run Transbot Python scripts with a minimal, clean environment.

Usage:
  python3 Transbot/Script/safe_run.py split_chapters
  python3 Transbot/Script/safe_run.py scan_branches
"""

import os
import sys
import subprocess
from pathlib import Path

ROOT = Path('/sdcard/My Agent/Transbot')
SCRIPT_DIR = ROOT / 'Script'

SCRIPT_MAP = {
    'split_chapters': SCRIPT_DIR / 'split_chapters.py',
    'scan_branches': SCRIPT_DIR / 'scan_branches.py',
}

BAD_ENV_PREFIXES = (
    'LD_',
    'DYLD_',
    'PYTHONHOME',
)


def clean_env():
    env = {}
    keep = {
        'HOME': os.environ.get('HOME', '/data/data/com.termux/files/home'),
        'USER': os.environ.get('USER', 'u0_a146'),
        'LOGNAME': os.environ.get('LOGNAME', os.environ.get('USER', 'u0_a146')),
        'LANG': os.environ.get('LANG', 'C.UTF-8'),
        'LC_ALL': os.environ.get('LC_ALL', 'C.UTF-8'),
        'PATH': '/data/data/com.termux/files/usr/bin:/usr/bin:/bin:/system/bin:/system/xbin',
        'TMPDIR': os.environ.get('TMPDIR', '/data/data/com.termux/files/usr/tmp'),
    }
    env.update(keep)

    # Explicitly do not propagate loader-related variables.
    for k, v in os.environ.items():
        if k.startswith(BAD_ENV_PREFIXES):
            continue
        if k in env:
            continue
        # Keep only safe app metadata if needed.
        if k.startswith('GOCLAW_'):
            env[k] = v
    return env


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in SCRIPT_MAP:
        print('Usage: safe_run.py <script>')
        print('Available:', ', '.join(sorted(SCRIPT_MAP)))
        sys.exit(2)

    target = SCRIPT_MAP[sys.argv[1]]
    if not target.exists():
        print(f'ERROR: script not found: {target}')
        sys.exit(1)

    python = sys.executable or '/data/data/com.termux/files/usr/bin/python3'
    env = clean_env()
    cmd = [python, str(target), *sys.argv[2:]]

    print('Safe runner executing:')
    print('  python:', python)
    print('  target:', target)
    print('  cwd:', ROOT)
    print('  LD_* stripped: yes')

    proc = subprocess.run(cmd, cwd=str(ROOT), env=env, text=True)
    sys.exit(proc.returncode)


if __name__ == '__main__':
    main()
