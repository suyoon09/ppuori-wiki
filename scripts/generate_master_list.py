#!/usr/bin/env python3
"""
Generate the master ingredient list for the ingredient wiki.

This script creates a comprehensive JSON file of all Korean health functional food
ingredients based on MFDS (식약처) classifications. The data is structured in 3 tiers:
  - Tier 1 (Full Page): ~150 high-consumer-interest functional ingredients
  - Tier 2 (Standard): ~200 moderate-interest functional + key sub-ingredients
  - Tier 3 (Brief): ~200+ additives and minor sub-ingredients

Source: MFDS 건강기능식품 공전 (고시형 원료) + 개별인정형 원료 categories
"""

import json
import os

def build_master_list():
    """Build the complete ingredient master list."""
    
    ingredients = []
    
    # =========================================================================
    # TIER 1: Full Page — High consumer interest, rich content
    # =========================================================================
    
    # --- Vitamins (수용성) ---
    tier1_vitamins_water = [
        {"id": "vitamin-b1", "name": "비타민B1", "name_en": "Thiamine", "aliases": ["티아민", "Thiamine"], "nickname": "탄수화물 에너지의 점화 플러그", "category": "vitamin", "subcategory": "b-complex", "tags_purpose": ["만성피로", "학습-수험생"], "tags_function": ["에너지 생성"], "tags_bodypart": ["뇌", "전신"], "daily_recommended": "1.2mg (남성), 1.1mg (여성)", "mfds_functionality": "탄수화물과 에너지 대사에 필요"},
        {"id": "vitamin-b2", "name": "비타민B2", "name_en": "Riboflavin", "aliases": ["리보플라빈", "Riboflavin"], "nickname": "에너지 전달의 중간 매개자", "category": "vitamin", "subcategory": "b-complex", "tags_purpose": ["만성피로", "피부"], "tags_function": ["에너지 생성"], "tags_bodypart": ["피부", "전신"], "daily_recommended": "1.5mg", "mfds_functionality": "체내 에너지 생성에 필요"},
        {"id": "vitamin-b3", "name": "비타민B3", "name_en": "Niacin", "aliases": ["나이아신", "니코틴산", "니코틴아미드", "나이아신아마이드", "Niacin", "Nicotinamide"], "nickname": "세포의 에너지 통화", "category": "vitamin", "subcategory": "b-complex", "tags_purpose": ["만성피로", "피부", "노화방지"], "tags_function": ["에너지 생성", "항산화"], "tags_bodypart": ["피부", "전신"], "daily_recommended": "16mg NE (남성), 14mg NE (여성)", "upper_limit": "35mg/일", "mfds_functionality": "체내 에너지 생성에 필요", "related_ingredients": ["vitamin-b2", "glutathione", "l-tryptophan"]},
        {"id": "vitamin-b5", "name": "비타민B5", "name_en": "Pantothenic Acid", "aliases": ["판토텐산", "Pantothenic Acid"], "nickname": "CoA의 원료 — 모든 대사의 교차점", "category": "vitamin", "subcategory": "b-complex", "tags_purpose": ["만성피로", "스트레스"], "tags_function": ["에너지 생성"], "tags_bodypart": ["전신"], "daily_recommended": "5mg", "mfds_functionality": "지방, 탄수화물, 단백질 대사와 에너지 생성에 필요"},
        {"id": "vitamin-b6", "name": "비타민B6", "name_en": "Pyridoxine", "aliases": ["피리독신", "Pyridoxine"], "nickname": "아미노산과 신경전달물질의 통역사", "category": "vitamin", "subcategory": "b-complex", "tags_purpose": ["만성피로", "수면", "스트레스", "임산부"], "tags_function": ["에너지 생성", "신경 안정"], "tags_bodypart": ["뇌", "전신"], "daily_recommended": "1.5mg", "upper_limit": "100mg/일", "mfds_functionality": "단백질 및 아미노산 이용에 필요, 혈액의 호모시스테인 수준을 정상으로 유지하는 데 필요"},
        {"id": "vitamin-b7", "name": "비타민B7", "name_en": "Biotin", "aliases": ["비오틴", "Biotin"], "nickname": "피부·모발·손톱의 구조 재료", "category": "vitamin", "subcategory": "b-complex", "tags_purpose": ["탈모", "피부"], "tags_function": ["모발 건강", "피부 건강"], "tags_bodypart": ["모발", "피부"], "daily_recommended": "30μg", "mfds_functionality": "지방, 탄수화물, 단백질 대사와 에너지 생성에 필요"},
        {"id": "vitamin-b9", "name": "비타민B9", "name_en": "Folic Acid", "aliases": ["엽산", "폴산", "Folic Acid", "Folate"], "nickname": "세포 분열의 설계도 복사기", "category": "vitamin", "subcategory": "b-complex", "tags_purpose": ["임산부", "노화방지"], "tags_function": ["태아 발달", "세포 보호"], "tags_bodypart": ["전신"], "daily_recommended": "400μg", "upper_limit": "1,000μg/일", "mfds_functionality": "세포와 혈액 생성에 필요, 태아 신경관의 정상 발달에 필요"},
        {"id": "vitamin-b12", "name": "비타민B12", "name_en": "Cobalamin", "aliases": ["코발라민", "시아노코발라민", "메틸코발라민", "Cobalamin"], "nickname": "식물에는 없는 비타민", "category": "vitamin", "subcategory": "b-complex", "tags_purpose": ["만성피로", "노화방지"], "tags_function": ["에너지 생성", "세포 보호"], "tags_bodypart": ["뇌", "전신"], "daily_recommended": "2.4μg", "mfds_functionality": "정상적인 엽산 대사에 필요"},
        {"id": "vitamin-c", "name": "비타민C", "name_en": "Ascorbic Acid", "aliases": ["아스코르브산", "Ascorbic Acid"], "nickname": "인간이 직접 만들지 못하는 항산화제", "category": "vitamin", "subcategory": "water-soluble", "tags_purpose": ["면역", "피부", "노화방지"], "tags_function": ["항산화", "면역 기능", "콜라겐 합성"], "tags_bodypart": ["피부", "전신"], "daily_recommended": "100mg", "upper_limit": "2,000mg/일", "mfds_functionality": "항산화 작용을 하여 유해산소로부터 세포를 보호하는 데 필요, 결합조직 형성과 기능 유지에 필요", "related_ingredients": ["iron", "glutathione", "vitamin-e"]},
    ]
    
    # --- Vitamins (지용성) ---
    tier1_vitamins_fat = [
        {"id": "vitamin-a", "name": "비타민A", "name_en": "Retinol", "aliases": ["레티놀", "베타카로틴", "Retinol", "Beta-carotene"], "nickname": "어둠에서 보는 힘", "category": "vitamin", "subcategory": "fat-soluble", "tags_purpose": ["눈건강", "피부", "면역"], "tags_function": ["눈 건강", "피부 건강", "면역 기능"], "tags_bodypart": ["눈", "피부"], "daily_recommended": "700-900μg RAE", "upper_limit": "3,000μg RAE/일", "mfds_functionality": "어두운 곳에서 시각 적응을 위해 필요, 피부와 점막을 형성하고 기능을 유지하는 데 필요"},
        {"id": "vitamin-d", "name": "비타민D", "name_en": "Cholecalciferol", "aliases": ["콜레칼시페롤", "비타민D3", "Vitamin D3", "Cholecalciferol"], "nickname": "햇빛이 만드는 비타민", "category": "vitamin", "subcategory": "fat-soluble", "tags_purpose": ["뼈-관절", "면역", "어린이성장"], "tags_function": ["뼈 건강", "면역 기능"], "tags_bodypart": ["뼈·관절", "전신"], "daily_recommended": "400-800IU", "upper_limit": "4,000IU/일", "mfds_functionality": "칼슘과 인이 흡수되고 이용되는 데 필요, 뼈의 형성과 유지에 필요", "related_ingredients": ["calcium", "magnesium"]},
        {"id": "vitamin-e", "name": "비타민E", "name_en": "Tocopherol", "aliases": ["토코페롤", "Tocopherol"], "nickname": "세포막의 방패", "category": "vitamin", "subcategory": "fat-soluble", "tags_purpose": ["노화방지", "피부"], "tags_function": ["항산화", "세포 보호"], "tags_bodypart": ["피부", "전신"], "daily_recommended": "11mg α-TE", "upper_limit": "540mg α-TE/일", "mfds_functionality": "항산화 작용을 하여 유해산소로부터 세포를 보호하는 데 필요", "related_ingredients": ["vitamin-c", "selenium"]},
        {"id": "vitamin-k", "name": "비타민K", "name_en": "Vitamin K", "aliases": ["비타민K1", "비타민K2", "필로퀴논", "메나퀴논", "Phylloquinone", "Menaquinone"], "nickname": "칼슘을 뼈로 보내는 교통 경찰", "category": "vitamin", "subcategory": "fat-soluble", "tags_purpose": ["뼈-관절"], "tags_function": ["뼈 건강"], "tags_bodypart": ["뼈·관절"], "daily_recommended": "70-80μg", "mfds_functionality": "정상적인 혈액 응고에 필요, 뼈의 구성에 필요"},
    ]
    
    # --- Minerals ---
    tier1_minerals = [
        {"id": "calcium", "name": "칼슘", "name_en": "Calcium", "aliases": ["Calcium", "Ca"], "nickname": "뼈의 주성분이자 신호 전달 물질", "category": "mineral", "tags_purpose": ["뼈-관절", "어린이성장", "갱년기"], "tags_function": ["뼈 건강"], "tags_bodypart": ["뼈·관절"], "daily_recommended": "700-1,000mg", "upper_limit": "2,500mg/일", "mfds_functionality": "뼈와 치아 형성에 필요, 신경과 근육 기능 유지에 필요", "related_ingredients": ["vitamin-d", "vitamin-k", "magnesium"]},
        {"id": "magnesium", "name": "마그네슘", "name_en": "Magnesium", "aliases": ["Magnesium", "Mg"], "nickname": "300개 효소의 조력자", "category": "mineral", "tags_purpose": ["수면", "스트레스", "만성피로", "뼈-관절"], "tags_function": ["신경 안정", "에너지 생성", "뼈 건강"], "tags_bodypart": ["뇌", "뼈·관절", "근육"], "daily_recommended": "315-370mg", "upper_limit": "350mg/일 (보충제)", "mfds_functionality": "에너지 이용에 필요, 신경과 근육 기능 유지에 필요"},
        {"id": "iron", "name": "철분", "name_en": "Iron", "aliases": ["철", "Iron", "Fe"], "nickname": "산소를 운반하는 택배 기사", "category": "mineral", "tags_purpose": ["만성피로", "임산부"], "tags_function": ["빈혈 예방", "에너지 생성"], "tags_bodypart": ["전신"], "daily_recommended": "10-14mg", "upper_limit": "45mg/일", "mfds_functionality": "체내 산소 운반과 혈액 생성에 필요, 에너지 생성에 필요", "related_ingredients": ["vitamin-c"]},
        {"id": "zinc", "name": "아연", "name_en": "Zinc", "aliases": ["Zinc", "Zn"], "nickname": "면역과 회복의 촉매", "category": "mineral", "tags_purpose": ["면역", "탈모", "성기능", "피부"], "tags_function": ["면역 기능", "모발 건강"], "tags_bodypart": ["피부", "모발", "전신"], "daily_recommended": "8.5-10mg", "upper_limit": "35mg/일", "mfds_functionality": "정상적인 면역 기능에 필요, 정상적인 세포 분열에 필요"},
        {"id": "selenium", "name": "셀레늄", "name_en": "Selenium", "aliases": ["셀렌", "Selenium", "Se"], "nickname": "항산화 효소의 핵심 부품", "category": "mineral", "tags_purpose": ["노화방지", "면역"], "tags_function": ["항산화", "면역 기능"], "tags_bodypart": ["전신"], "daily_recommended": "55μg", "upper_limit": "400μg/일", "mfds_functionality": "유해산소로부터 세포를 보호하는 데 필요", "related_ingredients": ["vitamin-e"]},
        {"id": "iodine", "name": "요오드", "name_en": "Iodine", "aliases": ["아이오딘", "Iodine", "I"], "nickname": "갑상선 호르몬의 원료", "category": "mineral", "tags_purpose": ["만성피로"], "tags_function": ["에너지 생성"], "tags_bodypart": ["전신"], "daily_recommended": "150μg", "upper_limit": "2,400μg/일", "mfds_functionality": "갑상선 호르몬의 합성에 필요, 에너지 생성에 필요"},
        {"id": "chromium", "name": "크롬", "name_en": "Chromium", "aliases": ["Chromium", "Cr"], "nickname": "인슐린의 보조 열쇠", "category": "mineral", "tags_purpose": ["혈압-혈당", "다이어트"], "tags_function": ["혈당 조절"], "tags_bodypart": ["전신"], "daily_recommended": "30μg", "mfds_functionality": "체내 탄수화물, 지방, 단백질 대사에 필요"},
        {"id": "copper", "name": "구리", "name_en": "Copper", "aliases": ["Copper", "Cu"], "nickname": "철분의 파트너", "category": "mineral", "tags_purpose": ["만성피로"], "tags_function": ["에너지 생성"], "tags_bodypart": ["전신"], "daily_recommended": "800μg", "upper_limit": "10,000μg/일", "mfds_functionality": "철의 운반과 이용에 필요"},
        {"id": "manganese", "name": "망간", "name_en": "Manganese", "aliases": ["Manganese", "Mn"], "nickname": "뼈와 연골의 조립 도구", "category": "mineral", "tags_purpose": ["뼈-관절"], "tags_function": ["뼈 건강"], "tags_bodypart": ["뼈·관절"], "daily_recommended": "3.5mg", "upper_limit": "11mg/일", "mfds_functionality": "뼈 형성에 필요, 에너지 이용에 필요"},
        {"id": "molybdenum", "name": "몰리브덴", "name_en": "Molybdenum", "aliases": ["Molybdenum", "Mo"], "nickname": "독소 분해 효소의 중심 금속", "category": "mineral", "tags_purpose": ["간건강"], "tags_function": ["간 건강"], "tags_bodypart": ["간"], "daily_recommended": "25μg", "upper_limit": "600μg/일", "mfds_functionality": "산화·환원 효소의 활성에 필요"},
        {"id": "potassium", "name": "칼륨", "name_en": "Potassium", "aliases": ["Potassium", "K"], "nickname": "세포의 전기 스위치", "category": "mineral", "tags_purpose": ["혈압-혈당", "운동"], "tags_function": ["혈압 조절"], "tags_bodypart": ["심장·혈관", "근육"], "daily_recommended": "3,500mg", "mfds_functionality": "체내 수분 균형에 필요"},
    ]
    
    # --- Amino Acids ---
    tier1_amino = [
        {"id": "l-arginine", "name": "L-아르기닌", "name_en": "L-Arginine", "aliases": ["아르기닌", "L-Arginine"], "nickname": "혈관을 넓히는 아미노산", "category": "amino_acid", "tags_purpose": ["운동", "성기능", "혈압-혈당"], "tags_function": ["혈행 개선"], "tags_bodypart": ["심장·혈관", "근육"], "mfds_functionality": ""},
        {"id": "l-theanine", "name": "L-테아닌", "name_en": "L-Theanine", "aliases": ["테아닌", "L-Theanine"], "nickname": "녹차가 주는 긴장 없는 집중", "category": "amino_acid", "tags_purpose": ["스트레스", "수면", "학습-수험생"], "tags_function": ["신경 안정"], "tags_bodypart": ["뇌"], "mfds_functionality": ""},
        {"id": "l-tryptophan", "name": "L-트립토판", "name_en": "L-Tryptophan", "aliases": ["트립토판", "L-Tryptophan"], "nickname": "세로토닌과 멜라토닌의 원료", "category": "amino_acid", "tags_purpose": ["수면", "스트레스"], "tags_function": ["수면 건강", "신경 안정"], "tags_bodypart": ["뇌"], "mfds_functionality": ""},
        {"id": "taurine", "name": "타우린", "name_en": "Taurine", "aliases": ["Taurine"], "nickname": "세포 보호제이자 담즙산의 파트너", "category": "amino_acid", "tags_purpose": ["만성피로", "간건강", "운동"], "tags_function": ["에너지 생성", "간 건강"], "tags_bodypart": ["간", "근육"], "mfds_functionality": ""},
        {"id": "glutathione", "name": "글루타치온", "name_en": "Glutathione", "aliases": ["글루타티온", "L-글루타치온", "GSH", "Glutathione"], "nickname": "마스터 항산화제", "category": "amino_acid", "subcategory": "tripeptide", "tags_purpose": ["노화방지", "피부", "간건강"], "tags_function": ["항산화", "세포 보호", "간 건강", "피부 건강"], "tags_bodypart": ["간", "피부", "전신"], "mfds_functionality": "", "related_ingredients": ["vitamin-c", "vitamin-b3", "selenium", "nac"]},
        {"id": "nac", "name": "NAC", "name_en": "N-Acetyl Cysteine", "aliases": ["N-아세틸시스테인", "N-Acetyl Cysteine"], "nickname": "글루타치온의 원료", "category": "amino_acid", "tags_purpose": ["간건강", "노화방지"], "tags_function": ["항산화", "간 건강"], "tags_bodypart": ["간", "전신"], "mfds_functionality": "", "related_ingredients": ["glutathione"]},
        {"id": "bcaa", "name": "BCAA", "name_en": "Branched-Chain Amino Acids", "aliases": ["분지사슬아미노산", "류신", "이소류신", "발린"], "nickname": "근육의 재료이자 피로 차단제", "category": "amino_acid", "tags_purpose": ["운동"], "tags_function": ["근력 향상"], "tags_bodypart": ["근육"], "mfds_functionality": ""},
    ]
    
    # --- Fatty Acids ---
    tier1_fatty = [
        {"id": "omega-3", "name": "오메가3", "name_en": "Omega-3", "aliases": ["EPA", "DHA", "오메가3지방산", "Omega-3 Fatty Acids"], "nickname": "뇌와 혈관의 윤활유", "category": "fatty_acid", "subcategory": "omega", "tags_purpose": ["학습-수험생", "혈압-혈당", "콜레스테롤", "눈건강"], "tags_function": ["혈행 개선", "혈중 지질 개선", "인지 기능"], "tags_bodypart": ["뇌", "심장·혈관", "눈"], "daily_recommended": "500-2,000mg (EPA+DHA)", "mfds_functionality": "혈중 중성지질 개선에 도움을 줄 수 있음, 혈행 개선에 도움을 줄 수 있음"},
        {"id": "gamma-linolenic-acid", "name": "감마리놀렌산", "name_en": "GLA", "aliases": ["GLA", "Gamma-Linolenic Acid", "달맞이꽃종자유"], "nickname": "염증 조절의 균형추", "category": "fatty_acid", "tags_purpose": ["피부", "갱년기"], "tags_function": ["피부 건강"], "tags_bodypart": ["피부"], "mfds_functionality": ""},
    ]
    
    # --- Probiotics ---
    tier1_probiotics = [
        {"id": "probiotics", "name": "프로바이오틱스", "name_en": "Probiotics", "aliases": ["유산균", "Probiotics", "Lactobacillus", "Bifidobacterium"], "nickname": "장의 생태계를 가꾸는 유익균", "category": "probiotic", "tags_purpose": ["장건강", "면역", "피부"], "tags_function": ["장 건강", "면역 기능"], "tags_bodypart": ["장"], "daily_recommended": "1억-100억 CFU", "mfds_functionality": "유익균 증식 및 유해균 억제에 도움을 줄 수 있음, 배변 활동 원활에 도움을 줄 수 있음"},
    ]
    
    # --- Key Functional Ingredients ---
    tier1_functional = [
        {"id": "lutein", "name": "루테인", "name_en": "Lutein", "aliases": ["루테인", "Lutein"], "nickname": "망막의 자연 선글라스", "category": "other_functional", "tags_purpose": ["눈건강"], "tags_function": ["눈 건강"], "tags_bodypart": ["눈"], "daily_recommended": "10-20mg", "mfds_functionality": "노화로 인해 감소될 수 있는 황반색소밀도를 유지하는 데 도움을 줄 수 있음"},
        {"id": "zeaxanthin", "name": "지아잔틴", "name_en": "Zeaxanthin", "aliases": ["제아잔틴", "Zeaxanthin"], "nickname": "루테인의 짝꿍 — 황반의 이중 방어", "category": "other_functional", "tags_purpose": ["눈건강"], "tags_function": ["눈 건강"], "tags_bodypart": ["눈"], "mfds_functionality": "노화로 인해 감소될 수 있는 황반색소밀도를 유지하는 데 도움을 줄 수 있음", "related_ingredients": ["lutein"]},
        {"id": "coq10", "name": "코엔자임Q10", "name_en": "Coenzyme Q10", "aliases": ["CoQ10", "유비퀴논", "유비퀴놀", "Ubiquinone", "Ubiquinol"], "nickname": "세포 발전소의 마지막 기어", "category": "other_functional", "tags_purpose": ["만성피로", "노화방지", "혈압-혈당"], "tags_function": ["에너지 생성", "항산화", "혈압 조절"], "tags_bodypart": ["심장·혈관", "전신"], "daily_recommended": "90-200mg", "mfds_functionality": "항산화에 도움을 줄 수 있음, 높은 혈압 감소에 도움을 줄 수 있음"},
        {"id": "collagen", "name": "콜라겐", "name_en": "Collagen", "aliases": ["콜라겐 펩타이드", "피쉬콜라겐", "Collagen Peptide"], "nickname": "피부·연골·뼈의 구조 단백질", "category": "protein", "tags_purpose": ["피부", "뼈-관절"], "tags_function": ["피부 건강", "관절 건강"], "tags_bodypart": ["피부", "뼈·관절"], "mfds_functionality": "피부 보습에 도움을 줄 수 있음"},
        {"id": "hyaluronic-acid", "name": "히알루론산", "name_en": "Hyaluronic Acid", "aliases": ["HA", "Hyaluronic Acid"], "nickname": "수분을 붙잡는 스펀지 분자", "category": "other_functional", "tags_purpose": ["피부"], "tags_function": ["피부 건강"], "tags_bodypart": ["피부"], "mfds_functionality": "피부 보습에 도움을 줄 수 있음"},
        {"id": "milk-thistle", "name": "밀크씨슬", "name_en": "Milk Thistle", "aliases": ["실리마린", "Silymarin", "Milk Thistle"], "nickname": "간세포의 방탄 조끼", "category": "extract", "tags_purpose": ["간건강", "숙취"], "tags_function": ["간 건강"], "tags_bodypart": ["간"], "mfds_functionality": "간 건강에 도움을 줄 수 있음"},
        {"id": "red-yeast-rice", "name": "홍국", "name_en": "Red Yeast Rice", "aliases": ["모나콜린K", "Monacolin K", "Red Yeast Rice"], "nickname": "쌀에서 자란 천연 스타틴", "category": "other_functional", "tags_purpose": ["콜레스테롤"], "tags_function": ["혈중 지질 개선"], "tags_bodypart": ["심장·혈관"], "mfds_functionality": "혈중 콜레스테롤 개선에 도움을 줄 수 있음"},
        {"id": "glucosamine", "name": "글루코사민", "name_en": "Glucosamine", "aliases": ["글루코사민", "Glucosamine"], "nickname": "연골의 재료이자 윤활제", "category": "other_functional", "tags_purpose": ["뼈-관절"], "tags_function": ["관절 건강"], "tags_bodypart": ["뼈·관절"], "daily_recommended": "1,500mg", "mfds_functionality": "관절 건강에 도움을 줄 수 있음"},
        {"id": "msm", "name": "MSM", "name_en": "Methylsulfonylmethane", "aliases": ["메틸설포닐메탄", "MSM", "식이유황"], "nickname": "관절과 결합조직의 유황 공급원", "category": "other_functional", "tags_purpose": ["뼈-관절"], "tags_function": ["관절 건강"], "tags_bodypart": ["뼈·관절"], "mfds_functionality": "관절 및 연골 건강에 도움을 줄 수 있음"},
        {"id": "saw-palmetto", "name": "쏘팔메토", "name_en": "Saw Palmetto", "aliases": ["쏘팔메또", "Saw Palmetto"], "nickname": "전립선 건강의 대표 원료", "category": "extract", "tags_purpose": ["성기능"], "tags_function": ["남성 건강"], "tags_bodypart": ["전신"], "mfds_functionality": "전립선 건강의 유지에 도움을 줄 수 있음"},
        {"id": "red-ginseng", "name": "홍삼", "name_en": "Red Ginseng", "aliases": ["홍삼 농축액", "진세노사이드", "Ginsenoside", "Red Ginseng"], "nickname": "한국 대표 건기식 — 면역과 피로 회복", "category": "extract", "tags_purpose": ["면역", "만성피로"], "tags_function": ["면역 기능", "에너지 생성"], "tags_bodypart": ["전신"], "mfds_functionality": "면역력 증진에 도움을 줄 수 있음, 피로 개선에 도움을 줄 수 있음"},
        {"id": "curcumin", "name": "커큐민", "name_en": "Curcumin", "aliases": ["울금", "강황추출물", "Curcumin", "Turmeric"], "nickname": "강황의 노란 항산화 성분", "category": "extract", "tags_purpose": ["간건강", "노화방지"], "tags_function": ["항산화", "간 건강"], "tags_bodypart": ["간"], "mfds_functionality": "간 건강에 도움을 줄 수 있음"},
        {"id": "melatonin", "name": "멜라토닌", "name_en": "Melatonin", "aliases": ["Melatonin"], "nickname": "수면의 스위치", "category": "other_functional", "tags_purpose": ["수면"], "tags_function": ["수면 건강"], "tags_bodypart": ["뇌"], "mfds_functionality": ""},
        {"id": "garcinia", "name": "가르시니아캄보지아", "name_en": "Garcinia Cambogia", "aliases": ["가르시니아", "HCA", "Garcinia Cambogia"], "nickname": "탄수화물이 지방으로 바뀌는 걸 차단", "category": "extract", "tags_purpose": ["다이어트"], "tags_function": ["체지방 감소", "탄수화물 흡수 억제"], "tags_bodypart": ["전신"], "mfds_functionality": "체지방 감소에 도움을 줄 수 있음"},
        {"id": "conjugated-linoleic-acid", "name": "공액리놀레산", "name_en": "CLA", "aliases": ["CLA", "Conjugated Linoleic Acid"], "nickname": "체지방 분해에 관여하는 특수 지방산", "category": "fatty_acid", "tags_purpose": ["다이어트"], "tags_function": ["체지방 감소"], "tags_bodypart": ["전신"], "mfds_functionality": "체지방 감소에 도움을 줄 수 있음"},
        {"id": "prebiotics", "name": "프리바이오틱스", "name_en": "Prebiotics", "aliases": ["프락토올리고당", "FOS", "이눌린", "Inulin", "Prebiotics"], "nickname": "유익균의 먹이", "category": "fiber", "tags_purpose": ["장건강"], "tags_function": ["장 건강", "배변 활동"], "tags_bodypart": ["장"], "mfds_functionality": "유익균 증식 및 유해균 억제에 도움을 줄 수 있음", "related_ingredients": ["probiotics"]},
        {"id": "dietary-fiber", "name": "식이섬유", "name_en": "Dietary Fiber", "aliases": ["식이섬유", "Dietary Fiber"], "nickname": "장을 쓸어내리는 빗자루", "category": "fiber", "tags_purpose": ["장건강", "다이어트", "혈압-혈당"], "tags_function": ["배변 활동", "혈당 조절"], "tags_bodypart": ["장"], "mfds_functionality": "배변 활동 원활에 도움을 줄 수 있음"},
        {"id": "isoflavone", "name": "이소플라본", "name_en": "Isoflavone", "aliases": ["이소플라본", "대두이소플라본", "Isoflavone"], "nickname": "식물성 에스트로겐 유사체", "category": "other_functional", "tags_purpose": ["갱년기", "뼈-관절"], "tags_function": ["여성 건강", "뼈 건강"], "tags_bodypart": ["뼈·관절", "전신"], "mfds_functionality": "뼈 건강에 도움을 줄 수 있음"},
        {"id": "phosphatidylserine", "name": "포스파티딜세린", "name_en": "Phosphatidylserine", "aliases": ["PS", "Phosphatidylserine"], "nickname": "뇌 세포막의 핵심 구성 성분", "category": "other_functional", "tags_purpose": ["학습-수험생", "노화방지"], "tags_function": ["인지 기능"], "tags_bodypart": ["뇌"], "mfds_functionality": ""},
        {"id": "astaxanthin", "name": "아스타잔틴", "name_en": "Astaxanthin", "aliases": ["Astaxanthin"], "nickname": "바다에서 온 초강력 항산화제", "category": "other_functional", "tags_purpose": ["노화방지", "눈건강"], "tags_function": ["항산화"], "tags_bodypart": ["눈", "전신"], "mfds_functionality": ""},
        {"id": "propolis", "name": "프로폴리스", "name_en": "Propolis", "aliases": ["프로폴리스", "Propolis"], "nickname": "벌이 만든 천연 항균 물질", "category": "other_functional", "tags_purpose": ["면역", "구강"], "tags_function": ["면역 기능", "구강 건강"], "tags_bodypart": ["전신", "구강"], "mfds_functionality": ""},
        {"id": "royal-jelly", "name": "로열젤리", "name_en": "Royal Jelly", "aliases": ["Roayl Jelly"], "nickname": "여왕벌의 식단", "category": "other_functional", "tags_purpose": ["면역", "만성피로"], "tags_function": ["면역 기능"], "tags_bodypart": ["전신"], "mfds_functionality": ""},
    ]
    
    # Combine all Tier 1
    for item in (tier1_vitamins_water + tier1_vitamins_fat + tier1_minerals + 
                 tier1_amino + tier1_fatty + tier1_probiotics + tier1_functional):
        item["tier"] = 1
        item["source_type"] = item.get("source_type", "고시형")
        item.setdefault("tags_age", ["전연령"])
        item.setdefault("tags_gender", ["공통"])
        item.setdefault("aliases", [])
        item.setdefault("related_ingredients", [])
        item.setdefault("upper_limit", "")
        item.setdefault("daily_recommended", "")
        item.setdefault("mfds_functionality", "")
        item.setdefault("subcategory", "")
        ingredients.append(item)
    
    # =========================================================================
    # TIER 2: Standard Page — Moderate interest
    # =========================================================================
    
    tier2_items = [
        # Extracts & Plant-based
        {"id": "green-tea-extract", "name": "녹차추출물", "name_en": "Green Tea Extract", "aliases": ["카테킨", "EGCG", "Green Tea Extract"], "nickname": "차 한 잔의 활성 성분을 농축한 원료", "category": "extract", "tags_purpose": ["다이어트", "노화방지"], "tags_function": ["체지방 감소", "항산화"], "tags_bodypart": ["전신"]},
        {"id": "ginkgo-biloba", "name": "은행잎추출물", "name_en": "Ginkgo Biloba", "aliases": ["징코빌로바", "Ginkgo Biloba"], "nickname": "뇌 혈류를 개선하는 오래된 나무의 잎", "category": "extract", "tags_purpose": ["학습-수험생", "노화방지"], "tags_function": ["혈행 개선", "인지 기능"], "tags_bodypart": ["뇌"]},
        {"id": "pomegranate-extract", "name": "석류추출물", "name_en": "Pomegranate Extract", "aliases": ["석류", "Pomegranate"], "nickname": "여성 건강의 대표 과일 추출물", "category": "extract", "tags_purpose": ["갱년기", "피부"], "tags_function": ["여성 건강", "항산화"], "tags_bodypart": ["전신"]},
        {"id": "bilberry-extract", "name": "빌베리추출물", "name_en": "Bilberry Extract", "aliases": ["빌베리", "Bilberry", "안토시아닌"], "nickname": "블루베리의 사촌 — 눈 건강의 보라색 원료", "category": "extract", "tags_purpose": ["눈건강"], "tags_function": ["눈 건강", "항산화"], "tags_bodypart": ["눈"]},
        {"id": "evening-primrose-oil", "name": "달맞이꽃종자유", "name_en": "Evening Primrose Oil", "aliases": ["달맞이꽃종자유", "EPO", "Evening Primrose Oil"], "nickname": "감마리놀렌산의 대표 공급원", "category": "fatty_acid", "tags_purpose": ["갱년기", "피부"], "tags_function": ["피부 건강", "여성 건강"], "tags_bodypart": ["피부"]},
        {"id": "chlorella", "name": "클로렐라", "name_en": "Chlorella", "aliases": ["Chlorella"], "nickname": "영양소를 가득 품은 단세포 녹조", "category": "other_functional", "tags_purpose": ["면역"], "tags_function": ["면역 기능"], "tags_bodypart": ["전신"]},
        {"id": "spirulina", "name": "스피룰리나", "name_en": "Spirulina", "aliases": ["Spirulina"], "nickname": "우주 식량으로도 연구된 슈퍼조류", "category": "other_functional", "tags_purpose": ["만성피로", "면역"], "tags_function": ["면역 기능"], "tags_bodypart": ["전신"]},
        {"id": "black-garlic-extract", "name": "흑마늘추출물", "name_en": "Black Garlic Extract", "aliases": ["흑마늘", "Black Garlic"], "nickname": "숙성 과정에서 항산화력이 증폭된 마늘", "category": "extract", "tags_purpose": ["면역", "만성피로"], "tags_function": ["항산화", "면역 기능"], "tags_bodypart": ["전신"]},
        {"id": "white-willow-bark", "name": "화이트윌로우바크", "name_en": "White Willow Bark", "aliases": ["서양버드나무껍질추출물"], "nickname": "아스피린의 식물 기원", "category": "extract", "tags_purpose": ["뼈-관절"], "tags_function": ["관절 건강"], "tags_bodypart": ["뼈·관절"]},
        {"id": "grape-seed-extract", "name": "포도씨추출물", "name_en": "Grape Seed Extract", "aliases": ["OPC", "프로안토시아니딘", "Grape Seed Extract"], "nickname": "포도 껍질의 항산화 폴리페놀", "category": "extract", "tags_purpose": ["노화방지", "혈압-혈당"], "tags_function": ["항산화", "혈행 개선"], "tags_bodypart": ["심장·혈관"]},
        {"id": "elderberry-extract", "name": "엘더베리추출물", "name_en": "Elderberry Extract", "aliases": ["엘더베리", "Elderberry"], "nickname": "유럽 전통 면역 보조 열매", "category": "extract", "tags_purpose": ["면역"], "tags_function": ["면역 기능"], "tags_bodypart": ["전신"]},
        {"id": "aloe-vera", "name": "알로에 전잎", "name_en": "Aloe Vera", "aliases": ["알로에", "알로에베라", "Aloe Vera"], "nickname": "장 건강의 식물 젤", "category": "extract", "tags_purpose": ["장건강", "피부"], "tags_function": ["배변 활동", "피부 건강"], "tags_bodypart": ["장", "피부"]},
        {"id": "maca", "name": "마카", "name_en": "Maca", "aliases": ["Maca", "Lepidium meyenii"], "nickname": "안데스 고원의 활력 뿌리", "category": "extract", "tags_purpose": ["성기능", "만성피로", "운동"], "tags_function": ["남성 건강", "에너지 생성"], "tags_bodypart": ["전신"]},
        {"id": "ashwagandha", "name": "아슈와간다", "name_en": "Ashwagandha", "aliases": ["위타니아솜니페라", "Ashwagandha", "Withania somnifera"], "nickname": "인도 전통 스트레스 완화 허브", "category": "extract", "tags_purpose": ["스트레스", "수면", "운동"], "tags_function": ["신경 안정", "부신 건강"], "tags_bodypart": ["뇌"]},
        {"id": "chondroitin", "name": "콘드로이틴", "name_en": "Chondroitin", "aliases": ["콘드로이틴황산", "Chondroitin Sulfate"], "nickname": "관절 연골의 쿠션 재료", "category": "other_functional", "tags_purpose": ["뼈-관절"], "tags_function": ["관절 건강"], "tags_bodypart": ["뼈·관절"]},
        {"id": "citrus-aurantium", "name": "시트러스추출물", "name_en": "Citrus Aurantium", "aliases": ["시네프린", "Synephrine", "Citrus Aurantium"], "nickname": "체지방 연소를 돕는 감귤 추출물", "category": "extract", "tags_purpose": ["다이어트"], "tags_function": ["체지방 감소"], "tags_bodypart": ["전신"]},
        {"id": "psyllium-husk", "name": "차전자피", "name_en": "Psyllium Husk", "aliases": ["차전자피식이섬유", "Psyllium Husk"], "nickname": "물을 흡수해 부풀어 오르는 식이섬유", "category": "fiber", "tags_purpose": ["장건강", "다이어트", "콜레스테롤"], "tags_function": ["배변 활동", "혈중 지질 개선"], "tags_bodypart": ["장"]},
        {"id": "boswellia", "name": "보스웰리아", "name_en": "Boswellia", "aliases": ["Boswellia", "보스웰릭산"], "nickname": "관절 건강의 유향나무 수지", "category": "extract", "tags_purpose": ["뼈-관절"], "tags_function": ["관절 건강"], "tags_bodypart": ["뼈·관절"]},
        {"id": "creatine", "name": "크레아틴", "name_en": "Creatine", "aliases": ["Creatine", "크레아틴 모노하이드레이트"], "nickname": "순간 폭발력의 즉석 에너지", "category": "amino_acid", "tags_purpose": ["운동"], "tags_function": ["근력 향상"], "tags_bodypart": ["근육"]},
        {"id": "lecithin", "name": "레시틴", "name_en": "Lecithin", "aliases": ["포스파티딜콜린", "Lecithin", "Phosphatidylcholine"], "nickname": "세포막의 지질 성분이자 유화제", "category": "other_functional", "tags_purpose": ["학습-수험생", "간건강"], "tags_function": ["인지 기능", "간 건강"], "tags_bodypart": ["뇌", "간"]},
        {"id": "vitex", "name": "카모마일추출물(체스트베리)", "name_en": "Vitex", "aliases": ["체스트베리", "비텍스", "Vitex agnus-castus"], "nickname": "여성 호르몬 균형의 전통 허브", "category": "extract", "tags_purpose": ["갱년기"], "tags_function": ["여성 건강", "호르몬 균형"], "tags_bodypart": ["전신"]},
    ]
    
    for item in tier2_items:
        item["tier"] = 2
        item["source_type"] = item.get("source_type", "부원료")
        item.setdefault("tags_age", ["전연령"])
        item.setdefault("tags_gender", ["공통"])
        item.setdefault("aliases", [])
        item.setdefault("related_ingredients", [])
        item.setdefault("upper_limit", "")
        item.setdefault("daily_recommended", "")
        item.setdefault("mfds_functionality", "")
        item.setdefault("subcategory", "")
        item.setdefault("nickname", "")
        ingredients.append(item)
    
    # =========================================================================
    # TIER 3: Brief Entry — Additives & minor ingredients
    # =========================================================================
    
    tier3_items = [
        {"id": "magnesium-stearate", "name": "스테아린산마그네슘", "name_en": "Magnesium Stearate", "nickname": "알약 제조에 사용되는 활택제", "category": "additive", "tags_purpose": [], "tags_function": []},
        {"id": "silicon-dioxide", "name": "이산화규소", "name_en": "Silicon Dioxide", "nickname": "분말이 뭉치지 않게 하는 고결방지제", "category": "additive", "tags_purpose": [], "tags_function": []},
        {"id": "hpmc", "name": "히드록시프로필메틸셀룰로스", "name_en": "HPMC", "aliases": ["HPMC", "식물성 캡슐"], "nickname": "식물 유래 캡슐 소재", "category": "additive", "tags_purpose": [], "tags_function": []},
        {"id": "gelatin", "name": "젤라틴", "name_en": "Gelatin", "nickname": "동물 유래 캡슐 소재", "category": "additive", "tags_purpose": [], "tags_function": []},
        {"id": "microcrystalline-cellulose", "name": "결정셀룰로스", "name_en": "Microcrystalline Cellulose", "aliases": ["MCC"], "nickname": "정제 형태를 유지하는 부형제", "category": "additive", "tags_purpose": [], "tags_function": []},
        {"id": "titanium-dioxide", "name": "이산화티타늄", "name_en": "Titanium Dioxide", "nickname": "정제를 하얗게 만드는 착색제", "category": "additive", "tags_purpose": [], "tags_function": []},
        {"id": "carnauba-wax", "name": "카르나우바왁스", "name_en": "Carnauba Wax", "nickname": "정제 표면의 광택 코팅제", "category": "additive", "tags_purpose": [], "tags_function": []},
        {"id": "citric-acid", "name": "구연산", "name_en": "Citric Acid", "nickname": "산도 조절과 맛 보정에 쓰이는 유기산", "category": "additive", "tags_purpose": [], "tags_function": []},
        {"id": "maltodextrin", "name": "말토덱스트린", "name_en": "Maltodextrin", "nickname": "분말 원료의 부형제이자 안정제", "category": "additive", "tags_purpose": [], "tags_function": []},
        {"id": "erythritol", "name": "에리스리톨", "name_en": "Erythritol", "nickname": "칼로리가 거의 없는 당알코올 감미료", "category": "additive", "tags_purpose": [], "tags_function": []},
        {"id": "sucralose", "name": "수크랄로스", "name_en": "Sucralose", "nickname": "설탕의 600배 단맛을 내는 인공 감미료", "category": "additive", "tags_purpose": [], "tags_function": []},
        {"id": "croscarmellose-sodium", "name": "크로스카멜로스나트륨", "name_en": "Croscarmellose Sodium", "nickname": "정제가 위장에서 빨리 풀리게 하는 붕해제", "category": "additive", "tags_purpose": [], "tags_function": []},
        {"id": "shellac", "name": "셸락", "name_en": "Shellac", "nickname": "장용 코팅에 쓰이는 천연 수지", "category": "additive", "tags_purpose": [], "tags_function": []},
        {"id": "beeswax", "name": "밀랍", "name_en": "Beeswax", "nickname": "캡슐 안정화에 쓰이는 천연 왁스", "category": "additive", "tags_purpose": [], "tags_function": []},
        {"id": "glycerin", "name": "글리세린", "name_en": "Glycerin", "nickname": "연질 캡슐의 연화제이자 보습제", "category": "additive", "tags_purpose": [], "tags_function": []},
    ]
    
    for item in tier3_items:
        item["tier"] = 3
        item["source_type"] = "식품첨가물"
        item.setdefault("tags_age", [])
        item.setdefault("tags_gender", [])
        item.setdefault("tags_bodypart", [])
        item.setdefault("aliases", [])
        item.setdefault("related_ingredients", [])
        item.setdefault("upper_limit", "")
        item.setdefault("daily_recommended", "")
        item.setdefault("mfds_functionality", "")
        item.setdefault("subcategory", "")
        item.setdefault("tags_type", [])
        ingredients.append(item)
    
    return ingredients


