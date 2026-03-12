# -*- coding: utf-8 -*-
"""
Bulk content expansion for ALL ingredients in the wiki.
Uses existing metadata to generate longer, richer content for every ingredient.
Target: web/src/data/ingredients.json (canonical data source).
"""
import json
import re

DATA_PATH = '/Users/sungjunyoon/Desktop/UnionHouse/ingredient-wiki/web/src/data/ingredients.json'

CATEGORY_KR = {
    'vitamin': '비타민',
    'mineral': '미네랄',
    'amino_acid': '아미노산',
    'fatty_acid': '지방산',
    'probiotic': '프로바이오틱스',
    'extract': '추출물',
    'enzyme': '효소',
    'protein': '단백질',
    'fiber': '식이섬유',
    'additive': '식품첨가물',
    'other_functional': '기능성 원료',
}

ORIGIN_CONTEXT = {
    '현대과학': '현대 과학 연구를 통해 발견·규명된 원료로, 주로 20세기 이후 약리학·생화학·영양학 연구에서 기능이 확인되었습니다.',
    '전통한방': '한의학 처방에서 오랜 역사를 가진 원료로, 동의보감 등 전통 의서에 기록이 남아 있습니다. 현대 과학적 검증이 진행 중입니다.',
    '전통의학': '아유르베다, 유럽 약초학, 민간요법 등 각지의 전통 의학에서 사용되어 온 원료입니다.',
    '식품유래': '일반 식품에서 유효 성분을 추출·농축하여 건강기능식품 원료로 활용하는 소재입니다.',
    '아유르베다': '인도 전통 의학 아유르베다 체계에서 오랜 사용 역사를 가진 약용 식물 유래 원료입니다.',
}

BODYPART_CONTEXT = {
    '전신': '전신의 기능 유지와 건강에 관여합니다',
    '뇌': '뇌 기능과 인지 건강에 기여합니다',
    '장': '장 건강과 소화 기능을 지원합니다',
    '심장·혈관': '심혈관 건강 유지에 도움을 줍니다',
    '피부': '피부 건강과 장벽 기능을 지원합니다',
    '뼈·관절': '뼈 밀도와 관절 건강 유지에 관여합니다',
    '간': '간 기능과 해독 작용을 지원합니다',
    '근육': '근육 기능과 운동 수행 능력에 기여합니다',
    '눈': '눈 건강과 시각 기능을 보호합니다',
    '모발': '모발의 성장과 건강 유지에 관여합니다',
    '구강': '구강 건강과 치아 기능을 지원합니다',
    '위': '위 점막 보호와 소화 기능에 관여합니다',
}

EVIDENCE_CONTEXT = {
    '매우 양호': '다수의 대규모 임상시험과 메타분석에서 효과가 일관되게 확인되어, 높은 수준의 과학적 근거를 가집니다.',
    '양호': '복수의 임상시험에서 일관된 결과가 보고되어 있으나, 대규모 연구는 제한적입니다.',
    '보통': '일부 임상 연구와 전임상 연구에서 가능성이 시사되었으나, 대규모 검증은 아직 이루어지지 않았습니다.',
    '제한적': '전통적 사용 근거 또는 예비 연구 수준의 데이터만 존재하며, 추가 연구가 필요합니다.',
}


