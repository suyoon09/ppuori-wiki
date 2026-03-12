#!/usr/bin/env python3
"""T1 fix-up: 25 remaining entries with correct IDs"""
import json, os

T1 = {
    "curcumin": {"desc":"강황의 주요 커큐미노이드. NF-kB, COX-2, 5-LOX 등 다중 염증 경로를 동시 억제하는 '다중표적 분자'.","origin_type":"전통의학","origin_story":"인도 아유르베다 4,000년 역사. 결혼식에서 신부에게 강황을 바르는 '할디' 의식이 아직도 전승.","dosage":"500-2000mg/일","evidence":"양호","food_sources":"강황(~3% 커큐민), 보충제","fun_fact":"커큐민의 생체이용률은 1-2%. 피페린(후추)이 2000% 향상. 파이토솜·리포좀 기술이 차세대 흡수 경쟁."},
    "garcinia": {"desc":"가르시니아 캄보지아 과피의 HCA(하이드록시시트르산). ATP-시트레이트 라이아제 억제 → 지방산 합성 차단.","origin_type":"전통의학","origin_story":"동남아·인도에서 요리 양념과 식욕 억제에 전통 사용. Dr. Oz 쇼에서 '기적의 다이어트 성분'으로 대중화.","dosage":"500-1000mg HCA x3/일(식전)","evidence":"보통","food_sources":"보충제","fun_fact":"Dr. Oz 쇼 이후 FTC 과장 광고 지적. 메타분석에서 체중 감소 효과는 통계적으로 유의하나 임상적 의미는 미미."},
    "red-clover": {"desc":"레드클로버 추출물. 이소플라본(포르모네틴, 바이오카닌A) 함유. 갱년기 안면홍조·골밀도에 연구.","origin_type":"전통의학","origin_story":"유럽 민간에서 피부·호흡기에 전통 사용. 갱년기 식물 대안으로 1990년대 재조명.","dosage":"40-80mg 이소플라본/일","evidence":"보통","food_sources":"보충제, 레드클로버 차","fun_fact":"레드클로버의 이소플라본은 대두보다 4종류가 더 다양(포르모네틴, 바이오카닌A 추가)."},
    "cranberry-extract": {"desc":"크랜베리 추출물. A형 프로안토시아니딘(PAC)이 E. coli의 요로 벽 부착을 차단. 요로감염(UTI) 예방에 연구.","origin_type":"식품유래","origin_story":"북미 원주민이 페미컨(전통 식량)에 크랜베리를 혼합. 19세기부터 UTI 민간 요법으로 유명.","dosage":"36mg PAC/일","evidence":"양호","food_sources":"크랜베리주스(무가당), 건조 크랜베리, 보충제","fun_fact":"시장의 크랜베리 주스 대부분은 설탕 첨가 칵테일. UTI 예방 목적이면 PAC 표준화 보충제가 더 효율적."},
    "berberine": {"desc":"황련·황백에서 추출한 이소퀴놀린 알칼로이드. AMPK 활성화 → 포도당 흡수 촉진, 인슐린 감수성 개선. '천연 메트포르민'으로 불림.","origin_type":"전통한방","origin_story":"한의학 황련(黃連)이 수천 년 전통. 2008년 메타분석에서 혈당·콜레스테롤 저하 효과가 메트포르민에 필적하다는 보고.","dosage":"500mg x2-3회/일(식전)","evidence":"양호","food_sources":"보충제 (황련, 황백, 골든실 유래)","fun_fact":"'천연 메트포르민'이라는 별명은 AMPK 활성화 기전이 동일하기 때문. 단, 의약품 대체가 아닌 보조적 사용으로 한정."},
    "kudzu-root": {"desc":"칡(갈근) 뿌리 추출. 퓨에라린·다이드제인 함유. 숙취·혈류개선에 한의학 전통 사용. 갈근탕의 주약.","origin_type":"전통한방","origin_story":"동의보감의 갈근탕 — 감기 초기에 처방하는 대표적 한약. '갈증을 풀고 열을 내리는' 약재.","dosage":"3-9g/일","evidence":"보통","food_sources":"칡즙, 칡차, 한약재","fun_fact":"칡은 미국 남부에서 '악마의 덩굴(devil's vine)'로 불리는 대표적 침입종. 한국에서는 약재, 미국에서는 골칫거리."},
    "artichoke-extract": {"desc":"아티초크 잎 추출물. 시나린·클로로겐산 함유. 담즙 분비 촉진과 소화 보조에 독일에서 의약품으로 사용.","origin_type":"전통의학","origin_story":"고대 이집트와 로마에서 소화 촉진 식품으로 사용. 독일 Commission E가 소화불량에 승인.","dosage":"600-1200mg/일","evidence":"양호","food_sources":"아티초크(식용), 보충제","fun_fact":"아티초크를 먹으면 물이 달게 느껴지는 사람이 있음. 시나린이 단맛 수용체를 일시적으로 자극하기 때문."},
    "olive-leaf-extract": {"desc":"올리브 잎 추출물. 올레유로페인 함량이 올리브 오일의 40배. 항산화·항균·혈압 관리에 연구.","origin_type":"전통의학","origin_story":"성경에 비둘기가 올리브 가지를 물고 온 평화의 상징. 전통 지중해 의학에서 해열과 감염에 올리브 잎 차.","dosage":"500-1000mg/일","evidence":"보통","food_sources":"보충제, 올리브잎 차","fun_fact":"올리브 나무는 수천 년 생존 가능. 게세마네 동산의 올리브 나무는 약 900년. 올리브잎의 자체 방어 물질이 올레유로페인."},
    "schisandra": {"desc":"오미자 추출물. 리그난(시잔드린 계열)이 핵심. 간 보호(Phase I/II 해독 효소 조절), 어댑토젠, 인지 기능에 연구.","origin_type":"전통한방","origin_story":"다섯 맛(酸·甘·苦·鹹·辛)을 동시에 가진 유일한 약재. 오장(五臟)에 각각 작용한다는 한의학 이론.","dosage":"1-3g/일","evidence":"보통","food_sources":"오미자차, 오미자청, 보충제","fun_fact":"러시아에서 소련 시절 군인·우주비행사의 스트레스 내성 강화 목적으로 기밀 연구 수행. 어댑토젠 3대 허브(홍경천, 가시오갈피, 오미자)."},
    "licorice-root": {"desc":"감초 뿌리 추출물. 글리시리진(설탕의 50배 단맛)과 플라보노이드 함유. 위 점막 보호와 항염에 광범위한 전통 사용.","origin_type":"전통한방","origin_story":"'약방의 감초' — 한약 처방의 90%에 감초가 포함된다는 표현. 동서양 공통으로 가장 많이 사용된 약재.","dosage":"200-600mg/일","evidence":"양호","food_sources":"감초차, 한약재, 보충제","fun_fact":"감초의 글리시리진은 코르티솔 비활성화 효소(11β-HSD2)를 억제하여, 장기간 대량 섭취 시 혈압 상승·칼륨 저하 부작용 가능."},
    "ginger-extract": {"desc":"생강 추출물. 진저롤·쇼가올이 5-HT3 수용체를 차단하여 항구토. 위장 운동 촉진과 항염에 연구.","origin_type":"식품유래","origin_story":"기원전 5세기 공자가 매끼 생강을 먹었다는 기록. 영국 '진저 에일'은 뱃멀미 방지에서 유래. WHO가 임신 입덧에 효과적이라 인정.","dosage":"250-1000mg/일","evidence":"양호","food_sources":"생강(생, 건조), 생강차, 보충제","fun_fact":"생강을 건조하면 진저롤이 쇼가올로 전환되어 매운맛이 강해짐. 건강(乾薑)은 한의학에서 생강과 다른 약효로 구분."},
    "cinnamon-extract": {"desc":"계피 추출물. 시나몬알데히드·A형 프로시아니딘이 인슐린 수용체 감수성을 개선. 혈당 관리에 연구.","origin_type":"전통의학","origin_story":"이집트 미라 방부제에 사용될 만큼 귀한 향신료. 중세 유럽에서 금보다 비쌌던 시절. 실론 계피(true cinnamon)와 카시아 계피 구분.","dosage":"500-2000mg/일","evidence":"보통","food_sources":"계피 가루, 계피차, 보충제","fun_fact":"카시아 계피에는 쿠마린(간독성 물질)이 다량 함유. 실론 계피(Ceylon/True cinnamon)는 쿠마린이 극소량. 장기 섭취 시 실론 계피가 안전."},
    "panax-ginseng": {"desc":"인삼(수삼). 진세노사이드(Rb1, Rg1 등)가 핵심. 면역, 인지, 피로, 혈당에 대한 수천 건의 연구.","origin_type":"전통한방","origin_story":"'Panax'는 그리스어 pan(모든)+akos(치료제)='만병통치'. 학명 자체가 인삼에 대한 기대를 담고 있음. 고려인삼은 국제 브랜드.","dosage":"200-400mg 추출물/일","evidence":"양호","food_sources":"인삼 수삼, 인삼차, 인삼 보충제","fun_fact":"인삼 뿌리의 인간 형태(人蔘)가 이름의 유래. '사람 모양의 뿌리일수록 좋다'는 전통은 과학적 근거 없으나 문화적 가치는 지대."},
    "reishi": {"desc":"영지버섯. 가노데릭산(트리테르펜)·베타글루칸이 핵심. 면역 조절·수면·스트레스 적응에 동아시아 전통.","origin_type":"전통한방","origin_story":"진시황의 불로초 전설. 중국에서 '선초(仙草)' 또는 '만년초'. 야생 영지는 참나무 1만 그루에 1개꼴.","dosage":"1-3g 추출물/일","evidence":"보통","food_sources":"영지 추출물, 영지 차, 보충제","fun_fact":"영지의 쓴맛 = 가노데릭산(항염 활성). 쓴맛이 강할수록 트리테르펜 함량이 높다는 품질 지표."},
    "lions-mane": {"desc":"노루궁뎅이버섯. 헤리세논(자실체)·에리나신(균사체)이 NGF(신경성장인자) 합성 촉진. 인지·신경 재생 연구.","origin_type":"전통한방","origin_story":"중의학 '후두고(猴頭菇)'. 일본 '야마부시타케'. 1991년 Kawagishi 교수가 NGF 유도 능력 발견.","dosage":"500-3000mg/일","evidence":"보통","food_sources":"노루궁뎅이버섯(식용), 보충제","fun_fact":"노루궁뎅이버섯은 맛이 랍스터와 비슷하다고 묘사됨. 요리 재료로도 인기. 버터에 구우면 해산물 풍미."},
    "chaga": {"desc":"차가버섯. 자작나무 베툴린·멜라닌·베타글루칸 함유. 시베리아 전통 면역차.","origin_type":"전통의학","origin_story":"슬라브어 '츠하가(чага)'에서 유래. 솔제니친의 소설 '암병동'에서 언급되어 서구에 알려짐.","dosage":"1-3g 추출물/일","evidence":"제한적","food_sources":"차가 차, 보충제","fun_fact":"차가는 버섯이 아닌 균핵(sclerotium). 자작나무의 베툴린을 흡수하여 축적. 야생 채취만 가능."},
    "green-lipped-mussel": {"desc":"뉴질랜드산 초록입홍합 추출물. ETA(에이코사테트라에노산)·GAG·오메가3 함유. 관절 건강에 연구.","origin_type":"전통의학","origin_story":"마오리족이 해안가에서 날것으로 먹으며 관절염이 적었다는 역학 관찰에서 연구 시작.","dosage":"600-1200mg/일","evidence":"양호","food_sources":"초록입홍합(뉴질랜드산), 보충제","fun_fact":"뉴질랜드 해안 마오리족은 내륙 거주자보다 관절염 발생률이 유의미하게 낮았음. 이 역학적 관찰이 연구의 기원."},
    "corosolic-acid": {"desc":"바나바잎에서 추출한 트리테르펜. GLUT4 전위를 촉진하여 포도당 세포 내 흡수를 증가. 혈당 관리에 연구.","origin_type":"전통의학","origin_story":"필리핀에서 바나바잎 차를 '식물 인슐린(Plant Insulin)'이라 부르며 혈당 관리에 전통 음용.","dosage":"1mg 코로솔산/일(바나바잎 32-48mg)","evidence":"보통","food_sources":"바나바잎 차, 보충제","fun_fact":"바나바(Lagerstroemia speciosa)는 동남아시아에서 흔한 가로수. 필리핀에서는 일상적 건강차."},
    "helianthus-tuberosus": {"desc":"돼지감자(예루살렘 아티초크) 추출물. 이눌린(프락토올리고당)이 약 75%로 프리바이오틱스의 최고 공급원.","origin_type":"식품유래","origin_story":"북미 원주민의 전통 식량. '예루살렘'은 이탈리아어 girasole(해바라기)의 영어 와전에서 유래.","dosage":"5-10g 이눌린/일","evidence":"양호","food_sources":"돼지감자(뿌리), 이눌린 보충제","fun_fact":"돼지감자의 이눌린은 칼로리가 거의 없고(1.5kcal/g) 혈당을 올리지 않아 당뇨 식이에 적합. 다만 과다 섭취 시 가스·복부 팽만."},
    "guggul": {"desc":"인도산 코미포라 나무 수지 추출. 구굴스테론이 FXR(파네소이드X수용체)에 작용. 콜레스테롤과 갑상선에 아유르베다 전통.","origin_type":"아유르베다","origin_story":"아유르베다에서 3,000년간 사용. 산스크리트어로 '질병으로부터 보호하는 것'이라는 뜻.","dosage":"500-1000mg/일(구굴스테론 25mg)","evidence":"보통","food_sources":"보충제","fun_fact":"인도 연구에서 콜레스테롤 저하 효과가 보고되었으나, 미국 연구에서는 오히려 LDL이 증가한 상반된 결과로 논란."},
    "marigold-lutein": {"desc":"마리골드(금잔화)에서 추출한 루테인·지아잔틴. 눈 건강 보충제의 주요 원료. FloraGLO가 대표 브랜드.","origin_type":"현대과학","origin_story":"마리골드 꽃잎이 루테인의 가장 효율적 산업 공급원. Kemin사의 FloraGLO가 AREDS2 연구에 사용된 바로 그 루테인.","dosage":"10-20mg 루테인/일","evidence":"매우 양호","food_sources":"보충제(마리골드 추출)","fun_fact":"루테인을 식품에서 섭취할 수도 있지만(케일, 시금치), 눈 건강 연구의 유효 용량(10mg+)은 보충제가 현실적."},
    "coleus-forskohlii": {"desc":"콜레우스 포스콜리 뿌리 추출. 포스콜린이 아데닐릴 사이클라아제를 직접 활성화 → cAMP 상승. 체조성과 혈압에 연구.","origin_type":"아유르베다","origin_story":"아유르베다에서 심장·폐·피부 건강에 전통 사용. 1970년대 포스콜린의 cAMP 경로 활성화가 밝혀지며 서구 연구 시작.","dosage":"250mg 추출물(10% 포스콜린) x2/일","evidence":"보통","food_sources":"보충제","fun_fact":"cAMP 상승은 교감신경 활성화와 유사한 효과를 내어, 지방분해·기관지 이완·혈관 확장을 동시에 유도."},
    "plum-extract": {"desc":"매실(청매) 추출물. 유기산(구연산, 사과산), 피크르산 함유. 소화 촉진과 피로 회복에 한국 전통 사용.","origin_type":"식품유래","origin_story":"한국 전통 매실청(매실액기스)은 여름 건강 음료의 대명사. 동의보감에 '오매(烏梅, 훈제 매실)'가 기침·설사에 기록.","dosage":"매실청(희석), 300-500mg 추출물","evidence":"제한적","food_sources":"매실청, 매실차, 보충제","fun_fact":"매실은 덜 익은 청매 상태에서 아미그달린(청산배당체)이 있어 생으로 먹으면 위험. 매실청 담그기나 가열로 분해됨."},
    "guava-leaf": {"desc":"구아바 잎 추출물. 퀘르세틴 배당체 함유. 식후 혈당 상승 억제(알파글루코시다아제 억제)에 연구. 일본에서 특정보건용식품(FOSHU) 승인.","origin_type":"전통의학","origin_story":"열대 아시아·남미 원산. 민간에서 설사와 소화불량에 구아바잎 차 음용.","dosage":"400mg/일(식전)","evidence":"양호","food_sources":"구아바잎 차, 보충제","fun_fact":"일본 반소도(蕃爽麗, Bansourei) 차가 혈당 관련 FOSHU 인증을 받은 대표 구아바잎 제품."},
    "sanghwang-mushroom": {"desc":"상황버섯(Phellinus linteus) 추출물. 다당류·히스피딘 함유. 면역 활성(NK세포, 대식세포)에 한국 주도 연구.","origin_type":"전통한방","origin_story":"뽕나무(桑)에서 자라는 노란(黃) 버섯. 한국 전통에서 '항암 버섯'으로 높은 인지도.","dosage":"1-3g/일","evidence":"보통","food_sources":"상황버섯 달인 물, 보충제","fun_fact":"상황버섯은 뽕나무 기생성이 가장 약효가 높다고 전통 주장. 참나무·벚나무 기생성과의 차이가 연구 중."},
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
    t1_done = sum(1 for i in data if i['tier']==1 and 'content_description' in i)
    t1_total = sum(1 for i in data if i['tier']==1)
    print(f"Fix-up updated: {updated}")
    print(f"Overall T1: {t1_done}/{t1_total}")
    size = os.path.getsize(path)
    print(f"File size: {size/1024:.0f} KB")

if __name__ == "__main__":
    main()