def generate_stats(ingredients):
    """Print statistics about the ingredient list."""
    tier_counts = {}
    category_counts = {}
    source_counts = {}
    
    for ing in ingredients:
        tier = ing["tier"]
        tier_counts[tier] = tier_counts.get(tier, 0) + 1
        
        cat = ing["category"]
        category_counts[cat] = category_counts.get(cat, 0) + 1
        
        src = ing["source_type"]
        source_counts[src] = source_counts.get(src, 0) + 1
    
    print("=" * 50)
    print("INGREDIENT MASTER LIST — STATISTICS")
    print("=" * 50)
    print(f"\nTotal ingredients: {len(ingredients)}")
    print(f"\nBy tier:")
    for t in sorted(tier_counts.keys()):
        label = {1: "Full Page", 2: "Standard", 3: "Brief"}[t]
        print(f"  Tier {t} ({label}): {tier_counts[t]}")
    print(f"\nBy category:")
    for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count}")
    print(f"\nBy source type:")
    for src, count in sorted(source_counts.items(), key=lambda x: -x[1]):
        print(f"  {src}: {count}")


if __name__ == "__main__":
    ingredients = build_master_list()
    
    # Save to JSON
    output_path = os.path.join(os.path.dirname(__file__), "..", "data", "ingredients.json")
    output_path = os.path.abspath(output_path)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(ingredients, f, ensure_ascii=False, indent=2)
    
    print(f"Saved {len(ingredients)} ingredients to {output_path}")
    generate_stats(ingredients)
    
    print(f"\n--- NOTE ---")
    print(f"This is the SEED list. It covers the most common and important ingredients.")
    print(f"To reach the target of ~550 total, expand Tier 2 (more extracts, ")
    print(f"functional foods) and Tier 3 (more additives) in subsequent batches.")