def expand_description(item: dict) -> str:
    """Generate an expanded description if current one is too short."""
    current = item.get('content_description', '')
    if len(current) > 300:
        return current  # Already expanded

    name = item['name']
    name_en = item.get('name_en', '')
    nickname = item.get('nickname', '')
    cat = CATEGORY_KR.get(item.get('category', ''), item.get('category', ''))
    mfds = item.get('mfds_functionality', '')
    origin_type = item.get('origin_type', '')
    evidence = item.get('evidence_level', '')
    tags_fn = item.get('tags_function', [])
    tags_bp = item.get('tags_bodypart', [])
    tags_purpose = item.get('tags_purpose', [])
    daily = item.get('daily_recommended', '')
    upper = item.get('upper_limit', '')
    dosage = item.get('dosage_reference', '')
    source_type = item.get('source_type', '')
    aliases = item.get('aliases', [])
    subcategory = item.get('subcategory', '')

    # Build paragraph 1: What it is + core function
    p1_parts = []
    if name_en:
        p1_parts.append(f"{name}({name_en})은(는) {cat} 계열의 건강기능식품 원료입니다.")
    else:
        p1_parts.append(f"{name}은(는) {cat} 계열의 건강기능식품 원료입니다.")

    if current and len(current) > 20:
        p1_parts.append(current)

    if mfds:
        p1_parts.append(f"식약처에서 인정한 기능성은 '{mfds}'입니다.")

    p1 = ' '.join(p1_parts)

    # Build paragraph 2: Body context + function tags
    p2_parts = []
    if tags_fn:
        fn_str = ', '.join(tags_fn)
        p2_parts.append(f"주요 기능으로는 {fn_str}이(가) 있습니다.")

    bp_descs = [BODYPART_CONTEXT.get(bp, '') for bp in tags_bp if bp in BODYPART_CONTEXT]
    if bp_descs:
        p2_parts.append(' '.join(bp_descs) + '.')

    if tags_purpose:
        purpose_str = ', '.join(tags_purpose[:4])
        p2_parts.append(f"주로 {purpose_str} 등의 목적으로 섭취됩니다.")

    p2 = ' '.join(p2_parts) if p2_parts else ''

    # Build paragraph 3: Evidence + dosage
    p3_parts = []
    if origin_type and origin_type in ORIGIN_CONTEXT:
        p3_parts.append(ORIGIN_CONTEXT[origin_type])

    if evidence and evidence in EVIDENCE_CONTEXT:
        p3_parts.append(EVIDENCE_CONTEXT[evidence])

    if daily:
        p3_parts.append(f"일일 권장 섭취량은 {daily}이며")
        if upper:
            p3_parts[-1] = p3_parts[-1] + f", 상한섭취량은 {upper}입니다."
        elif dosage:
            p3_parts[-1] = p3_parts[-1] + f", 보충 시 참고 용량은 {dosage}입니다."
        else:
            p3_parts[-1] = p3_parts[-1] + '.'

    if source_type:
        p3_parts.append(f"원료 유형은 '{source_type}'으로 분류됩니다.")

    p3 = ' '.join(p3_parts) if p3_parts else ''

    parts = [p for p in [p1, p2, p3] if p]
    return '\n\n'.join(parts)


def expand_origin_story(item: dict) -> str:
    """Expand origin story if too short."""
    current = item.get('origin_story', '')
    if len(current) > 250:
        return current

    name = item['name']
    origin_type = item.get('origin_type', '')

    p1 = current if current else f"{name}의 발견과 사용 역사에 대한 기록은 다양한 문화권에서 확인됩니다."

    p2_parts = []
    if origin_type == '전통한방':
        p2_parts.append(f"{name}은(는) 한의학에서 오랜 역사를 가진 약재로, 동의보감을 비롯한 전통 의서에서 처방 기록을 찾을 수 있습니다. 전통적으로 다양한 증상의 치료와 건강 유지에 활용되어 왔으며, 현대에 들어 과학적 검증이 진행되고 있습니다.")
    elif origin_type == '아유르베다':
        p2_parts.append(f"{name}은(는) 인도 전통 의학 아유르베다에서 수천 년간 사용되어 온 약용 소재입니다. 아유르베다에서는 체질(도샤) 균형과 전반적 생명력 회복에 중요한 약재로 여겨져 왔습니다.")
    elif origin_type == '전통의학':
        p2_parts.append(f"{name}은(는) 다양한 문화권의 전통 의학 체계에서 치료 목적으로 사용되어 온 역사를 가지고 있습니다. 전통적 경험이 현대 과학 연구의 출발점이 되는 경우가 많습니다.")
    elif origin_type == '식품유래':
        p2_parts.append(f"{name}은(는) 일상적인 식품에서 유래한 원료로, 특정 유효 성분을 추출하거나 농축하여 건강기능식품으로 활용됩니다. 식품으로서의 안전한 섭취 역사를 기반으로 합니다.")
    elif origin_type == '현대과학':
        p2_parts.append(f"{name}은(는) 20세기 이후 현대 과학 연구를 통해 그 기능과 중요성이 밝혀진 원료입니다. 생화학, 영양학, 약리학의 발전과 함께 체계적인 연구가 이루어지고 있습니다.")

    p2 = ' '.join(p2_parts) if p2_parts else ''
    parts = [p for p in [p1, p2] if p]
    return '\n\n'.join(parts)


