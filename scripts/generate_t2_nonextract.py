#!/usr/bin/env python3
"""T2 content for non-extract categories: amino_acid, enzyme, fatty_acid, fiber, mineral, other_functional, probiotic, protein, vitamin (89 entries)"""
import json, os

T2 = {
    # === AMINO ACIDS (10) ===
    "5-htp": {"desc":"트립토판에서 세로토닌으로 전환되는 중간 대사체. 기분 안정과 수면 유도에 관여.","origin_type":"현대과학","origin_story":"1990년대 세로토닌 전구체로서 수면 보조 효과가 확인됨. 서아프리카산 그리포니아 씨앗(Griffonia simplicifolia)에서 추출.","dosage":"100-200mg/일","evidence":"보통"},
    "hmb": {"desc":"류신(BCAA의 구성 아미노산)의 대사산물. 근육 단백질 분해를 억제하여 근손실 방지에 기여.","origin_type":"현대과학","origin_story":"1990년대 아이오와 주립대 Steven Nissen 교수팀이 류신 대사 연구 중 발견.","dosage":"1.5-3g/일","evidence":"양호"},
    "s-adenosylmethionine": {"desc":"메티오닌과 ATP의 결합체. 체내 200가지 이상의 메틸화 반응에 관여하는 핵심 분자.","origin_type":"현대과학","origin_story":"1952년 이탈리아 과학자 Giulio Cantoni가 발견. 유럽에서는 간 보호와 관절 건강 목적으로 의약품으로 처방.","dosage":"400-1600mg/일","evidence":"양호"},
    "beta-alanine": {"desc":"체내에서 카르노신 합성의 전구체. 근육 내 산성도(H⁺) 축적을 완충하여 고강도 운동 시 피로를 지연.","origin_type":"현대과학","origin_story":"2006년 Roger Harris 교수가 베타알라닌 보충이 근육 카르노신 농도를 높인다는 것을 확인.","dosage":"2-5g/일","evidence":"양호"},
    "betaine": {"desc":"사탕무에서 발견된 아미노산 유도체. 간에서 호모시스테인을 메티오닌으로 전환하는 메틸 공여체.","origin_type":"식품유래","origin_story":"사탕무(Beta vulgaris)에서 처음 분리되어 이름이 유래. 간 보호와 운동 능력 향상에 연구.","dosage":"1.5-6g/일","evidence":"보통"},
    "citrulline-malate": {"desc":"시트룰린에 말산을 결합한 형태. 체내에서 아르기닌으로 전환되어 일산화질소 생성을 촉진.","origin_type":"현대과학","origin_story":"원래 유럽에서 피로 회복 의약품으로 사용. 2002년 저항 운동 시 피로 감소 효과 연구 발표.","dosage":"6-8g/일","evidence":"양호"},
    "ornithine": {"desc":"요소 회로(Urea Cycle)의 구성 아미노산. 암모니아 해독을 촉진하여 간 부담을 경감.","origin_type":"현대과학","origin_story":"1930년대 Hans Krebs가 요소 회로를 규명하며 역할이 밝혀짐.","dosage":"400-800mg/일","evidence":"보통"},
    "carnosine": {"desc":"베타알라닌과 히스티딘이 결합한 디펩타이드. 근육과 뇌에 높은 농도로 존재하며 항산화·완충 역할.","origin_type":"현대과학","origin_story":"1900년 러시아 화학자 Vladimir Gulewitch가 고기 추출물에서 최초 발견.","dosage":"500-2000mg/일","evidence":"보통"},
    "creatine": {"desc":"체내에서 간과 신장에서 합성되는 유기산. 근육 세포의 ATP 재합성을 촉진하여 폭발적 에너지 공급.","origin_type":"현대과학","origin_story":"1832년 프랑스 화학자 Michel Eugène Chevreul이 고기에서 발견. 1990년대 스포츠 보충제로 폭발적 인기.","dosage":"3-5g/일","evidence":"매우 양호"},
    "gamma-aminobutyric-acid-rice": {"desc":"현미를 유산균으로 발효하여 자연 생성시킨 GABA. 신경 안정과 혈압 조절에 기여.","origin_type":"식품유래","origin_story":"일본에서 현미 발효 전통을 기반으로 GABA 함량을 극대화한 기능성 소재로 개발.","dosage":"100-200mg/일","evidence":"보통"},

    # === ENZYMES (3) ===
    "superoxide-dismutase": {"desc":"체내 가장 강력한 항산화 효소. 활성산소(슈퍼옥사이드)를 과산화수소로 전환하여 세포 보호.","origin_type":"현대과학","origin_story":"1969년 Joe McCord와 Irwin Fridovich가 발견. 노화와 산화 스트레스 연구의 핵심 분자.","dosage":"250-500 IU/일","evidence":"보통"},
    "laccase": {"desc":"구리 함유 산화효소. 폴리페놀 산화에 관여하며 항산화 시스템 보조.","origin_type":"현대과학","origin_story":"옻나무 수액(lacquer tree)에서 처음 분리되어 이름이 유래.","dosage":"제품별 상이","evidence":"제한적"},
    "lactoperoxidase": {"desc":"모유와 타액에 자연 존재하는 항균 효소. 구강 내 유해균을 억제.","origin_type":"식품유래","origin_story":"모유의 면역 성분 연구에서 발견. 자연 항균 시스템의 일부로 구강 건강 제품에 응용.","dosage":"제품별 상이","evidence":"보통"},

    # === FATTY ACIDS (14) ===
    "evening-primrose-oil": {"desc":"달맞이꽃 씨에서 추출한 오일. 감마리놀렌산(GLA)이 풍부하여 피부 보습과 호르몬 균형에 기여.","origin_type":"전통의학","origin_story":"북미 원주민이 달맞이꽃을 상처 치유와 피부 관리에 전통적으로 사용.","dosage":"500-2000mg/일","evidence":"보통"},
    "camellia-oil": {"desc":"동백 씨에서 추출한 오일. 올레산이 풍부하여 피부 보습과 항산화에 기여.","origin_type":"전통의학","origin_story":"한국·일본·중국에서 수백 년간 머리카락과 피부 관리에 사용한 전통 오일.","dosage":"외용 또는 1-2g/일","evidence":"제한적"},
    "perilla-oil": {"desc":"들깨에서 추출한 오일. 알파리놀렌산(ALA)이 약 60%로 식물성 오메가3의 최고 함량.","origin_type":"식품유래","origin_story":"한국 전통 식재료. 들깨는 삼국시대부터 재배 기록이 있으며 식용유로 광범위하게 사용.","dosage":"2-5ml/일","evidence":"보통"},
    "borage-oil": {"desc":"보라지(지치과 식물) 씨에서 추출한 오일. GLA 함량이 20-26%로 달맞이꽃 오일보다 높음.","origin_type":"전통의학","origin_story":"중세 유럽에서 '용기의 허브'로 불렸으며 기분 개선 목적으로 사용.","dosage":"1000-2000mg/일","evidence":"보통"},
    "gamma-linolenic-borage": {"desc":"보라지 종자유에서 추출한 고순도 감마리놀렌산. 항염과 피부 장벽 강화에 특화.","origin_type":"현대과학","origin_story":"보라지 오일에서 GLA를 고농도로 분리한 기능성 소재.","dosage":"300-600mg GLA/일","evidence":"보통"},
    "sacha-inchi": {"desc":"페루 아마존 원산 별 모양 견과에서 추출한 오일. 알파리놀렌산(ALA)이 약 50%.","origin_type":"전통의학","origin_story":"잉카 문명에서 3000년 이상 재배. 현지어로 '잉카 땅콩'이라 불림.","dosage":"2-5ml/일","evidence":"제한적"},
    "pomegranate-seed-oil": {"desc":"석류 씨에서 추출한 오일. 퓨닉산(Punicic Acid)이 풍부하여 피부 재생과 항산화에 기여.","origin_type":"식품유래","origin_story":"석류는 고대 페르시아에서 '생명의 과일'로 숭배. 씨 오일은 현대에 들어 피부 관리에 응용.","dosage":"1-2g/일","evidence":"제한적"},
    "argan-oil": {"desc":"모로코 원산 아르간 나무 씨에서 추출한 오일. 비타민E와 올레산이 풍부.","origin_type":"전통의학","origin_story":"모로코 베르베르족이 수백 년간 식용과 피부 관리에 사용. '모로코의 액체 금'이라 불림.","dosage":"외용 또는 1-2 tsp/일","evidence":"제한적"},
    "flaxseed-oil": {"desc":"아마씨에서 추출한 오일. 식물성 오메가3(ALA)의 대표 공급원.","origin_type":"식품유래","origin_story":"기원전 3000년 바빌로니아에서 재배 기록. 히포크라테스가 소화 장애에 추천.","dosage":"1-2 tbsp/일","evidence":"양호"},
    "avocado-oil": {"desc":"아보카도 과육에서 추출한 오일. 올레산, 비타민E, 식물스테롤이 풍부.","origin_type":"식품유래","origin_story":"중남미 원산. 아즈텍 문명에서 식용과 피부 관리에 사용한 기록이 있음.","dosage":"1-2 tbsp/일","evidence":"보통"},
    "pine-nut-oil": {"desc":"잣에서 추출한 오일. 피놀렌산이 포함되어 식욕 조절 호르몬(CCK)을 촉진한다는 연구.","origin_type":"식품유래","origin_story":"한국에서 전통적 고급 식재료. 한의학에서 폐와 장을 윤활하는 용도로 기록.","dosage":"3g/일","evidence":"제한적"},
    "green-mussel-lipid": {"desc":"뉴질랜드산 초록입홍합에서 추출한 지질. 오메가3와 독특한 ETA(에이코사테트라에노산) 포함.","origin_type":"전통의학","origin_story":"뉴질랜드 마오리족이 전통적으로 관절 건강 목적으로 초록입홍합을 섭취.","dosage":"600-1200mg/일","evidence":"양호"},
    "coconut-oil": {"desc":"코코넛 과육에서 추출한 오일. 중쇄지방산(MCT)이 약 60%로 빠른 에너지원.","origin_type":"식품유래","origin_story":"동남아시아·태평양 섬 지역에서 수천 년간 주요 식용유. '생명의 나무' 오일.","dosage":"1-2 tbsp/일","evidence":"보통"},
    "krill-oil": {"desc":"남극 크릴새우에서 추출한 오일. 인지질 결합 형태의 EPA/DHA를 함유하여 흡수율이 높음.","origin_type":"현대과학","origin_story":"1990년대 노르웨이에서 크릴 오일의 인지질 결합 오메가3가 기존 어유보다 생체이용률이 높다는 연구 발표.","dosage":"500-2000mg/일","evidence":"양호"},

    # === FIBERS (3) ===
    "oat-beta-glucan": {"desc":"귀리에 함유된 수용성 식이섬유. 장에서 젤을 형성하여 콜레스테롤 흡수를 차단.","origin_type":"식품유래","origin_story":"1997년 FDA가 귀리 베타글루칸의 콜레스테롤 저하 효과를 건강강조표시로 인정.","dosage":"3g/일","evidence":"매우 양호"},
    "barley-beta-glucan": {"desc":"보리에 함유된 수용성 식이섬유. 귀리 베타글루칸과 유사한 콜레스테롤 저하 작용.","origin_type":"식품유래","origin_story":"보리는 세계 최초의 재배 곡물 중 하나. 2006년 FDA가 보리 베타글루칸 건강강조표시 승인.","dosage":"3g/일","evidence":"양호"},
    "psyllium-husk": {"desc":"질경이 씨앗 껍질에서 추출한 수용성 식이섬유. 물을 흡수하면 40배 이상 팽창하여 장운동 촉진.","origin_type":"전통의학","origin_story":"인도 아유르베다에서 수천 년간 소화 건강 목적으로 사용. 현재 전 세계 식이섬유 보충제의 대표 원료.","dosage":"5-10g/일","evidence":"매우 양호"},

    # === MINERALS (8) ===
    "calcium-citrate": {"desc":"칼슘의 구연산 결합 형태. 위산이 적어도 흡수되어 공복·식후 모두 섭취 가능.","origin_type":"현대과학","origin_story":"탄산칼슘의 흡수 한계를 개선하기 위해 개발된 킬레이트 형태.","dosage":"500-1000mg/일","evidence":"양호"},
    "magnesium-glycinate": {"desc":"마그네슘과 글리신의 킬레이트 결합. 흡수율이 높고 위장 자극이 적어 수면·이완 목적에 선호.","origin_type":"현대과학","origin_story":"킬레이션 기술을 통해 마그네슘의 생체이용률을 높인 현대 제형.","dosage":"200-400mg/일","evidence":"양호"},
    "magnesium-threonate": {"desc":"마그네슘의 트레온산 결합 형태. 뇌혈관장벽(BBB)을 통과하여 뇌 마그네슘 농도를 직접 높임.","origin_type":"현대과학","origin_story":"2010년 MIT 연구팀(Guosong Liu)이 개발. 학습·기억 향상 효과를 동물 실험에서 확인.","dosage":"1500-2000mg/일","evidence":"보통"},
    "calcium-hydroxyapatite": {"desc":"뼈 조직의 주성분과 동일한 칼슘-인산 결정. 뼈에 직접 통합되는 형태.","origin_type":"현대과학","origin_story":"뉴질랜드에서 골다공증 연구 중 뼈 유래 칼슘의 우수한 흡수율이 확인됨.","dosage":"500-1000mg/일","evidence":"양호"},
    "zinc-carnosine": {"desc":"아연과 카르노신의 킬레이트 결합. 위 점막에 직접 결합하여 위벽 보호.","origin_type":"현대과학","origin_story":"일본에서 위 건강 의약품(Polaprezinc)으로 개발. 위궤양과 위염에 처방.","dosage":"75-150mg/일","evidence":"양호"},
    "zinc-picolinate": {"desc":"아연과 피콜린산의 킬레이트 결합. 소장에서 흡수가 잘 되는 아연의 고흡수율 형태.","origin_type":"현대과학","origin_story":"1980년대 미국에서 아연 흡수율 연구 중 피콜린산 결합 형태의 우수성 확인.","dosage":"15-30mg/일","evidence":"양호"},
    "iron-bisglycinate": {"desc":"철분과 글리신의 이중 킬레이트 결합. 위장 부작용이 적고 흡수율이 높은 프리미엄 철분 형태.","origin_type":"현대과학","origin_story":"Albion Minerals사가 개발한 킬레이트 철분. 기존 황산철의 위장 자극 문제를 해결.","dosage":"18-27mg/일","evidence":"양호"},
    "red-algae-calcium": {"desc":"아일랜드·아이슬란드 해역의 석회조류에서 추출한 식물성 칼슘. 73가지 미량 미네랄 포함.","origin_type":"식품유래","origin_story":"북대서양 해역의 석회화 해조류(Lithothamnion)에서 추출. 비건 칼슘의 대표.","dosage":"500-1000mg/일","evidence":"보통"},

    # === PROBIOTICS (14) ===
    "lactobacillus-rhamnosus": {"desc":"장 상피세포 부착력이 강한 유산균. 면역 조절과 설사 예방에 가장 많은 연구.","origin_type":"현대과학","origin_story":"1983년 Sherwood Gorbach와 Barry Goldin이 건강한 인체 장에서 분리(GG주). 세계 최다 연구 프로바이오틱스.","dosage":"10-20억 CFU/일","evidence":"매우 양호"},
    "lactobacillus-reuteri": {"desc":"인체 소화관에 자연 서식하는 유산균. 위 건강, 구강 건강, 영유아 산통 완화에 연구.","origin_type":"현대과학","origin_story":"1960년대 독일 미생물학자 Gerhard Reuter가 발견하여 이름이 유래.","dosage":"1-10억 CFU/일","evidence":"양호"},
    "lactobacillus-acidophilus": {"desc":"소장에 주로 서식하는 대표적 유산균. 유당 분해를 돕고 유해균 증식을 억제.","origin_type":"현대과학","origin_story":"1900년 노벨상 수상자 Élie Metchnikoff가 장수와 유산균의 관련성을 최초 제안.","dosage":"10-50억 CFU/일","evidence":"양호"},
    "lactobacillus-casei": {"desc":"소장과 대장 전역에 서식하는 유산균. 항염과 면역 조절에 관여.","origin_type":"현대과학","origin_story":"치즈 숙성 과정에서 분리. 'casei'는 라틴어로 치즈(caseus)에서 유래.","dosage":"10-50억 CFU/일","evidence":"양호"},
    "lactobacillus-plantarum": {"desc":"김치, 사워크라우트 등 발효 식품에 풍부한 유산균. 장벽 강화와 면역 조절.","origin_type":"식품유래","origin_story":"한국 전통 김치에서 높은 비율로 검출. 발효 식품의 핵심 균주.","dosage":"10-100억 CFU/일","evidence":"양호"},
    "lactobacillus-helveticus": {"desc":"스위스 치즈와 발효유에서 분리된 유산균. 혈압 조절 펩타이드(VPP/IPP) 생성 능력.","origin_type":"식품유래","origin_story":"'helveticus'는 라틴어로 스위스(Helvetia)를 의미. 에멘탈 치즈 제조의 핵심 균주.","dosage":"10-50억 CFU/일","evidence":"보통"},
    "lactococcus-lactis": {"desc":"유제품 발효에 사용되는 대표적 유산균. 니신(Nisin) 등 항균 물질을 생산.","origin_type":"식품유래","origin_story":"치즈와 버터밀크 제조에 수천 년간 사용. 최초의 유전체 해독 유산균 중 하나.","dosage":"10-50억 CFU/일","evidence":"보통"},
    "bacillus-coagulans": {"desc":"포자를 형성하는 유산균. 위산과 열에 강해 생존율이 높음. 장까지 살아서 도달.","origin_type":"현대과학","origin_story":"1915년 처음 분리. 포자 형성 능력 덕분에 상온 보관이 가능한 유산균으로 주목.","dosage":"10-20억 CFU/일","evidence":"양호"},
    "bifidobacterium-lactis": {"desc":"대장에 주로 서식하는 비피더스균. 면역 세포 활성화와 장 건강에 폭넓은 연구.","origin_type":"현대과학","origin_story":"1990년대 덴마크 Chr. Hansen사가 BB-12주를 분리. 세계 최다 연구 비피더스균.","dosage":"10-100억 CFU/일","evidence":"매우 양호"},
    "bifidobacterium-longum": {"desc":"모유 수유 영아의 장에 높은 비율로 존재하는 비피더스균. 생애 초기 면역 발달에 중요.","origin_type":"현대과학","origin_story":"1899년 프랑스 파스퇴르 연구소의 Henri Tissier가 건강한 영아 분변에서 최초 분리.","dosage":"10-100억 CFU/일","evidence":"양호"},
    "bifidobacterium-breve": {"desc":"영유아 장에 풍부한 비피더스균. 알레르기와 피부 건강에 대한 연구가 진행 중.","origin_type":"현대과학","origin_story":"'breve'는 라틴어로 '짧은'이란 뜻. 모유에서 영아 장으로 전달되는 균주.","dosage":"10-100억 CFU/일","evidence":"보통"},
    "bifidobacterium-animalis": {"desc":"대장 건강과 장 통과 시간 개선에 연구된 비피더스균.","origin_type":"현대과학","origin_story":"다논(Danone)사가 DN-173 010주를 상업화하여 기능성 유제품에 사용.","dosage":"10-100억 CFU/일","evidence":"양호"},
    "streptococcus-thermophilus": {"desc":"요구르트와 치즈 제조의 핵심 스타터 균주. 유당 분해 효소(락타아제)를 생산.","origin_type":"식품유래","origin_story":"수천 년간 요구르트 제조에 사용. L. bulgaricus와 함께 요구르트의 필수 2대 균주.","dosage":"10-50억 CFU/일","evidence":"양호"},
    "weissella-cibaria": {"desc":"김치에서 분리된 유산균. 구강 내 구취균(F. nucleatum) 억제와 잇몸 건강에 연구.","origin_type":"식품유래","origin_story":"한국 KAIST 연구팀이 김치에서 분리한 구강 프로바이오틱스. 'cibaria'는 라틴어로 음식.","dosage":"5-10억 CFU/일","evidence":"보통"},

    # === PROTEINS (4) ===
    "egg-shell-membrane": {"desc":"달걀 껍질 안쪽의 얇은 막. 콜라겐, 엘라스틴, 글루코사민, 히알루론산을 자연 함유.","origin_type":"식품유래","origin_story":"달걀 산업 부산물을 관절 건강 소재로 재활용. NEM(Natural Eggshell Membrane)이 대표 브랜드.","dosage":"500mg/일","evidence":"보통"},
    "silk-peptide": {"desc":"누에 실크(견사)를 효소 분해한 저분자 펩타이드. 보습과 피부 재생에 연구.","origin_type":"전통의학","origin_story":"한국 잠사(養蠶) 전통에서 유래. 견사 단백질(피브로인)을 식용·뷰티 소재로 개발.","dosage":"200-400mg/일","evidence":"제한적"},
    "colostrum": {"desc":"출산 후 48시간 내 분비되는 초기 모유. 면역글로불린(IgG), 락토페린, 성장인자가 농축.","origin_type":"식품유래","origin_story":"소(牛) 초유를 면역 보충제로 사용. 아유르베다에서도 초유의 치유력을 기록.","dosage":"1-3g/일","evidence":"양호"},
    "marine-collagen": {"desc":"해양 어류(주로 비늘·껍질)에서 추출한 제1형 콜라겐 펩타이드. 분자량이 작아 흡수율 높음.","origin_type":"현대과학","origin_story":"돼지·소 유래 콜라겐의 종교적·안전성 이슈를 해결하기 위해 해양 원료로 개발.","dosage":"5-10g/일","evidence":"양호"},

    # === VITAMINS (3) ===
    "methylcobalamin": {"desc":"비타민B12의 활성 형태. 체내 메틸화 반응에 직접 참여하여 전환 과정 없이 이용 가능.","origin_type":"현대과학","origin_story":"시아노코발라민(합성 B12)의 체내 전환 한계를 보완하기 위해 개발된 활성 형태.","dosage":"500-5000mcg/일","evidence":"양호"},
    "vitamin-d2": {"desc":"식물·버섯 유래 비타민D. 자외선 조사로 에르고스테롤에서 생성. 비건 비타민D의 대안.","origin_type":"현대과학","origin_story":"1920년대 구루병 예방 인자 연구 중 발견. D3 대비 효력은 낮지만 비건 소재로 가치.","dosage":"600-2000 IU/일","evidence":"보통"},
    "k2-mk7": {"desc":"비타민K2의 MK-7 형태. 낫토(나또)에서 유래하며, 칼슘을 혈관이 아닌 뼈로 유도.","origin_type":"식품유래","origin_story":"일본 전통 발효 식품 낫토(나또)에서 높은 함량 발견. 네덜란드 연구진이 뼈·혈관 건강 효과 규명.","dosage":"100-200mcg/일","evidence":"양호"},
}

