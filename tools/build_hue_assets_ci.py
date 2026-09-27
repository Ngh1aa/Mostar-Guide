#!/usr/bin/env python3
"""Stable CI entrypoint for Huế asset production.

Wikimedia may reject arbitrary thumbnail widths with HTTP 400. Use canonical
original-file URLs, then let build_hue_assets normalize local masters to max
2560 px before committing them.
"""

import build_hue_assets as builder

builder.SOURCES["A01"]["download_url"] = (
    "https://upload.wikimedia.org/wikipedia/commons/3/33/"
    "Ngo_Mon_Gate_for_entry_to_the_Imperial_Citadel%2C_Hue_%2831654316702%29.jpg"
)
builder.SOURCES["A04"]["download_url"] = (
    "https://upload.wikimedia.org/wikipedia/commons/5/5e/"
    "Khai_Dinh_tomb_Hue_%2827767136409%29.jpg"
)
builder.SOURCES["A05"]["download_url"] = (
    "https://upload.wikimedia.org/wikipedia/commons/0/05/"
    "Dong_Ba_market%2C_Th%C3%A0nh_ph%E1%BB%91_Hu%E1%BA%BF%2C_Vietnam_%28Unsplash%29.jpg"
)

raise SystemExit(builder.main())
