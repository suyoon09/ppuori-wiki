#!/usr/bin/env python3
"""Fix remaining 13 QC issues — context-aware replacements"""
import json, os

def main():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "ingredients.json")
    path = os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    fixes = 0

    # === TARGETED AD_TONE FIXES (context-aware) ===
    targeted = {
        "digestive-enzyme": {
            "fun_fact": ("표준 치료로", "표준 보조 요법으로"),
        },
        "saccharomyces-boulardii": {
            "origin_story": ("설사를 치료하는", "설사를 관리하는"),
        },
        "pycnogenol": {
            "origin_story": ("괴혈병 치료 일화", "괴혈병 대응 일화"),
        },
        "panax-ginseng": {
            "fun_fact": ("치료제)='만병통치'", "도움)='만능 보양'"),
        },
        "turkey-tail": {
            "origin_story": ("보조 치료 의약품", "보조 의약품"),
        },
        "cranberry-extract": {
            "origin_story": ("민간 요법", "전통 건강관리법"),
        },
        "vitamin-b1": {
            "origin_story": ("퇴치에 성공한", "극복에 성공한"),
        },
    }

    for item in data:
        if item["id"] in targeted:
            for field, (old, new) in targeted[item["id"]].items():
                text = item.get(field, "")
                if old in text:
                    item[field] = text.replace(old, new)
                    fixes += 1

    # === DOSAGE FORMAT FIXES ===
    dosage_targeted = {
        "omega-9": "별도 권장량 없음/일",
        "peppermint": "장용코팅 캡슐 0.2ml x3회/일",
        "plum-extract": "300-500mg 추출물/일",
        "coenzyme-a": "판토텐산으로 보충 (제품별 상이)",
        "hijiki": "식품으로 섭취 (제품별 상이)",
        "chamomile": "270-400mg/일",
    }

    for item in data:
        if item["id"] in dosage_targeted:
            item["dosage_reference"] = dosage_targeted[item["id"]]
            fixes += 1

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Applied {fixes} targeted fixes")

if __name__ == "__main__":
    main()
