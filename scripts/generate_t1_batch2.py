#!/usr/bin/env python3
"""T1 content batch 2: minerals (19) + fatty acids (12) = 31 entries"""
import json, os

T1 = {
    # === MINERALS (19) ===
    "calcium": {"desc":"체내 가장 풍부한 미네랄. 99%는 뼈·치아, 나머지 1%가 근수축, 신경전달, 혈액응고, 효소 활성화에 관여.","origin_type":"현대과학","origin_story":"1808년 Humphry Davy가 전기분해로 칼슘 금속 분리. 그러나 우유가 뼈를 강하게 한다는 지식은 히포크라테스 시대부터.","dosage":"800-1000mg/일","evidence":"매우 양호","food_sources":"우유, 치즈, 요구르트, 멸치, 뼈째 먹는 생선, 두부, 케일","fun_fact":"칼슘은 비타민D 없이는 소장에서 흡수율이 10-15%에 불과. 비타민D가 있으면 30-40%로 상승."},
    "magnesium": {"desc":"300개 이상의 효소 반응에 관여. 근이완, 신경 안정(NMDA 수용체 조절), ATP 안정화, 혈압 조절에 필수.","origin_type":"현대과학","origin_story":"그리스 마그네시아(Magnesia) 지역에서 이름 유래. 현대인의 결핍률이 가장 높은 미네랄 중 하나.","dosage":"310-420mg/일","evidence":"매우 양호","food_sources":"호박씨, 다크초콜릿, 아몬드, 시금치, 바나나, 아보카도","fun_fact":"산화마그네슘은 흡수율이 4%로 최저, 글리시네이트·트레오네이트·타우레이트 등 킬레이트 형태는 흡수율이 유의미하게 높음."},
    "iron": {"desc":"헤모글로빈(산소 운반)과 미오글로빈(근육 내 산소 저장)의 핵심. 전자전달계의 시토크롬에도 필수.","origin_type":"현대과학","origin_story":"3,500년 전 시작된 철기시대. 의학적으로는 1681년 Thomas Sydenham이 빈혈에 철 보충을 처방한 것이 최초 기록.","dosage":"8-18mg/일","evidence":"매우 양호","food_sources":"간, 소고기, 시금치, 렌틸콩, 두부, 다크초콜릿","fun_fact":"식물성 철분(비헴철)의 흡수율은 2-20%이지만, 비타민C와 함께 먹으면 2-3배 향상. 차·커피의 탄닌은 흡수를 방해."},
    "zinc": {"desc":"200개 이상의 효소에 관여하는 미량 미네랄. 면역 세포(T세포, NK세포) 발달, DNA 합성, 상처 치유, 미각·후각에 필수.","origin_type":"현대과학","origin_story":"1961년 이란의 Ananda Prasad 교수가 아연 결핍으로 인한 성장 지연과 성선기능저하를 보고하며 필수 미네랄로 인정.","dosage":"8-11mg/일","evidence":"매우 양호","food_sources":"굴(100g=78mg!), 소고기, 호박씨, 렌틸콩, 캐슈넛","fun_fact":"굴 100g이면 일일 권장량의 700%를 초과. 돈후안이 매일 굴을 먹었다는 전설이 아연과 성 건강의 연관성을 암시."},
    "selenium": {"desc":"글루타치온 퍼옥시다아제(GPx) 등 셀레노효소의 핵심 구성. 간접 항산화, 갑상선 호르몬 활성화(T4→T3), 면역 조절.","origin_type":"현대과학","origin_story":"달의 여신 셀레네(Selene)에서 이름 유래. 1957년 필수 미량 미네랄로 인정. 토양 셀레늄 농도에 따라 식품 함량 차이 극대.","dosage":"55-70mcg/일","evidence":"양호","food_sources":"브라질너트(1-2알=일일 권장량), 참치, 새우, 달걀, 간","fun_fact":"브라질너트 2알이면 일일 셀레늄을 충족하지만 6알 이상은 과잉. 미네랄 중 독성 임계치가 가장 좁은 편."},
    "iodine": {"desc":"갑상선 호르몬(T3, T4)의 구성 성분. 기초대사율, 체온 조절, 태아 뇌 발달에 결정적.","origin_type":"현대과학","origin_story":"1811년 Bernard Courtois가 해초 재에서 자주색 증기(ioeides=보라색)로 발견. 요오드 결핍은 여전히 세계 최대 예방 가능 지적장애 원인.","dosage":"150mcg/일","evidence":"매우 양호","food_sources":"해조류(다시마, 미역), 유제품, 달걀, 요오드 강화 소금","fun_fact":"한국인은 해조류 소비가 높아 요오드 결핍보다 과잉이 더 문제일 수 있음. 갑상선 질환자는 해조류 과다 섭취 주의."},
    "chromium": {"desc":"인슐린 수용체 신호를 강화하는 미량 미네랄. 인슐린 감수성 개선과 혈당 안정에 연구.","origin_type":"현대과학","origin_story":"1957년 Walter Mertz가 맥주 효모의 'GTF(포도당 내성 인자)'에서 크롬의 역할을 발견.","dosage":"25-35mcg/일","evidence":"보통","food_sources":"브로콜리, 포도주스, 맥주효모, 감자, 전곡류","fun_fact":"크롬 피콜리네이트가 가장 흔한 보충 형태. '체지방 감소' 마케팅이 활발하나, 메타분석에서 효과 크기는 미미."},
    "potassium": {"desc":"세포 내 주요 양이온. 나트륨과 길항하여 혈압 조절, 근수축·이완, 신경 임펄스 전달에 필수.","origin_type":"현대과학","origin_story":"식물 재(pot ash)에서 이름 유래. DASH 식단 연구에서 칼륨 풍부한 식단의 혈압 강하 효과가 대규모로 확인.","dosage":"2600-3400mg/일","evidence":"매우 양호","food_sources":"바나나, 고구마, 시금치, 아보카도, 렌틸콩, 연어","fun_fact":"바나나 1개에 약 400mg이지만, 고구마(540mg), 렌틸콩(730mg/컵)이 사실 더 높은 칼륨 공급원."},
    "phosphorus": {"desc":"칼슘 다음으로 풍부한 체내 미네랄. 뼈·치아 구조(하이드록시아파타이트), ATP·DNA·세포막(인지질)의 구성 성분.","origin_type":"현대과학","origin_story":"1669년 Hamburg 연금술사 Hennig Brand가 소변에서 빛나는 물질 분리. 그리스어 phosphoros(빛을 나르는 것)에서 이름 유래.","dosage":"700mg/일","evidence":"양호","food_sources":"유제품, 육류, 생선, 견과류, 콩류","fun_fact":"현대 가공식품에 인산염 첨가물이 과도하게 사용되어, 결핍보다 과잉이 더 문제. 칼슘:인 비율 불균형은 뼈 건강에 부정적."},
    "copper": {"desc":"철대사(세룰로플라스민), 결합조직 형성(라이실 산화효소), 항산화(SOD), 흑색 멜라닌 합성에 관여하는 미량 미네랄.","origin_type":"현대과학","origin_story":"구리(Cuprum)는 키프로스(Cyprus) 섬에서 이름 유래. 인류가 최초로 사용한 금속(기원전 9000년).","dosage":"0.9mg/일","evidence":"양호","food_sources":"간, 굴, 다크초콜릿, 캐슈넛, 해바라기씨","fun_fact":"아연과 구리는 흡수에서 경쟁. 아연을 고용량 보충하면 구리 결핍이 올 수 있어, 장기 아연 보충 시 구리도 함께 고려."},
    "manganese": {"desc":"SOD2(미토콘드리아 항산화효소), 뼈 형성(글리코실트랜스퍼라제), 탄수화물·지질 대사에 관여하는 미량 미네랄.","origin_type":"현대과학","origin_story":"마그네시아(Magnesia) 광석에서 마그네슘과 함께 발견. 두 원소가 이름이 비슷한 이유.","dosage":"1.8-2.3mg/일","evidence":"양호","food_sources":"통곡류, 견과류, 파인애플, 시금치, 녹차","fun_fact":"파인애플 1컵에 일일 권장량의 67%. 식물성 식품 위주 식단에서는 결핍이 거의 없음."},
    "molybdenum": {"desc":"아황산 산화효소, 잔틴 산화효소, 알데히드 산화효소의 보조인자. 황 함유 아미노산 대사에 필수.","origin_type":"현대과학","origin_story":"그리스어 molybdos(납 유사 광석)에서 유래. 1778년 스웨덴 화학자 Carl Wilhelm Scheele가 분리.","dosage":"45mcg/일","evidence":"양호","food_sources":"콩류, 곡류, 간, 견과류","fun_fact":"식품 섭취로 충분히 공급되어 결핍이 극히 드뭄. 보충제로 따로 섭취할 필요가 거의 없는 미네랄."},
    "vanadium": {"desc":"인슐린 유사 작용이 연구된 초미량 미네랄. 인슐린 수용체 인산화를 조절한다는 가설.","origin_type":"현대과학","origin_story":"스칸디나비아 여신 바나디스(Vanadis)에서 이름 유래. 필수 미네랄 여부는 아직 확정되지 않음.","dosage":"6-20mcg/일","evidence":"제한적","food_sources":"버섯, 후추, 파슬리, 딜, 맥주","fun_fact":"당뇨 연구에서 관심을 받았으나, 유효 용량이 독성 임계치에 가까워 보충제로서의 안전성 논란."},
    "boron": {"desc":"뼈 건강(칼슘·마그네슘·비타민D 대사), 에스트로겐·테스토스테론 대사에 관여하는 초미량 미네랄.","origin_type":"현대과학","origin_story":"1910년대 식물 필수 원소로 확인. 인체 필수성은 아직 공식 인정되지 않았으나 연구 축적 중.","dosage":"3-6mg/일","evidence":"보통","food_sources":"건자두, 건포도, 아보카도, 견과류, 포도","fun_fact":"건자두가 뼈 건강에 좋다는 연구의 주요 기전 중 하나가 붕소 함량. 칼슘만으로는 설명이 안 되는 효과."},
    "fluorine": {"desc":"치아 에나멜의 하이드록시아파타이트를 플루오로아파타이트로 전환하여 내산성을 강화. 충치 예방의 핵심.","origin_type":"현대과학","origin_story":"1901년 콜로라도 브라운 스테인(갈색 반점 치아) 연구에서 불소와 치아의 관계 발견. 1945년 미국 그랜드래피즈시에서 세계 최초 수돗물 불소 첨가.","dosage":"3-4mg/일","evidence":"매우 양호","food_sources":"불소 첨가 수돗물, 녹차, 새우, 게","fun_fact":"수돗물 불소 첨가는 CDC가 '20세기 10대 공중보건 업적' 중 하나로 선정. 동시에 가장 많은 논란을 받는 정책이기도."},
    "silicon": {"desc":"콜라겐과 결합조직의 가교 결합에 관여. 피부 탄력, 모발 두께, 뼈 무기질화에 연구.","origin_type":"현대과학","origin_story":"1972년 Edith Carlisle가 닭에서 규소 결핍 시 뼈·결합조직 이상을 보고하며 관심 시작.","dosage":"5-20mg/일","evidence":"보통","food_sources":"맥주(규산으로), 전곡류, 바나나, 녹두, 미네랄워터","fun_fact":"맥주가 의외의 규소 공급원. 맥아 가공 중 규산이 용출되어 맥주 1잔에 약 6mg의 규소 함유."},
    "copper-gluconate": {"desc":"구리의 글루콘산 킬레이트 형태. 일반 구리염 대비 위장 자극이 적고 흡수율이 개선.","origin_type":"현대과학","origin_story":"구리 보충의 필요성이 인식되며 위장 친화적 킬레이트 형태로 개발.","dosage":"0.9-2mg 구리/일","evidence":"양호","food_sources":"보충제 (구리 식품 공급원은 위 구리 항목 참조)","fun_fact":"모발·피부 색소에 구리가 필요. 구리 결핍 시 머리카락이 탈색되는 현상(백모)이 관찰됨."},
    "zinc-gluconate": {"desc":"아연의 글루콘산 결합 형태. 아연 로젠지(감기 초기 사용)와 보충제에서 가장 흔한 형태.","origin_type":"현대과학","origin_story":"아연 로젠지의 감기 이환 기간 단축 효과로 유명. 1984년 George Eby의 감기 연구에서 최초 보고.","dosage":"15-30mg 아연/일","evidence":"양호","food_sources":"보충제 (아연 식품 공급원은 위 아연 항목 참조)","fun_fact":"감기 증상 시작 24시간 이내에 아연 로젠지를 빨면 이환 기간이 평균 33% 단축된다는 메타분석."},
    "heme-iron": {"desc":"동물성 식품의 헤모글로빈·미오글로빈에서 유래한 철분 형태. 헴 수송체를 통해 직접 흡수되어 흡수율 15-35%.","origin_type":"식품유래","origin_story":"비헴철(식물성, 2-20%)의 낮은 흡수율 문제를 해결하기 위해 동물 유래 헴철을 보충제로 개발.","dosage":"18-27mg 철분/일","evidence":"양호","food_sources":"간, 소고기, 돼지고기(적색육), 조개·굴","fun_fact":"채식주의자는 비헴철만 섭취하므로 철분 권장량이 일반인의 1.8배(32mg). 비타민C 동반 섭취가 특히 중요."},

    # === FATTY ACIDS (12) ===
    "omega-3": {"desc":"EPA·DHA·ALA의 총칭. 세포막 유동성, 항염(레졸빈·프로텍틴), 뇌·망막 구조 성분, 심혈관 보호.","origin_type":"식품유래","origin_story":"1970년대 덴마크 연구진이 그린란드 이누이트의 심혈관 질환 발생률이 극도로 낮은 것을 관찰 → 해양 식단의 오메가3 효과 제안.","dosage":"EPA+DHA 1000-2000mg/일","evidence":"매우 양호","food_sources":"연어, 고등어, 정어리, 참치, 아마씨, 호두","fun_fact":"이누이트 연구가 오메가3 열풍의 시작이었지만, 최근 재분석에서 이누이트의 심혈관 질환이 과소평가되었을 가능성이 제기됨. 그럼에도 EPA/DHA의 효과 자체는 수천 건의 후속 연구로 확인."},
    "dha": {"desc":"도코사헥사에노산. 뇌 지방산의 약 40%, 망막의 60%를 구성. 태아·영아 뇌 발달에 결정적.","origin_type":"식품유래","origin_story":"1990년대 분유에 DHA 강화가 시작되며 영유아 뇌 발달 필수 영양소로 인식. 모유에는 자연 함유.","dosage":"200-500mg/일","evidence":"매우 양호","food_sources":"연어, 고등어, 정어리, 참치, 미세조류(비건DHA)","fun_fact":"뇌는 체중의 2%이지만 체내 DHA의 20%를 보유. DHA가 부족하면 세포막 강성이 높아져 신경전달 효율 저하."},
    "epa": {"desc":"에이코사펜타에노산. 항염 지질 매개체(레졸빈, 프로텍틴) 합성의 전구체. 심혈관·정신건강에 연구.","origin_type":"식품유래","origin_story":"EPA 단일 고함량 제제(Vascepa/이코사펜트에틸)가 2019년 심혈관 위험 감소 의약품으로 FDA 승인.","dosage":"1000-2000mg/일","evidence":"매우 양호","food_sources":"고등어, 정어리, 청어, 멸치","fun_fact":"우울증 연구에서 EPA:DHA 비율이 중요. EPA 함량이 60% 이상인 제품이 기분 개선에 더 효과적이라는 메타분석."},
    "omega-6": {"desc":"리놀레산(LA)·아라키돈산(AA) 계열. 세포막 구성, 피부 장벽, 염증 반응(프로스타글란딘) 조절.","origin_type":"식품유래","origin_story":"필수지방산으로 1930년대 발견. 현대 식단은 오메가6:3 비율이 15-20:1로 과잉 경향(이상적 비율 4:1 이하).","dosage":"11-17g/일","evidence":"양호","food_sources":"대두유, 옥수수유, 해바라기유, 호두, 참깨","fun_fact":"오메가6 자체가 나쁜 것이 아님. 문제는 오메가3과의 비율. 식물성 기름 과다 + 생선 섭취 부족이 현대인의 패턴."},
    "omega-7": {"desc":"팔미톨레산. 점막 조직(위, 장, 비뇨기) 보호와 피부 보습에 연구. 비타민나무 열매에 풍부.","origin_type":"현대과학","origin_story":"2000년대 이후 '잊혀진 오메가'로 재조명. 고등어에도 소량 함유되지만, 비타민나무(씨벅턴)가 가장 풍부.","dosage":"200-500mg/일","evidence":"보통","food_sources":"비타민나무열매(씨벅턴), 마카다미아너트, 고등어","fun_fact":"위장 점막이 건조한 사람(속쓰림, 안구건조증)에서 오메가7의 점막 보호 효과가 주목 받는 추세."},
    "omega-9": {"desc":"올레산. 체내 합성 가능(비필수). 올리브오일의 주성분. 심혈관 보호와 인슐린 감수성에 연구.","origin_type":"식품유래","origin_story":"지중해식 식단의 핵심. 올리브오일의 건강 효과 연구가 오메가9 인식의 배경. PREDIMED 연구(2013).","dosage":"별도 권장량 없음","evidence":"양호","food_sources":"올리브오일, 아보카도, 아몬드, 캐슈넛, 마카다미아","fun_fact":"올리브오일은 오메가9(올레산)이 약 73%. 올리브오일의 건강 효과가 올레산 때문인지, 동반 폴리페놀 때문인지 아직 논쟁 중."},
    "gamma-linolenic-acid": {"desc":"오메가6 계열이지만 항염 방향으로 대사되는 특이한 지방산. 프로스타글란딘E1(PGE1, 항염) 합성 전구체.","origin_type":"현대과학","origin_story":"달맞이꽃오일·보라지오일에서 주로 공급. 1980년대 David Horrobin이 GLA의 항염 가설을 대중화.","dosage":"240-480mg GLA/일","evidence":"보통","food_sources":"달맞이꽃오일, 보라지오일, 블랙커런트씨오일","fun_fact":"대부분의 오메가6는 염증을 촉진하지만, GLA는 PGE1 경로를 통해 항염 방향으로 작용하는 역설적 오메가6."},
    "evening-primrose-gla": {"desc":"달맞이꽃 종자유에서 추출한 GLA. 위의 GLA와 동일 성분의 특정 공급원 표기.","origin_type":"전통의학","origin_story":"북미 원주민이 달맞이꽃(Oenothera biennis)을 상처·피부에 사용한 전통. 씨앗 오일의 GLA가 핵심.","dosage":"500-2000mg 달맞이꽃오일/일","evidence":"보통","food_sources":"달맞이꽃오일 보충제","fun_fact":"달맞이꽃은 저녁에 꽃이 피어 'Evening Primrose'라 불림. GLA 함량은 약 8-10%(보라지 오일은 20-24%)."},
    "conjugated-linoleic-acid": {"desc":"CLA. 리놀레산의 이성질체. 체지방 감소(PPARγ 조절)와 근육량 유지에 연구. 지방세포의 지질 축적 억제.","origin_type":"현대과학","origin_story":"1987년 Michael Pariza가 구운 쇠고기에서 항돌연변이 물질로 발견. 이후 체조성 개선 연구로 확장.","dosage":"3-6g/일","evidence":"보통","food_sources":"풀먹인 소고기, 양고기, 치즈, 버터","fun_fact":"풀을 먹인 소(목초 사육)의 CLA 함량이 곡물 사육 대비 2-3배 높음. 반추 동물의 위에서 세균이 CLA를 합성."},
    "mct-oil": {"desc":"중쇄중성지방(6-12탄소). 긴 소화 경로를 거치지 않고 간에서 직접 케톤체로 전환. 빠른 에너지원.","origin_type":"현대과학","origin_story":"1950년대 지방 흡수 장애 환자의 영양 공급 목적으로 의료용 개발. 2010년대 방탄커피(Bulletproof Coffee) 트렌드로 대중화.","dosage":"15-30ml/일","evidence":"보통","food_sources":"코코넛오일(약 60% MCT), MCT오일(정제)","fun_fact":"MCT오일은 C8(카프릴산)과 C10(카프르산)이 가장 효율적으로 케톤체를 생성. C8 단일 오일이 프리미엄 제품."},
    "essential-fatty-acid": {"desc":"체내 합성이 불가능하여 반드시 식품으로 섭취해야 하는 지방산: 리놀레산(오메가6)과 알파리놀렌산(오메가3).","origin_type":"현대과학","origin_story":"1929년 George Burr 부부가 지방을 완전히 제거한 쥐 식단에서 피부 질환 등이 발생하는 것을 관찰하여 '필수지방산' 개념 제안.","dosage":"LA 11-17g/일, ALA 1.1-1.6g/일","evidence":"매우 양호","food_sources":"견과류, 씨앗류, 식물성 기름, 등푸른 생선","fun_fact":"필수지방산은 비타민처럼 결핍 시 특이 증상을 일으킴: 피부 건조·비늘화, 상처 치유 지연, 성장 장애."},
    "shark-liver-oil": {"desc":"심해상어 간유. 알콕시글리세롤(AKG) 함유. 면역 세포(대식세포, 호중구) 막 구성에 관여.","origin_type":"전통의학","origin_story":"북유럽 어부들이 수백 년간 민간 건강 보조제로 사용. 스칸디나비아에서는 'gold of the sea'로 불림.","dosage":"250-1000mg/일","evidence":"제한적","food_sources":"심해상어 간유 보충제","fun_fact":"상어는 연골어류로 뼈가 없고 면역체계가 독특. 상어에 대한 윤리적 우려로 합성 AKG 개발 연구 진행 중."},
}


def main():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "ingredients.json")
    path = os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    updated = 0
    for item in data:
        if item["tier"] != 1: continue
        if "content_description" in item: continue
        if item["id"] in T1:
            c = T1[item["id"]]
            item["content_description"] = c["desc"]
            item["origin_type"] = c["origin_type"]
            item["origin_story"] = c["origin_story"]
            item["dosage_reference"] = c["dosage"]
            item["evidence_level"] = c["evidence"]
            item["food_sources"] = c.get("food_sources","")
            item["fun_fact"] = c.get("fun_fact","")
            updated += 1
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"T1 batch 2 updated: {updated}/{len(T1)}")

if __name__ == "__main__":
    main()
