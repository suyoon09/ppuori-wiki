#!/usr/bin/env python3
"""T2 extract content batch 1: entries sorted alphabetically by Korean name (first 100)"""
import json, os

T2_EXT = {
    "licorice-dgl": {"desc":"감초에서 글리시리진을 제거한 형태. 위산 역류나 위염 없이 감초의 위 점막 보호 효과만 활용.","origin_type":"전통의학","origin_story":"감초(甘草)는 한의학에서 '약방의 감초'라 불릴 만큼 가장 광범위하게 사용된 약재. DGL은 글리시리진의 혈압 상승 부작용을 제거한 현대 개량 형태.","dosage":"400-800mg/일","evidence":"양호"},
    "uc-ii-collagen": {"desc":"닭 흉골 연골에서 추출한 비변성 2형 콜라겐. 경구 면역관용 기전으로 관절 연골 파괴를 억제.","origin_type":"현대과학","origin_story":"하버드 의대 David Trentham 교수가 1993년 류마티스 관절염에 대한 경구 면역관용 개념을 제안하며 연구 시작.","dosage":"40mg/일","evidence":"양호"},
    "siberian-ginseng": {"desc":"가시오갈피(엘레우테로코커스). 인삼과 같은 두릅나무과이나 진세노사이드는 없음. 어댑토젠으로 분류.","origin_type":"전통한방","origin_story":"시베리아·만주 지역에서 수백 년간 체력 강화에 사용. 소련 우주비행사와 올림픽 선수들이 복용하며 세계적 주목.","dosage":"300-1200mg/일","evidence":"보통"},
    "gamma-butyrolactone": {"desc":"어류 단백질에서 추출한 펩타이드. 혈압 조절에 관여하는 ACE 억제 펩타이드를 함유.","origin_type":"현대과학","origin_story":"어류 가공 부산물에서 기능성 펩타이드를 분리하는 바이오리파이너리 기술로 개발.","dosage":"제품별 상이","evidence":"제한적"},
    "persimmon-leaf": {"desc":"감나무 잎에서 추출. 감잎차로 전통 음용. 플라보노이드와 비타민C가 풍부.","origin_type":"전통한방","origin_story":"한국과 일본에서 감잎차로 수백 년간 음용. 동의보감에 '감엽(柿葉)'으로 기록.","dosage":"500-1000mg/일","evidence":"제한적"},
    "licorice-root-extract": {"desc":"감초 뿌리 전체 추출물. 글리시리진과 플라보노이드를 포함. 위 점막 보호와 피부 미백에 연구.","origin_type":"전통한방","origin_story":"동의보감, 본초강목 등 동아시아 전통 의서에서 가장 많이 등장하는 약재 중 하나. '국로(國老)'라 불림.","dosage":"200-600mg/일","evidence":"보통"},
    "turmeric-extract": {"desc":"강황 뿌리에서 추출. 커큐미노이드(특히 커큐민)가 핵심 성분. 항염·항산화에 폭넓은 연구.","origin_type":"전통의학","origin_story":"인도에서 4,000년 이상 요리와 의약에 사용. 아유르베다에서 '황금 향신료'로 소화와 상처 치유에 처방.","dosage":"500-2000mg/일 (커큐미노이드 기준)","evidence":"양호"},
    "mistletoe": {"desc":"겨우살이 추출물. 유럽 전통에서 면역 보조와 종양 보조 요법으로 사용. 렉틴이 핵심 성분.","origin_type":"전통의학","origin_story":"켈트 드루이드 사제들이 신성한 식물로 숭배. 유럽 민간에서 '만병통치약'으로 전승.","dosage":"제품별 상이","evidence":"제한적"},
    "cassia-seed": {"desc":"결명자(決明子) 씨앗 추출물. 전통적으로 눈 건강과 장 운동에 사용.","origin_type":"전통한방","origin_story":"'눈을 밝힌다(決明)'는 뜻의 이름. 동의보감에서 간의 열을 내리고 눈을 밝게 하는 약재로 기록.","dosage":"10-15g/일 (차로 음용 시)","evidence":"보통"},
    "sophora-flavescens": {"desc":"고삼(苦參) 뿌리 추출물. 마트린·옥시마트린이 핵심 성분. 피부 질환에 전통 사용.","origin_type":"전통한방","origin_story":"한의학에서 피부 가려움과 습진에 외용과 내복 모두 사용. '쓸 고(苦)'자가 이름에 포함될 만큼 맛이 씀.","dosage":"200-500mg/일","evidence":"제한적"},
    "cats-whisker": {"desc":"고양이수염차(자바차). 동남아시아에서 전통적으로 혈당 관리와 이뇨에 사용.","origin_type":"전통의학","origin_story":"말레이시아·인도네시아에서 수백 년간 신장과 방광 건강 목적으로 음용. 꽃 모양이 고양이 수염을 닮음.","dosage":"차로 음용","evidence":"제한적"},
    "wasabi-extract": {"desc":"고추냉이(와사비) 추출물. 이소티오시아네이트가 핵심 성분. 항균과 소화 자극에 연구.","origin_type":"식품유래","origin_story":"일본 전통 식문화에서 생선회와 함께 제공. 항균 효과로 식중독 예방 역할을 겸했음.","dosage":"제품별 상이","evidence":"제한적"},
    "gotu-kola": {"desc":"병풀(센텔라 아시아티카)의 대체명. 아시아티코사이드가 핵심 성분. 피부 재생과 인지 건강에 연구.","origin_type":"전통의학","origin_story":"아유르베다와 중의학 모두에서 사용. 스리랑카 전설에서 코끼리가 이 풀을 먹어 장수했다고 전해짐.","dosage":"300-600mg/일","evidence":"보통"},
    "goji-berry": {"desc":"구기자(枸杞子) 열매. 베타인, 지아잔틴, 다당류가 풍부. 눈 건강과 면역에 전통 사용.","origin_type":"전통한방","origin_story":"본초강목에 '오랜 복용 시 몸이 가벼워지고 늙지 않는다'고 기록. 닝샤(寧夏) 지역 최고 품질로 유명.","dosage":"6-15g/일","evidence":"보통"},
    "chrysanthemum": {"desc":"국화추출물. 전통적으로 눈 피로와 두통에 차로 음용. 루테올린, 아피게닌 함유.","origin_type":"전통한방","origin_story":"중국 당나라부터 약용차로 사용. 한의학에서 구기자와 함께 '눈을 밝히는 조합'으로 유명.","dosage":"차로 음용 (3-5g)","evidence":"제한적"},
    "oyster-shell-calcium": {"desc":"굴 껍데기를 분쇄한 칼슘 원료. 탄산칼슘 주성분. 천연 칼슘 공급원.","origin_type":"식품유래","origin_story":"해안 지역에서 굴 가공 부산물을 칼슘 원료로 활용한 전통에서 유래.","dosage":"500-1000mg/일","evidence":"보통"},
    "licorice-glycyrrhizin": {"desc":"감초의 주요 사포닌 성분. 코르티솔 대사를 조절하여 항염·면역 조절 작용. 장기간 고용량 시 혈압 상승 주의.","origin_type":"전통한방","origin_story":"감초의 강한 단맛(설탕의 50배)을 내는 성분. 동서양 모두에서 감기와 소화 불량의 대표 처방 약재.","dosage":"최대 100mg 글리시리진/일","evidence":"양호"},
    "noni": {"desc":"노니(모린다시트리폴리아) 열매 추출. 이리도이드가 핵심 성분. 면역과 항산화에 전통 사용.","origin_type":"전통의학","origin_story":"폴리네시아 원주민이 2,000년 이상 만병통치 약재로 사용. 하와이에서 '통증의 나무(Noni)'라 불림.","dosage":"주스 30-60ml/일","evidence":"제한적"},
    "nopal-cactus": {"desc":"노팔 선인장(부채선인장) 추출. 식이섬유와 플라보노이드가 풍부. 혈당 관리에 멕시코 전통 사용.","origin_type":"전통의학","origin_story":"아즈텍 문명부터 식용과 약용을 겸한 선인장. 멕시코 국기에 독수리가 선인장 위에 앉은 문양이 바로 이것.","dosage":"500-1000mg/일","evidence":"보통"},
    "mung-bean": {"desc":"녹두추출물. 비텍신, 이소비텍신 등 플라보노이드 함유. 열을 내리고 해독하는 전통 용도.","origin_type":"전통한방","origin_story":"동아시아에서 수천 년간 해열·해독 목적으로 사용. 여름철 녹두탕은 한국 전통 보양식.","dosage":"제품별 상이","evidence":"제한적"},
    "green-coffee-bean": {"desc":"로스팅 전 생커피 원두 추출물. 클로로겐산이 핵심 성분. 포도당 흡수와 지방 대사에 관여.","origin_type":"현대과학","origin_story":"2012년 Dr. Oz 쇼에서 '기적의 다이어트 성분'으로 소개되며 폭발적 인기. 이후 과장 광고 논란도 겪음.","dosage":"200-400mg (클로로겐산 45-50%)","evidence":"보통"},
    "deer-antler": {"desc":"사슴의 성장기 뿔(녹용)을 건조·추출한 것. IGF-1, 콘드로이틴, 아미노산 함유. 한의학 최상위 보양 약재.","origin_type":"전통한방","origin_story":"동의보감에서 '녹용은 정(精)을 보하고 골수를 채운다'고 기록. 한의학에서 인삼과 함께 2대 보양재.","dosage":"1-3g/일 (한의 처방 기준)","evidence":"보통"},
    "green-tea-extract": {"desc":"녹차잎에서 카테킨(특히 EGCG)을 농축 추출. 체지방 산화와 항산화에 가장 많은 연구.","origin_type":"전통의학","origin_story":"중국 신농본초경에 '차는 독을 다스린다'고 기록. 일본 선종 승려 에이사이가 '끽다양생기'에서 차의 약효를 체계화.","dosage":"300-500mg EGCG/일","evidence":"양호"},
    "damiana": {"desc":"중남미 원산 관목. 잎을 건조하여 차로 음용. 전통적 성기능 보조 허브.","origin_type":"전통의학","origin_story":"마야 문명에서 최음제(aphrodisiac)로 사용. 멕시코 민간에서 수백 년간 성 건강 목적으로 음용.","dosage":"400-800mg/일","evidence":"제한적"},
    "kelp": {"desc":"대형 갈조류(다시마, 켈프). 요오드 함량이 매우 높으며 후코이단, 알긴산 함유.","origin_type":"식품유래","origin_story":"한국·일본에서 수천 년간 주요 식재료. 출산 후 미역국은 한국의 대표적 전통 보양식.","dosage":"요오드 150-300mcg/일 기준","evidence":"보통"},
    "evening-primrose": {"desc":"달맞이꽃 추출물(오일이 아닌 전초 추출). 감마리놀렌산과 폴리페놀 함유.","origin_type":"전통의학","origin_story":"북미 원주민이 전초를 식용·상처 치유에 사용. 17세기 유럽에 전파.","dosage":"500-1500mg/일","evidence":"보통"},
    "soy-protein": {"desc":"대두에서 추출한 식물성 단백질. 필수아미노산 프로필이 동물성에 가장 가깝고 이소플라본 함유.","origin_type":"식품유래","origin_story":"동아시아 수천 년 식문화의 핵심. 두부, 된장, 두유의 원료. 비건 단백질의 대표.","dosage":"20-50g/일","evidence":"양호"},
    "jujube": {"desc":"대추(대조) 추출물. 사포닌, 플라보노이드, 다당류 함유. 수면과 소화에 전통 사용.","origin_type":"전통한방","origin_story":"한의학에서 대추는 '비장을 보하고 기(氣)를 돋운다'고 기록. 약방의 감초처럼 한약 처방에 빈번히 포함.","dosage":"3-15g/일","evidence":"보통"},
    "platycodon": {"desc":"도라지(길경) 뿌리 추출. 사포닌이 핵심 성분. 기관지와 면역에 전통 사용.","origin_type":"전통한방","origin_story":"동의보감에서 '길경은 폐를 열고 담(痰)을 제거한다'고 기록. 한국에서는 나물과 반찬으로도 광범위하게 식용.","dosage":"3-10g/일","evidence":"보통"},
    "dolomite": {"desc":"돌로마이트 광석에서 추출한 칼슘·마그네슘 복합 미네랄. 천연 미네랄 공급원.","origin_type":"현대과학","origin_story":"프랑스 지질학자 Déodat de Dolomieu의 이름에서 유래. 알프스 돌로미티 산맥의 주 광물.","dosage":"500-1000mg/일","evidence":"보통"},
    "eucommia-bark": {"desc":"두충(杜仲) 나무 껍질 추출. 클로로겐산, 피노레시놀 함유. 관절과 혈압에 전통 사용.","origin_type":"전통한방","origin_story":"본초강목에 '두충은 허리와 무릎을 강하게 한다'고 기록. 한의학에서 뼈와 힘줄 강화의 대표 약재.","dosage":"3-9g/일","evidence":"보통"},
    "eucommia": {"desc":"두충추출물(잎 또는 껍질). 위와 동일 원료의 다른 부위 추출 형태.","origin_type":"전통한방","origin_story":"두충나무 껍질을 꺾으면 실처럼 늘어나는 고무질 섬유가 보이는데, 이것이 두충의 특징적 감별법.","dosage":"3-9g/일","evidence":"보통"},
    "solomon-seal": {"desc":"둥글레(옥죽) 뿌리 추출. 다당류와 플라보노이드 함유. 폐와 위를 윤택하게 하는 전통 용도.","origin_type":"전통한방","origin_story":"동의보감에서 '옥죽은 몸의 진액을 보한다'고 기록. 한국에서 둥글레차로 일상 음용.","dosage":"차로 음용 (6-12g)","evidence":"제한적"},
    "perilla-leaf": {"desc":"들깻잎 추출물. 로즈마린산, 루테올린 함유. 항알레르기와 면역 조절에 연구.","origin_type":"식품유래","origin_story":"한국 식문화에서 독보적인 쌈 채소. 일본에서는 차조기(시소)로 불리며 약용과 식용을 겸함.","dosage":"500-1000mg/일","evidence":"제한적"},
    "lavender": {"desc":"라벤더 추출물. 리날룰, 리날릴아세테이트가 핵심 성분. 이완과 수면 보조에 아로마테라피 전통.","origin_type":"전통의학","origin_story":"라틴어 lavare(씻다)에서 유래. 고대 로마인이 목욕물에 넣어 사용. 프로방스 라벤더 밭은 프랑스 상징.","dosage":"80-160mg/일 (Silexan 기준)","evidence":"양호"},
    "lemongrass-extract": {"desc":"레몬그라스 추출물. 시트랄이 핵심 성분. 소화 촉진과 항균에 동남아시아 전통 사용.","origin_type":"전통의학","origin_story":"태국·베트남 등 동남아 요리의 핵심 허브. 산후 조리와 소화 불량에 전통 약차로 음용.","dosage":"차로 음용","evidence":"제한적"},
    "lemon-balm": {"desc":"레몬밤(멜리사) 추출물. 로즈마린산이 핵심 성분. 불안 완화와 인지 기능에 유럽 전통 사용.","origin_type":"전통의학","origin_story":"그리스어 melissa(꿀벌)에서 유래. 꿀벌이 좋아하는 식물. 중세 수도승들이 '장수의 엘릭서'로 처방.","dosage":"300-600mg/일","evidence":"보통"},
    "rosemary-extract-func": {"desc":"로즈마리 추출물(기능성 용도). 카르노스산, 로즈마린산이 핵심 성분. 기억력과 항산화에 연구.","origin_type":"전통의학","origin_story":"셰익스피어 햄릿에서 오필리아가 '기억의 허브'라 부름. 고대 그리스 학생들이 시험 때 머리에 꽂고 공부.","dosage":"500-1000mg/일","evidence":"보통"},
    "rosehip": {"desc":"로즈힙(장미 열매) 추출물. 비타민C, 갈락토리피드 함유. 관절과 피부에 유럽 전통 사용.","origin_type":"식품유래","origin_story":"제2차 세계대전 중 영국에서 오렌지 수입이 끊기자 로즈힙 시럽으로 비타민C를 보충한 역사.","dosage":"5-10g/일","evidence":"보통"},
    "rooibos-extract": {"desc":"남아프리카 세더버그 지역 고유 식물. 카페인이 없으며 아스팔라틴(고유 플라보노이드) 함유.","origin_type":"전통의학","origin_story":"남아프리카 코이산족이 수백 년간 약용차로 음용. 1930년대 상업 재배 시작. 세계에서 유일하게 이 지역에서만 자생.","dosage":"차로 음용","evidence":"제한적"},
    "manuka-honey": {"desc":"뉴질랜드 마누카 나무 꽃에서 유래한 꿀. 메틸글리옥살(MGO)이 핵심 항균 성분.","origin_type":"전통의학","origin_story":"마오리족이 마누카 나무를 '치유의 나무'로 사용. 1991년 와이카토 대학 Peter Molan 교수가 MGO 항균력 규명.","dosage":"MGO 100+ 등급, 1 tsp/일","evidence":"양호"},
    "garlic-extract": {"desc":"마늘 추출물. 알리신(→아조엔, S-알릴시스테인)이 핵심 성분. 심혈관과 면역에 폭넓은 연구.","origin_type":"식품유래","origin_story":"기원전 3000년 이집트 피라미드 건설 노동자에게 마늘을 배급한 기록. 세계 모든 문명에서 약용 식품으로 사용.","dosage":"600-1200mg/일","evidence":"양호"},
    "marshmallow-root": {"desc":"마시멜로우(접시꽃과) 뿌리 추출. 점액질 다당류가 풍부하여 위장과 기관지 점막을 코팅·보호.","origin_type":"전통의학","origin_story":"고대 그리스 의사 히포크라테스가 상처 치유에 사용한 기록. 원래 마시멜로 과자는 이 식물의 뿌리즙으로 만들었음.","dosage":"1-5g/일","evidence":"보통"},
    "maca": {"desc":"페루 안데스 고원(4,000m 이상)에서 자라는 십자화과 뿌리. 마카마이드, 글루코시놀레이트 함유.","origin_type":"전통의학","origin_story":"잉카 전사들이 전투 전 힘과 지구력을 위해 섭취했다는 전승. 스페인 식민지 시대 기록에도 등장.","dosage":"1.5-3g/일","evidence":"보통"},
    "matcha-powder": {"desc":"차광 재배한 녹차잎을 통째로 분쇄한 분말. 일반 녹차 대비 EGCG·L-테아닌 함량이 수배 높음.","origin_type":"전통의학","origin_story":"12세기 일본 선종 승려 에이사이가 중국에서 전래. 일본 다도(茶道)의 핵심 소재로 발전.","dosage":"1-2g/일","evidence":"보통"},
    "mangosteen": {"desc":"동남아시아 원산 '과일의 여왕'. 잔톤(Xanthone)이 핵심 성분. 항산화와 항염에 연구.","origin_type":"식품유래","origin_story":"빅토리아 여왕이 이 과일을 너무 좋아해 가져오는 사람에게 기사 작위를 내리겠다고 했다는 일화.","dosage":"500-1000mg/일","evidence":"제한적"},
    "gum-mastic": {"desc":"그리스 키오스 섬의 매스틱 나무 수지. 위에서 헬리코박터 파일로리균 억제에 연구.","origin_type":"전통의학","origin_story":"고대 그리스에서 씹는 검(gum)의 원조. 히포크라테스가 소화 건강에 처방. 현재도 키오스 섬에서만 수확.","dosage":"350-1000mg/일","evidence":"양호"},
    "moringa": {"desc":"모링가 잎 분말. 비타민, 미네랄, 아미노산이 고도로 농축. '기적의 나무'로 불림.","origin_type":"전통의학","origin_story":"인도 아유르베다에서 300가지 이상의 질병에 사용했다고 기록. 아프리카에서 영양 결핍 대응 식물로 FAO 추천.","dosage":"1-3g/일","evidence":"보통"},
    "mozuku": {"desc":"오키나와산 갈조류. 후코이단 함량이 해조류 중 가장 높음. 면역과 위 건강에 연구.","origin_type":"식품유래","origin_story":"오키나와 장수 식단의 핵심 해조류. 일본에서 후코이단 연구의 대부분이 모즈쿠에서 시작됨.","dosage":"1-3g/일","evidence":"보통"},
    "muira-puama": {"desc":"아마존 원산 관목. 브라질에서 '남성의 나무(potency wood)'로 불림. 성기능 보조에 전통 사용.","origin_type":"전통의학","origin_story":"브라질 원주민이 수백 년간 성 건강과 신경 강장에 사용. 프랑스 약전에 등재됨.","dosage":"1-1.5g/일","evidence":"제한적"},
    "rice-bran-extract": {"desc":"쌀겨에서 추출. 감마오리자놀, 토코트리에놀, 피토스테롤 함유. 콜레스테롤 관리에 연구.","origin_type":"식품유래","origin_story":"일본에서 쌀겨유(미강유)로 전통 사용. 쌀 도정 과정의 부산물을 기능성 원료로 활용.","dosage":"300mg 감마오리자놀/일","evidence":"보통"},
    "wakame": {"desc":"미역 추출물. 후코잔틴, 후코이단, 알긴산 함유. 체중 관리와 면역에 연구.","origin_type":"식품유래","origin_story":"한국 산후 미역국 전통은 세계적으로 독특한 식문화. 일본에서도 된장국의 필수 재료.","dosage":"1-5g/일","evidence":"보통"},
    "dandelion-root": {"desc":"민들레 뿌리 추출. 타락사신, 이눌린 함유. 간 보호와 이뇨에 유럽·한의학 공통 사용.","origin_type":"전통의학","origin_story":"동서양 모두에서 전통 약재로 사용된 드문 식물. 유럽에서는 이뇨제, 한의학에서는 포공영(蒲公英)이라 하여 해열·해독.","dosage":"2-8g/일","evidence":"보통"},
    "wheat-grass": {"desc":"밀의 어린잎(밀싹)을 착즙·분쇄한 것. 클로로필, 비타민, 효소가 풍부.","origin_type":"현대과학","origin_story":"1930년대 미국 Ann Wigmore가 밀싹 주스 건강법을 대중화. 원시 식이 운동의 아이콘.","dosage":"3-5g/일 (분말)","evidence":"제한적"},
    "baobab": {"desc":"아프리카 바오밥 나무 열매 분말. 비타민C, 식이섬유, 칼슘이 풍부한 슈퍼푸드.","origin_type":"식품유래","origin_story":"아프리카에서 '생명의 나무'로 불림. 수천 년 수명을 가진 나무로 어린 왕자에도 등장.","dosage":"5-15g/일","evidence":"제한적"},
    "bacopa": {"desc":"바코파(브라미) 추출물. 바코사이드가 핵심 성분. 기억력과 학습 능력에 아유르베다 전통 사용.","origin_type":"아유르베다","origin_story":"'브라미'는 힌두교 창조의 신 브라마(Brahma)에서 유래. 인도에서 학생들에게 먹이던 '뇌의 허브'.","dosage":"300-600mg/일 (바코사이드 50%)","evidence":"양호"},
    "valerian": {"desc":"발레리안(쥐오줌풀) 뿌리 추출. 발레렌산이 GABA-A 수용체에 결합하여 진정·수면 유도.","origin_type":"전통의학","origin_story":"히포크라테스가 불면에 처방한 기록. 제1차 세계대전 중 포탄 쇼크(PTSD) 치료에 사용.","dosage":"300-600mg/일 (취침 전)","evidence":"보통"},
    "fermented-red-clover": {"desc":"레드클로버를 발효하여 이소플라본 흡수율을 높인 형태. 에쿠올 전환 효율 향상 목적.","origin_type":"현대과학","origin_story":"일반 레드클로버 이소플라본의 낮은 흡수율을 발효 기술로 개선한 차세대 소재.","dosage":"40-80mg 이소플라본/일","evidence":"보통"},
    "fermented-ginseng": {"desc":"홍삼을 유산균 발효하여 진세노사이드의 생체이용률을 높인 형태. Compound K 함량 증가.","origin_type":"전통한방","origin_story":"한국 전통 홍삼 가공법에 현대 발효 기술을 접목. 진세노사이드 Rb1→Compound K 전환.","dosage":"1-3g/일","evidence":"양호"},
    "chestnut-inner-shell": {"desc":"밤 속 껍질(내피) 추출물. 탄닌과 폼라보노이드 함유. 5-알파환원효소 억제에 연구(탈모 관련).","origin_type":"식품유래","origin_story":"한국에서 밤 가공 부산물(속 껍질)을 탈모 관리 기능성 소재로 개발한 국내 특허 원료.","dosage":"200-400mg/일","evidence":"제한적"},
    "cactus-extract": {"desc":"백년초(천년초) 선인장 열매·줄기 추출. 베타레인, 플라보노이드 함유. 면역과 항산화에 연구.","origin_type":"전통의학","origin_story":"제주도 월령리 선인장 군락은 천연기념물. 제주 전통에서 백년초 열매를 식용·약용으로 사용.","dosage":"500-1000mg/일","evidence":"제한적"},
    "pueraria-mirifica": {"desc":"백수오추출물. 식물성 에스트로겐인 미로에스트롤 함유. 갱년기 증상 완화에 연구.","origin_type":"전통의학","origin_story":"한국에서 백수오는 전통 보양 약재. 다만 2015년 간 독성 이슈로 식약처가 원료 재평가.","dosage":"200-400mg/일","evidence":"보통 (간독성 주의)"},
    "white-peony": {"desc":"백작약(白芍) 뿌리 추출. 페오니플로린이 핵심 성분. 혈액 순환과 근육 이완에 전통 사용.","origin_type":"전통한방","origin_story":"한의학 4물탕(사물탕)의 구성 약재. '피를 보하고 통증을 멈춘다'는 전통적 용도.","dosage":"5-15g/일 (한약 처방)","evidence":"보통"},
    "atractylodes": {"desc":"백출(白朮) 추출물. 아트락틸렌이 핵심 성분. 소화와 비장 기능에 한의학 핵심 약재.","origin_type":"전통한방","origin_story":"한의학 4군자탕의 구성 약재. '비장을 건강하게 하고 습기를 제거한다'는 전통 용도.","dosage":"5-15g/일 (한약 처방)","evidence":"제한적"},
    "bee-pollen": {"desc":"꿀벌이 수집한 꽃가루 덩어리. 단백질, 비타민, 미네랄, 효소가 농축. '완전 식품'으로 불림.","origin_type":"식품유래","origin_story":"이집트 파피루스에 '생명을 주는 먼지'로 기록. 히포크라테스와 플리니우스도 약용 가치를 인정.","dosage":"5-20g/일","evidence":"제한적"},
    "palm-extract-beta-sitosterol": {"desc":"식물 세포막의 구성 성분인 피토스테롤. 소장에서 콜레스테롤 흡수를 경쟁적으로 억제.","origin_type":"현대과학","origin_story":"1950년대 대학 연구에서 식물스테롤의 콜레스테롤 저하 효과 확인. 전립선 건강 연구로 확장.","dosage":"130-200mg/일","evidence":"양호"},
    "barley-grass": {"desc":"보리의 어린잎을 수확하여 분쇄한 분말. 클로로필, SOD 효소, 비타민 함유.","origin_type":"현대과학","origin_story":"1970년대 일본 약학자 하기와라 요시히데가 보리새싹의 영양학적 우수성을 연구·대중화.","dosage":"3-6g/일","evidence":"제한적"},
    "boswellia": {"desc":"보스웰리아 나무 수지에서 추출. 보스웰릭산(AKBA)이 핵심 성분. 5-LOX 억제를 통한 항염.","origin_type":"전통의학","origin_story":"성경에 등장하는 유향(프랭킨센스)이 바로 보스웰리아 수지. 동방박사가 아기 예수에게 바친 세 가지 선물 중 하나.","dosage":"300-500mg (AKBA 30% 기준)","evidence":"양호"},
    "boswellia-serrata": {"desc":"인도산 보스웰리아 종. 위의 보스웰리아와 동일 나무의 학명 표기 변형.","origin_type":"전통의학","origin_story":"아유르베다에서 '살라이 구갈'이라 불리며 관절과 호흡기 건강에 수천 년간 사용.","dosage":"300-500mg/일","evidence":"양호"},
    "poria": {"desc":"복령(茯苓). 소나무 뿌리에 기생하는 버섯(곰팡이). 다당류(파키만, 파키모스) 함유.","origin_type":"전통한방","origin_story":"사군자탕·십전대보탕 등 한의학 대표 처방의 필수 약재. '비장을 보하고 습기를 제거한다'.","dosage":"6-18g/일 (한약 처방)","evidence":"제한적"},
    "brazil-nut": {"desc":"브라질너트. 셀레늄 함량이 식품 중 최고. 1-2알로 일일 셀레늄 권장량 충족.","origin_type":"식품유래","origin_story":"아마존 열대우림 원주민의 주요 에너지원. 야생 나무에서만 수확(재배 불가). 나무 하나가 500년 이상 생존.","dosage":"1-3알/일","evidence":"양호"},
    "broccoli-sprout": {"desc":"브로콜리 새싹 추출. 설포라판의 전구체인 글루코라파닌이 성숙 브로콜리의 10-100배 농축.","origin_type":"현대과학","origin_story":"1992년 존스홉킨스대 Paul Talalay 교수가 브로콜리 새싹의 설포라판 함량이 극도로 높음을 발견.","dosage":"30-60mg 설포라판/일","evidence":"양호"},
    "black-cumin-seed": {"desc":"블랙커민씨드(니겔라 사티바) 오일. 티모퀴논이 핵심 활성 성분. 면역과 항염에 연구.","origin_type":"전통의학","origin_story":"이슬람 선지자 무함마드가 '죽음을 제외한 모든 병을 고친다'고 했다는 전승. 투탕카멘 무덤에서도 발견.","dosage":"1-3g/일","evidence":"보통"},
    "black-cohosh": {"desc":"블랙코호시 뿌리 추출. 트리테르펜 글리코사이드가 핵심 성분. 갱년기 증상(안면 홍조)에 연구.","origin_type":"전통의학","origin_story":"북미 원주민이 여성 건강과 관절통에 사용. 독일에서 갱년기 의약품(Remifemin)으로 상업화.","dosage":"20-40mg/일","evidence":"양호"},
    "blueberry-extract": {"desc":"블루베리 추출물. 안토시아닌이 핵심 성분. 눈 건강과 인지 기능에 연구.","origin_type":"식품유래","origin_story":"북미 원주민이 야생 블루베리를 식용·약용으로 사용한 전통. USDA 항산화 식품 순위 상위권.","dosage":"300-600mg/일","evidence":"보통"},
    "sea-buckthorn": {"desc":"비타민나무(산자나무) 열매 추출. 비타민C, E, 오메가7(팔미톨레산), 카로티노이드 함유.","origin_type":"전통의학","origin_story":"학명 Hippophae는 '빛나는 말'이란 뜻. 고대 그리스에서 이 열매를 먹은 말의 털이 윤기났다는 전설.","dosage":"500-1000mg/일","evidence":"보통"},
    "bilberry-extract": {"desc":"빌베리(유럽 블루베리) 추출물. 안토시아노사이드가 핵심 성분. 야간 시력과 망막 혈류에 연구.","origin_type":"전통의학","origin_story":"제2차 세계대전 중 영국 RAF 조종사들이 야간 폭격 전 빌베리 잼을 먹었다는 일화로 유명.","dosage":"160-480mg/일","evidence":"보통"},
    "mulberry-leaf": {"desc":"뽕잎(상엽) 추출물. DNJ(1-데옥시노지리마이신)가 핵심 성분. 알파글루코시다아제를 억제하여 혈당 상승 둔화.","origin_type":"전통한방","origin_story":"누에에게 먹이는 잎으로 유명하지만 한의학에서는 상엽(桑葉)이라 하여 혈당과 풍열(風熱) 관리에 사용.","dosage":"500-1000mg/일","evidence":"양호"},
    "apple-polyphenol": {"desc":"사과 껍질에서 추출한 폴리페놀. 프로시아니딘B2, 클로로겐산 함유. 체지방과 항산화에 연구.","origin_type":"식품유래","origin_story":"'An apple a day keeps the doctor away' — 이 격언의 과학적 근거를 찾는 연구에서 사과 폴리페놀이 주목.","dosage":"300-600mg/일","evidence":"보통"},
    "cnidium-seed": {"desc":"사상자(蛇床子) 씨앗 추출. 오스톨이 핵심 성분. 남성 건강과 피부에 한의학 전통 사용.","origin_type":"전통한방","origin_story":"본초강목에 '양기(陽氣)를 강하게 한다'고 기록. 외용으로도 피부 질환에 사용한 이중 용도 약재.","dosage":"200-500mg/일","evidence":"제한적"},
    "saffron-extract": {"desc":"사프란(크로커스) 추출물. 크로신, 사프라날이 핵심 성분. 기분 개선과 수면에 연구.","origin_type":"전통의학","origin_story":"세계에서 가장 비싼 향신료. 1g에 꽃 150송이 필요. 페르시아에서 3,000년 전부터 약용·염색용.","dosage":"30mg/일","evidence":"양호"},
    "hawthorn": {"desc":"산사나무 열매 추출. 프로시아니딘, 비텍신 함유. 심장 기능과 혈압에 유럽·한의학 공통 사용.","origin_type":"전통의학","origin_story":"유럽에서 '심장의 허브'로 불림. 독일 Commission E가 심부전 보조에 승인한 식물.","dosage":"300-1000mg/일","evidence":"양호"},
    "cornelian-cherry": {"desc":"산수유(山茱萸) 열매 추출. 모로니사이드, 로가닌 함유. 보신(補腎)의 대표 한약재.","origin_type":"전통한방","origin_story":"한의학 6미지황환의 핵심 약재. '신장의 정(精)을 보한다'는 전통. 한국 산수유축제로도 유명.","dosage":"6-12g/일 (한약 처방)","evidence":"보통"},
    "yam-extract": {"desc":"산약(山藥, 참마) 추출물. 디오스게닌, 점액질 다당류 함유. 소화와 호르몬에 전통 사용.","origin_type":"전통한방","origin_story":"동의보감에서 '비위(脾胃)를 보하는 상약(上藥)'으로 분류. 한국에서 마로 불리며 일상 식재료.","dosage":"3-15g/일","evidence":"보통"},
    "coral-calcium": {"desc":"산호에서 추출한 칼슘. 탄산칼슘 + 미량 미네랄(70여 종) 함유. 일본 오키나와산으로 유명.","origin_type":"현대과학","origin_story":"오키나와 장수의 비결로 마케팅되었으나, 일반 탄산칼슘 대비 우월성에 대한 과학적 근거는 제한적.","dosage":"500-1000mg/일","evidence":"제한적"},
    "mulberry-root-bark": {"desc":"뽕나무 뿌리 껍질(상백피) 추출. 모루신, 케르세틴 함유. 혈당과 항염에 전통 사용.","origin_type":"전통한방","origin_story":"한의학에서 상백피는 '폐의 열을 내리고 부종을 빼는' 약재로 분류. 천식과 기침에 처방.","dosage":"6-12g/일 (한약 처방)","evidence":"보통"},
    "black-soybean": {"desc":"서리태(검은콩) 추출물. 안토시아닌, 이소플라본 함유. 항산화와 탈모 관리에 한국 전통 사용.","origin_type":"식품유래","origin_story":"한국 전통에서 검은콩을 먹으면 머리카락이 검어진다는 민간 전승. 동의보감에 '해독, 보신' 효능 기록.","dosage":"300-600mg/일","evidence":"제한적"},
    "pomegranate-concentrate": {"desc":"석류 과즙을 농축한 것. 엘라그산, 퓨니칼라긴 함유. 갱년기 증상과 항산화에 연구.","origin_type":"식품유래","origin_story":"고대 페르시아에서 '생명의 과일', 그리스 신화에서 페르세포네와 하데스 이야기의 핵심 소재.","dosage":"200-500ml 주스/일","evidence":"보통"},
    "pomegranate-extract": {"desc":"석류 과피·씨까지 포함한 전체 추출물. 엘라그산·퓨니칼라긴이 주스보다 고농축.","origin_type":"식품유래","origin_story":"석류의 항산화 성분은 과즙보다 껍질에 더 많이 농축되어 있어, 추출물 형태가 효율적.","dosage":"250-500mg/일","evidence":"보통"},
    "sulforaphane": {"desc":"브로콜리 등 십자화과 채소의 Nrf2 경로 활성 화합물. 해독 효소 유도와 항염에 연구.","origin_type":"현대과학","origin_story":"1992년 존스홉킨스대 연구에서 항암 잠재력 보고. Phase 2 해독 효소를 강력하게 유도하는 자연물.","dosage":"30-60mg/일","evidence":"양호"},
    "st-johns-wort": {"desc":"세인트존스워트(관엽연교) 추출. 히페리신, 하이퍼포린이 핵심 성분. 경도-중등도 우울증에 유럽에서 의약품.","origin_type":"전통의학","origin_story":"세례 요한(St. John)의 축일(6/24)에 꽃이 피어 이름 유래. 중세 유럽에서 '악마를 쫓는 풀'로 사용.","dosage":"300mg x3회/일(히페리신 0.3%)","evidence":"매우 양호"},
    "centella-extract": {"desc":"센텔라(병풀) 추출물. 아시아티코사이드, 마데카소사이드가 핵심 성분. 피부 재생과 상처 치유에 연구.","origin_type":"전통의학","origin_story":"스리랑카에서 호랑이가 상처에 이 풀을 문질러 치유했다는 전설. 한국에서는 '마데카솔' 연고의 원료로 유명.","dosage":"300-600mg/일","evidence":"양호"},
    "pine-bark": {"desc":"해안 소나무 껍질 추출물. 프로시아니딘(OPC)이 핵심 성분. 피크노제놀(Pycnogenol)이 대표 브랜드.","origin_type":"전통의학","origin_story":"1535년 프랑스 탐험가 Jacques Cartier의 선원들이 괴혈병에 걸렸을 때, 원주민이 소나무 껍질 차를 제공하여 회복.","dosage":"100-200mg/일","evidence":"양호"},
    "pine-needle": {"desc":"솔잎 추출물. 테르펜, 플라보노이드 함유. 혈액 순환과 항산화에 한국 전통 사용.","origin_type":"전통한방","origin_story":"한국에서 솔잎주·솔잎차로 민간 전통. 동의보감에 '풍(風)을 다스리고 기(氣)를 통한다'고 기록.","dosage":"1000-2000mg/일","evidence":"제한적"},
    "pine-pollen": {"desc":"소나무 꽃가루(송화분). 테스토스테론 유사 식물 스테로이드가 미량 함유.","origin_type":"전통한방","origin_story":"한국 전통 다식(송화다식)과 송화수(꽃가루주)의 원료. 중국 본초강목에도 기록된 보양 식품.","dosage":"1-3g/일","evidence":"제한적"},
    "portulaca": {"desc":"쇠비름(마치현) 추출물. 오메가3(ALA), 멜라토닌, 베탈레인 함유. 피부와 항산화에 연구.","origin_type":"식품유래","origin_story":"세계 각국에서 식용 잡초로 먹어온 역사. 한국에서 나물로, 그리스에서 샐러드로, 멕시코에서 스튜 재료로.","dosage":"500-1000mg/일","evidence":"제한적"},
    "aged-garlic": {"desc":"마늘을 10-20개월 숙성시킨 추출물. 알리신 대신 S-알릴시스테인(SAC)이 핵심 성분. 냄새가 거의 없음.","origin_type":"현대과학","origin_story":"일본 Wakunaga사가 1955년 개발한 Kyolic이 대표 브랜드. UCLA에서 심혈관 연구가 집중적으로 수행됨.","dosage":"600-2400mg/일","evidence":"양호"},
    "rehmannia": {"desc":"숙지황(熟地黃). 지황 뿌리를 구증구포(아홉 번 찌고 말리기)한 전통 가공 약재. 카탈폴 함유.","origin_type":"전통한방","origin_story":"한의학 6미지황환의 군약(주인공 약재). '피를 보하고 정(精)을 채운다'는 최상위 보혈 약재.","dosage":"9-30g/일 (한약 처방)","evidence":"보통"},
    "slippery-elm": {"desc":"느릅나무 내피 추출. 점액질이 풍부하여 위장·식도 점막을 코팅 보호.","origin_type":"전통의학","origin_story":"북미 원주민이 상처와 화상에 습포제로 사용. 독립전쟁 시 군인들의 식량 대용으로도 사용.","dosage":"400-1000mg/일","evidence":"보통"},
    "cissus": {"desc":"시서스(네모골풀) 추출물. 케토스테론이 핵심 성분. 체중 관리와 뼈 건강에 연구.","origin_type":"전통의학","origin_story":"아유르베다에서 뼈 골절 치유에 전통 사용. 'Hadjod(뼈를 잇는 것)'라는 별명.","dosage":"500-1000mg/일","evidence":"보통"},
}

def main():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "ingredients.json")
    path = os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    for item in data:
        if item["tier"] != 2 or item.get("category") != "extract":
            continue
        if item["id"] in T2_EXT:
            c = T2_EXT[item["id"]]
            item["content_description"] = c["desc"]
            item["origin_type"] = c["origin_type"]
            item["origin_story"] = c["origin_story"]
            item["dosage_reference"] = c["dosage"]
            item["evidence_level"] = c["evidence"]
            updated += 1

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Batch 1 updated: {updated}/{len(T2_EXT)} entries")

if __name__ == "__main__":
    main()
