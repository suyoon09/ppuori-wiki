#!/usr/bin/env python3
"""Expand Tier 2 & Tier 3 to complete the database."""
import json, os

NEW_T2 = [
    {"id":"turmeric-extract","name":"강황추출물","name_en":"Turmeric Extract","aliases":["강황","터메릭"],"nickname":"커큐민을 함유한 노란 뿌리","category":"extract","tags_purpose":["간건강","노화방지"],"tags_function":["항산화","간 건강"],"tags_bodypart":["간"]},
    {"id":"rhodiola","name":"홍경천추출물","name_en":"Rhodiola Rosea","aliases":["홍경천","Rhodiola"],"nickname":"고산지대 스트레스 적응 허브","category":"extract","tags_purpose":["스트레스","만성피로","운동"],"tags_function":["에너지 생성","신경 안정"],"tags_bodypart":["뇌"]},
    {"id":"valerian","name":"발레리안추출물","name_en":"Valerian Root","aliases":["쥐오줌풀","Valerian"],"nickname":"유럽 전통 수면 보조 허브","category":"extract","tags_purpose":["수면"],"tags_function":["수면 건강"],"tags_bodypart":["뇌"]},
    {"id":"passionflower","name":"패션플라워추출물","name_en":"Passionflower","aliases":["시계꽃","Passiflora"],"nickname":"불안 완화에 사용되는 남미 덩굴꽃","category":"extract","tags_purpose":["수면","스트레스"],"tags_function":["신경 안정"],"tags_bodypart":["뇌"]},
    {"id":"lemon-balm","name":"레몬밤추출물","name_en":"Lemon Balm","aliases":["레몬밤","Melissa officinalis"],"nickname":"레몬 향이 나는 긴장 완화 허브","category":"extract","tags_purpose":["스트레스","수면"],"tags_function":["신경 안정"],"tags_bodypart":["뇌"]},
    {"id":"st-johns-wort","name":"세인트존스워트","name_en":"St. John's Wort","aliases":["St. John's Wort","서양고추나물"],"nickname":"가벼운 우울감에 사용되는 유럽 허브","category":"extract","tags_purpose":["스트레스"],"tags_function":["신경 안정"],"tags_bodypart":["뇌"]},
    {"id":"bacopa","name":"바코파추출물","name_en":"Bacopa Monnieri","aliases":["바코파","Bacopa"],"nickname":"인도 전통 기억력 허브","category":"extract","tags_purpose":["학습-수험생"],"tags_function":["인지 기능"],"tags_bodypart":["뇌"]},
    {"id":"gotu-kola","name":"고투콜라","name_en":"Gotu Kola","aliases":["센텔라아시아티카","Centella asiatica","시카"],"nickname":"CICA — 피부 재생과 인지에 사용되는 식물","category":"extract","tags_purpose":["피부","학습-수험생"],"tags_function":["피부 건강","인지 기능"],"tags_bodypart":["피부","뇌"]},
    {"id":"echinacea","name":"에키네시아","name_en":"Echinacea","aliases":["Echinacea"],"nickname":"북미 원주민의 면역 부스트 허브","category":"extract","tags_purpose":["면역"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"astragalus","name":"황기추출물","name_en":"Astragalus","aliases":["황기","Astragalus"],"nickname":"한방 면역 보조의 대표 원료","category":"extract","tags_purpose":["면역","만성피로"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"cat-claw","name":"캣츠클로","name_en":"Cat's Claw","aliases":["Cat's Claw","Uncaria tomentosa"],"nickname":"아마존의 면역 조절 덩굴","category":"extract","tags_purpose":["면역","뼈-관절"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"elderflower","name":"엘더플라워","name_en":"Elderflower","aliases":["Elderflower"],"nickname":"엘더베리 꽃의 호흡기 건강 원료","category":"extract","tags_purpose":["면역"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"black-cohosh","name":"블랙코호시","name_en":"Black Cohosh","aliases":["Cimicifuga","승마"],"nickname":"갱년기 증상 완화의 서양 허브","category":"extract","tags_purpose":["갱년기"],"tags_function":["여성 건강"],"tags_bodypart":["전신"]},
    {"id":"dong-quai","name":"중국당귀","name_en":"Dong Quai","aliases":["Angelica sinensis","중국당귀"],"nickname":"한/중의학 공통 여성 건강 원료","category":"extract","tags_purpose":["갱년기"],"tags_function":["여성 건강","혈행 개선"],"tags_bodypart":["전신"]},
    {"id":"wild-yam","name":"야생참마추출물","name_en":"Wild Yam","aliases":["Wild Yam","Dioscorea"],"nickname":"디오스게닌 함유 갱년기 원료","category":"extract","tags_purpose":["갱년기"],"tags_function":["여성 건강"],"tags_bodypart":["전신"]},
    {"id":"dandelion-root","name":"민들레추출물","name_en":"Dandelion Root","aliases":["민들레","Taraxacum"],"nickname":"이뇨와 간 건강에 전통적으로 사용된 뿌리","category":"extract","tags_purpose":["간건강"],"tags_function":["간 건강"],"tags_bodypart":["간"]},
    {"id":"burdock-root","name":"우엉추출물","name_en":"Burdock Root","aliases":["우엉","Arctium lappa"],"nickname":"혈액 정화에 사용된 전통 뿌리 채소","category":"extract","tags_purpose":["피부","간건강"],"tags_function":["항산화"],"tags_bodypart":["피부","간"]},
    {"id":"nettle","name":"쐐기풀추출물","name_en":"Nettle","aliases":["쐐기풀","Urtica dioica"],"nickname":"전립선과 알레르기에 연구된 유럽 허브","category":"extract","tags_purpose":["성기능"],"tags_function":["남성 건강"],"tags_bodypart":["전신"]},
    {"id":"hawthorn","name":"산사나무추출물","name_en":"Hawthorn","aliases":["산사","Crataegus"],"nickname":"심장 건강에 사용된 유럽 전통 열매","category":"extract","tags_purpose":["혈압-혈당"],"tags_function":["혈행 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"garlic-extract","name":"마늘추출물","name_en":"Garlic Extract","aliases":["마늘","알리신","Allicin"],"nickname":"혈압과 콜레스테롤 관리의 대중 원료","category":"extract","tags_purpose":["혈압-혈당","콜레스테롤","면역"],"tags_function":["혈행 개선","혈중 지질 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"bitter-melon","name":"여주추출물","name_en":"Bitter Melon","aliases":["여주","고과","Momordica charantia"],"nickname":"혈당 관리의 아시아 채소","category":"extract","tags_purpose":["혈압-혈당"],"tags_function":["혈당 조절"],"tags_bodypart":["전신"]},
    {"id":"mulberry-leaf","name":"뽕잎추출물","name_en":"Mulberry Leaf","aliases":["뽕잎","상엽","DNJ"],"nickname":"당 흡수를 억제하는 뽕나무 잎","category":"extract","tags_purpose":["혈압-혈당","다이어트"],"tags_function":["혈당 조절","탄수화물 흡수 억제"],"tags_bodypart":["전신"]},
    {"id":"white-kidney-bean","name":"흰강낭콩추출물","name_en":"White Kidney Bean Extract","aliases":["흰강낭콩","파세올라민","Phaseolamin"],"nickname":"탄수화물 소화효소를 억제하는 콩 추출물","category":"extract","tags_purpose":["다이어트"],"tags_function":["탄수화물 흡수 억제"],"tags_bodypart":["전신"]},
    {"id":"green-coffee-bean","name":"녹색커피빈추출물","name_en":"Green Coffee Bean Extract","aliases":["그린커피빈"],"nickname":"로스팅 전 커피콩의 클로로겐산","category":"extract","tags_purpose":["다이어트"],"tags_function":["체지방 감소"],"tags_bodypart":["전신"]},
    {"id":"caralluma","name":"카랄루마","name_en":"Caralluma Fimbriata","aliases":["Caralluma"],"nickname":"식욕 억제에 연구된 인도 선인장","category":"extract","tags_purpose":["다이어트"],"tags_function":["체지방 감소"],"tags_bodypart":["전신"]},
    {"id":"fucoxanthin","name":"후코잔틴","name_en":"Fucoxanthin","aliases":["Fucoxanthin"],"nickname":"해조류의 갈색 색소 — 체지방 연구 성분","category":"other_functional","tags_purpose":["다이어트"],"tags_function":["체지방 감소"],"tags_bodypart":["전신"]},
    {"id":"acai-berry","name":"아사이베리","name_en":"Acai Berry","aliases":["아사이","Acai"],"nickname":"아마존의 고항산화 보라색 열매","category":"extract","tags_purpose":["노화방지"],"tags_function":["항산화"],"tags_bodypart":["전신"]},
    {"id":"mangosteen","name":"망고스틴추출물","name_en":"Mangosteen","aliases":["망고스틴","잔톤"],"nickname":"과일의 여왕 — 잔톤 함유 항산화 원료","category":"extract","tags_purpose":["노화방지"],"tags_function":["항산화"],"tags_bodypart":["전신"]},
    {"id":"noni","name":"노니추출물","name_en":"Noni","aliases":["노니","Morinda citrifolia"],"nickname":"남태평양 전통 건강 과일","category":"extract","tags_purpose":["면역"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"moringa","name":"모링가","name_en":"Moringa","aliases":["Moringa oleifera"],"nickname":"영양소 밀도가 높은 열대 나무 잎","category":"extract","tags_purpose":["만성피로","면역"],"tags_function":["항산화"],"tags_bodypart":["전신"]},
    {"id":"pine-nut-oil","name":"잣기름","name_en":"Pine Nut Oil","aliases":["잣","Pine Nut Oil"],"nickname":"식욕 조절에 연구된 한국의 견과류 기름","category":"fatty_acid","tags_purpose":["다이어트"],"tags_function":["체지방 감소"],"tags_bodypart":["전신"]},
    {"id":"perilla-oil","name":"들기름","name_en":"Perilla Oil","aliases":["들깨기름","Perilla Oil","알파리놀렌산"],"nickname":"식물성 오메가3(ALA)가 풍부한 국산 기름","category":"fatty_acid","tags_purpose":["혈압-혈당","콜레스테롤"],"tags_function":["혈중 지질 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"krill-oil","name":"크릴오일","name_en":"Krill Oil","aliases":["크릴오일","Krill Oil"],"nickname":"인지질 결합형 오메가3","category":"fatty_acid","tags_purpose":["혈압-혈당","콜레스테롤"],"tags_function":["혈중 지질 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"flaxseed-oil","name":"아마씨오일","name_en":"Flaxseed Oil","aliases":["아마씨","아마인유","Flaxseed"],"nickname":"식물성 오메가3의 대표 오일","category":"fatty_acid","tags_purpose":["혈압-혈당"],"tags_function":["혈중 지질 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"borage-oil","name":"보라지오일","name_en":"Borage Oil","aliases":["Borage Oil"],"nickname":"GLA 함량이 가장 높은 식물성 오일","category":"fatty_acid","tags_purpose":["피부","갱년기"],"tags_function":["피부 건강"],"tags_bodypart":["피부"]},
    {"id":"vitamin-d2","name":"비타민D2","name_en":"Ergocalciferol","aliases":["에르고칼시페롤","비건비타민D"],"nickname":"식물 유래 비타민D","category":"vitamin","subcategory":"fat-soluble","tags_purpose":["뼈-관절","면역"],"tags_function":["뼈 건강"],"tags_bodypart":["뼈·관절"]},
    {"id":"methylcobalamin","name":"메틸코발라민","name_en":"Methylcobalamin","aliases":["활성형 B12"],"nickname":"신경 조직에 직접 사용 가능한 B12 형태","category":"vitamin","subcategory":"b-complex","tags_purpose":["만성피로"],"tags_function":["에너지 생성"],"tags_bodypart":["뇌"]},
    {"id":"k2-mk7","name":"비타민K2(MK-7)","name_en":"Menaquinone-7","aliases":["MK-7","메나퀴논-7"],"nickname":"칼슘을 동맥이 아닌 뼈로 보내는 K2 형태","category":"vitamin","subcategory":"fat-soluble","tags_purpose":["뼈-관절"],"tags_function":["뼈 건강"],"tags_bodypart":["뼈·관절"]},
    {"id":"magnesium-glycinate","name":"마그네슘글리시네이트","name_en":"Magnesium Glycinate","aliases":["마그네슘 글리시네이트"],"nickname":"흡수율이 높고 위장 부담이 적은 마그네슘","category":"mineral","tags_purpose":["수면","스트레스"],"tags_function":["신경 안정"],"tags_bodypart":["뇌","근육"]},
    {"id":"magnesium-threonate","name":"마그네슘트레오네이트","name_en":"Magnesium Threonate","aliases":["마그네슘 L-트레오네이트","Magtein"],"nickname":"뇌혈관장벽을 통과하는 마그네슘 형태","category":"mineral","tags_purpose":["학습-수험생","수면"],"tags_function":["인지 기능"],"tags_bodypart":["뇌"]},
    {"id":"zinc-picolinate","name":"아연피콜리네이트","name_en":"Zinc Picolinate","aliases":["아연 피콜리네이트"],"nickname":"흡수율이 높은 아연의 킬레이트 형태","category":"mineral","tags_purpose":["면역","탈모"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"iron-bisglycinate","name":"철분 비스글리시네이트","name_en":"Iron Bisglycinate","aliases":["킬레이트 철분"],"nickname":"변비 부작용이 적은 고흡수율 철분","category":"mineral","tags_purpose":["만성피로","임산부"],"tags_function":["빈혈 예방"],"tags_bodypart":["전신"]},
    {"id":"calcium-citrate","name":"구연산칼슘","name_en":"Calcium Citrate","aliases":["칼슘시트레이트"],"nickname":"공복에도 흡수가 잘 되는 칼슘 형태","category":"mineral","tags_purpose":["뼈-관절"],"tags_function":["뼈 건강"],"tags_bodypart":["뼈·관절"]},
    {"id":"d-mannose","name":"D-만노스","name_en":"D-Mannose","aliases":["D-Mannose"],"nickname":"요로 건강에 사용되는 단당류","category":"other_functional","tags_purpose":["면역"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"diindolylmethane","name":"DIM","name_en":"Diindolylmethane","aliases":["DIM","인돌-3-카비놀"],"nickname":"십자화과 채소의 에스트로겐 대사 성분","category":"other_functional","tags_purpose":["갱년기"],"tags_function":["여성 건강","호르몬 균형"],"tags_bodypart":["전신"]},
    {"id":"s-adenosylmethionine","name":"SAMe","name_en":"S-Adenosylmethionine","aliases":["SAMe"],"nickname":"메틸화 반응의 핵심 기질","category":"amino_acid","tags_purpose":["간건강","스트레스","뼈-관절"],"tags_function":["간 건강","신경 안정"],"tags_bodypart":["간","뇌"]},
    {"id":"5-htp","name":"5-HTP","name_en":"5-Hydroxytryptophan","aliases":["5-하이드록시트립토판"],"nickname":"세로토닌 직전 단계의 전구체","category":"amino_acid","tags_purpose":["수면","스트레스"],"tags_function":["수면 건강","신경 안정"],"tags_bodypart":["뇌"]},
    {"id":"beta-alanine","name":"베타알라닌","name_en":"Beta-Alanine","aliases":["Beta-Alanine"],"nickname":"근육 버퍼 카르노신의 원료","category":"amino_acid","tags_purpose":["운동"],"tags_function":["근력 향상"],"tags_bodypart":["근육"]},
    {"id":"hmb","name":"HMB","name_en":"Beta-Hydroxy Beta-Methylbutyrate","aliases":["HMB"],"nickname":"류신 대사물 — 근육 분해 억제","category":"amino_acid","tags_purpose":["운동"],"tags_function":["근력 향상"],"tags_bodypart":["근육"]},
    {"id":"citicoline","name":"시티콜린","name_en":"Citicoline","aliases":["CDP-Choline","시티콜린"],"nickname":"뇌 세포막 합성의 원료","category":"other_functional","tags_purpose":["학습-수험생"],"tags_function":["인지 기능"],"tags_bodypart":["뇌"]},
    {"id":"pqq","name":"PQQ","name_en":"Pyrroloquinoline Quinone","aliases":["피롤로퀴놀린퀴논"],"nickname":"새로운 미토콘드리아 생성을 자극하는 성분","category":"other_functional","tags_purpose":["노화방지","만성피로"],"tags_function":["에너지 생성","항산화"],"tags_bodypart":["전신"]},
    {"id":"nmn","name":"NMN","name_en":"Nicotinamide Mononucleotide","aliases":["니코틴아미드모노뉴클레오타이드"],"nickname":"NAD+ 전구체 — 세포 노화 연구의 핫 이슈","category":"other_functional","tags_purpose":["노화방지"],"tags_function":["세포 보호"],"tags_bodypart":["전신"]},
    {"id":"nr","name":"NR","name_en":"Nicotinamide Riboside","aliases":["니코틴아미드리보사이드","Niagen"],"nickname":"NMN과 경쟁하는 또 다른 NAD+ 전구체","category":"other_functional","tags_purpose":["노화방지"],"tags_function":["세포 보호"],"tags_bodypart":["전신"]},
    {"id":"spermidine","name":"스퍼미딘","name_en":"Spermidine","aliases":["Spermidine"],"nickname":"세포 자가포식(오토파지) 유도 물질","category":"other_functional","tags_purpose":["노화방지"],"tags_function":["세포 보호"],"tags_bodypart":["전신"]},
    {"id":"sulforaphane","name":"설포라판","name_en":"Sulforaphane","aliases":["브로콜리추출물","Sulforaphane"],"nickname":"브로콜리 새싹의 해독 효소 활성화 성분","category":"extract","tags_purpose":["노화방지","간건강"],"tags_function":["항산화","간 건강"],"tags_bodypart":["간","전신"]},
    {"id":"dim-sum-extract","name":"흑미추출물","name_en":"Black Rice Extract","aliases":["흑미","안토시아닌"],"nickname":"항산화 안토시아닌이 풍부한 유색미","category":"extract","tags_purpose":["노화방지"],"tags_function":["항산화"],"tags_bodypart":["전신"]},
    {"id":"colostrum","name":"초유","name_en":"Colostrum","aliases":["Colostrum","소초유"],"nickname":"출산 직후 분비되는 면역 인자 농축 유즙","category":"protein","tags_purpose":["면역","장건강"],"tags_function":["면역 기능","장 건강"],"tags_bodypart":["장","전신"]},
    {"id":"silk-peptide","name":"실크펩타이드","name_en":"Silk Peptide","aliases":["실크아미노산","Silk Peptide"],"nickname":"누에고치에서 추출한 아미노산 복합체","category":"protein","tags_purpose":["피부"],"tags_function":["피부 건강"],"tags_bodypart":["피부"]},
    {"id":"marine-collagen","name":"해양콜라겐","name_en":"Marine Collagen","aliases":["피쉬콜라겐","Fish Collagen"],"nickname":"어류 유래 저분자 콜라겐","category":"protein","tags_purpose":["피부","뼈-관절"],"tags_function":["피부 건강"],"tags_bodypart":["피부"]},
]

NEW_T3 = [
    {"id":"polyvinylpyrrolidone","name":"폴리비닐피롤리돈","name_en":"PVP","aliases":["PVP","포비돈"],"nickname":"정제의 결합제"},
    {"id":"povidone","name":"포비돈","name_en":"Povidone","aliases":["Povidone K30"],"nickname":"분말의 결합 보조제"},
    {"id":"talc","name":"탈크","name_en":"Talc","aliases":["활석"],"nickname":"정제 코팅에 사용되는 광물 분말"},
    {"id":"calcium-carbonate","name":"탄산칼슘","name_en":"Calcium Carbonate","aliases":["탄산칼슘"],"nickname":"정제 부형제이자 칼슘 공급원"},
    {"id":"dicalcium-phosphate","name":"제이인산칼슘","name_en":"Dicalcium Phosphate","aliases":["DCP"],"nickname":"정제의 충전제와 칼슘·인 공급"},
    {"id":"hydroxypropyl-cellulose","name":"히드록시프로필셀룰로스","name_en":"HPC","aliases":["HPC"],"nickname":"필름 코팅과 결합에 쓰이는 셀룰로스 유도체"},
    {"id":"sodium-starch-glycolate","name":"전분글리콜산나트륨","name_en":"Sodium Starch Glycolate","aliases":["SSG"],"nickname":"정제 붕해를 촉진하는 팽윤제"},
    {"id":"pregelatinized-starch","name":"알파전분","name_en":"Pregelatinized Starch","aliases":["알파화전분"],"nickname":"냉수에 풀리는 변성 전분 — 결합제 역할"},
    {"id":"lactose","name":"유당","name_en":"Lactose","aliases":["Lactose"],"nickname":"정제의 전통적 충전제 — 유당불내증 주의"},
    {"id":"sucrose","name":"자당","name_en":"Sucrose","aliases":["설탕"],"nickname":"당의정 코팅에 사용되는 감미료"},
    {"id":"xylitol","name":"자일리톨","name_en":"Xylitol","aliases":["자일리톨"],"nickname":"충치 예방 효과가 있는 당알코올"},
    {"id":"sorbitol","name":"소르비톨","name_en":"Sorbitol","aliases":["Sorbitol"],"nickname":"습기 조절과 감미에 사용되는 당알코올"},
    {"id":"mannitol","name":"만니톨","name_en":"Mannitol","aliases":["Mannitol"],"nickname":"씹어 먹는 정제의 냉감 감미료"},
    {"id":"stevia","name":"스테비아","name_en":"Stevia","aliases":["스테비올배당체"],"nickname":"설탕의 200배 단맛을 내는 천연 감미료"},
    {"id":"acesulfame-k","name":"아세설팜칼륨","name_en":"Acesulfame K","aliases":["아세설팜K"],"nickname":"열에 안정적인 제로칼로리 인공 감미료"},
    {"id":"aspartame","name":"아스파탐","name_en":"Aspartame","aliases":["Aspartame"],"nickname":"아미노산 기반 인공 감미료"},
    {"id":"polydextrose","name":"폴리덱스트로스","name_en":"Polydextrose","aliases":["Polydextrose"],"nickname":"식이섬유 기능도 하는 수용성 충전제"},
    {"id":"medium-chain-triglyceride","name":"중쇄지방산트리글리세라이드","name_en":"MCT (additive)","aliases":["MCT"],"nickname":"캡슐 내용물의 용매 역할"},
    {"id":"soybean-oil","name":"대두유","name_en":"Soybean Oil","aliases":["대두유"],"nickname":"연질 캡슐의 기저 오일"},
    {"id":"sunflower-oil","name":"해바라기유","name_en":"Sunflower Oil","aliases":["해바라기유"],"nickname":"캡슐 내 용매 또는 안정화 오일"},
    {"id":"palm-oil","name":"팜유","name_en":"Palm Oil","aliases":["팜유"],"nickname":"지용성 비타민의 캡슐화 기저 오일"},
    {"id":"yellow-beeswax","name":"황색밀랍","name_en":"Yellow Beeswax","aliases":["황밀랍"],"nickname":"연질 캡슐의 안정화 왁스"},
    {"id":"mixed-tocopherol","name":"혼합토코페롤","name_en":"Mixed Tocopherols","aliases":["혼합토코페롤"],"nickname":"오일 산화 방지를 위한 천연 항산화제"},
    {"id":"rosemary-extract-preserv","name":"로즈마리추출물(보존)","name_en":"Rosemary Extract (preservative)","aliases":["로즈마리추출물"],"nickname":"천연 보존 및 항산화 목적의 허브 추출물"},
    {"id":"annatto","name":"아나토색소","name_en":"Annatto","aliases":["아나토"],"nickname":"캡슐에 주황색을 부여하는 천연 색소"},
    {"id":"chlorophyllin","name":"클로로필린","name_en":"Chlorophyllin","aliases":["동클로로필린"],"nickname":"녹색 정제의 천연 색소"},
    {"id":"caramel-color","name":"캐러멜색소","name_en":"Caramel Color","aliases":["카라멜색소"],"nickname":"갈색 정제의 착색에 사용"},
    {"id":"riboflavin-color","name":"리보플라빈(색소)","name_en":"Riboflavin (colorant)","aliases":["비타민B2 색소"],"nickname":"정제에 노란색을 부여하는 비타민 색소"},
    {"id":"iron-oxide-red","name":"산화철(적)","name_en":"Iron Oxide Red","aliases":["적색산화철"],"nickname":"적갈색 정제 코팅의 무기 색소"},
    {"id":"iron-oxide-yellow","name":"산화철(황)","name_en":"Iron Oxide Yellow","aliases":["황색산화철"],"nickname":"황색 정제 코팅의 무기 색소"},
    {"id":"iron-oxide-black","name":"산화철(흑)","name_en":"Iron Oxide Black","aliases":["흑색산화철"],"nickname":"흑색 인쇄 잉크의 무기 색소"},
    {"id":"sodium-carboxymethylcellulose","name":"카르복시메틸셀룰로스나트륨","name_en":"CMC-Na","aliases":["CMC"],"nickname":"점도 조절과 안정화에 사용되는 셀룰로스"},
    {"id":"guar-gum","name":"구아검","name_en":"Guar Gum","aliases":["Guar Gum"],"nickname":"점도 증가와 안정화에 쓰이는 식물성 검"},
    {"id":"xanthan-gum","name":"잔탄검","name_en":"Xanthan Gum","aliases":["Xanthan Gum"],"nickname":"액상 건기식의 점도 안정제"},
    {"id":"locust-bean-gum","name":"로커스트빈검","name_en":"Locust Bean Gum","aliases":["캐럽검"],"nickname":"젤리형 건기식의 겔화 보조제"},
    {"id":"pectin","name":"펙틴","name_en":"Pectin","aliases":["Pectin"],"nickname":"젤리 비타민의 겔화제"},
    {"id":"agar","name":"한천","name_en":"Agar","aliases":["Agar"],"nickname":"해조류 유래 천연 겔화제"},
    {"id":"stearic-acid","name":"스테아린산","name_en":"Stearic Acid","aliases":["Stearic Acid"],"nickname":"정제 제조의 활택제 원료 지방산"},
    {"id":"ascorbyl-palmitate","name":"아스코르빌팔미테이트","name_en":"Ascorbyl Palmitate","aliases":["아스코빌팔미테이트"],"nickname":"지용성 비타민C 유도체 — 항산화 보존 목적"},
    {"id":"dl-alpha-tocopheryl-acetate","name":"dl-알파토코페릴아세테이트","name_en":"dl-Alpha-Tocopheryl Acetate","aliases":["합성 비타민E"],"nickname":"비타민E 안정화 형태 — 보존 목적"},
    {"id":"sodium-benzoate","name":"안식향산나트륨","name_en":"Sodium Benzoate","aliases":["안식향산나트륨"],"nickname":"액상 건기식의 보존료"},
    {"id":"potassium-sorbate","name":"소르빈산칼륨","name_en":"Potassium Sorbate","aliases":["소르빈산칼륨"],"nickname":"액상 제품의 곰팡이 억제 보존료"},
    {"id":"malic-acid","name":"사과산","name_en":"Malic Acid","aliases":["Malic Acid"],"nickname":"신맛 부여 및 산도 조절 유기산"},
    {"id":"tartaric-acid","name":"주석산","name_en":"Tartaric Acid","aliases":["Tartaric Acid"],"nickname":"포도 유래 산도 조절제"},
    {"id":"silicon-dioxide-colloidal","name":"콜로이달실리카","name_en":"Colloidal Silicon Dioxide","aliases":["콜로이드성이산화규소"],"nickname":"미세 입자의 고결방지 및 흐름성 개선"},
    {"id":"triethyl-citrate","name":"구연산트리에틸","name_en":"Triethyl Citrate","aliases":["TEC"],"nickname":"필름 코팅의 가소제"},
    {"id":"polyethylene-glycol","name":"폴리에틸렌글리콜","name_en":"PEG","aliases":["PEG","폴리에틸렌글리콜"],"nickname":"필름 코팅의 가소제 및 용매"},
    {"id":"medium-chain-triglyceride-filler","name":"MCT(부형제)","name_en":"MCT (filler)","aliases":["MCT 부형제"],"nickname":"분말 원료의 희석 및 캡슐 충전용"},
]

def main():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "ingredients.json")
    path = os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as f:
        existing = json.load(f)
    existing_ids = {i["id"] for i in existing}
    added_t2 = added_t3 = 0

    for item in NEW_T2:
        if item["id"] in existing_ids: continue
        item["tier"] = 2
        item["source_type"] = item.get("source_type", "부원료")
        for k in ["tags_age","tags_gender","aliases","related_ingredients"]:
            item.setdefault(k, ["전연령"] if k=="tags_age" else ["공통"] if k=="tags_gender" else [])
        for k in ["upper_limit","daily_recommended","mfds_functionality","subcategory","nickname","name_en","tags_bodypart"]:
            item.setdefault(k, [] if k=="tags_bodypart" else "")
        existing.append(item); added_t2 += 1; existing_ids.add(item["id"])

    for item in NEW_T3:
        if item["id"] in existing_ids: continue
        item["tier"] = 3; item["source_type"] = "식품첨가물"; item["category"] = "additive"
        for k in ["tags_purpose","tags_function","tags_bodypart","tags_age","tags_gender","aliases","related_ingredients"]:
            item.setdefault(k, [])
        for k in ["upper_limit","daily_recommended","mfds_functionality","subcategory","name_en"]:
            item.setdefault(k, "")
        existing.append(item); added_t3 += 1; existing_ids.add(item["id"])

    with open(path, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)

    counts = {}
    for i in existing: counts[i["tier"]] = counts.get(i["tier"], 0) + 1
    print(f"Added {added_t2} T2, {added_t3} T3.")
    for t in sorted(counts): print(f"  Tier {t}: {counts[t]}")
    print(f"  GRAND TOTAL: {len(existing)}")

if __name__ == "__main__":
    main()