# === OTHER_FUNCTIONAL (30) ===
T2_OTHER = {
    "d-ribose": {"desc":"세포 에너지 화폐 ATP의 구성 당. 심근과 골격근의 에너지 재합성을 촉진.","origin_type":"현대과학","origin_story":"1990년대 심장 수술 후 심근 회복 연구에서 효과 확인.","dosage":"5-15g/일","evidence":"보통"},
    "d-mannose": {"desc":"크랜베리에 함유된 단당류. 요로감염(UTI) 유발균(E. coli)이 요로 벽에 부착하는 것을 차단.","origin_type":"식품유래","origin_story":"크랜베리의 요로 건강 효과 연구에서 핵심 활성 성분으로 확인됨.","dosage":"500-2000mg/일","evidence":"양호"},
    "diindolylmethane": {"desc":"브로콜리 등 십자화과 채소에서 유래. 에스트로겐 대사를 조절하여 호르몬 균형에 기여.","origin_type":"식품유래","origin_story":"인돌-3-카비놀(I3C)의 체내 대사산물. 십자화과 채소와 암 예방 연구에서 주목.","dosage":"100-300mg/일","evidence":"보통"},
    "dmae": {"desc":"뇌 내 아세틸콜린 전구체. 정어리 등 생선에 소량 존재하며 집중력 향상에 연구.","origin_type":"현대과학","origin_story":"1950년대 ADHD 연구에서 처음 사용. 이후 인지 기능 보충제로 전환.","dosage":"100-300mg/일","evidence":"제한적"},
    "ip6": {"desc":"곡물·두류에 풍부한 이노시톨 인산. 세포 성장 조절과 자연 살상(NK) 세포 활성에 연구.","origin_type":"식품유래","origin_story":"현미, 콩 등에 풍부. 1990년대 AbulKalam Shamsuddin 교수가 항암 잠재력을 보고.","dosage":"1-4g/일","evidence":"제한적"},
    "nmn": {"desc":"NAD+ 전구체. 세포 에너지 대사와 DNA 복구에 필수적인 NAD+를 직접 보충.","origin_type":"현대과학","origin_story":"2016년 하버드 David Sinclair 교수의 노화 연구에서 NMN이 NAD+ 수준을 회복시킴이 확인.","dosage":"250-1000mg/일","evidence":"보통 (인체 연구 초기)"},
    "nr": {"desc":"비타민B3의 한 형태이자 NAD+ 전구체. NMN보다 먼저 상업화된 NAD+ 보충 소재.","origin_type":"현대과학","origin_story":"2004년 Dartmouth 대학 Charles Brenner 교수가 NR의 NAD+ 전구체 역할을 규명.","dosage":"300-1000mg/일","evidence":"보통"},
    "pqq": {"desc":"세포 내 미토콘드리아 신생(biogenesis)을 촉진하는 비타민 유사 물질. 강력한 항산화력.","origin_type":"현대과학","origin_story":"1979년 발견. 2003년 쥐 실험에서 PQQ 결핍 시 성장 장애가 나타나 필수 영양소 후보로 제안.","dosage":"10-20mg/일","evidence":"보통"},
    "r-alpha-lipoic-acid": {"desc":"알파리포산의 자연 R형 이성질체. S형 대비 생체이용률이 높고 미토콘드리아에서 직접 작용.","origin_type":"현대과학","origin_story":"일반 알파리포산은 R형+S형 혼합물. R형만 추출하여 효율을 높인 프리미엄 소재.","dosage":"100-300mg/일","evidence":"보통"},
    "gallic-acid": {"desc":"녹차, 포도, 오배자 등에 함유된 폴리페놀. 항산화와 항염 작용에 연구.","origin_type":"식품유래","origin_story":"오배자(갈(gall) 나무 혹)에서 처음 분리되어 이름이 유래. 전통 잉크 원료이기도 함.","dosage":"제품별 상이","evidence":"제한적"},
    "citrus-bioflavonoid": {"desc":"감귤류 과피에 함유된 플라보노이드 복합체. 비타민C의 작용을 강화하고 모세혈관을 보호.","origin_type":"식품유래","origin_story":"1930년대 노벨상 수상자 Albert Szent-Györgyi가 '비타민P'로 제안했던 물질군.","dosage":"500-1000mg/일","evidence":"보통"},
    "glucuronolactone": {"desc":"포도당 대사산물. 간에서 해독 작용을 보조하며 에너지 음료의 흔한 성분.","origin_type":"현대과학","origin_story":"1960년대 유럽에서 간 보호 목적으로 연구. 이후 에너지 음료 성분으로 상업화.","dosage":"500-1000mg/일","evidence":"제한적"},
    "hyaluronic-acid-chicken": {"desc":"닭벼슬(볏)에서 추출한 히알루론산. 관절액과 피부의 보습 성분과 동일한 구조.","origin_type":"식품유래","origin_story":"닭벼슬은 히알루론산의 천연 고농도 공급원. 발효법 보급 전 주요 원료였음.","dosage":"60-200mg/일","evidence":"보통"},
    "lecithin": {"desc":"대두 또는 해바라기에서 추출한 인지질 복합체. 세포막 구성 성분이자 콜린 공급원.","origin_type":"식품유래","origin_story":"그리스어 lekithos(달걀 노른자)에서 유래. 달걀에서 처음 분리되었으나 현재는 대두가 주 원료.","dosage":"1-5g/일","evidence":"보통"},
    "spermidine": {"desc":"세포 내 자가포식(오토파지)을 활성화하는 폴리아민. 세포 정화와 장수 연구의 핵심 물질.","origin_type":"식품유래","origin_story":"1678년 정자(sperm)에서 처음 결정이 관찰되어 이름 유래. 숙성 치즈, 콩, 버섯에도 풍부.","dosage":"1-6mg/일","evidence":"보통 (인체 연구 초기)"},
    "spirulina": {"desc":"시아노박테리아(남조류)의 일종. 단백질 60-70%, 철분, 비타민B12 유사체, 피코시아닌 함유.","origin_type":"전통의학","origin_story":"아즈텍 문명이 텍스코코 호수에서 채취하여 주식으로 사용. 아프리카 차드 호수에서도 전통 식품.","dosage":"3-10g/일","evidence":"보통"},
    "citicoline": {"desc":"뇌 세포막 인지질(포스파티딜콜린) 합성의 중간체. 인지 기능과 뇌 에너지 대사에 관여.","origin_type":"현대과학","origin_story":"1950년대 일본에서 뇌졸중 회복 의약품으로 개발. 이후 인지 기능 보충제로 전환.","dosage":"250-500mg/일","evidence":"양호"},
    "phytosterol-ester": {"desc":"식물스테롤에 지방산을 결합하여 지용성과 흡수율을 높인 형태. 콜레스테롤 흡수 경쟁 억제.","origin_type":"현대과학","origin_story":"2000년 FDA가 식물스테롤/스타놀의 콜레스테롤 저하 건강강조표시를 승인.","dosage":"2g/일","evidence":"매우 양호"},
    "anthocyanin": {"desc":"베리류·포도에 보라색~적색을 부여하는 플라보노이드. 항산화와 눈 건강에 연구.","origin_type":"식품유래","origin_story":"그리스어 anthos(꽃) + kyanos(파란)에서 유래. 빌베리·블루베리의 핵심 기능 성분.","dosage":"200-500mg/일","evidence":"보통"},
    "ellagic-acid": {"desc":"석류, 딸기, 라즈베리 등에 함유된 폴리페놀. 항산화와 세포 보호에 연구.","origin_type":"식품유래","origin_story":"석류의 핵심 항산화 성분 중 하나. 고대 이집트에서 석류를 의약 용도로 사용한 기록.","dosage":"200-500mg/일","evidence":"제한적"},
    "catechin": {"desc":"녹차의 주요 폴리페놀. 특히 EGCG는 체지방 산화와 항산화에 가장 많은 연구.","origin_type":"식품유래","origin_story":"중국에서 수천 년간 약용 차(茶)로 사용. 현대 연구에서 EGCG의 열생산 촉진 효과 확인.","dosage":"300-500mg EGCG/일","evidence":"양호"},
    "coenzyme-a": {"desc":"아세틸기 전달 효소. 지방산 산화, TCA 회로, 에너지 대사의 핵심 보조인자.","origin_type":"현대과학","origin_story":"1945년 Fritz Lipmann이 발견(노벨상 수상). 판토텐산(비타민B5)에서 체내 합성.","dosage":"보통 판토텐산으로 보충","evidence":"보통"},
    "chondroitin": {"desc":"연골 조직의 주요 구성 성분인 글리코사미노글리칸. 관절액의 점성과 탄력 유지.","origin_type":"현대과학","origin_story":"상어 연골, 소 연골에서 추출. 1960년대 유럽에서 관절 건강 의약품으로 사용 시작.","dosage":"800-1200mg/일","evidence":"양호"},
    "chlorella": {"desc":"담수 녹조류. 클로로필(엽록소) 함량이 식물 중 최고 수준이며 중금속 배출에 연구.","origin_type":"현대과학","origin_story":"1890년 네덜란드 미생물학자 Beyerinck이 발견. 1950년대 미래 식량 자원으로 연구 시작.","dosage":"3-10g/일","evidence":"보통"},
    "proanthocyanidin": {"desc":"포도씨·소나무 껍질에 풍부한 축합형 탄닌. 강력한 항산화력과 혈관 보호 작용.","origin_type":"식품유래","origin_story":"1947년 프랑스 과학자 Jacques Masquelier가 땅콩 껍질에서 최초 분리.","dosage":"100-300mg/일","evidence":"양호"},
    "pterostilbene": {"desc":"레스베라트롤의 메틸화 유도체. 생체이용률이 레스베라트롤의 약 4배.","origin_type":"식품유래","origin_story":"블루베리에서 발견. 레스베라트롤의 한계(낮은 흡수율)를 보완하는 차세대 소재.","dosage":"50-250mg/일","evidence":"보통"},
    "pyruvate": {"desc":"포도당 대사의 중간 산물. 지방산 산화를 촉진하고 운동 시 에너지 효율을 높이는 연구.","origin_type":"현대과학","origin_story":"1990년대 Pittsburgh 대학 연구에서 체지방 감소 효과가 보고됨.","dosage":"6-30g/일","evidence":"제한적"},
    "red-mold-rice-monacolin": {"desc":"홍국(붉은 효모 쌀)에서 추출한 모나콜린K. 스타틴 계열 콜레스테롤 저하제와 동일 성분.","origin_type":"전통의학","origin_story":"중국 당나라(900년경) 의서에 홍국이 기록. 소화 촉진과 혈액 순환에 사용.","dosage":"모나콜린K 10mg/일","evidence":"매우 양호"},
    "yeast-beta-glucan": {"desc":"효모(Saccharomyces cerevisiae) 세포벽에서 추출한 베타-1,3/1,6-글루칸. 대식세포를 활성화.","origin_type":"현대과학","origin_story":"1940년대 Louis Pillemer가 효모 세포벽의 면역 활성 성분을 최초 발견.","dosage":"250-500mg/일","evidence":"양호"},
    "fucoxanthin": {"desc":"갈조류(미역, 다시마)에 함유된 카로티노이드. 미토콘드리아 UCP1 활성화를 통한 열생산 촉진.","origin_type":"식품유래","origin_story":"일본 홋카이도 대학 연구에서 후코잔틴의 내장지방 감소 효과가 2005년 보고됨.","dosage":"2-8mg/일","evidence":"보통"},
}

T2.update(T2_OTHER)

def main():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "ingredients.json")
    path = os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    missing = []
    for item in data:
        if item["tier"] != 2:
            continue
        if item.get("category") == "extract":
            continue  # handled in separate script
        if item["id"] in T2:
            c = T2[item["id"]]
            item["content_description"] = c["desc"]
            item["origin_type"] = c["origin_type"]
            item["origin_story"] = c["origin_story"]
            item["dosage_reference"] = c["dosage"]
            item["evidence_level"] = c["evidence"]
            updated += 1
        else:
            missing.append(f'{item["id"]} ({item["name"]})')

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    target = len([i for i in data if i["tier"]==2 and i.get("category")!="extract"])
    print(f"Updated: {updated}/{target}")
    if missing:
        print(f"Missing: {len(missing)}")
        for m in missing:
            print(f"  - {m}")

if __name__ == "__main__":
    main()
