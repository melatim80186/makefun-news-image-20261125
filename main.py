"""Salin gambar jadi entry.png ke folder output make.fun.

Gambar sudah jadi di samping file ini; program hanya memindahkannya
apa adanya ke MAKEFUN_OUTPUT_DIR (atau /output) supaya penilai
mendapat satu PNG 1024x1024 yang sama persis setiap kali jalan.
"""

import os
from pathlib import Path


def deliver_entry() -> None:
    source = Path(__file__).resolve().parent / "entry.png"
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    target.write_bytes(source.read_bytes())


deliver_entry()
