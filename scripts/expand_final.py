#!/usr/bin/env python3
"""Final expansion — fill remaining gaps to reach ~550 total."""
import json, os

# More Tier 1 to reach ~150
MORE_T1 = [
    {"id":"vitamin-a-beta-carotene","name":"베타카로틴","name_en":"Beta-Carotene","aliases":["프로비타민A"],"nickname":"체내에서 비타민A로 전환되는 식물 색소","category":"vitamin","tags_purpose":["눈건강","피부","면역"],"tags_function":["눈 건강","항산화"],"tags_bodypart":["눈","피부"]},
    {"id":"folate-5mthf","name":"활성엽산","name_en":"5-MTHF","aliases":["메틸폴레이트","5-MTHF","Methylfolate"],"nickname":"체내 전환 없이 바로 쓰이는 엽산 형태","category":"vitamin","tags_purpose":["임산부"],"tags_function":["태아 발달"],"tags_bodypart":["전신"]},
    {"id":"thiamine-benfotiamine","name":"벤포티아민","name_en":"Benfotiamine","aliases":["벤포티아민"],"nickname":"지용성으로 개량한 고흡수 비타민B1","category":"vitamin","tags_purpose":["혈압-혈당","만성피로"],"tags_function":["에너지 생성"],"tags_bodypart":["전신"]},
    {"id":"ubiquinol","name":"유비퀴놀","name_en":"Ubiquinol","aliases":["환원형 CoQ10"],"nickname":"CoQ10의 환원(활성) 형태","category":"other_functional","tags_purpose":["만성피로","노화방지"],"tags_function":["에너지 생성","항산화"],"tags_bodypart":["심장·혈관"]},
    {"id":"vitamin-c-liposomal","name":"리포좀 비타민C","name_en":"Liposomal Vitamin C","aliases":["리포소말 비타민C"],"nickname":"지질막에 감싸 흡수율을 높인 비타민C","category":"vitamin","tags_purpose":["면역","피부"],"tags_function":["항산화","면역 기능"],"tags_bodypart":["전신"]},
    {"id":"methylsulfonylmethane-msm","name":"MSM(관절)","name_en":"MSM","aliases":["유기유황"],"nickname":"관절과 결합조직의 유황 공급원 (식약처 인정)","category":"other_functional","tags_purpose":["뼈-관절"],"tags_function":["관절 건강"],"tags_bodypart":["뼈·관절"],"mfds_functionality":"관절 및 연골 건강에 도움을 줄 수 있음"},
    {"id":"galactooligosaccharide","name":"갈락토올리고당","name_en":"GOS","aliases":["GOS","갈락토올리고당"],"nickname":"모유에도 있는 프리바이오틱 올리고당","category":"fiber","tags_purpose":["장건강","어린이성장"],"tags_function":["장 건강"],"tags_bodypart":["장"]},
    {"id":"xylooligosaccharide","name":"자일로올리고당","name_en":"XOS","aliases":["XOS"],"nickname":"옥수수속대에서 유래한 프리바이오틱","category":"fiber","tags_purpose":["장건강"],"tags_function":["장 건강","배변 활동"],"tags_bodypart":["장"]},
    {"id":"heme-iron","name":"헴철","name_en":"Heme Iron","aliases":["Heme Iron"],"nickname":"동물성 식품에 있는 고흡수 철분 형태","category":"mineral","tags_purpose":["만성피로","임산부"],"tags_function":["빈혈 예방"],"tags_bodypart":["전신"]},
    {"id":"gamma-aminobutyric-acid","name":"가바","name_en":"GABA","aliases":["GABA","감마아미노뷰티르산"],"nickname":"뇌의 브레이크 역할을 하는 억제성 신경전달물질","category":"amino_acid","tags_purpose":["수면","스트레스"],"tags_function":["신경 안정","수면 건강"],"tags_bodypart":["뇌"],"mfds_functionality":""},
    {"id":"chondroitin-sulfate","name":"콘드로이틴황산나트륨","name_en":"Chondroitin Sulfate Sodium","aliases":["CS"],"nickname":"관절 연골의 수분을 유지하는 GAG","category":"other_functional","tags_purpose":["뼈-관절"],"tags_function":["관절 건강"],"tags_bodypart":["뼈·관절"],"mfds_functionality":"관절 및 연골 건강에 도움을 줄 수 있음"},
    {"id":"evening-primrose-gla","name":"감마리놀렌산(GLA)","name_en":"GLA","aliases":["감마리놀렌산"],"nickname":"피부 장벽과 여성 건강의 오메가6","category":"fatty_acid","tags_purpose":["피부","갱년기"],"tags_function":["피부 건강"],"tags_bodypart":["피부"]},
    {"id":"lycopene","name":"리코펜","name_en":"Lycopene","aliases":["Lycopene","라이코펜"],"nickname":"토마토의 붉은 항산화 색소","category":"other_functional","tags_purpose":["노화방지","성기능"],"tags_function":["항산화"],"tags_bodypart":["전신"]},
    {"id":"bromelain","name":"브로멜라인","name_en":"Bromelain","aliases":["Bromelain"],"nickname":"파인애플 유래 단백질 분해 효소","category":"enzyme","tags_purpose":["장건강","뼈-관절"],"tags_function":["장 건강"],"tags_bodypart":["장"]},
    {"id":"papain","name":"파파인","name_en":"Papain","aliases":["Papain"],"nickname":"파파야 유래 소화 효소","category":"enzyme","tags_purpose":["장건강"],"tags_function":["장 건강"],"tags_bodypart":["장"]},
    {"id":"saccharomyces-cerevisiae","name":"맥주효모","name_en":"Brewer's Yeast","aliases":["맥주효모","Saccharomyces cerevisiae"],"nickname":"B비타민과 단백질이 풍부한 효모","category":"other_functional","tags_purpose":["만성피로","탈모"],"tags_function":["에너지 생성","모발 건강"],"tags_bodypart":["모발","전신"]},
    {"id":"copper-gluconate","name":"글루콘산구리","name_en":"Copper Gluconate","aliases":["구리 글루코네이트"],"nickname":"흡수율이 높은 구리의 킬레이트 형태","category":"mineral","tags_purpose":["만성피로","탈모"],"tags_function":["에너지 생성"],"tags_bodypart":["전신","모발"]},
    {"id":"zinc-gluconate","name":"글루콘산아연","name_en":"Zinc Gluconate","aliases":["아연 글루코네이트"],"nickname":"일반적인 아연 보충 형태","category":"mineral","tags_purpose":["면역","피부"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"coenzyme-q10-ubiquinone","name":"산화형 CoQ10","name_en":"Ubiquinone","aliases":["유비퀴논","산화형 코큐텐"],"nickname":"CoQ10의 산화(비활성) 형태 — 체내 환원 필요","category":"other_functional","tags_purpose":["만성피로"],"tags_function":["에너지 생성"],"tags_bodypart":["심장·혈관"]},
    {"id":"omega-6","name":"오메가6","name_en":"Omega-6","aliases":["리놀레산","Linoleic Acid"],"nickname":"필수 지방산이지만 과잉 주의가 필요","category":"fatty_acid","tags_purpose":["피부"],"tags_function":["피부 건강"],"tags_bodypart":["피부"]},
    {"id":"omega-7","name":"오메가7","name_en":"Omega-7","aliases":["팔미톨레산","Palmitoleic Acid"],"nickname":"점막 건강에 연구되는 불포화 지방산","category":"fatty_acid","tags_purpose":["장건강","피부"],"tags_function":["피부 건강"],"tags_bodypart":["피부","장"]},
    {"id":"omega-9","name":"오메가9","name_en":"Omega-9","aliases":["올레산","Oleic Acid"],"nickname":"올리브유의 주요 지방산","category":"fatty_acid","tags_purpose":["혈압-혈당"],"tags_function":["혈행 개선"],"tags_bodypart":["심장·혈관"]},
]

# More Tier 2 — Korean/Asian traditional + more extracts
MORE_T2 = [
    {"id":"aronia-extract","name":"아로니아추출물","name_en":"Aronia Extract","aliases":["아로니아","초크베리"],"nickname":"안토시아닌 함량이 높은 베리류"},
    {"id":"acerola-extract","name":"아세로라추출물","name_en":"Acerola Extract","aliases":["아세로라"],"nickname":"비타민C가 오렌지의 30배인 열대 과일"},
    {"id":"camu-camu","name":"카무카무","name_en":"Camu Camu","aliases":["Camu Camu"],"nickname":"세계에서 비타민C가 가장 많은 열대 과일"},
    {"id":"baobab","name":"바오밥추출물","name_en":"Baobab","aliases":["바오밥","Baobab"],"nickname":"아프리카 슈퍼푸드 — 비타민C와 식이섬유"},
    {"id":"sea-buckthorn","name":"비타민나무열매추출물","name_en":"Sea Buckthorn","aliases":["비타민나무","산자나무","Hippophae"],"nickname":"200종 이상 영양소를 함유한 범용 열매"},
    {"id":"schisandra-berry","name":"오미자","name_en":"Schisandra Berry","aliases":["Schisandra chinensis"],"nickname":"신맛·단맛·짠맛·쓴맛·매운맛 다섯 가지 맛"},
    {"id":"goji-berry","name":"구기자","name_en":"Goji Berry","aliases":["구기자","Lycium barbarum","울프베리"],"nickname":"한방 눈 건강의 붉은 열매"},
    {"id":"mulberry","name":"오디추출물","name_en":"Mulberry","aliases":["오디","뽕나무열매"],"nickname":"안토시아닌과 레스베라트롤을 함유한 국산 베리"},
    {"id":"solomon-seal","name":"둥글레추출물","name_en":"Solomon's Seal","aliases":["둥글레","옥죽"],"nickname":"한방 자양강장의 뿌리줄기"},
    {"id":"rehmannia","name":"숙지황","name_en":"Rehmannia","aliases":["지황","Rehmannia glutinosa"],"nickname":"한방 보혈의 대표 약재"},
    {"id":"cnidium","name":"천궁추출물","name_en":"Cnidium","aliases":["천궁","Cnidium officinale"],"nickname":"한방 혈행 개선과 두통 관련 약재"},
    {"id":"white-peony","name":"백작약추출물","name_en":"White Peony Root","aliases":["백작약","Paeonia lactiflora"],"nickname":"한방 여성 건강에 사용되는 뿌리"},
    {"id":"atractylodes","name":"백출추출물","name_en":"Atractylodes","aliases":["백출","Atractylodes macrocephala"],"nickname":"소화 기능에 사용되는 한방 원료"},
    {"id":"poria","name":"복령추출물","name_en":"Poria","aliases":["복령","Poria cocos"],"nickname":"소나무 뿌리에서 자라는 약용 버섯"},
    {"id":"jujube","name":"대추추출물","name_en":"Jujube","aliases":["대추","Ziziphus jujuba"],"nickname":"안신 작용이 알려진 한방 열매"},
    {"id":"lotus-leaf","name":"연잎추출물","name_en":"Lotus Leaf","aliases":["연잎","Nelumbo nucifera"],"nickname":"체지방 관련 한방 원료"},
    {"id":"plantago-seed","name":"차전자피식이섬유","name_en":"Plantago Seed Husk","aliases":["차전자피"],"nickname":"물을 흡수해 부풀어 오르는 식이섬유"},
    {"id":"eucommia","name":"두충추출물","name_en":"Eucommia","aliases":["두충","Eucommia ulmoides"],"nickname":"한방 뼈·관절 건강의 나무 껍질"},
    {"id":"cissus","name":"시서스추출물","name_en":"Cissus Quadrangularis","aliases":["시서스","Cissus"],"nickname":"체중 관리에 연구되는 덩굴 식물"},
    {"id":"safflower-seed","name":"홍화씨추출물","name_en":"Safflower Seed","aliases":["홍화씨"],"nickname":"뼈 건강에 전통적으로 사용된 씨앗"},
    {"id":"evening-primrose","name":"달맞이꽃추출물","name_en":"Evening Primrose","aliases":["달맞이꽃"],"nickname":"GLA 외에도 다양한 활성 성분"},
    {"id":"rosehip","name":"로즈힙추출물","name_en":"Rosehip","aliases":["로즈힙","Rosa canina"],"nickname":"비타민C가 풍부한 야생 장미 열매"},
    {"id":"chamomile","name":"캐모마일추출물","name_en":"Chamomile","aliases":["캐모마일","카밀레"],"nickname":"수면과 소화에 사용되는 유럽 허브 차"},
    {"id":"lavender","name":"라벤더추출물","name_en":"Lavender","aliases":["라벤더"],"nickname":"긴장 완화에 사용되는 향기 허브"},
    {"id":"peppermint","name":"페퍼민트추출물","name_en":"Peppermint","aliases":["페퍼민트","박하"],"nickname":"소화 불편에 사용되는 시원한 허브"},
    {"id":"fennel","name":"회향추출물","name_en":"Fennel","aliases":["회향","펜넬"],"nickname":"소화 촉진에 사용되는 지중해 허브"},
    {"id":"milk-peptide","name":"유단백가수분해물","name_en":"Milk Peptide","aliases":["카소키닌","락토트리펩타이드"],"nickname":"우유단백에서 추출한 혈압 조절 펩타이드"},
    {"id":"gamma-butyrolactone","name":"감마부티로락톤","name_en":"Fish Peptide","aliases":["어류 콜라겐 펩타이드"],"nickname":"저분자 어류 펩타이드 — 혈압 관련 연구"},
    {"id":"soy-protein","name":"대두단백","name_en":"Soy Protein","aliases":["대두단백질","Soy Protein"],"nickname":"식물성 단백질의 대표 — 완전 아미노산 프로필"},
    {"id":"hemp-protein","name":"햄프단백","name_en":"Hemp Protein","aliases":["대마단백질"],"nickname":"오메가3와 식이섬유를 함유한 식물 단백질"},
    {"id":"pea-protein","name":"완두단백","name_en":"Pea Protein","aliases":["완두 단백질"],"nickname":"알레르기 걱정 적은 식물성 단백질"},
    {"id":"brown-rice-protein","name":"현미단백","name_en":"Brown Rice Protein","aliases":["현미 단백질"],"nickname":"현미에서 추출한 저알레르기 단백질"},
    {"id":"chlorella-growth-factor","name":"클로렐라성장인자","name_en":"CGF","aliases":["CGF","클로렐라 성장인자"],"nickname":"클로렐라 핵산 추출물"},
    {"id":"spirulina-phycocyanin","name":"피코시아닌","name_en":"Phycocyanin","aliases":["피코시아닌","C-Phycocyanin"],"nickname":"스피룰리나의 파란 항산화 색소"},
    {"id":"bee-pollen","name":"벌화분","name_en":"Bee Pollen","aliases":["Bee Pollen"],"nickname":"영양 밀도가 높은 벌의 식량"},
    {"id":"manuka-honey","name":"마누카꿀","name_en":"Manuka Honey","aliases":["마누카 허니"],"nickname":"뉴질랜드산 항균 활성 꿀"},
    {"id":"marine-magnesium","name":"해양 마그네슘","name_en":"Marine Magnesium","aliases":["해양심층수 마그네슘"],"nickname":"바다에서 유래한 천연 미네랄 복합체"},
    {"id":"coral-calcium","name":"산호칼슘","name_en":"Coral Calcium","aliases":["Coral Calcium"],"nickname":"미량 미네랄을 함유한 산호 유래 칼슘"},
    {"id":"dolomite","name":"돌로마이트","name_en":"Dolomite","aliases":["Dolomite"],"nickname":"칼슘과 마그네슘을 함유한 광물"},
    {"id":"oyster-shell-calcium","name":"굴껍질칼슘","name_en":"Oyster Shell Calcium","aliases":["패각칼슘"],"nickname":"굴 껍데기에서 유래한 탄산칼슘"},
    {"id":"hydroxyapatite","name":"하이드록시아파타이트","name_en":"Hydroxyapatite","aliases":["MCHC"],"nickname":"뼈 자체의 칼슘 형태"},
]

# More Tier 3 — flavors, more coating agents, processing aids
MORE_T3 = [
    {"id":"vanilla-flavor","name":"바닐라향","name_en":"Vanilla Flavor","nickname":"분말·액상 건기식의 향미 첨가제"},
    {"id":"cocoa-powder","name":"코코아분말","name_en":"Cocoa Powder","nickname":"초콜릿맛 건기식의 풍미 원료"},
    {"id":"lemon-flavor","name":"레몬향","name_en":"Lemon Flavor","nickname":"츄어블·음료형 건기식의 향미제"},
    {"id":"strawberry-flavor","name":"딸기향","name_en":"Strawberry Flavor","nickname":"어린이용 건기식의 대표 향미제"},
    {"id":"orange-flavor","name":"오렌지향","name_en":"Orange Flavor","nickname":"비타민C 제품의 자주 쓰이는 향미제"},
    {"id":"mixed-fruit-flavor","name":"종합과일향","name_en":"Mixed Fruit Flavor","nickname":"젤리·구미형 건기식의 향미 블렌드"},
    {"id":"mint-flavor","name":"민트향","name_en":"Mint Flavor","nickname":"구강 건강 제품의 청량 향미제"},
    {"id":"corn-starch","name":"옥수수전분","name_en":"Corn Starch","nickname":"정제의 충전제 및 붕해 보조제"},
    {"id":"rice-starch","name":"쌀전분","name_en":"Rice Starch","nickname":"캡슐 충전에 사용되는 곡물 전분"},
    {"id":"potato-starch","name":"감자전분","name_en":"Potato Starch","nickname":"정제 제조의 부형제"},
    {"id":"dextrin","name":"덱스트린","name_en":"Dextrin","nickname":"전분을 가수분해한 수용성 식이섬유"},
    {"id":"cyclodextrin","name":"사이클로덱스트린","name_en":"Cyclodextrin","aliases":["베타사이클로덱스트린"],"nickname":"향미와 안정성을 높이는 포접 물질"},
    {"id":"carrageenan","name":"카라기난","name_en":"Carrageenan","nickname":"해조류 유래 겔화·안정화제"},
    {"id":"sodium-alginate","name":"알긴산나트륨","name_en":"Sodium Alginate","nickname":"갈조류 유래 겔화제"},
    {"id":"gellan-gum","name":"젤란검","name_en":"Gellan Gum","nickname":"미생물 발효 유래 겔화제"},
    {"id":"arabic-gum","name":"아라비아검","name_en":"Gum Arabic","nickname":"아카시아 수지 유래 유화·안정제"},
    {"id":"tragacanth","name":"트래거캔스","name_en":"Tragacanth","nickname":"식물 수지 유래 증점제"},
    {"id":"cellulose-acetate-phthalate","name":"셀룰로스아세테이트프탈레이트","name_en":"CAP","nickname":"장용성 코팅의 pH 반응 고분자"},
    {"id":"methacrylic-acid-copolymer","name":"메타크릴산공중합체","name_en":"Methacrylic Acid Copolymer","aliases":["유드라짓"],"nickname":"서방형·장용 코팅의 합성 고분자"},
    {"id":"ethylcellulose","name":"에틸셀룰로스","name_en":"Ethylcellulose","nickname":"서방형 정제 코팅의 불용성 셀룰로스"},
    {"id":"calcium-silicate","name":"규산칼슘","name_en":"Calcium Silicate","nickname":"분말의 흡습 방지제"},
    {"id":"tricalcium-phosphate","name":"제삼인산칼슘","name_en":"Tricalcium Phosphate","aliases":["TCP"],"nickname":"고결방지제 겸 칼슘 공급원"},
    {"id":"sodium-croscarmellose","name":"크로스카르멜로스칼슘","name_en":"Croscarmellose Calcium","nickname":"정제 붕해 보조 변형 셀룰로스"},
    {"id":"low-substituted-hpc","name":"저치환도히드록시프로필셀룰로스","name_en":"L-HPC","nickname":"붕해와 결합을 동시에 하는 셀룰로스"},
    {"id":"medium-chain-triglyceride-capsule","name":"MCT(캡슐충전)","name_en":"MCT (capsule fill)","nickname":"연질 캡슐 내용물의 용매 오일"},
    {"id":"cetyl-alcohol","name":"세틸알코올","name_en":"Cetyl Alcohol","nickname":"정제 코팅의 점도 조절제"},
    {"id":"cacao-mass","name":"카카오매스","name_en":"Cacao Mass","nickname":"초콜릿형 건기식의 기저 원료"},
    {"id":"palm-kernel-oil","name":"팜핵유","name_en":"Palm Kernel Oil","nickname":"정제 코팅의 식물성 왁스 대체"},
    {"id":"fatty-acid-glyceride","name":"지방산글리세리드","name_en":"Fatty Acid Glyceride","nickname":"유화와 안정화에 쓰이는 지방산 에스테르"},
    {"id":"polysorbate-80","name":"폴리소르베이트80","name_en":"Polysorbate 80","aliases":["트윈80"],"nickname":"수용성·지용성 성분의 유화제"},
    {"id":"lecithin-emulsifier","name":"레시틴(유화제)","name_en":"Lecithin (emulsifier)","nickname":"대두 유래 천연 유화제"},
    {"id":"sucrose-ester","name":"자당지방산에스테르","name_en":"Sucrose Ester","nickname":"식품 유래 천연 유화제"},
    {"id":"mono-diglyceride","name":"모노디글리세리드","name_en":"Mono/Diglyceride","nickname":"유화 안정화에 사용되는 지방산 에스테르"},
    {"id":"sodium-ascorbate","name":"아스코르빈산나트륨","name_en":"Sodium Ascorbate","nickname":"비타민C의 비산성 형태 — 보존 및 영양 강화"},
    {"id":"tocopheryl-acetate","name":"토코페릴아세테이트","name_en":"Tocopheryl Acetate","nickname":"안정화된 비타민E — 보존 목적 첨가"},
    {"id":"calcium-pantothenate","name":"판토텐산칼슘","name_en":"Calcium Pantothenate","nickname":"비타민B5의 칼슘 결합 보충 형태"},
    {"id":"pyridoxine-hcl","name":"피리독신염산염","name_en":"Pyridoxine HCl","nickname":"비타민B6의 일반적 보충 형태"},
    {"id":"thiamine-hcl","name":"티아민염산염","name_en":"Thiamine HCl","nickname":"비타민B1의 수용성 보충 형태"},
    {"id":"riboflavin-phosphate","name":"리보플라빈인산나트륨","name_en":"Riboflavin 5'-Phosphate Sodium","nickname":"활성형 비타민B2 — 색소로도 사용"},
    {"id":"folic-acid-synthetic","name":"합성엽산","name_en":"Folic Acid (synthetic)","nickname":"건기식에 가장 흔한 엽산 형태"},
    {"id":"cyanocobalamin","name":"시아노코발라민","name_en":"Cyanocobalamin","nickname":"가장 안정적이고 저렴한 B12 형태"},
    {"id":"d-alpha-tocopherol","name":"d-알파토코페롤","name_en":"d-Alpha Tocopherol","nickname":"천연 비타민E의 가장 활성 높은 형태"},
    {"id":"zinc-oxide","name":"산화아연","name_en":"Zinc Oxide","nickname":"아연의 가장 기본적인 보충 형태"},
    {"id":"ferrous-fumarate","name":"푸마르산제일철","name_en":"Ferrous Fumarate","nickname":"철분의 일반적 보충 형태"},
    {"id":"magnesium-oxide","name":"산화마그네슘","name_en":"Magnesium Oxide","nickname":"함량은 높지만 흡수율은 낮은 마그네슘"},
    {"id":"calcium-phosphate","name":"인산칼슘","name_en":"Calcium Phosphate","nickname":"칼슘과 인을 동시에 공급하는 보충 형태"},
    {"id":"sodium-selenite","name":"아셀렌산나트륨","name_en":"Sodium Selenite","nickname":"무기 셀레늄의 일반적 보충 형태"},
    {"id":"chromium-picolinate","name":"크롬피콜리네이트","name_en":"Chromium Picolinate","nickname":"흡수율을 높인 크롬의 킬레이트 형태"},
    {"id":"potassium-iodide","name":"요오드화칼륨","name_en":"Potassium Iodide","nickname":"요오드의 가장 일반적인 보충 형태"},
    {"id":"manganese-sulfate","name":"황산망간","name_en":"Manganese Sulfate","nickname":"망간의 일반적 보충 형태"},
    {"id":"cupric-sulfate","name":"황산구리","name_en":"Cupric Sulfate","nickname":"구리의 일반적 보충 형태"},
    {"id":"sodium-molybdate","name":"몰리브덴산나트륨","name_en":"Sodium Molybdate","nickname":"몰리브덴의 일반적 보충 형태"},
    {"id":"silicon-dioxide-flow","name":"이산화규소(흐름)","name_en":"Silicon Dioxide (flow agent)","nickname":"분말 흐름성 개선용 미세 이산화규소"},
]

def main():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "ingredients.json")
    path = os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as f:
        existing = json.load(f)
    existing_ids = {i["id"] for i in existing}
    a1 = a2 = a3 = 0
    for item in MORE_T1:
        if item["id"] in existing_ids: continue
        item["tier"]=1; item["source_type"]=item.get("source_type","고시형")
        for k in ["tags_age","tags_gender","aliases","related_ingredients"]:
            item.setdefault(k,["전연령"] if k=="tags_age" else ["공통"] if k=="tags_gender" else [])
        for k in ["upper_limit","daily_recommended","mfds_functionality","subcategory","nickname","name_en","tags_bodypart","tags_purpose","tags_function"]:
            item.setdefault(k,[] if k.startswith("tags") else "")
        existing.append(item); a1+=1; existing_ids.add(item["id"])
    for item in MORE_T2:
        if item["id"] in existing_ids: continue
        item["tier"]=2; item["source_type"]=item.get("source_type","부원료"); item.setdefault("category","extract")
        for k in ["tags_age","tags_gender","aliases","related_ingredients","tags_purpose","tags_function","tags_bodypart"]:
            item.setdefault(k,["전연령"] if k=="tags_age" else ["공통"] if k=="tags_gender" else [])
        for k in ["upper_limit","daily_recommended","mfds_functionality","subcategory","nickname","name_en"]:
            item.setdefault(k,"")
        existing.append(item); a2+=1; existing_ids.add(item["id"])
    for item in MORE_T3:
        if item["id"] in existing_ids: continue
        item["tier"]=3; item["source_type"]="식품첨가물"; item["category"]="additive"
        for k in ["tags_purpose","tags_function","tags_bodypart","tags_age","tags_gender","aliases","related_ingredients"]:
            item.setdefault(k,[])
        for k in ["upper_limit","daily_recommended","mfds_functionality","subcategory","name_en"]:
            item.setdefault(k,"")
        existing.append(item); a3+=1; existing_ids.add(item["id"])
    with open(path,"w",encoding="utf-8") as f:
        json.dump(existing,f,ensure_ascii=False,indent=2)
    counts={}
    for i in existing: counts[i["tier"]]=counts.get(i["tier"],0)+1
    print(f"Added T1:{a1}, T2:{a2}, T3:{a3}")
    for t in sorted(counts): print(f"  Tier {t}: {counts[t]}")
    print(f"  GRAND TOTAL: {len(existing)}")

if __name__=="__main__":
    main()
