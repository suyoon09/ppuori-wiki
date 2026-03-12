#!/usr/bin/env python3
"""Content QC script for ingredients.json — checks completeness, consistency, and tone."""
import json, re, os

def main():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "ingredients.json")
    path = os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    issues = []
    stats = {"total": len(data), "t1": 0, "t2": 0, "t3": 0}
    evidence_vals = set()
    origin_vals = set()

    # Advertising / overstatement patterns (Korean)
    ad_patterns = [
        (r"최고의|최강의|가장 좋은", "과장 표현 의심"),
        (r"반드시 효과|확실한 효과|놀라운 효과", "효능 보장 표현"),
        (r"기적|마법|혁명적", "과장 수식어"),
        (r"모든 사람에게|누구나", "일반화 표현"),
        (r"부작용이 없", "안전성 보장 표현"),
        (r"완치|치료", "의약품 표현 (건기식 부적절)"),
    ]

    for item in data:
        tier = item["tier"]
        iid = item["id"]
        name = item["name"]
        prefix = f"[T{tier}] {name} ({iid})"

        if tier == 1:
            stats["t1"] += 1
            # T1 required fields
            for f in ["content_description", "origin_type", "origin_story", 
                       "dosage_reference", "evidence_level", "food_sources", "fun_fact"]:
                if not item.get(f):
                    issues.append(("MISSING_FIELD", prefix, f"필드 누락: {f}"))
            
            # T1 description length check (should be substantial)
            desc = item.get("content_description", "")
            if len(desc) < 30:
                issues.append(("SHORT_CONTENT", prefix, f"설명 너무 짧음: {len(desc)}자"))

        elif tier == 2:
            stats["t2"] += 1
            for f in ["content_description", "origin_type", "origin_story",
                       "dosage_reference", "evidence_level"]:
                if not item.get(f):
                    issues.append(("MISSING_FIELD", prefix, f"필드 누락: {f}"))
            
            desc = item.get("content_description", "")
            if len(desc) < 15:
                issues.append(("SHORT_CONTENT", prefix, f"설명 너무 짧음: {len(desc)}자"))

        elif tier == 3:
            stats["t3"] += 1
            for f in ["content_brief", "content_role", "safety_class"]:
                if not item.get(f):
                    issues.append(("MISSING_FIELD", prefix, f"필드 누락: {f}"))

        # Collect evidence/origin values for consistency check
        if item.get("evidence_level"):
            evidence_vals.add(item["evidence_level"])
        if item.get("origin_type"):
            origin_vals.add(item["origin_type"])

        # Ad tone check on all text fields
        text_fields = [item.get("content_description", ""), 
                       item.get("content_brief", ""),
                       item.get("origin_story", "")]
        combined_text = " ".join(text_fields)
        for pattern, reason in ad_patterns:
            matches = re.findall(pattern, combined_text)
            if matches:
                issues.append(("AD_TONE", prefix, f"{reason}: '{matches[0]}'"))

        # Check for empty name_en
        if not item.get("name_en"):
            issues.append(("MISSING_FIELD", prefix, "영문명(name_en) 누락"))

        # Check nickname exists for T1/T2
        if tier in [1, 2] and not item.get("nickname"):
            pass  # nickname is optional, skip

        # Dosage format consistency (should contain /일 or similar)
        dosage = item.get("dosage_reference", "")
        if dosage and tier in [1, 2]:
            if not any(u in dosage for u in ["/일", "제품별", "처방", "음용", "외용", "상이"]):
                issues.append(("FORMAT", prefix, f"용량 형식 불일치: '{dosage}'"))

    # === SUMMARY ===
    print("=" * 60)
    print("뿌리 (Ppuri) — 콘텐츠 QC 리포트")
    print("=" * 60)
    print(f"\n총 엔트리: {stats['total']}")
    print(f"  T1 Full Page:  {stats['t1']}")
    print(f"  T2 Standard:   {stats['t2']}")
    print(f"  T3 Brief:      {stats['t3']}")

    print(f"\n근거 수준 값: {sorted(evidence_vals)}")
    print(f"기원 유형 값: {sorted(origin_vals)}")

    # Group issues by type
    issue_types = {}
    for typ, prefix, msg in issues:
        if typ not in issue_types:
            issue_types[typ] = []
        issue_types[typ].append((prefix, msg))

    print(f"\n총 이슈: {len(issues)}건")
    for typ in sorted(issue_types):
        count = len(issue_types[typ])
        print(f"\n--- {typ} ({count}건) ---")
        # Show first 5 of each type
        for prefix, msg in issue_types[typ][:5]:
            print(f"  {prefix}: {msg}")
        if count > 5:
            print(f"  ... 외 {count-5}건")

    # === DUPLICATE CHECK ===
    print("\n--- DUPLICATE CHECK ---")
    ids = [i["id"] for i in data]
    names = [i["name"] for i in data]
    dup_ids = [x for x in ids if ids.count(x) > 1]
    dup_names = [x for x in names if names.count(x) > 1]
    if dup_ids:
        print(f"  중복 ID: {set(dup_ids)}")
    else:
        print("  중복 ID 없음 ✓")
    if dup_names:
        print(f"  중복 이름: {set(dup_names)}")
    else:
        print("  중복 이름 없음 ✓")

    # === CROSS-CHECK: T1 entries should have tags_purpose ===
    print("\n--- T1 TAGS CHECK ---")
    t1_no_tags = [i for i in data if i["tier"]==1 and not i.get("tags_purpose")]
    if t1_no_tags:
        print(f"  태그 없는 T1: {len(t1_no_tags)}건")
        for i in t1_no_tags[:5]:
            print(f"    {i['id']} ({i['name']})")
    else:
        print("  모든 T1에 태그 있음 ✓")

    print("\n" + "=" * 60)
    print("QC 완료")

if __name__ == "__main__":
    main()
