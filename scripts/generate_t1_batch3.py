#!/usr/bin/env python3
"""T1 content batch 3: other_functional (34) entries"""
import json, os

T1 = {
    "coq10": {"desc":"미토콘드리아 전자전달계의 전자 운반체이자 지용성 항산화제. 심장·근육처럼 에너지 수요가 높은 조직에 농축.","origin_type":"현대과학","origin_story":"1957년 위스콘신대 Frederick Crane이 소 심장 미토콘드리아에서 발견. 1978년 Peter Mitchell이 전자전달계에서의 역할로 노벨상 수상.","dosage":"100-300mg/일","evidence":"양호","food_sources":"내장육(심장, 간), 소고기, 정어리, 시금치, 브로콜리","fun_fact":"스타틴(콜레스테롤 약)이 CoQ10 합성도 억제하여 근육통 부작용 유발 가능. 스타틴 복용자의 CoQ10 보충이 연구되는 이유."},
    "coenzyme-q10-ubiquinone": {"desc":"CoQ10의 산화형(ubiquinone). 체내에서 유비퀴놀(환원형)로 전환 후 항산화 기능. 40대 이후 전환 효율 감소.","origin_type":"현대과학","origin_story":"ubiquinone은 'ubiquitous(어디에나)'에서 유래. 모든 세포의 미토콘드리아에 존재하기 때문.","dosage":"100-300mg/일","evidence":"양호","food_sources":"위 CoQ10 항목 참조","fun_fact":"40대 이후에는 유비퀴논→유비퀴놀 전환 효율이 떨어져, 나이 든 사용자는 유비퀴놀 형태가 더 효율적이라는 주장."},
    "ubiquinol": {"desc":"CoQ10의 환원형(활성형). 유비퀴논을 체내에서 전환할 필요 없이 직접 항산화 작용. 생체이용률이 유비퀴논의 2-8배.","origin_type":"현대과학","origin_story":"일본 카네카(Kaneka)사가 안정화된 유비퀴놀 보충제를 최초 상업화(QH). 산화되기 쉬운 환원형을 안정화하는 기술이 핵심.","dosage":"100-200mg/일","evidence":"양호","food_sources":"보충제 전용","fun_fact":"유비퀴놀은 산화에 매우 민감. 캡슐이 주황색에서 갈색으로 변했다면 산화된 것이므로 폐기."},
    "glucosamine": {"desc":"연골 기질의 글리코사미노글리칸(GAG) 합성의 전구체. 관절액의 점성과 완충 기능 유지에 관여.","origin_type":"현대과학","origin_story":"1969년 독일에서 관절 건강 의약품으로 처음 사용. 새우·게 등 갑각류 껍질의 키틴에서 추출.","dosage":"1500mg/일","evidence":"양호","food_sources":"새우·게 껍질(보충제로만 유효 용량 섭취 가능)","fun_fact":"GAIT 연구(2006)에서 글루코사민+콘드로이틴 병용이 중등도-중증 관절통에서 유의미한 효과. 경증에서는 위약 대비 차이 미미."},
    "chondroitin-sulfate": {"desc":"연골 기질의 주요 GAG. 수분을 끌어당겨 연골의 탄력과 완충 기능을 유지. 글루코사민과 병용이 일반적.","origin_type":"현대과학","origin_story":"상어 또는 소 연골에서 추출. 유럽에서 1960년대 관절 건강 의약품으로 사용 시작.","dosage":"800-1200mg/일","evidence":"양호","food_sources":"보충제 (연골, 뼈국물에 소량)","fun_fact":"경구 콘드로이틴은 분자량이 커서 흡수율 논란. 저분자 형태(1만 Da 이하)가 흡수에 유리하다는 연구."},
    "msm": {"desc":"유기 황 화합물. 결합조직(콜라겐, 케라틴)의 이황화 결합에 황을 공급. 항염과 관절 건강에 연구.","origin_type":"현대과학","origin_story":"1970년대 Robert Herschler와 Stanley Jacob이 DMSO(산업용 용매)의 대사산물인 MSM의 생체 활성을 연구.","dosage":"1500-3000mg/일","evidence":"보통","food_sources":"양배추, 브로콜리, 양파, 마늘(극소량)","fun_fact":"MSM은 DMSO(디메틸설폭시드)가 체내에서 산화된 형태. DMSO는 피부 투과 촉진제로도 사용되는 산업 화학물질."},
    "methylsulfonylmethane-msm": {"desc":"위 MSM과 동일 성분의 관절 특화 표기. 글루코사민·콘드로이틴과의 3종 콤보가 관절 건강 프리미엄 제품의 표준.","origin_type":"현대과학","origin_story":"관절 건강 3대 원료(글루코사민+콘드로이틴+MSM) 콤보 트렌드에서 파생된 별도 등록.","dosage":"1500-3000mg/일","evidence":"보통","food_sources":"위 MSM 항목 참조","fun_fact":"관절 3종 콤보는 한국 건기식 관절 카테고리에서 가장 흔한 조합."},
    "lutein": {"desc":"카로티노이드. 황반(macula)에 지아잔틴과 함께 농축되어 청색광(블루라이트) 필터와 항산화 방어 역할.","origin_type":"식품유래","origin_story":"라틴어 luteus(노란색)에서 유래. 2006년 AREDS2 연구에서 루테인+지아잔틴이 눈 건강에 유효함을 대규모로 확인.","dosage":"10-20mg/일","evidence":"매우 양호","food_sources":"케일, 시금치, 브로콜리, 달걀노른자, 옥수수","fun_fact":"달걀노른자의 노란색이 루테인과 지아잔틴 때문. 방목 달걀이 공장식 달걀보다 루테인 함량이 높음."},
    "zeaxanthin": {"desc":"루테인과 함께 황반의 '선글라스' 역할을 하는 카로티노이드. 황반 중심부(fovea)에 더 높은 농도.","origin_type":"식품유래","origin_story":"옥수수(Zea mays)에서 이름 유래. AREDS2에서 루테인과 함께 연구.","dosage":"2mg/일 (루테인과 5:1 비율)","evidence":"양호","food_sources":"고지베리(구기자), 빨간 파프리카, 옥수수, 달걀노른자","fun_fact":"루테인:지아잔틴 = 5:1 비율이 자연 식단에서의 비율과 유사하여 보충제에서도 이 비율 채택."},
    "astaxanthin": {"desc":"카로티노이드 중 가장 강력한 항산화력(비타민E의 550배, 베타카로틴의 40배). 세포막 내 '가교' 위치로 독특한 보호.","origin_type":"현대과학","origin_story":"연어·새우의 붉은색이 아스타잔틴. 헤마토코쿠스 미세조류에서 추출하는 것이 현재 주류.","dosage":"4-12mg/일","evidence":"양호","food_sources":"연어(양식>자연산, 사료 첨가), 새우, 게, 랍스터","fun_fact":"플라밍고의 분홍색도 아스타잔틴. 야생 연어의 붉은 살색은 먹이사슬(크릴→연어)을 통한 아스타잔틴 축적."},
    "resveratrol": {"desc":"적포도주의 폴리페놀. SIRT1 활성화를 통한 세포 장수 경로 자극, 항염, 혈관 내피 보호에 연구.","origin_type":"식품유래","origin_story":"1992년 '프렌치 패러독스' — 프랑스인이 고지방 식단에도 심혈관 질환이 적은 이유로 적포도주 지목. David Sinclair(하버드)의 장수 유전자 연구로 세계적 주목.","dosage":"150-500mg/일","evidence":"보통","food_sources":"적포도 껍질, 적포도주, 땅콩, 블루베리, 다크초콜릿","fun_fact":"레스베라트롤의 경구 생체이용률은 1% 미만. 흡수되더라도 빠르게 대사됨. 트랜스-레스베라트롤이 시스-형보다 생활성이 높음."},
    "alpha-lipoic-acid": {"desc":"미토콘드리아 효소(피루브산탈수소효소)의 보조인자이자, 수용성·지용성 모두에서 작용하는 '만능 항산화제'.","origin_type":"현대과학","origin_story":"1937년 발견. 당뇨병성 신경병증 치료제로 독일에서 의약품(Thioctacid)으로 처방. 항산화와 혈당 조절 이중 연구.","dosage":"300-600mg/일","evidence":"양호","food_sources":"시금치, 브로콜리, 간, 효모(극소량)","fun_fact":"다른 항산화제(비타민C, E, 글루타치온)를 재생시키는 '항산화제의 항산화제'. R형이 체내 자연 형태이며 S형보다 효과적."},
    "quercetin": {"desc":"가장 풍부한 식이 플라보노이드. 비만세포 안정화(히스타민 억제), 항염(NF-kB), 항바이러스, 세놀리틱(노화세포 제거) 연구.","origin_type":"식품유래","origin_story":"라틴어 quercetum(참나무 숲)에서 유래. 양파, 사과, 녹차에 풍부. 2020년 코로나19 대유행 중 면역 보충제로 주목.","dosage":"500-1000mg/일","evidence":"보통","food_sources":"양파(특히 붉은 양파), 사과, 베리류, 녹차, 케이퍼","fun_fact":"퀘르세틴 + 다사티닙 조합이 노화 세포(senescent cells)를 선택적으로 제거하는 세놀리틱 요법으로 노화 연구의 최전선."},
    "royal-jelly": {"desc":"여왕벌 전용 영양물질. 10-HDA(지방산), 로열릭틴(단백질) 등 고유 성분. 면역과 피로에 전통 사용.","origin_type":"식품유래","origin_story":"일벌과 여왕벌의 유일한 차이가 로열젤리 섭취. 같은 유전자에서 40배 수명 차이를 만드는 후성유전학의 상징.","dosage":"300-6000mg/일","evidence":"보통","food_sources":"보충제 (양봉 수확)","fun_fact":"여왕벌은 일벌과 유전적으로 동일. 로열젤리만 먹고 자라면 여왕벌이 되고, 꽃가루를 먹으면 일벌. 후성유전학의 대표 사례."},
    "propolis": {"desc":"꿀벌이 나무 수지에 효소를 섞어 만든 항균 물질. 벌집의 '천연 방부제'. CAPE(항염·항산화) 함유.","origin_type":"전통의학","origin_story":"그리스어 pro(앞) + polis(도시) = '도시를 지키는 것'. 히포크라테스가 상처와 궤양에 처방한 기록.","dosage":"300-500mg/일","evidence":"양호","food_sources":"보충제, 프로폴리스 스프레이","fun_fact":"벌집 내부 온도는 35°C, 습도 95% — 세균·곰팡이 번식에 최적이지만 프로폴리스 덕분에 내부는 거의 무균."},
    "beta-glucan": {"desc":"효모·버섯·귀리의 다당류. 면역계의 패턴인식 수용체(Dectin-1)에 결합하여 대식세포·NK세포를 활성화.","origin_type":"현대과학","origin_story":"1940년대 Louis Pillemer가 효모 세포벽의 면역 활성 물질 발견. 1,3/1,6 구조(효모)와 1,3/1,4 구조(귀리)로 면역·콜레스테롤 각각 연구.","dosage":"250-500mg/일","evidence":"양호","food_sources":"효모, 표고버섯, 영지버섯, 귀리, 보리","fun_fact":"귀리 베타글루칸은 콜레스테롤에, 효모 베타글루칸은 면역에 주로 연구. 같은 '베타글루칸'이지만 구조와 효능이 다름."},
    "plant-sterol": {"desc":"식물 세포막의 구성 성분. 소장에서 콜레스테롤과 흡수를 경쟁하여 혈중 LDL 콜레스테롤을 5-15% 낮춤.","origin_type":"현대과학","origin_story":"2000년 FDA가 식물스테롤/스타놀의 콜레스테롤 저하 건강강조표시 승인.","dosage":"2g/일","evidence":"매우 양호","food_sources":"식물성 기름, 견과류, 콩류, 곡류(소량)","fun_fact":"일일 2g 식물스테롤 = LDL 콜레스테롤 ~10% 감소. 이 효과는 스타틴과 독립적이므로 병용 시 추가 효과."},
    "isoflavone": {"desc":"대두의 식물성 에스트로겐(제니스테인, 다이드제인). 에스트로겐 수용체 β에 선택적 결합하여 갱년기 증상 완화.","origin_type":"식품유래","origin_story":"아시아 여성의 갱년기 증상이 서구보다 가볍다는 역학 관찰 → 콩 식품 섭취와의 관련성 연구.","dosage":"40-80mg/일","evidence":"양호","food_sources":"콩, 두부, 된장, 낫토, 에다마메","fun_fact":"에쿠올(equol) — 다이드제인의 장내 대사산물 — 을 생산하는 능력이 아시아인에서 60%, 서양인에서 30%로 차이. 이것이 효과 차이의 원인 가설."},
    "melatonin": {"desc":"송과체에서 분비되는 수면 호르몬. 일주기 리듬(circadian rhythm) 조절의 마스터 시계. 총 수면 시간 증가보다 입면 시간 단축에 더 효과적.","origin_type":"현대과학","origin_story":"1958년 Aaron Lerner가 소 송과체에서 분리. 그리스어 melas(검은) + tonos(변화)에서 유래 — 멜라닌(피부 색소) 연구 중 우연히 발견.","dosage":"0.5-3mg/일 (취침 30-60분 전)","evidence":"양호","food_sources":"타트체리, 피스타치오, 포도, 달걀, 우유","fun_fact":"한국에서는 전문의약품이지만 미국에서는 식품보충제로 자유 판매. 고용량(10mg+)보다 저용량(0.5-1mg)이 생리적 수준과 가까움."},
    "squalene": {"desc":"트리테르펜 탄화수소. 피부 피지의 약 12%를 구성하며 보습·보호막 형성. 심해상어 간유에서 추출하거나 올리브에서 식물성으로 공급.","origin_type":"현대과학","origin_story":"1906년 일본 화학자 Mitsumaru Tsujimoto가 상어(squalus) 간유에서 발견하여 이름 유래. 이후 올리브유에서도 높은 함량 확인.","dosage":"500-2000mg/일","evidence":"제한적","food_sources":"올리브오일, 아마란스 기름, 쌀겨유, 밀배아유","fun_fact":"스쿠알렌은 코로나19 백신의 면역증강제(adjuvant)로도 사용됨. MF59(노바백스)가 스쿠알렌 기반."},
    "ceramide": {"desc":"피부 각질층 세포간 지질의 약 50%를 구성하는 스핑고지질. 피부 장벽의 '벽돌 사이 시멘트' 역할.","origin_type":"현대과학","origin_story":"라틴어 cera(밀랍)에서 유래. 피부과에서 아토피·건조증 관리의 핵심 성분으로 인식.","dosage":"350mcg/일 (식물 유래)","evidence":"보통","food_sources":"고구마, 쌀, 밀(식물성 글루코실세라마이드)","fun_fact":"나이가 들면 체내 세라마이드 합성이 감소하여 피부 건조가 심해짐. 경구 보충과 외용 모두 연구 중."},
    "saccharomyces-cerevisiae": {"desc":"맥주효모(빵효모). 비타민B군, 크롬, 셀레늄, 베타글루칸의 천연 복합 공급원.","origin_type":"식품유래","origin_story":"인류가 가장 오래 사용한 미생물. 기원전 3000년 이집트 맥주·빵 제조부터. 1996년 최초로 전체 유전체가 해독된 진핵생물.","dosage":"1-3g/일","evidence":"양호","food_sources":"맥주효모 분말/정제, 뉴트리셔널 이스트","fun_fact":"뉴트리셔널 이스트(영양효모)는 비활성 맥주효모에 비타민B12를 강화한 것. 비건이 B12와 감칠맛을 동시에 얻는 식품."},
    "dhea": {"desc":"부신에서 분비되는 프로호르몬. 테스토스테론과 에스트로겐의 전구체. 25세 이후 매년 2-3%씩 감소.","origin_type":"현대과학","origin_story":"1934년 발견. 'DHEA는 노화의 바이오마커'라는 가설이 1990년대 안티에이징 보충제 열풍을 일으킴.","dosage":"25-50mg/일","evidence":"보통","food_sources":"보충제 전용 (체내 합성)","fun_fact":"한국에서는 의약품 분류이지만 미국에서는 자유 판매. 도핑 검사 양성 반응을 일으킬 수 있어 운동선수 주의."},
    "gamma-oryzanol": {"desc":"쌀겨에서 추출한 페룰산 에스터. 자율신경 조절과 갱년기 증상 완화에 일본에서 1960년대부터 의약품으로 사용.","origin_type":"식품유래","origin_story":"쌀(Oryza sativa)에서 이름 유래. 일본에서 갱년기·자율신경 조절 처방약으로 수십 년 사용 역사.","dosage":"300mg/일","evidence":"보통","food_sources":"쌀겨, 쌀겨유(미강유)","fun_fact":"감마오리자놀은 일본에서 의약품, 한국에서 건기식 원료, 미국에서 식품보충제로 각각 다른 규제 분류."},
    "rutin": {"desc":"플라보노이드 배당체. 모세혈관 투과성을 줄이고 혈관벽을 강화. 항산화와 항염에 연구.","origin_type":"식품유래","origin_story":"운향(Ruta graveolens)에서 이름 유래. 1930년대 Albert Szent-Györgyi가 '비타민P(투과성 비타민)'로 제안했던 물질.","dosage":"500-1000mg/일","evidence":"보통","food_sources":"메밀, 감귤류, 아스파라거스, 무화과","fun_fact":"메밀(소바, 냉면)이 혈관 건강에 좋다는 전통 지식의 과학적 근거 중 하나가 루틴 함량."},
    "lycopene": {"desc":"토마토의 적색 카로티노이드. 비타민A로 전환되지 않는(non-provitamin A) 강력한 단일항산소 소거제.","origin_type":"식품유래","origin_story":"토마토(Solanum lycopersicum)에서 이름 유래. 1990년대 하버드 연구에서 토마토 섭취와 전립선 건강의 역학적 관련성 보고.","dosage":"6-30mg/일","evidence":"보통","food_sources":"토마토(특히 조리·가공), 수박, 핑크자몽, 구아바","fun_fact":"생 토마토보다 토마토소스·케첩에서 리코펜 흡수가 2-3배 높음. 지방(올리브오일)과 함께 조리하면 더 증가."},
    "octacosanol": {"desc":"사탕수수 왁스에서 추출한 장쇄 알코올. 지질 대사와 운동 지구력에 연구.","origin_type":"현대과학","origin_story":"1990년대 쿠바에서 사탕수수 왁스 유래 PPG(Policosanol) 연구. 콜레스테롤 저하 효과 주장.","dosage":"10-20mg/일","evidence":"보통","food_sources":"사탕수수 왁스, 밀배아유, 쌀겨유","fun_fact":"쿠바산 폴리코사놀의 콜레스테롤 효과는 쿠바 외 연구에서 재현 실패가 많아 논란이 있음."},
    "phosphatidylserine": {"desc":"세포막 인지질. 뇌 세포막의 약 15%를 구성. 인지 기능, 스트레스 반응, 운동 후 코르티솔에 연구.","origin_type":"현대과학","origin_story":"원래 소 뇌에서 추출했으나 광우병 우려로 현재는 대두 레시틴에서 식물성 추출.","dosage":"100-300mg/일","evidence":"보통","food_sources":"대두, 흰강낭콩, 달걀노른자, 간, 고등어","fun_fact":"2003년 FDA가 PS의 인지 건강 '한정적 건강강조표시(qualified health claim)' 를 승인한 드문 사례."},
    "chlorogenic-acid": {"desc":"커피·사과의 주요 폴리페놀. 알파글루코시다아제와 G6Pase 억제로 포도당 흡수와 간 당 방출을 억제.","origin_type":"식품유래","origin_story":"커피 한 잔에 약 70-200mg 함유. 녹색커피빈 추출물의 핵심 활성 성분.","dosage":"200-400mg/일","evidence":"보통","food_sources":"커피, 녹색커피빈, 사과, 블루베리, 아티초크","fun_fact":"클로로겐산은 로스팅 과정에서 대부분 파괴됨. 라이트 로스트 커피가 다크 로스트보다 클로로겐산이 높음."},
    "hesperidin": {"desc":"감귤류 과피의 주요 플라보노이드. 모세혈관 투과성 개선과 혈류 촉진. 냉증(말초 혈류 개선)에 일본 연구.","origin_type":"식품유래","origin_story":"그리스 신화의 헤스페리데스(황금사과를 지키는 님프)에서 이름 유래. 감귤류의 쓴맛 성분 중 하나.","dosage":"500mg/일","evidence":"양호","food_sources":"오렌지·자몽 과피, 레몬, 귤","fun_fact":"감귤 과즙보다 껍질(과피)에 헤스페리딘이 10배 이상 농축. 귤 껍질(진피)을 한약에서 사용하는 과학적 근거."},
    "red-yeast-rice": {"desc":"홍국(붉은 효모 쌀). 모나콜린K(=로바스타틴)를 자연 생성. 스타틴 계열 콜레스테롤 약과 동일 성분.","origin_type":"전통한방","origin_story":"중국 당나라(900년경) 의서에 홍국 기록. 1987년 Merck가 아스퍼길러스에서 로바스타틴을 의약품으로 개발(메바코). 같은 성분이 식품과 의약품으로 이중 존재.","dosage":"모나콜린K 10mg/일","evidence":"매우 양호","food_sources":"홍국 보충제 (붉은 효모 쌀 발효)","fun_fact":"동일 성분이 보충제(홍국)로는 합법이고 의약품(로바스타틴)으로도 존재하는 규제 모순. 유럽에서는 모나콜린K 함량 규제 논란."},
    "fucoidan": {"desc":"갈조류(미역, 다시마, 모즈쿠)의 황산화 다당류. NK세포 활성, 항종양, 위 점막 보호에 연구.","origin_type":"식품유래","origin_story":"1913년 Karl Kylin이 미역에서 처음 분리. 후코스(fucose) 당이 주 구성 성분이라 이름 유래.","dosage":"1-3g/일","evidence":"보통","food_sources":"모즈쿠, 미역, 다시마, 톳","fun_fact":"오키나와 장수 식단의 해조류(모즈쿠) 소비와 후코이단의 관련성이 주목받으며 일본에서 활발히 연구."},
    "hyaluronic-acid": {"desc":"체내 결합조직에 광범위하게 존재하는 글리코사미노글리칸. 분자량 1g당 6L의 수분 보유. 피부·관절액의 보습·윤활 핵심.","origin_type":"현대과학","origin_story":"1934년 컬럼비아대 Karl Meyer가 소 눈의 초자체(vitreous humor)에서 발견. hyalos(유리) + uronic acid에서 이름 유래.","dosage":"120-240mg/일","evidence":"보통","food_sources":"닭벼슬, 뼈국물(소량). 대부분 발효법 생산.","fun_fact":"히알루론산 필러(피부과)와 경구 보충제는 분자량이 다름. 경구 저분자 HA(~300kDa)가 흡수에 유리하다는 연구."},
    "methylsulfonylmethane": {"desc":"히알루론산나트륨 — 히알루론산의 나트륨 염 형태. 수용성이 더 높아 화장품과 보충제에서 선호되는 형태.","origin_type":"현대과학","origin_story":"히알루론산의 수용성을 높이기 위해 나트륨 염으로 가공한 형태. 화장품과 건기식에서 가장 흔한 HA 형태.","dosage":"120-240mg/일","evidence":"보통","food_sources":"보충제, 화장품","fun_fact":"피부에 바르는 HA(외용)는 고분자가 보습에 유리하고, 먹는 HA(경구)는 저분자가 흡수에 유리. 같은 성분이지만 최적 분자량이 다름."},
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
    print(f"T1 batch 3 updated: {updated}/{len(T1)}")

if __name__ == "__main__":
    main()
