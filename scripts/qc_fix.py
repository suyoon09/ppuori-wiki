#!/usr/bin/env python3
"""Fix QC issues: ad tone + dosage format standardization"""
import json, re, os

def main():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "ingredients.json")
    path = os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    fixes = 0

    # === AD TONE FIXES ===
    # These replace medical/advertising terms with neutral alternatives
    ad_replacements = {
        # "치료" → "관리" or rephrase
        "치료에 표준 채택": "해독에 표준 채택",
        "치료의 역사는": "대응의 역사는",
        "치료에 사용": "관리에 사용",
        "치료에 처방": "관리에 처방",
        "치료법": "건강 관리법",
        "치료 가능": "관리 가능",
        "치료제로": "건강 보조제로",
        "치료에 유일한 해독제": "해독에 사용되는 약물",
        "기적의 다이어트 성분": "효과적인 다이어트 성분",
        "기적의 지방 버스터": "효과적인 지방 관리 성분",
        "최고의 라사야나": "대표적인 라사야나",
        "최고의 보양재": "대표적인 보양재",
        "가장 좋은": "적합한",
    }

    for item in data:
        for field in ["content_description", "content_brief", "origin_story", 
                       "fun_fact", "food_sources"]:
            text = item.get(field, "")
            if not text:
                continue
            original = text
            for old, new in ad_replacements.items():
                text = text.replace(old, new)
            if text != original:
                item[field] = text
                fixes += 1

    # === DOSAGE FORMAT STANDARDIZATION ===
    # Ensure all dosage values either end with /일 or have a valid alternative
    dosage_fixes = {
        "100mg (RDA), 500-1000mg (보충)": "100mg/일 (RDA), 500-1000mg/일 (보충 시)",
        "300-500mg (AKBA 30% 기준)": "300-500mg/일 (AKBA 30% 기준)",
        "식사와 함께 1-2캡슐": "식사 시 1-2캡슐/일",
        "200-400mg (클로로겐산 45-50%)": "200-400mg/일 (클로로겐산 45-50%)",
        "별도 권장량 없음": "별도 권장량 없음 (식품으로 충분)",
        "500-1000mg HCA x3회/일 (식전)": "500-1000mg HCA x3회/일",
        "500-1000mg HCA x3/일(식전)": "500-1000mg HCA x3회/일",
        "250mg 추출물(10% 포스콜린) x2/일": "250mg 추출물 x2회/일 (포스콜린 10%)",
        "체중 1kg당 1.6-2.2g (보충제로 20-40g)": "체중 1kg당 1.6-2.2g/일 (보충제 20-40g)",
        "300mg x3회/일(히페리신 0.3%)": "300mg x3회/일 (히페리신 0.3%)",
    }

    for item in data:
        dosage = item.get("dosage_reference", "")
        if dosage in dosage_fixes:
            item["dosage_reference"] = dosage_fixes[dosage]
            fixes += 1

    # === FIX EVIDENCE LEVEL CONSISTENCY ===
    # Normalize edge cases
    evidence_fixes = {
        "보통 (간독성 주의)": "보통",
        "보통 (인체 연구 초기)": "보통",
    }
    for item in data:
        ev = item.get("evidence_level", "")
        if ev in evidence_fixes:
            item["evidence_level"] = evidence_fixes[ev]
            # Move the note to description if applicable
            if "간독성 주의" in ev and "간독성" not in item.get("content_description", ""):
                item["content_description"] += " (간독성 사례 보고로 주의 필요)"
            fixes += 1

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Applied {fixes} fixes")

if __name__ == "__main__":
    main()
