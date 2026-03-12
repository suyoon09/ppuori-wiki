#!/usr/bin/env python3
"""T2 extract content batch 2: remaining 97 entries"""
import json, os

T2_EXT = {
    "citrus-aurantium": {"desc":"시트러스 오란티움(쓴 오렌지) 추출. 시네프린이 핵심 성분. 에페드린 유사 교감신경 자극으로 열생산 촉진.","origin_type":"현대과학","origin_story":"에페드라(마황) 금지 이후 대체 다이어트 성분으로 부상. 시네프린은 에페드린보다 심혈관 부작용이 적다고 주장됨.","dosage":"10-20mg 시네프린/일","evidence":"보통"},
    "shilajit": {"desc":"히말라야 고산지대 암석에서 스며나오는 천연 수지. 풀빅산과 80여 종 미네랄 함유.","origin_type":"아유르베다","origin_story":"산스크리트어로 '산의 정복자'. 아유르베다에서 수천 년간 최고의 라사야나(회춘제)로 사용.","dosage":"300-500mg/일","evidence":"보통"},
    "stinging-nettle-root": {"desc":"쐐기풀 뿌리 추출. 전립선 비대증(BPH)에서 SHBG 결합 억제를 통한 테스토스테론 가용성 증가 연구.","origin_type":"전통의학","origin_story":"고대 로마 병사들이 추운 지역에서 혈액순환을 위해 피부에 쐐기풀을 때렸다는 기록(Urtication).","dosage":"300-600mg/일","evidence":"보통"},
    "nettle": {"desc":"쐐기풀 잎·전초 추출. 뿌리 추출과 달리 항히스타민 효과로 계절성 알레르기에 연구.","origin_type":"전통의학","origin_story":"유럽 전통에서 봄철 해독 차로 음용. 쐐기풀 수프는 북유럽 전통 음식.","dosage":"300-600mg/일","evidence":"보통"},
    "mugwort": {"desc":"쑥 추출물. 아르테미시닌 유도체와 플라보노이드 함유. 한의학에서 뜸(灸)의 핵심 원료.","origin_type":"전통한방","origin_story":"단군신화에서 쑥과 마늘을 먹고 인간이 되었다는 한민족 기원 식물. 한의학에서 뜸·쑥찜·약용으로 광범위하게 사용.","dosage":"3-9g/일","evidence":"보통"},
    "aronia-extract": {"desc":"아로니아(초크베리) 추출물. 안토시아닌 함량이 블루베리의 2-4배. 항산화에 연구.","origin_type":"식품유래","origin_story":"북미 원주민이 건조 과일로 사용. 폴란드에서 1950년대부터 대규모 재배. 한국에서 2010년대 건강 열풍.","dosage":"300-500mg/일","evidence":"보통"},
    "almond-extract": {"desc":"아몬드 추출물. 비타민E, 올레산, 폴리페놀 함유. 피부 보습과 항산화에 연구.","origin_type":"식품유래","origin_story":"고대 이집트와 페르시아에서 미용과 식품으로 사용. 성경에도 등장하는 오래된 견과류.","dosage":"제품별 상이","evidence":"제한적"},
    "acai-berry": {"desc":"아사이베리 추출물. 안토시아닌과 올레산이 풍부. 항산화 슈퍼푸드로 마케팅.","origin_type":"식품유래","origin_story":"브라질 아마존 원주민의 주식. 'açaí'는 투피어로 '물이 나오는 과일'이라는 뜻.","dosage":"500-1000mg/일","evidence":"제한적"},
    "acerola-vitamin-c": {"desc":"아세로라 체리에서 추출한 천연 비타민C. 바이오플라보노이드가 동반 함유.","origin_type":"식품유래","origin_story":"카리브해 원산. 비타민C 함량이 오렌지의 약 30배로 천연 비타민C 원료의 대표.","dosage":"100-500mg 비타민C/일","evidence":"양호"},
    "acerola-extract": {"desc":"아세로라 전체 추출물. 비타민C 외에도 카로티노이드, 안토시아닌 등 동반 항산화 성분 포함.","origin_type":"식품유래","origin_story":"푸에르토리코에서 1940년대 과학 연구가 시작되며 비타민C 천연 원료로 세계적 주목.","dosage":"500-1000mg/일","evidence":"보통"},
    "ashwagandha": {"desc":"인도 전통 어댑토젠. 위타놀라이드가 HPA축(스트레스 반응 시스템)을 조절하여 코르티솔 감소.","origin_type":"아유르베다","origin_story":"산스크리트어로 '말의 냄새'이자 '말의 힘'. 3,000년 이상 아유르베다 최고의 라사야나(회춘 약초).","dosage":"300-600mg/일 (KSM-66)","evidence":"양호"},
    "pygeum": {"desc":"아프리카 자두나무(피지움) 껍질 추출. 피토스테롤, 소사모닌 함유. 전립선 건강에 유럽 의약품.","origin_type":"전통의학","origin_story":"남아프리카 전통 의학에서 전립선과 비뇨기 건강에 사용. 프랑스에서 의약품으로 상업화.","dosage":"100-200mg/일","evidence":"양호"},
    "andrographis": {"desc":"안드로그라피스(센시니드) 추출. 안드로그라폴라이드가 핵심 성분. 상기도 감염에 스칸디나비아에서 연구.","origin_type":"전통의학","origin_story":"인도·중국·동남아 전통에서 '감기의 왕(King of Bitters)'으로 불림. 극도로 쓴 맛이 특징.","dosage":"400mg/일","evidence":"양호"},
    "aloe-vera": {"desc":"알로에 전잎(겔+라텍스) 추출. 알로인(라텍스, 완하 작용)과 아세만난(겔, 면역) 함유.","origin_type":"전통의학","origin_story":"기원전 1550년 이집트 에베르스 파피루스에 기록. 클레오파트라의 미용 비밀이라는 전설.","dosage":"100-200mg/일 (내복)","evidence":"보통"},
    "aloe-gel": {"desc":"알로에 겔(과육 부분만) 추출. 라텍스(완하 성분) 제거. 피부 보습과 장 점막 보호에 연구.","origin_type":"식품유래","origin_story":"알로에 라텍스의 장 자극 문제를 해결하기 위해 겔 부분만 분리한 현대 제형.","dosage":"100-200mg/일","evidence":"보통"},
    "wild-yam": {"desc":"야생 참마 추출물. 디오스게닌 함유. 프로게스테론 전구체로 갱년기 보조에 전통 사용.","origin_type":"전통의학","origin_story":"멕시코 원주민이 관절통에 사용. 1940년대 Russell Marker가 디오스게닌에서 합성 프로게스테론 생산에 성공.","dosage":"250-500mg/일","evidence":"보통"},
    "houttuynia": {"desc":"어성초(삼백초과) 추출물. 데카노일아세트알데히드, 퀘르시트린 함유. 항균·항바이러스에 연구.","origin_type":"전통한방","origin_story":"한의학에서 '물고기 비린내 나는 풀'이라는 뜻의 어성초(魚腥草). 일본에서는 도쿠다미(독을 뽑는 풀).","dosage":"500-1500mg/일","evidence":"보통"},
    "echinacea": {"desc":"에키네시아(자주루드베키아) 추출. 알카미드, 다당류 함유. 면역 자극과 감기 예방에 광범위한 연구.","origin_type":"전통의학","origin_story":"북미 원주민(수족, 체로키족)이 뱀에 물렸을 때와 감기에 사용. 19세기 미국에서 '만병통치약'으로 유행.","dosage":"300-500mg/일","evidence":"양호"},
    "elderberry-syrup": {"desc":"엘더베리를 꿀이나 설탕과 함께 끓여 만든 시럽 형태. 안토시아닌과 비타민C 함유.","origin_type":"전통의학","origin_story":"유럽 민간에서 수백 년간 겨울철 감기 예방 시럽으로 가정에서 제조.","dosage":"15-30ml/일","evidence":"보통"},
    "elderberry-extract": {"desc":"엘더베리(유럽 딱총나무 열매) 농축 추출. 안토시아닌C3G가 핵심. 인플루엔자 증상 완화에 연구.","origin_type":"전통의학","origin_story":"히포크라테스가 '자연의 약상자'라 부른 식물. 해리포터의 '딱총나무 지팡이(Elder Wand)'도 이 나무.","dosage":"500-1000mg/일","evidence":"양호"},
    "elderflower": {"desc":"엘더(딱총나무)의 꽃 추출. 플라보노이드, 페놀산 함유. 발한·해열에 유럽 전통 사용.","origin_type":"전통의학","origin_story":"영국 전통에서 엘더플라워 코디알(시럽)이 여름 음료의 대표. 감기 초기에 차로 음용.","dosage":"차로 음용","evidence":"제한적"},
    "bitter-melon": {"desc":"여주(고과) 추출. 카란틴, 폴리펩타이드-p 함유. 인슐린 유사 작용으로 혈당 관리에 연구.","origin_type":"전통의학","origin_story":"인도·중국·동남아에서 수백 년간 당뇨 민간 요법으로 사용. '식물 인슐린'이라 불림.","dosage":"500-2000mg/일","evidence":"보통"},
    "lotus-leaf": {"desc":"연잎 추출물. 누시페린 함유. 지방 흡수 억제와 체중 관리에 연구.","origin_type":"전통한방","origin_story":"불교에서 연꽃은 깨달음의 상징. 한의학에서 연잎차는 서열(暑熱)을 내리는 여름 약차.","dosage":"500-1000mg/일","evidence":"제한적"},
    "acanthopanax": {"desc":"오가피(오갈피) 추출물. 엘레우테로사이드, 시린진 함유. 만성피로와 면역에 한의학 전통 사용.","origin_type":"전통한방","origin_story":"본초강목에 '오가피를 한 줌 얻느니 금옥을 한 수레 얻겠느냐'는 기록. 가시오갈피와 함께 한방 강장제의 대표.","dosage":"500-1000mg/일","evidence":"보통"},
    "mulberry": {"desc":"오디(뽕나무 열매) 추출물. 안토시아닌, 레스베라트롤 유사체 함유. 항산화에 연구.","origin_type":"식품유래","origin_story":"누에 양잠 문화와 함께 동아시아에서 수천 년 활용. 오디즙은 한국 전통 음료.","dosage":"제품별 상이","evidence":"제한적"},
    "oregano-oil": {"desc":"오레가노 에센셜 오일. 카르바크롤, 티몰이 핵심 성분. 강력한 항균·항진균 작용.","origin_type":"전통의학","origin_story":"그리스어로 'oros(산) + ganos(기쁨)' = '산의 기쁨'. 히포크라테스가 소화와 호흡기에 처방.","dosage":"100-200mg/일 (캡슐)","evidence":"보통"},
    "schisandra-berry": {"desc":"오미자 열매. 다섯 가지 맛(신·단·쓴·짠·매운)을 가진 독특한 약재. 리그난(시잔드린) 함유.","origin_type":"전통한방","origin_story":"본초경에서 상약(上藥)으로 분류. 다섯 맛이 오장(五臟)에 각각 작용한다는 이론.","dosage":"1-3g/일","evidence":"보통"},
    "schizandra-fruit": {"desc":"오미자 열매의 다른 표기. 간 보호(시잔드린의 간세포 보호 작용)에 연구 집중.","origin_type":"전통한방","origin_story":"동아시아 전통에서 오미자차는 여름 피로 회복과 갈증 해소의 대표 음료.","dosage":"1-3g/일","evidence":"보통"},
    "okra-extract": {"desc":"오크라(아욱과) 추출물. 점액질 다당류가 풍부. 장 점막 보호와 혈당 관리에 연구.","origin_type":"식품유래","origin_story":"아프리카 원산으로 중동과 인도를 거쳐 세계로 전파. 점액질이 장벽을 코팅하는 작용.","dosage":"제품별 상이","evidence":"제한적"},
    "olive-extract": {"desc":"올리브 잎·열매 추출. 올레유로페인, 하이드록시티로솔 함유. 지중해식 식단의 항산화 핵심.","origin_type":"식품유래","origin_story":"고대 그리스에서 올리브는 아테나 여신의 선물. 올림픽 승자에게 올리브 관을 씌움.","dosage":"500-1000mg/일","evidence":"보통"},
    "pea-protein": {"desc":"완두콩에서 추출한 식물성 단백질. BCAA 프로필이 우수하고 알레르기 리스크 낮음.","origin_type":"식품유래","origin_story":"유청·대두 알레르기 대체 단백질로 비건 피트니스 시장에서 급성장.","dosage":"20-40g/일","evidence":"양호"},
    "gentian": {"desc":"용담(겐티안) 뿌리 추출. 극도의 쓴맛이 특징. 소화액 분비 촉진에 유럽 전통.","origin_type":"전통의학","origin_story":"일리리아 왕 겐티우스(Gentius)가 처음 약용한 것에서 이름 유래. 유럽 소화제의 핵심 허브.","dosage":"식전 300-600mg/일","evidence":"보통"},
    "burdock-root": {"desc":"우엉 뿌리 추출. 이눌린(프락토올리고당), 아르크티게닌 함유. 해독과 피부에 전통 사용.","origin_type":"전통한방","origin_story":"한의학의 우방자(牛蒡子)로 해독·피부 처방에 사용. 일본에서는 고보(ゴボウ)라 하여 주요 식재료.","dosage":"1-2g/일","evidence":"보통"},
    "milk-peptide": {"desc":"우유 단백질을 효소 분해한 펩타이드. 트립신 가수분해로 이완 효과의 α-s1 카소제핀 생성.","origin_type":"현대과학","origin_story":"모유 수유 후 영아가 편안해지는 현상에서 착안. 프랑스에서 Lactium으로 상업화.","dosage":"150-300mg/일","evidence":"보통"},
    "eurycoma": {"desc":"유리코마 롱기폴리아(통캇알리와 동일 식물의 학명 표기). 쿠아시노이드가 핵심 성분.","origin_type":"전통의학","origin_story":"말레이시아에서 '알리의 지팡이'라는 뜻. 전통적으로 말라리아와 남성 활력 목적으로 사용.","dosage":"200-400mg/일","evidence":"보통"},
    "ginkgo-biloba": {"desc":"은행잎 추출물. 플라보노이드와 테르페노이드(징코라이드) 함유. 뇌 혈류 개선과 인지 기능에 연구.","origin_type":"전통한방","origin_story":"2억 7천만 년 전부터 존재한 '살아있는 화석'. 히로시마 원폭 후 최초로 새싹을 틔운 나무가 은행나무.","dosage":"120-240mg/일 (EGb 761)","evidence":"양호"},
    "horny-goat-weed": {"desc":"음양곽(淫羊藿) 추출. 이카린이 핵심 성분. PDE5 억제 작용(비아그라 유사 기전)에 연구.","origin_type":"전통한방","origin_story":"한 목동이 이 풀을 먹은 양이 교미가 왕성해진 것을 발견했다는 중국 전설에서 이름 유래.","dosage":"250-1000mg/일","evidence":"보통"},
    "xylitol-oral": {"desc":"자일리톨을 구강 건강 목적으로 사용. 충치균(S. mutans)의 대사를 방해하여 산 생성 억제.","origin_type":"현대과학","origin_story":"핀란드 투르크 대학 연구에서 자일리톨 검이 충치를 40-70% 감소시킨다는 결과 발표(1970년대).","dosage":"6-10g/일 (검으로)","evidence":"매우 양호"},
    "peony-root": {"desc":"작약(芍藥) 뿌리 추출. 페오니플로린의 항염·면역 조절 작용. 갱년기와 통증에 한의학 전통 사용.","origin_type":"전통한방","origin_story":"작약은 '함박꽃'으로도 불림. 한의학 사물탕(四物湯)에서 혈액을 보하는 핵심 약재.","dosage":"5-15g/일 (한약)","evidence":"보통"},
    "bamboo-salt": {"desc":"소금을 대나무 통에 넣고 소나무 장작으로 구워 만든 전통 소금. 미네랄 조성 변화.","origin_type":"전통한방","origin_story":"한국 전통 사찰에서 유래. 인산 김일훈 선생이 현대적 개념을 정립한 것으로 알려짐.","dosage":"소량 (일반 소금 대체)","evidence":"제한적"},
    "bamboo-extract": {"desc":"대나무 잎 추출물. 플라본C-글리코사이드(오리엔틴, 호모오리엔틴) 함유. 항산화에 중국 전통 사용.","origin_type":"전통한방","origin_story":"중의학에서 죽엽(竹葉)은 열을 내리고 갈증을 해소하는 약재. 죽엽석고탕의 구성.","dosage":"500-1000mg/일","evidence":"제한적"},
    "dong-quai": {"desc":"중국 당귀(Angelica sinensis). 한국 당귀(A. gigas)와 종이 다름. 리구스틸라이드 함유.","origin_type":"전통한방","origin_story":"중의학에서 '여성의 인삼'이라 불림. 사물탕의 군약. '당귀'는 '남편이 돌아오기를 바란다'는 뜻.","dosage":"3-15g/일 (한약)","evidence":"보통"},
    "rg3-ginsenoside": {"desc":"인삼/홍삼의 특정 진세노사이드 분획. 면역 세포 활성과 항종양 연구.","origin_type":"전통한방","origin_story":"홍삼 가공(증삼) 과정에서 Rb1→Rg3 전환이 일어남. 한국에서 개별인정형 원료로 개발.","dosage":"3-6mg/일","evidence":"보통"},
    "ginger-gingerol": {"desc":"생강의 핵심 매운맛 성분. 위장 운동 촉진과 항구토 작용. 건조하면 쇼가올로 전환(더 매워짐).","origin_type":"식품유래","origin_story":"기원전 5세기 공자가 매끼 생강을 먹었다는 기록. 동서양 모두에서 소화제의 대표.","dosage":"250-1000mg/일","evidence":"양호"},
    "gymnema-sylvestre": {"desc":"짐네마(인도 원산 덩굴). 짐네마산이 혀의 단맛 수용체를 차단하고 소장의 당 흡수를 억제.","origin_type":"아유르베다","origin_story":"힌디어 이름 'Gurmar'는 '설탕을 파괴하는 것'이라는 뜻. 잎을 씹으면 2시간 동안 단맛을 못 느낌.","dosage":"400-800mg/일","evidence":"보통"},
    "plantago-seed": {"desc":"차전자피(질경이씨 껍질) 식이섬유. 수용성 식이섬유로 장운동 촉진과 콜레스테롤 관리.","origin_type":"전통한방","origin_story":"한의학에서 차전자(車前子)는 '수레 앞에 나는 풀'이라는 뜻. 이뇨와 눈 건강에 전통 사용.","dosage":"5-10g/일","evidence":"양호"},
    "cnidium": {"desc":"천궁(川芎) 추출물. 리구스틸라이드, 페룰산 함유. 혈액순환과 두통에 한의학 핵심 약재.","origin_type":"전통한방","origin_story":"사물탕의 구성 약재. '피를 움직이고 기를 통하게 한다'. 여성 건강 처방의 필수 약재.","dosage":"3-9g/일 (한약)","evidence":"보통"},
    "fermented-soybean": {"desc":"청국장 추출물. 나토키나아제, 비타민K2, 폴리글루탐산 함유. 혈전 용해와 콜레스테롤에 연구.","origin_type":"식품유래","origin_story":"한국 전통 발효 식품. 삼국시대부터 전쟁터에서 장병 식량으로 사용했다는 기록. 일본 낫토와 유사.","dosage":"500-2000mg/일","evidence":"보통"},
    "chia-seed": {"desc":"치아씨드. 오메가3(ALA), 식이섬유, 단백질이 풍부. 물에 닿으면 10배 팽창하는 점액질.","origin_type":"전통의학","origin_story":"아즈텍 전사들의 에너지 식품. 'Chia'는 나와틀어로 '힘'이라는 뜻. 마야에서도 주요 식량.","dosage":"15-25g/일","evidence":"보통"},
    "caralluma": {"desc":"카랄루마 핌브리아타. 인도 원산 선인장과 식물. 식욕 억제와 체지방 감소에 연구.","origin_type":"전통의학","origin_story":"인도 부족민이 사냥 원정 시 배고픔을 억제하기 위해 씹던 식물. '기근 식물'로 불림.","dosage":"500-1000mg/일","evidence":"보통"},
    "calendula": {"desc":"카렌듈라(금잔화) 추출물. 트리테르펜 사포닌, 플라보노이드 함유. 피부 진정과 상처 치유.","origin_type":"전통의학","origin_story":"라틴어 calendae(매달 1일)에서 유래 — 거의 매달 꽃이 핀다는 뜻. 중세 유럽에서 상처 치유 연고.","dosage":"외용 또는 300-600mg/일","evidence":"보통"},
    "vitex": {"desc":"체스트베리(비텍스) 추출물. 도파민 수용체 작용으로 프로락틴 분비를 억제. PMS와 갱년기에 유럽 의약품.","origin_type":"전통의학","origin_story":"그리스어 'agnos(순결)'에서 유래. 중세 수도원에서 수도승의 성욕을 억제하기 위해 사용했다는 전설.","dosage":"20-40mg/일","evidence":"양호"},
    "camu-camu": {"desc":"카무카무 열매 추출. 비타민C 함량이 과일 중 최고 수준(오렌지의 60배).","origin_type":"식품유래","origin_story":"페루·브라질 아마존 원주민의 전통 과일. 현지에서는 주스와 아이스크림으로 소비.","dosage":"500-1000mg/일","evidence":"제한적"},
    "cacao-extract": {"desc":"카카오 추출물. 에피카테킨, 테오브로민 함유. 혈관 내피 기능과 인지에 대규모 연구(COSMOS).","origin_type":"식품유래","origin_story":"마야어로 '신의 음식'이라는 뜻의 Theobroma. 아즈텍 황제 몬테수마가 매일 50잔의 카카오 음료를 마셨다는 기록.","dosage":"200-900mg 플라바놀/일","evidence":"양호"},
    "chamomile": {"desc":"캐모마일(카밀레) 추출물. 아피게닌이 GABA-A 수용체에 결합하여 이완·수면 보조.","origin_type":"전통의학","origin_story":"이집트인이 태양신 라에게 바친 허브. 독일에서는 'alles zutraut(모든 것을 치유하는)'이라는 별명.","dosage":"270-400mg/일","evidence":"보통"},
    "cat-claw": {"desc":"캣츠클로(고양이 발톱, 우나 데 가토). 페루 아마존 원산 덩굴. 옥신돌알칼로이드가 면역 조절.","origin_type":"전통의학","origin_story":"페루 아슈아르족이 관절과 감염에 수백 년간 사용. 줄기 가시가 고양이 발톱을 닮아 이름 유래.","dosage":"250-350mg/일","evidence":"보통"},
    "turmeric-curcuminoid": {"desc":"강황에서 커큐미노이드만 농축 추출. 커큐민 95% 이상 표준화된 고농축 형태.","origin_type":"전통의학","origin_story":"강황 전체 추출 대비 커큐미노이드 순도를 높여 효능을 극대화한 현대 제형.","dosage":"500-1500mg/일","evidence":"양호"},
    "curcumin-phytosome": {"desc":"커큐민을 인지질(포스파티딜콜린)로 감싼 파이토솜 기술. 일반 커큐민 대비 생체이용률 29배 향상.","origin_type":"현대과학","origin_story":"이탈리아 Indena사가 개발한 Meriva/Cursol 기술. 리포좀·피페린에 이은 3세대 커큐민 흡수 기술.","dosage":"200-500mg/일","evidence":"양호"},
    "coffee-fruit-extract": {"desc":"커피 열매(커피 체리)에서 원두를 제거한 과피·과육 추출. BDNF(뇌유래신경영양인자) 증가에 연구.","origin_type":"현대과학","origin_story":"커피 산업 부산물(과피)을 기능성 소재로 재활용. NeuroFactor가 대표 브랜드.","dosage":"100mg/일","evidence":"제한적"},
    "kale-extract": {"desc":"케일 추출물. 설포라판 전구체, 루테인, 비타민K 함유. 해독과 항산화에 연구.","origin_type":"식품유래","origin_story":"2010년대 미국에서 '슈퍼푸드의 왕'으로 마케팅 열풍. 로마 시대부터 유럽에서 재배.","dosage":"500-1000mg/일","evidence":"제한적"},
    "chlorella-growth-factor": {"desc":"클로렐라 세포 분열 시 생성되는 핵산·펩타이드 복합체(CGF). 세포 재생과 면역에 연구.","origin_type":"현대과학","origin_story":"클로렐라가 20-24시간마다 4분열하는 강력한 증식력의 핵심 물질을 분리한 것.","dosage":"제품별 상이","evidence":"제한적"},
    "chlorella-extract": {"desc":"클로렐라 추출물 형태. 엽록소, CGF, 베타글루칸 포함. 중금속 배출과 면역에 일본 연구 집중.","origin_type":"현대과학","origin_story":"대만·일본에서 건강식품으로 1960년대부터 대중화. 세포벽 파쇄 기술이 흡수율의 핵심.","dosage":"3-10g/일","evidence":"보통"},
    "tart-cherry": {"desc":"타트체리(몬트모렌시 체리) 추출. 안토시아닌과 천연 멜라토닌 함유. 수면과 운동 회복에 연구.","origin_type":"식품유래","origin_story":"2010년대 안토시아닌의 항염 효과와 천연 멜라토닌 함유가 밝혀지며 수면·운동 보충제로 급성장.","dosage":"480-1000mg/일","evidence":"양호"},
    "hijiki": {"desc":"톳(갈조류) 추출물. 후코이단, 칼슘, 철분 함유. 한국·일본 전통 해조류 식품.","origin_type":"식품유래","origin_story":"한국과 일본에서 전통 밑반찬(톳나물, 히지키). 미네랄이 풍부한 해조류.","dosage":"식품으로 섭취","evidence":"제한적"},
    "tongkat-ali": {"desc":"통캇알리(유리코마 롱기폴리아). 말레이시아 국보급 허브. 쿠아시노이드가 테스토스테론 지지에 연구.","origin_type":"전통의학","origin_story":"말레이시아어로 '알리의 지팡이'. 전통적으로 남성 활력과 말라리아에 사용. 말레이시아 정부가 공식 연구 지원.","dosage":"200-400mg/일","evidence":"보통"},
    "tributyrin": {"desc":"트리뷰티린. 부티르산(낙산)의 트리글리세리드 형태. 대장까지 도달하여 장 상피세포의 에너지원 제공.","origin_type":"현대과학","origin_story":"부티르산이 대장 건강의 핵심이라는 연구에서 출발. 직접 섭취 시 악취 문제를 트리글리세리드 형태로 해결.","dosage":"300-600mg/일","evidence":"보통"},
    "tea-tree-oil": {"desc":"호주 멜라루카 나무 잎에서 증류한 에센셜 오일. 테르피넨-4-올이 핵심 항균·항진균 성분.","origin_type":"전통의학","origin_story":"호주 원주민 분달중족이 질병 치료에 수천 년간 사용. 1770년 쿡 선장이 이 잎으로 차를 만들어 'Tea Tree'라 명명.","dosage":"외용 (5-10% 농도)","evidence":"양호"},
    "pineapple-enzyme": {"desc":"파인애플 줄기/과즙에서 추출한 단백질 분해 효소(브로멜라인). 소화 보조와 항염.","origin_type":"식품유래","origin_story":"남미 원주민이 파인애플을 소화제와 상처 치유에 사용. 현대에는 줄기에서 브로멜라인을 산업적 추출.","dosage":"200-500mg/일","evidence":"보통"},
    "papaya-enzyme": {"desc":"파파야 열매에서 추출한 단백질 분해 효소(파파인). 소화 보조와 항염.","origin_type":"식품유래","origin_story":"중남미 원주민이 고기를 파파야 잎에 싸서 연하게 만든 전통. 천연 육류 연화제.","dosage":"200-500mg/일","evidence":"보통"},
    "adzuki-bean": {"desc":"팥 추출물. 사포닌, 폴리페놀 함유. 이뇨와 부종 관리에 동아시아 전통 사용.","origin_type":"전통한방","origin_story":"한의학의 적소두(赤小豆). '이뇨와 습기 제거'의 대표 약재. 한국에서 동지에 팥죽을 먹는 전통.","dosage":"제품별 상이","evidence":"제한적"},
    "passionflower": {"desc":"패션플라워(시계꽃) 추출물. 크리신, 비텍신이 GABA-A 수용체에 결합하여 이완·수면 보조.","origin_type":"전통의학","origin_story":"스페인 선교사가 꽃의 구조를 예수 수난(Passion)의 상징으로 해석하여 이름 유래.","dosage":"200-500mg/일","evidence":"보통"},
    "peppermint": {"desc":"페퍼민트 추출물. 멘톨이 핵심 성분. 장관 평활근 이완(IBS)과 소화에 연구.","origin_type":"전통의학","origin_story":"그리스 신화에서 님프 민테(Minthe)가 변신한 식물. 장용 코팅 오일 캡슐이 IBS에 유럽에서 처방.","dosage":"장용코팅 캡슐 0.2ml x3회","evidence":"양호"},
    "grape-skin": {"desc":"포도 껍질 추출물. 레스베라트롤, 안토시아닌, 프로시아니딘 함유. '프렌치 패러독스'의 핵심.","origin_type":"식품유래","origin_story":"프랑스인이 고지방 식단에도 심혈관 질환이 적은 '프렌치 패러독스'의 원인으로 적포도주가 지목됨.","dosage":"200-500mg/일","evidence":"보통"},
    "grape-seed-extract": {"desc":"포도씨 추출물. OPC(올리고머릭 프로시아니딘)이 핵심 성분. 혈관 보호와 항산화에 연구.","origin_type":"현대과학","origin_story":"1947년 프랑스 Jacques Masquelier 교수가 땅콩 껍질에서 OPC 발견 후, 포도씨에서 상업화.","dosage":"100-300mg/일","evidence":"양호"},
    "spirulina-phycocyanin": {"desc":"스피룰리나의 청색 색소 단백질. 강력한 항산화와 항염 작용. COX-2 억제에 연구.","origin_type":"현대과학","origin_story":"스피룰리나의 독특한 청록색을 내는 성분을 분리한 것. 식품 천연 색소로도 사용.","dosage":"100-200mg/일","evidence":"제한적"},
    "hydroxyapatite": {"desc":"하이드록시아파타이트. 뼈와 치아의 주성분과 동일한 칼슘-인산 결정 구조.","origin_type":"현대과학","origin_story":"뼈 조직의 주요 미네랄 성분을 그대로 보충하는 발상. MCHC(미세결정형)가 대표 형태.","dosage":"500-1000mg/일","evidence":"보통"},
    "marine-magnesium": {"desc":"해수 또는 해조류에서 추출한 마그네슘. 산화마그네슘 대비 천연 미네랄 동반 함유.","origin_type":"식품유래","origin_story":"아일랜드·프랑스 해역의 해수를 농축하여 마그네슘을 추출한 천연 미네랄 소재.","dosage":"200-400mg/일","evidence":"보통"},
    "hemp-protein": {"desc":"대마 씨앗에서 추출한 식물성 단백질. 필수아미노산 전체 함유. 에데스틴과 알부민 주성분.","origin_type":"식품유래","origin_story":"대마(hemp)는 섬유·식품·건축 소재로 1만 년 이상 재배 역사. THC는 미량(<0.3%) 함유.","dosage":"20-30g/일","evidence":"보통"},
    "hemp-seed": {"desc":"대마 씨앗(햄프시드). 오메가3·6 이상적 비율(1:3), GLA, 완전 단백질 함유.","origin_type":"식품유래","origin_story":"캐나다가 1998년 산업용 대마 재배를 합법화하며 슈퍼푸드로 부상.","dosage":"30-50g/일","evidence":"보통"},
    "hovenia-dulcis": {"desc":"헛개나무 열매/줄기 추출물. DHM(디하이드로미리세틴)이 핵심 성분. 알코올 대사 촉진과 간 보호.","origin_type":"전통한방","origin_story":"본초강목에 '지구자(枳椇子)는 술독을 풀고 갈증을 해소한다'고 기록. 한국에서 숙취 해소의 민간 대표.","dosage":"300-600mg/일","evidence":"양호"},
    "brown-rice-protein": {"desc":"현미에서 추출한 식물성 단백질. 저알레르기성으로 비건·알레르기 대응 단백질.","origin_type":"식품유래","origin_story":"쌀 가공 부산물에서 단백질을 분리하는 기술로 개발. 아시아 식문화 기반.","dosage":"20-30g/일","evidence":"보통"},
    "walnut-extract": {"desc":"호두 추출물. 엘라그산, 오메가3(ALA), 폴리페놀 함유. 뇌 건강에 '모양이 닮은 것은 약이 된다' 전통.","origin_type":"식품유래","origin_story":"뇌 모양을 닮은 호두가 뇌에 좋다는 전통(Doctrine of Signatures). 현대 연구에서도 인지 기능 관련성 확인 중.","dosage":"30-60g/일 (호두)","evidence":"보통"},
    "rhodiola": {"desc":"홍경천(로디올라 로제아) 추출물. 로사빈, 살리드로사이드가 핵심 성분. 어댑토젠의 대표.","origin_type":"전통의학","origin_story":"바이킹이 체력과 용기를 위해 복용했다는 전승. 소련 군의 공식 피로 회복제로 사용(기밀 연구).","dosage":"200-600mg/일","evidence":"양호"},
    "safflower-seed": {"desc":"홍화씨 추출물. 세로토닌 유도체와 불포화지방산 함유. 뼈 건강에 한국 전통 사용.","origin_type":"전통한방","origin_story":"한국 민간에서 '홍화씨가 뼈를 강하게 한다'는 전통. 골절 회복기에 홍화씨유를 먹는 관행.","dosage":"1-3g/일","evidence":"제한적"},
    "white-willow-bark": {"desc":"화이트윌로우(버드나무) 껍질 추출. 살리신이 핵심 성분 — 아스피린(아세틸살리실산)의 원조.","origin_type":"전통의학","origin_story":"기원전 400년 히포크라테스가 버드나무 껍질 차를 열과 통증에 처방. 1897년 바이엘이 살리신에서 아스피린 합성.","dosage":"240mg 살리신/일","evidence":"양호"},
    "skullcap": {"desc":"황금(黃芩, 바이칼 스컬캡) 추출물. 바이칼린, 우고닌 함유. 항염·항불안에 한의학 핵심 약재.","origin_type":"전통한방","origin_story":"한의학 청열해독(淸熱解毒)의 대표 약재. 황금의 노란 단면이 이름의 유래.","dosage":"500-2000mg/일","evidence":"보통"},
    "astragalus": {"desc":"황기(黃芪) 추출물. 아스트라갈로사이드IV, 다당류 함유. 면역과 기(氣) 보충의 대표 한약재.","origin_type":"전통한방","origin_story":"한의학에서 '기(氣)를 보하는 1등 약'으로 분류. 보중익기탕의 군약. 동의보감에서 최상위 보기(補氣) 약재.","dosage":"9-30g/일 (한약 처방)","evidence":"양호"},
    "coptis": {"desc":"황련(黃連) 추출물. 베르베린이 핵심 성분. 장내 항균과 혈당 조절에 연구.","origin_type":"전통한방","origin_story":"한의학에서 '심화(心火)를 내리는' 대표 약재. 극도로 쓴맛이 특징. 황련해독탕의 주약.","dosage":"500-1500mg 베르베린/일","evidence":"양호"},
    "phellodendron": {"desc":"황백(黃柏) 나무 껍질 추출. 베르베린, 팔마틴 함유. 장 건강과 항균에 한의학 전통 사용.","origin_type":"전통한방","origin_story":"황련과 함께 청열(淸熱) 약재의 대표. 노란 속껍질이 이름의 유래. 한약 염색에도 사용.","dosage":"3-12g/일 (한약)","evidence":"보통"},
    "fennel": {"desc":"회향(小茴香) 추출물. 아네톨이 핵심 성분. 소화 촉진과 영아 산통에 유럽 전통 사용.","origin_type":"전통의학","origin_story":"마라톤 전투지의 그리스어 이름이 '회향 밭(Marathon)'이었으며, 고대 올림픽 승리의 관으로도 사용.","dosage":"1-3g/일 (차)","evidence":"보통"},
    "magnolia-bark": {"desc":"후박(厚朴) 나무 껍질 추출. 마그놀올, 호노키올이 GABA-A 수용체에 결합하여 이완·항불안.","origin_type":"전통한방","origin_story":"한의학에서 '기를 돌리고 답답함을 해소하는' 약재. 반하후박탕의 핵심 구성.","dosage":"200-500mg/일","evidence":"양호"},
    "black-garlic-extract": {"desc":"마늘을 60-90일 숙성시킨 흑마늘 추출물. S-알릴시스테인, 멜라노이딘 함유. 항산화력 10배 이상.","origin_type":"식품유래","origin_story":"한국에서 2004년경 개발된 숙성 기법. 매일(Maeil) 유업이 상업화를 선도. 현재 글로벌 건강식품.","dosage":"500-1000mg/일","evidence":"보통"},
    "dim-sum-extract": {"desc":"흑미 추출물. 안토시아닌(시아니딘-3-글루코사이드) 함유. 항산화와 눈 건강에 연구.","origin_type":"식품유래","origin_story":"고대 중국에서 '금쌀(forbidden rice, 황제의 쌀)'로 불렸으며 황제만 먹을 수 있었다는 전설.","dosage":"300-500mg/일","evidence":"제한적"},
    "black-ginseng": {"desc":"인삼/홍삼을 9회 반복 증포(찐 후 건조)한 것. 진세노사이드 Rg3, Rg5, Rk1 함량 극대화.","origin_type":"전통한방","origin_story":"홍삼(1회 증포)을 넘어 구증구포(九蒸九曝) 가공으로 희귀 진세노사이드를 극대화한 프리미엄 제형.","dosage":"1-3g/일","evidence":"보통"},
    "black-sesame": {"desc":"흑임자(검은 깨) 추출물. 세사민, 세사몰린, 안토시아닌 함유. 탈모와 노화에 동아시아 전통 사용.","origin_type":"전통한방","origin_story":"동의보감에 '흑임자는 오장을 윤택하게 하고 흰머리를 검게 한다'고 기록. 한국·중국 전통 뷰티 식품.","dosage":"10-30g/일","evidence":"제한적"},
    "white-kidney-bean": {"desc":"흰강낭콩 추출물. 파세올라민(α-아밀라아제 억제제) 함유. 전분 소화를 차단하여 탄수화물 흡수 억제.","origin_type":"현대과학","origin_story":"1975년 미국 연구에서 강낭콩의 전분 분해 효소 억제 성분 발견. 이후 '탄수화물 블로커'로 상업화.","dosage":"500-1500mg/일 (식전)","evidence":"보통"},
    "hibiscus-extract": {"desc":"히비스커스(무궁화과) 꽃 추출. 안토시아닌, 히비스쿠스산 함유. 혈압 관리에 메타분석 존재.","origin_type":"전통의학","origin_story":"이집트에서 카르카데(hibiscus tea)로 수천 년간 음용. 멕시코의 아구아 데 자마이카도 히비스커스.","dosage":"1.25-2.5g/일 (차)","evidence":"양호"},
}


def main():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "ingredients.json")
    path = os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    missing = []
    for item in data:
        if item["tier"] != 2 or item.get("category") != "extract":
            continue
        if "content_description" in item:
            continue  # already done in batch 1
        if item["id"] in T2_EXT:
            c = T2_EXT[item["id"]]
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

    print(f"Batch 2 updated: {updated}/{len(T2_EXT)} entries")
    if missing:
        print(f"Still missing: {len(missing)}")
        for m in missing:
            print(f"  - {m}")

if __name__ == "__main__":
    main()