def expand_food_sources(item: dict) -> str:
    """Expand food sources if too short."""
    current = item.get('food_sources', '')
    if len(current) > 150:
        return current

    name = item['name']
    cat = item.get('category', '')

    if not current or len(current) < 10:
        if cat in ('extract', 'probiotic', 'enzyme', 'other_functional', 'additive'):
            return f"{name}은(는) 일반적인 식품에서 직접 섭취하기 어려우며, 주로 보충제 형태(캡슐, 정제, 분말)로 섭취합니다."
        else:
            return f"{name}은(는) 다양한 식품에 자연적으로 함유되어 있으며, 균형 잡힌 식단을 통해 일정량을 섭취할 수 있습니다."

    # Add context to short source lists
    cat_context = ''
    if cat in ('extract',):
        cat_context = f" 다만 치료적 용량을 식품만으로 확보하기는 어려워 표준화된 추출물 형태의 보충제 섭취가 일반적입니다."
    elif cat == 'probiotic':
        cat_context = f" 발효 식품을 통해서도 유사한 유산균을 섭취할 수 있으나, 특정 균주와 함량을 보장하기 위해서는 보충제가 더 정확합니다."

    if len(current) < 60 and ',' in current:
        items = [x.strip() for x in current.split(',')]
        listed = ', '.join(items)
        return f"{name}이(가) 풍부한 식품으로는 {listed} 등이 있습니다.{cat_context}"

    return current + cat_context


def expand_fun_fact(item: dict) -> str:
    """Expand fun fact if too short."""
    current = item.get('fun_fact', '')
    if len(current) > 150:
        return current

    name = item['name']
    cat = item.get('category', '')

    if not current or len(current) < 10:
        return ''

    return current


def expand_safety(item: dict) -> str:
    """Generate safety_class if missing."""
    current = item.get('safety_class', '')
    if len(current) > 80:
        return current

    name = item['name']
    upper = item.get('upper_limit', '')
    cat = item.get('category', '')

    parts = []
    if upper:
        parts.append(f"{name}의 상한섭취량은 {upper}입니다.")
        parts.append("이를 초과하여 장기간 섭취하는 것은 권장되지 않습니다.")
    else:
        if cat in ('vitamin',):
            parts.append(f"{name}은(는) 일반적으로 권장 용량 범위 내에서 안전하게 섭취할 수 있습니다.")
        elif cat in ('mineral',):
            parts.append(f"{name}은(는) 권장 용량 내에서 안전하며, 고용량 장기 섭취 시에는 전문가 상담이 권장됩니다.")
        elif cat in ('extract',):
            parts.append(f"{name}은(는) 표준화된 추출물 형태로 권장 용량 내에서 섭취할 경우 일반적으로 안전합니다.")
        elif cat in ('probiotic',):
            parts.append(f"{name}은(는) 대부분의 건강한 성인에게 안전합니다. 면역이 크게 저하된 경우에는 의료 전문가의 상담이 필요합니다.")
        elif cat in ('amino_acid',):
            parts.append(f"{name}은(는) 권장 용량 범위 내에서 일반적으로 안전합니다. 고용량 섭취 시 소화 불편이 나타날 수 있습니다.")
        else:
            parts.append(f"{name}은(는) 적정 용량 범위 내에서 안전한 것으로 알려져 있습니다.")

    parts.append("임산부, 수유부, 약물 복용 중인 경우에는 섭취 전 전문가와 상담하시기 바랍니다.")

    return ' '.join(parts)


def main():
    with open(DATA_PATH, 'r', encoding='utf-8') as f:
        data = json.load(f)

    updated = 0
    for item in data:
        changed = False

        # Expand description
        new_desc = expand_description(item)
        if len(new_desc) > len(item.get('content_description', '')) + 50:
            item['content_description'] = new_desc
            changed = True

        # Expand origin story
        new_origin = expand_origin_story(item)
        if len(new_origin) > len(item.get('origin_story', '')) + 50:
            item['origin_story'] = new_origin
            changed = True

        # Expand food sources
        new_food = expand_food_sources(item)
        if len(new_food) > len(item.get('food_sources', '')) + 20:
            item['food_sources'] = new_food
            changed = True

        # Add safety if missing
        new_safety = expand_safety(item)
        if len(new_safety) > len(item.get('safety_class', '')) + 30:
            item['safety_class'] = new_safety
            changed = True

        if changed:
            updated += 1

    with open(DATA_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Summary
    short_desc = sum(1 for x in data if len(x.get('content_description', '')) <= 200)
    short_origin = sum(1 for x in data if len(x.get('origin_story', '')) <= 100)
    no_safety = sum(1 for x in data if not x.get('safety_class', ''))

    print(f'Updated {updated} / {len(data)} ingredients')
    print(f'Still short descriptions (<=200c): {short_desc}')
    print(f'Still short origin stories (<=100c): {short_origin}')
    print(f'Missing safety: {no_safety}')


if __name__ == '__main__':
    main()
