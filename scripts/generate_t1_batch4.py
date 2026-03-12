#!/usr/bin/env python3
"""T1 content batch 4: extract(37) + protein(6) + fiber(6) + probiotic(5) + enzyme(5) = 59 entries"""
import json, os

T1 = {
    # === EXTRACT (37) ===
    "red-ginseng": {"desc":"6년근 수삼을 찌고 건조한 홍삼. 진세노사이드(Rg1, Rb1 등)가 핵심. 면역 조절, 피로 회복, 혈류 개선에 가장 많은 한국 연구.","origin_type":"전통한방","origin_story":"한반도에서 1,500년 이상 재배·가공된 인삼 문화의 정수. 고려 시대부터 '고려인삼'으로 국제 교역. 증삼 가공법(찌기)이 진세노사이드 프로필을 변환.","dosage":"3-6g/일","evidence":"매우 양호","food_sources":"홍삼정, 홍삼액, 홍삼 캡슐","fun_fact":"진세노사이드 Rb 계열(진정)과 Rg 계열(흥분)이 상반 작용하여 '양방향 조절(bidirectional regulation)' 효과."},
    "ginkgo-biloba": {"desc":"은행잎 추출물. 플라보노이드(24%)와 테르페노이드(6%, 징코라이드·빌로바라이드) 표준화. 뇌·말초 혈류 개선.","origin_type":"전통한방","origin_story":"2억 7천만 년 전부터 존재한 '살아있는 화석'. 히로시마 원폭 그라운드 제로에서 최초로 새싹을 틔운 식물이 은행나무. 독일 Schwabe사가 EGb 761 표준화 추출물 개발.","dosage":"120-240mg/일","evidence":"양호","food_sources":"보충제 (은행 열매는 독성 주의)","fun_fact":"은행열매(백과)와 은행잎 추출물은 전혀 다름. 열매에는 독성 물질(4'-O-메틸피리독신)이 있어 과다 섭취 시 경련 위험."},
    "tribulus": {"desc":"트리뷸러스(남가새). 스테로이드 사포닌(프로토디오신)이 핵심. 테스토스테론 지지와 운동 능력에 연구.","origin_type":"전통의학","origin_story":"아유르베다에서 'Gokshura'(암소의 발굽)로 남성 건강에 수천 년 사용. 불가리아 역도 대표팀이 사용하며 1990년대 스포츠 보충제로 부상.","dosage":"500-1500mg/일","evidence":"보통","food_sources":"보충제","fun_fact":"동유럽 연구에서 효과가 보고되었으나 서구 연구에서는 재현 실패가 많아 논란. 지역별 식물 활성 성분 차이 가능성."},
    "pycnogenol": {"desc":"프랑스 해안 소나무(Pinus pinaster) 껍질 표준화 추출물. OPC 복합체. 피크노제놀은 Horphag Research의 등록 상표.","origin_type":"전통의학","origin_story":"1535년 Jacques Cartier 탐험대의 괴혈병 치료 일화 → 1951년 Jacques Masquelier가 땅콩 껍질·포도씨에서 OPC 분리 → 1979년 프랑스 해안송 껍질로 상업화.","dosage":"100-200mg/일","evidence":"양호","food_sources":"보충제 (피크노제놀 브랜드)","fun_fact":"피크노제놀은 400건 이상의 임상 연구가 발표된 프리미엄 원료. 일반 소나무 껍질 추출물과 피크노제놀은 표준화 기준이 다름."},
    "haematococcus": {"desc":"헤마토코쿠스 미세조류에서 추출한 천연 아스타잔틴. 스트레스 조건에서 조류가 자체 보호 물질로 아스타잔틴을 대량 축적.","origin_type":"현대과학","origin_story":"이스라엘·하와이에서 대규모 미세조류 배양 기술 개발. 합성 아스타잔틴(석유화학)과 구분되는 천연 소재.","dosage":"4-12mg/일","evidence":"양호","food_sources":"보충제 (헤마토코쿠스 배양)","fun_fact":"비 올 때 바위에 붉은 줄이 생기는 것은 헤마토코쿠스가 스트레스(건조)를 받아 아스타잔틴을 폭발 합성하기 때문."},
    "fenugreek": {"desc":"호로파 씨앗 추출. 4-하이드록시이소류신과 갈락토만난 함유. 인슐린 감수성·테스토스테론·모유 분비에 연구.","origin_type":"전통의학","origin_story":"이집트 에베르스 파피루스(기원전 1500년)에 기록. 아유르베다에서 소화·산후 회복에 처방. 커리의 핵심 향신료.","dosage":"500-600mg/일","evidence":"보통","food_sources":"호로파씨, 커리분말(소량)","fun_fact":"호로파를 섭취하면 체액(땀, 소변)에서 메이플시럽 냄새가 나는 것이 특징. Maple Syrup Urine Disease와 혼동될 수 있음."},
    "sophora-japonica": {"desc":"회화나무(꽃·열매) 추출물. 루틴과 소포라비오사이드 함유. 모세혈관 강화와 혈당 관리에 연구.","origin_type":"전통한방","origin_story":"한의학에서 회화나무 열매를 '괴각(槐角)', 꽃봉오리를 '괴화(槐花)'라 하여 혈을 식히고 지혈하는 약재로 사용.","dosage":"500-1000mg/일","evidence":"보통","food_sources":"보충제","fun_fact":"루틴의 주요 상업적 공급원. 메밀보다 회화나무 열매에서 루틴을 산업적으로 추출하는 것이 더 효율적."},
    "saw-palmetto": {"desc":"쏘팔메토(톱야자) 열매 추출. 지방산과 피토스테롤이 5-알파환원효소를 억제하여 전립선 비대증(BPH)에 연구.","origin_type":"전통의학","origin_story":"북미 원주민(세미놀족)이 비뇨기 건강에 수백 년 사용. 독일·프랑스에서 BPH 의약품으로 처방.","dosage":"320mg/일","evidence":"양호","food_sources":"보충제","fun_fact":"미국에서 가장 많이 팔리는 식물 보충제 중 하나. STEP/CAMUS 연구에서 위약 대비 효과 논란이 있었으나 유럽에서는 의약품 지위 유지."},
    "korean-angelica": {"desc":"한국 당귀(Angelica gigas). 데쿠르신·데쿠르시놀 안젤레이트가 핵심 성분. 중국 당귀(A. sinensis)와 다른 종.","origin_type":"전통한방","origin_story":"사물탕의 핵심 약재. '当帰(당에 돌아가다)' — 남편이 돌아오기를 바라는 아내에게 처방한 약초라는 유래.","dosage":"3-9g/일","evidence":"보통","food_sources":"한약재 (한국 당귀)","fun_fact":"한국 당귀와 중국 당귀는 같은 이름이지만 다른 종, 다른 활성 성분. 한국산은 데쿠르신, 중국산은 리구스틸라이드가 핵심."},
    "milk-thistle": {"desc":"밀크씨슬(엉겅퀴) 씨앗 추출. 실리마린(실리빈·실리디아닌·실리크리스틴 복합체)이 간세포 보호의 핵심.","origin_type":"전통의학","origin_story":"고대 그리스 의사 Dioscorides가 담즙 문제에 처방. 줄기를 꺾으면 흰 유액(milk)이 나와 Milk Thistle. 독일 Commission E가 간 질환에 승인.","dosage":"200-400mg 실리마린/일","evidence":"양호","food_sources":"보충제","fun_fact":"알광대버섯(Amanita phalloides) 중독 시 실리빈 정맥주사가 유일한 해독제로 유럽에서 사용됨."},
    "turmeric-curcumin": {"desc":"강황에서 커큐민을 표준화 추출. NF-kB 억제를 통한 항염이 핵심 기전. 관절, 소화, 인지에 연구.","origin_type":"전통의학","origin_story":"인도에서 4,000년 약용 역사. 아유르베다의 '황금 향신료'. 커큐민의 낮은 생체이용률을 높이기 위한 기술 경쟁(피페린, 파이토솜, 나노입자) 진행 중.","dosage":"500-2000mg/일","evidence":"양호","food_sources":"강황 가루(커큐민 ~3%), 보충제","fun_fact":"커큐민의 경구 생체이용률은 1-2%로 극히 낮음. 피페린(후추)이 2000% 높인다는 연구. 지방과 함께 먹으면 추가 향상."},
    "garcinia-cambogia": {"desc":"가르시니아 캄보지아 과피 추출. HCA(하이드록시시트르산)가 ATP-시트레이트 라이아제를 억제하여 지방 합성 차단.","origin_type":"전통의학","origin_story":"동남아·인도에서 수백 년간 커리 양념과 식욕 억제 목적으로 사용. 2012년 Dr. Oz 쇼에서 '기적의 지방 버스터'로 소개.","dosage":"500-1000mg HCA x3회/일 (식전)","evidence":"보통","food_sources":"보충제","fun_fact":"Dr. Oz 쇼 출연 후 FTC(미연방거래위원회)에 의해 과장 광고로 지적받은 대표적 다이어트 원료."},
    "korean-red-ginseng-compound": {"desc":"홍삼의 특정 진세노사이드 콤파운드K — 장내 미생물이 Rb1을 대사하여 생성하는 최종 활성 대사체.","origin_type":"전통한방","origin_story":"진세노사이드 자체는 분자량이 커서 흡수 곤란. 장내 세균이 당을 떼어내야 활성 Compound K로 전환. 이 발견이 발효 홍삼 개발로 이어짐.","dosage":"제품별 상이","evidence":"보통","food_sources":"발효 홍삼 제품","fun_fact":"같은 홍삼을 먹어도 장내 미생물 조성에 따라 Compound K 전환율이 개인차가 큼. 이것이 '홍삼이 나에게 안 맞는다'는 체감의 과학적 설명."},
    "tomato-extract": {"desc":"토마토 추출물. 리코펜 외에도 피토엔, 피토플루엔 등 무색 카로티노이드와 폴리페놀 함유.","origin_type":"식품유래","origin_story":"남미 안데스 원산. 16세기 유럽 전래 시 '독 사과(poison apple)'로 의심받음. 이탈리아에서 '황금 사과(pomodoro)'로 재명명.","dosage":"15-30mg 리코펜/일","evidence":"보통","food_sources":"토마토, 토마토 소스, 토마토 페이스트, 수박","fun_fact":"토마토 'paradox' — 달콤한 신선 토마토보다 가공된 토마토 제품(소스, 페이스트)에서 리코펜 흡수가 2-3배 높음."},
    "lion-s-mane": {"desc":"노루궁뎅이버섯(사자갈기버섯). 헤리세논·에리나신이 NGF(신경성장인자) 합성을 촉진. 인지 건강과 신경 재생에 연구.","origin_type":"전통한방","origin_story":"중의학에서 '후두고(猴頭菇, 원숭이 머리 버섯)'로 위장 건강에 사용. 일본에서 '야마부시타케'. 현대에는 뇌 건강 보충제로 재조명.","dosage":"500-3000mg/일","evidence":"보통","food_sources":"노루궁뎅이버섯(식용), 보충제","fun_fact":"NGF 발견자 Rita Levi-Montalcini(노벨상)의 연구를 계승하여, 일본 과학자 Kawagishi가 헤리세논의 NGF 유도 능력을 1991년 발견."},
    "reishi-mushroom": {"desc":"영지버섯(영지). 베타글루칸·트리테르펜(가노데릭산) 함유. 면역 조절과 스트레스 적응에 동아시아 전통 사용.","origin_type":"전통한방","origin_story":"중국에서 '만년초(萬年草)' 또는 '불로초(不老草)'로 불린 신비의 버섯. 진시황이 영지를 찾아 불로장생을 추구한 전설.","dosage":"1-3g/일","evidence":"보통","food_sources":"보충제 (영지 추출물, 영지 분말)","fun_fact":"영지의 쓴맛이 강할수록 가노데릭산(트리테르펜) 함량이 높다는 품질 지표. 야생 영지는 매우 드물어 현재는 인공 재배가 주류."},
    "chaga-mushroom": {"desc":"차가버섯. 자작나무에 기생하며 베타글루칸·멜라닌·베툴린 함유. 시베리아 전통 면역차.","origin_type":"전통의학","origin_story":"러시아·시베리아에서 수백 년간 면역차로 음용. 솔제니친의 소설 '암병동(Cancer Ward)'에 등장하여 서구에 알려짐.","dosage":"1-3g/일 (추출물)","evidence":"제한적","food_sources":"보충제, 차가 차","fun_fact":"차가는 버섯이 아니라 균핵(sclerotium) — 버섯의 자실체(갓)가 형성되기 전 단계. 야생 채취만 가능하며 인공 재배가 어려움."},
    "cordyceps": {"desc":"동충하초. 코르디세핀(3'-데옥시아데노신)과 다당류 함유. 산소 활용 효율과 운동 지구력에 연구.","origin_type":"전통한방","origin_story":"'겨울에는 벌레, 여름에는 풀'이라는 뜻의 冬蟲夏草. 티벳 고원에서 야크 목동이 발견한 전설. 야생 채취 가격은 금보다 비쌈.","dosage":"1-3g/일","evidence":"보통","food_sources":"보충제 (C. militaris 재배가 대부분)","fun_fact":"1993년 중국 여자 육상 대표팀이 세계 기록을 경신하며 동충하초 섭취를 공개. 이후 스포츠 보충제로 세계적 관심."},
    "turkey-tail": {"desc":"구름버섯(운지). PSK(크레스틴)·PSP(다당펩타이드) 함유. 일본에서 항암 보조 의약품으로 승인(1977).","origin_type":"전통한방","origin_story":"칠면조 꼬리를 닮아 Turkey Tail. 일본에서 PSK가 위암·대장암 보조 치료 의약품으로 30년 이상 처방됨.","dosage":"1-3g/일","evidence":"양호","food_sources":"보충제","fun_fact":"미국 NIH가 유방암 환자의 면역 회복에 Turkey Tail 추출물 연구에 공식 자금 지원(2012). 버섯 중 가장 강력한 면역 연구 기반."},
    "maitake": {"desc":"잎새버섯(마이타케). D-프랙션(베타글루칸 복합체)이 핵심. 면역 세포(대식세포, NK세포, T세포) 활성화 연구.","origin_type":"전통한방","origin_story":"일본어로 '춤추는 버섯(舞茸)' — 산에서 이 버섯을 발견한 사람이 기뻐서 춤을 췄다는 유래. 또는 버섯의 모양이 춤추는 나비를 닮았다는 설.","dosage":"1-3g/일","evidence":"보통","food_sources":"마이타케 버섯(식용), 보충제","fun_fact":"Maitake D-Fraction은 Hiroaki Nanba 교수(고베약대)가 개발한 표준화 추출물로 면역 연구의 대표 브랜드."},
    "shiitake-extract": {"desc":"표고버섯 추출물. 렌티난(베타글루칸)이 핵심. 일본에서 항암 보조 주사제(렌티난주)로 승인.","origin_type":"전통한방","origin_story":"중국 송나라(960년)에 최초 인공 재배 기록. 한·중·일 동아시아 식문화의 핵심 버섯.","dosage":"1-3g/일","evidence":"양호","food_sources":"표고버섯(식용), 보충제","fun_fact":"표고버섯을 햇볕에 말리면 에르고스테롤→비타민D2 전환이 일어나 비타민D 함량이 급증. 건조 표고가 생 표고보다 비타민D가 훨씬 높음."},

    # === PROTEIN (6) ===
    "collagen": {"desc":"체내 단백질의 약 30%를 차지하는 구조 단백질. 피부·뼈·연골·힘줄·혈관벽의 물리적 골격. I형~V형이 대표적.","origin_type":"현대과학","origin_story":"그리스어 kolla(접착제)에서 유래 — 원래 동물 뼈를 끓여 만든 접착제가 콜라겐. 2000년대 저분자 콜라겐 펩타이드(가수분해) 기술로 보충제 시장 폭발.","dosage":"5-15g/일","evidence":"양호","food_sources":"뼈국물, 돼지 껍데기, 닭발, 젤라틴, 보충제","fun_fact":"콜라겐의 1/3이 글리신, 1/4이 프롤린+하이드록시프롤린. 이 독특한 아미노산 비율 때문에 일반 단백질에서는 부족한 아미노산을 보충."},
    "whey-protein": {"desc":"유청단백질. 우유에서 카세인을 분리한 나머지 수용성 단백질. BCAA(류신 11%) 함량이 높아 근합성(mTOR) 신호에 최적.","origin_type":"식품유래","origin_story":"치즈 제조 시 남는 부산물(유청)이었으나, 1990년대 운동 보충제로 가치가 재발견. WPC(농축)→WPI(분리)→WPH(가수분해) 순 정제.","dosage":"20-40g/일","evidence":"매우 양호","food_sources":"보충제 (유청단백 분말)","fun_fact":"WPC(80% 단백질)은 면역 글로불린·락토페린이 보존, WPI(90%+)는 유당이 거의 제거. 유당불내증이면 WPI 선택."},
    "protein-supplement": {"desc":"단백질 보충제 총칭. 유청, 카세인, 대두, 완두, 현미 등 다양한 원료. 근합성과 체조성 관리의 기본 영양소.","origin_type":"현대과학","origin_story":"체중당 1.6-2.2g 단백질이 근합성에 최적이라는 메타분석(Morton, 2018). 식사만으로 충족 어려운 경우 보충제 활용.","dosage":"체중 1kg당 1.6-2.2g (보충제로 20-40g)","evidence":"매우 양호","food_sources":"식품(닭가슴살, 달걀, 두부) + 보충제","fun_fact":"단백질 타이밍('아나볼릭 윈도우' 30분 이내)보다 총 일일 단백질 섭취량이 더 중요하다는 것이 현재 과학적 합의."},
    "lactoferrin": {"desc":"모유·초유에 고농도로 함유된 철 결합 당단백질. 항균(세균의 철 공급 차단), 면역 조절, 장 점막 보호.","origin_type":"식품유래","origin_story":"모유의 면역 성분 연구에서 발견. '유(lacto) + 철(ferrin)' = 젖 속의 철 결합 단백질. 신생아 면역의 핵심.","dosage":"100-300mg/일","evidence":"양호","food_sources":"초유, 모유(성숙유는 감소), 유청, 발효 치즈","fun_fact":"락토페린 1분자가 철 2개를 결합. 세균은 철이 없으면 증식 불가 → 락토페린이 철을 빼앗아 정균 효과."},
    "type-2-collagen": {"desc":"비변성(undenatured) 2형 콜라겐. 닭 흉골 연골에서 저온 추출하여 3차 구조 보존. 경구 면역관용 기전으로 관절 연골 보호.","origin_type":"현대과학","origin_story":"HarvardMed David Trentham 교수의 경구 면역관용 연구(1993)에서 출발. 일반 가수분해 콜라겐과 다른 기전(면역 조절).","dosage":"40mg/일","evidence":"양호","food_sources":"보충제 (UC-II가 대표 브랜드)","fun_fact":"하루 40mg — 일반 콜라겐(5-10g)의 1/100 용량. 적은 양이 장의 파이어판(Peyer's patch)에서 면역 관용을 유도하는 것이 핵심."},
    "elastin-peptide": {"desc":"피부·혈관·폐의 탄력을 담당하는 탄성 단백질. 콜라겐이 '뼈대'라면 엘라스틴은 '고무줄'.","origin_type":"현대과학","origin_story":"엘라스틴은 성인이 되면 거의 새로 합성되지 않음. 가수분해 엘라스틴 펩타이드가 데스모신(가교 결합) 합성을 자극한다는 연구.","dosage":"75-150mg/일","evidence":"제한적","food_sources":"보충제 (가쓰오부시=가다랑어 유래)","fun_fact":"피부 엘라스틴의 반감기는 약 74년 — 사실상 평생 교체되지 않음. 자외선이 엘라스틴을 파괴하면 탄력이 돌아오지 않는 이유."},

    # === FIBER (6) ===
    "dietary-fiber": {"desc":"인간의 소화효소로 분해되지 않는 다당류 총칭. 수용성(발효→단쇄지방산)과 불용성(부피→장운동)으로 구분.","origin_type":"식품유래","origin_story":"1972년 Denis Burkitt(영국 의사)가 아프리카인의 낮은 대장암·심혈관 질환률을 식이섬유 섭취와 연결(Burkitt 가설).","dosage":"25-30g/일","evidence":"매우 양호","food_sources":"현미, 귀리, 사과, 브로콜리, 콩류, 아몬드","fun_fact":"장내 미생물이 수용성 식이섬유를 발효하면 부티르산(단쇄지방산)이 생성됨 — 대장 세포의 주 에너지원이자 항염·항종양 물질."},
    "prebiotics": {"desc":"장내 유익균의 '먹이'가 되는 비소화성 식이 성분. 프락토올리고당(FOS), 갈락토올리고당(GOS), 이눌린이 대표.","origin_type":"현대과학","origin_story":"1995년 Marcel Roberfroid가 'prebiotic' 개념을 최초 정의: '숙주의 건강에 유익한 장내 미생물의 성장 또는 활성을 선택적으로 자극하는 비소화성 식품 성분'.","dosage":"3-10g/일","evidence":"양호","food_sources":"양파, 마늘, 바나나, 치커리 뿌리, 아스파라거스","fun_fact":"프로바이오틱스(균 자체)와 프리바이오틱스(균의 먹이)를 합친 것이 신바이오틱스(synbiotics). 둘을 함께 섭취하면 시너지."},
    "galactooligosaccharide": {"desc":"갈락토올리고당(GOS). 유당에서 효소적으로 생산. 비피더스균의 선택적 증식을 촉진하는 프리바이오틱스.","origin_type":"현대과학","origin_story":"모유에 함유된 모유올리고당(HMO)을 모방하여 개발. 영유아 장 건강에 특히 초점.","dosage":"2.5-5g/일","evidence":"양호","food_sources":"모유, GOS 강화 분유, 보충제","fun_fact":"모유에는 200종 이상의 올리고당(HMO)이 있어 영아 장내 비피더스균을 선택적으로 키움. GOS는 이것의 산업적 대체."},
    "xylooligosaccharide": {"desc":"자일로올리고당(XOS). 자일란(목질)에서 추출한 프리바이오틱스. FOS보다 적은 양에서도 비피더스균 증식 효과.","origin_type":"현대과학","origin_story":"옥수수 속대, 사탕수수 찌꺼기 등 농업 부산물에서 추출하는 지속가능 원료.","dosage":"1-3g/일","evidence":"보통","food_sources":"보충제, 대나무 죽순(소량)","fun_fact":"XOS는 FOS 대비 1/3~1/5 용량에서 유사한 프리바이오틱 효과. 소량으로 효과적이어서 복부 팽만감이 적음."},
    "konjac": {"desc":"곤약감자(구약나물)에서 추출한 글루코만난. 수분을 50배 이상 흡수하여 팽창. 포만감과 콜레스테롤에 연구.","origin_type":"식품유래","origin_story":"일본에서 수백 년간 곤약(こんにゃく)으로 식용. 중국에서도 전통 식재료. EFSA가 콜레스테롤·체중 관련 건강강조표시 승인.","dosage":"3g/일 (식전)","evidence":"양호","food_sources":"곤약, 곤약면(실곤약), 보충제","fun_fact":"물과 함께 충분히 섭취하지 않으면 식도에서 팽창하여 질식 위험이 있으므로, 반드시 물 200ml 이상과 함께 섭취."},
    "chitosan": {"desc":"갑각류 껍질의 키틴을 탈아세틸화한 양이온성 다당류. 음전하인 지방·담즙산과 결합하여 흡수를 차단. 체중 관리에 연구.","origin_type":"현대과학","origin_story":"1859년 Charles Rouget이 키틴에서 키토산을 최초 생산. 의료용 상처 드레싱과 다이어트 보충제로 이중 활용.","dosage":"1-3g/일 (식전)","evidence":"보통","food_sources":"보충제 (새우·게 껍질 유래)","fun_fact":"키토산이 지방 1g당 결합하는 양은 제한적(약 4-13kcal 흡수 차단). 과장 광고가 많은 다이어트 원료."},

    # === PROBIOTIC (5) ===
    "probiotics": {"desc":"장내 미생물 생태계를 개선하는 살아있는 미생물 총칭. Lactobacillus, Bifidobacterium이 대표 속(genus). 균주 특이적 효능.","origin_type":"현대과학","origin_story":"1907년 Élie Metchnikoff(노벨상)가 불가리아 장수 마을과 발효유의 관계를 제안 — 프로바이오틱스 개념의 시작.","dosage":"10-500억 CFU/일","evidence":"양호","food_sources":"요구르트, 김치, 사우어크라우트, 낫토, 콤부차","fun_fact":"'프로바이오틱스' 효과는 균주(strain) 특이적. L. rhamnosus GG와 L. rhamnosus 다른 균주는 효능이 다름. 속(genus) 수준의 일반화는 과학적으로 부정확."},
    "lactobacillus": {"desc":"락토바실러스 속(genus). 소장 주 서식. 유산 생산으로 장내 pH를 낮춰 유해균 증식 억제. 가장 많은 연구.","origin_type":"현대과학","origin_story":"'lactis(젖) + bacillus(막대)' = 젖을 발효하는 막대 모양 세균. 2020년 분류 개정으로 23개 새 속으로 재분류(L. rhamnosus → Lacticaseibacillus rhamnosus).","dosage":"균주별 상이","evidence":"양호","food_sources":"요구르트, 김치, 사우어크라우트, 발효 피클","fun_fact":"2020년 분류 개정으로 Lactobacillus가 23개 속으로 쪼개졌지만, 소비자 혼란을 피하기 위해 대부분 제품은 여전히 Lactobacillus 표기."},
    "bifidobacterium": {"desc":"비피도박테리움 속. 대장 주 서식. Y자 모양 특징. 영유아 장에 가장 풍부하며 나이와 함께 감소.","origin_type":"현대과학","origin_story":"1899년 Henri Tissier(파스퇴르 연구소)가 모유 수유 영아 분변에서 최초 분리. 건강한 영아의 장내 세균 중 80% 이상 차지.","dosage":"균주별 상이","evidence":"양호","food_sources":"요구르트(비피더스 강화), 발효유","fun_fact":"비피더스균은 나이가 들면 급격히 감소. 60세 이상에서는 장내 비피더스균 비율이 영아기의 1/10 수준."},
    "saccharomyces-boulardii": {"desc":"프로바이오틱 효모(비세균). 항생제에 의해 죽지 않아, 항생제 연관 설사(AAD) 예방에 가장 강력한 근거.","origin_type":"현대과학","origin_story":"1923년 프랑스 미생물학자 Henri Boulard가 인도차이나에서 현지인이 리치·망고스틴 껍질로 설사를 치료하는 것을 관찰하여 분리.","dosage":"250-500mg/일","evidence":"매우 양호","food_sources":"보충제 (효모 배양)","fun_fact":"S. boulardii는 효모이므로 항생제에 의해 죽지 않음. 항생제 복용 중 프로바이오틱스를 먹어야 한다면 이것이 유일한 선택지."},
    "postbiotics": {"desc":"프로바이오틱스의 대사산물·세포벽 성분·비활성 균체. 살아있는 균 없이도 면역 조절 효과를 발휘.","origin_type":"현대과학","origin_story":"2021년 ISAPP(국제프로바이오틱스학회)가 포스트바이오틱스를 '숙주에 건강 이점을 부여하는 비활성 미생물 및/또는 그 성분의 제제'로 공식 정의.","dosage":"제품별 상이","evidence":"보통","food_sources":"김치·된장·요구르트(발효 부산물로 자연 함유)","fun_fact":"프로바이오틱스의 한계(냉장 필요, 장까지 생존율, 면역저하자 감염 위험)를 보완하는 차세대 개념. 상온 보관 가능."},

    # === ENZYME (5) ===
    "nattokinase": {"desc":"낫토(나또) 발효 과정에서 Bacillus subtilis var. natto가 생성하는 세린 프로테아제. 피브린 용해(혈전 분해)에 연구.","origin_type":"식품유래","origin_story":"1987년 일본 과학자 Hiroyuki Sumi가 낫토의 혈전 용해 성분을 발견. 페트리 접시에 낫토를 올려놓은 심플한 실험에서 시작.","dosage":"2000-4000 FU/일","evidence":"양호","food_sources":"낫토(나또) — 일본 전통 발효 대두","fun_fact":"Sumi 교수가 낫토를 피브린 판에 올려놓고 집에 갔다가 돌아오니 피브린이 녹아 있었다는 우연한 발견. '세렌디피티의 과학'."},
    "bromelain": {"desc":"파인애플 줄기에서 추출한 시스테인 프로테아제 복합체. 단백질 소화 보조, 항염(피브린 분해), 부종 감소에 연구.","origin_type":"식품유래","origin_story":"1891년 처음 파인애플에서 분리. 독일에서 수술 후 부종·관절 염증에 의약품으로 처방.","dosage":"200-500mg/일 (식간: 항염, 식후: 소화)","evidence":"양호","food_sources":"파인애플(주로 줄기), 보충제","fun_fact":"파인애플을 많이 먹으면 혀가 아린 이유가 브로멜라인이 구강 점막 단백질을 분해하기 때문. 가열하면 효소가 불활성화."},
    "serrapeptase": {"desc":"누에나방 장내 세균(Serratia E15)이 생산하는 프로테아제. 원래 누에가 고치(실크 단백질)를 녹이고 나올 때 사용하는 효소.","origin_type":"현대과학","origin_story":"일본에서 1960년대 항염 의약품으로 개발. 유럽에서 수술 후 부종과 통증 완화에 사용.","dosage":"10,000-60,000 SPU/일","evidence":"보통","food_sources":"보충제 (발효 생산)","fun_fact":"누에가 고치를 뚫고 나오는 부드럽지만 강력한 단백질 분해 — 이 자연 현상에서 착안한 효소 의약품."},
    "digestive-enzyme": {"desc":"아밀라아제(전분), 프로테아제(단백질), 리파아제(지방) 등 소화효소 복합체. 소화 보조와 영양소 흡수 개선.","origin_type":"현대과학","origin_story":"췌장 효소 대체요법(PERT)이 의학적 기원. 췌장 기능 부전 환자에서 표준 치료로 100년 이상 사용.","dosage":"식사와 함께 1-2캡슐","evidence":"양호","food_sources":"보충제 (동물 췌장 or 미생물 발효 유래)","fun_fact":"건강한 사람은 체내 소화효소가 충분하므로 보충 효과가 제한적. 유당불내증(락타아제)이나 FODMAP 민감(알파갈락토시다아제) 같은 특정 상황에서 효과적."},
    "papain": {"desc":"파파야 열매에서 추출한 시스테인 프로테아제. 브로멜라인과 유사한 단백질 분해 효소. 소화 보조와 항염에 연구.","origin_type":"식품유래","origin_story":"중남미 원주민이 고기를 파파야 잎에 싸서 부드럽게 만든 전통. 상업적 육류 연화제(meat tenderizer)의 원료.","dosage":"200-500mg/일","evidence":"보통","food_sources":"파파야(특히 덜 익은 청 파파야), 보충제","fun_fact":"덜 익은 청 파파야에 파파인이 가장 풍부. 완전히 익으면 효소 활성이 감소. 파파야 산지에서는 고기 요리에 청 파파야를 함께 넣는 이유."},
}


def main():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "ingredients.json")
    path = os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    updated = 0
    missing = []
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
        else:
            missing.append(f'{item["id"]} ({item["name"]})')
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"T1 batch 4 updated: {updated}/{len(T1)}")
    if missing:
        print(f"Still missing: {len(missing)}")
        for m in missing:
            print(f"  - {m}")
    # Final verification
    t1_done = sum(1 for i in data if i['tier']==1 and 'content_description' in i)
    t1_total = sum(1 for i in data if i['tier']==1)
    print(f"\nOverall T1: {t1_done}/{t1_total}")

if __name__ == "__main__":
    main()
