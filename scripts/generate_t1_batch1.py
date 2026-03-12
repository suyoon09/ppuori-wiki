#!/usr/bin/env python3
"""T1 content batch 1: vitamins (21) + amino acids (15) = 36 entries"""
import json, os

T1 = {
    # === VITAMINS (21) ===
    "vitamin-a": {"desc":"지용성 비타민. 시각 세포의 로돕신 합성, 상피세포 분화, 면역 세포 발달에 필수.","origin_type":"현대과학","origin_story":"1913년 Elmer McCollum이 버터에서 '지용성 인자 A'를 발견. 야맹증 치료의 역사는 기원전 1500년 이집트까지 거슬러 올라감 — 당시 간을 먹으면 야맹증이 낫는다는 것을 경험적으로 알았다.","dosage":"700-900mcg RAE/일","evidence":"매우 양호","food_sources":"간(소), 고구마, 당근, 시금치, 망고","fun_fact":"북극곰 간에는 비타민A가 치사량 수준으로 농축되어 있어, 극지 탐험가들이 이를 먹고 중독된 사례가 기록됨."},
    "vitamin-b-complex": {"desc":"B1~B12까지 8종의 수용성 비타민 복합체. 에너지 대사, 신경 기능, 적혈구 생성에 각각 관여.","origin_type":"현대과학","origin_story":"원래 하나의 비타민으로 여겨졌으나, 1920-40년대에 걸쳐 8가지 별개의 물질임이 밝혀짐.","dosage":"제품별 상이","evidence":"매우 양호","food_sources":"전곡류, 달걀, 유제품, 녹색 채소, 콩류","fun_fact":"B 비타민에 B4, B8, B10 등의 번호가 빠진 이유는 처음에 비타민으로 분류되었다가 나중에 비타민 정의에 맞지 않아 삭제되었기 때문."},
    "vitamin-b1": {"desc":"티아민. 탄수화물 대사(피루브산 탈수소효소)의 필수 보조인자. 신경 전달과 근육 기능에 관여.","origin_type":"현대과학","origin_story":"1897년 네덜란드 군의관 Christiaan Eijkman이 쌀겨를 먹인 닭이 각기병에 걸리지 않는 것을 발견(노벨상 수상). 아시아에서 도정 백미 보급과 함께 각기병이 유행한 역사.","dosage":"1.1-1.2mg/일","evidence":"매우 양호","food_sources":"돼지고기, 해바라기씨, 현미, 두부, 렌틸콩","fun_fact":"일본 해군에서 각기병으로 수천 명이 사망. 다카키 가네히로 군의관이 식단 개선으로 퇴치에 성공한 것이 비타민 발견보다 10년 앞선 사건."},
    "vitamin-b2": {"desc":"리보플라빈. FAD/FMN 형태로 산화환원 반응에 관여. 에너지 대사, 피부·점막 건강, 철분 대사에 필수.","origin_type":"현대과학","origin_story":"우유에서 노란 형광 물질로 1879년 처음 관찰. 1933년 Richard Kuhn이 분리 성공(노벨상 수상).","dosage":"1.1-1.3mg/일","evidence":"매우 양호","food_sources":"간, 달걀, 우유, 아몬드, 표고버섯","fun_fact":"비타민B2를 먹으면 소변이 선명한 노란색이 되는데, 이는 리보플라빈의 형광 색소 때문이며 정상적인 현상."},
    "vitamin-b3": {"desc":"나이아신. NAD⁺/NADP⁺ 형태로 400개 이상의 효소 반응에 관여. 에너지 대사, 항산화(글루타치온 재생), 피부 장벽에 필수.","origin_type":"현대과학","origin_story":"20세기 초 미국 남부 펠라그라 대유행. 1938년 밀가루 나이아신 강화 의무화로 퇴치. 빵 한 조각이 수십만 명을 구함.","dosage":"14-16mg NE/일","evidence":"매우 양호","food_sources":"닭가슴살, 참치, 땅콩, 표고버섯, 커피","fun_fact":"나이아신(Niacin)은 Nicotinic Acid + Vitamin의 합성어. 원래 이름 '니코틴산'이 담배 니코틴과 혼동될 우려로 1940년대 개명."},
    "vitamin-b5": {"desc":"판토텐산. CoA(코엔자임A)의 구성 성분. 지방산 합성·산화, TCA 회로, 스테로이드 호르몬 합성에 관여.","origin_type":"현대과학","origin_story":"그리스어 'pantos(어디에나)'에서 유래 — 거의 모든 식품에 소량씩 존재하기 때문. 1931년 Roger Williams 발견.","dosage":"5mg/일","evidence":"양호","food_sources":"간, 표고버섯, 아보카도, 해바라기씨, 달걀노른자","fun_fact":"거의 모든 식품에 존재하기 때문에 건강한 식단에서 결핍은 극히 드묾. '어디에나 있는 비타민'."},
    "vitamin-b6": {"desc":"피리독신. 아미노산 대사(트랜스아미나제), 신경전달물질 합성(세로토닌, 도파민, GABA), 헤모글로빈 합성에 관여.","origin_type":"현대과학","origin_story":"1934년 Paul György가 피부염 예방 인자로 발견. 이후 100개 이상의 효소 반응에 관여하는 것으로 밝혀짐.","dosage":"1.3-1.7mg/일","evidence":"매우 양호","food_sources":"바나나, 닭가슴살, 감자, 병아리콩, 참치","fun_fact":"B6는 세로토닌과 멜라토닌 합성 경로에 관여하여 수면·기분에 간접적으로 영향. 임산부에서 입덧 완화에 사용된 역사."},
    "vitamin-b7": {"desc":"비오틴. 카르복실라아제 효소의 보조인자. 케라틴(모발·손톱 단백질) 인프라구조, 지방산 합성, 포도당 신생합성에 관여.","origin_type":"현대과학","origin_story":"1901년 달걀 흰자만 먹인 쥐에서 피부염 발생 관찰 → 노른자의 보호 인자로 비오틴 발견. 'bios(생명)'에서 이름 유래.","dosage":"30mcg/일","evidence":"양호","food_sources":"달걀노른자, 견과류, 간, 고구마, 시금치","fun_fact":"날달걀 흰자에 있는 아비딘(avidin)이 비오틴과 강하게 결합하여 흡수를 차단. 록키처럼 날달걀을 마시면 비오틴 결핍 위험."},
    "vitamin-b9": {"desc":"엽산. DNA 합성(티미딜레이트 합성효소)과 메틸화 반응에 필수. 태아 신경관 발달에 결정적.","origin_type":"현대과학","origin_story":"라틴어 folium(잎)에서 유래. 1941년 시금치 잎에서 분리. 1991년 엽산 보충이 신경관 결손을 70% 감소시킨다는 연구 발표.","dosage":"400mcg DFE/일 (임산부 600mcg)","evidence":"매우 양호","food_sources":"시금치, 콩류, 아스파라거스, 브로콜리, 아보카도","fun_fact":"MTHFR 유전자 변이(인구의 ~30%)가 있는 사람은 합성 엽산을 활성형(5-MTHF)으로 전환하는 효율이 낮아, 활성엽산 형태를 선호."},
    "vitamin-b12": {"desc":"코발라민. 코발트를 함유한 유일한 비타민. DNA 합성, 적혈구 성숙, 수초(미엘린) 형성, 호모시스테인 대사에 필수.","origin_type":"현대과학","origin_story":"1849년 악성빈혈(pernicious anemia) 기술 → 1926년 간 섭취로 치료 가능 발견(노벨상) → 1948년 간에서 B12 결정 분리 성공.","dosage":"2.4mcg/일","evidence":"매우 양호","food_sources":"간, 조개·굴, 고등어, 소고기, 달걀","fun_fact":"비타민 중 유일하게 식물에 존재하지 않음. 비건은 반드시 보충 필요. 체내 저장량이 풍부하여 결핍 증상이 수년 후에야 나타남."},
    "vitamin-c": {"desc":"아스코르브산. 콜라겐 합성의 필수 보조인자, 수용성 항산화 1차 방어선, 철분 흡수 촉진, 면역 세포 에너지원.","origin_type":"현대과학","origin_story":"1747년 James Lind의 괴혈병 통제 실험 — 역사상 최초의 임상시험. 1932년 Albert Szent-Györgyi가 파프리카에서 분리(노벨상).","dosage":"100mg (RDA), 500-1000mg (보충)","evidence":"매우 양호","food_sources":"카카두플럼, 아세로라, 파프리카, 키위, 브로콜리, 딸기, 오렌지","fun_fact":"인간이 비타민C를 합성하지 못하는 이유는 6,100만 년 전 GULO 유전자 돌연변이. 열대 과일이 풍부한 환경에서는 불이익이 없었음."},
    "vitamin-d": {"desc":"콜레칼시페롤. 사실상 호르몬 전구체. 칼슘·인 흡수 조절, 면역 세포 활성, 근육 기능, 유전자 발현 조절.","origin_type":"현대과학","origin_story":"1920년대 구루병 연구에서 발견. 자외선(UVB)이 피부에서 합성을 유도하는 유일한 비타민으로, '햇빛 비타민'이라 불림.","dosage":"600-2000 IU/일","evidence":"매우 양호","food_sources":"연어, 고등어, 표고버섯(UV 조사), 달걀노른자, 강화우유","fun_fact":"한국인의 약 80%가 비타민D 부족 또는 결핍 상태. 실내 생활과 자외선 차단제 사용이 주된 원인."},
    "vitamin-e": {"desc":"토코페롤·토코트리에놀 계열 8종의 지용성 항산화 비타민. 세포막의 지질 과산화를 차단하는 방어선.","origin_type":"현대과학","origin_story":"1922년 Herbert Evans가 생식에 필수적인 '항불임 인자'로 발견. 그리스어 tokos(출산) + phero(나르다)에서 이름 유래.","dosage":"15mg α-TE/일","evidence":"양호","food_sources":"해바라기씨, 아몬드, 올리브오일, 아보카도, 시금치","fun_fact":"비타민E 보충 시 합성(dl-α-토코페롤)보다 천연(d-α-토코페롤)의 생체이용률이 약 2배 높음. 라벨의 'd-'와 'dl-' 구분이 중요."},
    "vitamin-k": {"desc":"혈액응고인자(prothrombin 등) 활성화와 뼈 대사(오스테오칼신 활성화)에 필수. K1(필로퀴논)과 K2(메나퀴논) 구분.","origin_type":"현대과학","origin_story":"1929년 덴마크 생화학자 Henrik Dam이 '응고(Koagulation) 비타민'으로 발견(노벨상). K는 독일어 Koagulation의 첫 글자.","dosage":"90-120mcg/일","evidence":"양호","food_sources":"케일, 시금치, 브로콜리(K1), 낫토, 치즈(K2)","fun_fact":"K1은 간에서 혈액응고에, K2는 뼈와 혈관에서 칼슘 배치에 주로 작용. 항응고제(와파린) 복용자는 K1 섭취량을 일정하게 유지해야 함."},
    "paba": {"desc":"파라아미노벤조산. 엽산 합성의 전구체. 피부 보호(UV 필터)와 모발 색소 유지에 전통 사용.","origin_type":"현대과학","origin_story":"1940년대 자외선 차단 성분으로 초기 자외선 차단제에 사용. 이후 엽산 대사와의 관계가 밝혀짐.","dosage":"30-100mg/일","evidence":"제한적","food_sources":"간, 효모, 시금치, 버섯","fun_fact":"PABA는 세균의 엽산 합성에 필수. 설파제(sulfa drugs)가 PABA를 경쟁적으로 차단하여 항생 효과를 내는 원리."},
    "vitamin-c-liposomal": {"desc":"비타민C를 인지질(레시틴) 리포좀으로 감싼 형태. 위장 자극 없이 흡수율을 높이는 기술.","origin_type":"현대과학","origin_story":"약물전달 기술(DDS)을 영양 보충제에 적용한 사례. 정맥주사(IV) 비타민C의 경구 대안으로 개발.","dosage":"500-1000mg/일","evidence":"보통","food_sources":"보충제 전용","fun_fact":"리포좀은 세포막과 동일한 인지질 이중층으로 되어 있어, 직접 세포막에 융합하여 내용물을 전달."},
    "vitamin-a-beta-carotene": {"desc":"프로비타민A 카로티노이드. 체내에서 필요한 만큼만 비타민A(레티놀)로 전환. 과잉 독성 위험 낮음.","origin_type":"식품유래","origin_story":"당근(carrot)에서 이름 유래(carotene). 1831년 독일 화학자 Heinrich Wilhelm Ferdinand Wackenroder가 당근에서 분리.","dosage":"6-15mg/일","evidence":"양호","food_sources":"당근, 고구마, 호박, 망고, 시금치","fun_fact":"당근을 많이 먹으면 피부가 노란색이 되는 '카로틴혈증'이 올 수 있지만 건강상 무해하며, 섭취를 줄이면 원래대로 돌아옴."},
    "thiamine-benfotiamine": {"desc":"비타민B1의 지용성 유도체. 일반 티아민 대비 세포 내 흡수율이 5배 이상 높음.","origin_type":"현대과학","origin_story":"일본에서 1960년대 개발. 당뇨 합병증(신경병증, 망막병증)에서 AGE(최종당화산물) 생성 억제 연구.","dosage":"150-300mg/일","evidence":"보통","food_sources":"보충제 전용","fun_fact":"지용성이므로 일반 B1처럼 소변으로 빠져나가지 않고, 체내 체류 시간이 길어 효율적."},
    "inositol": {"desc":"비공식 비타민B8. 세포 신호전달(PI 경로)의 2차 메신저. 인슐린 감수성, PCOS, 불안에 연구.","origin_type":"현대과학","origin_story":"체내에서 포도당으로부터 합성 가능하여 엄밀한 비타민은 아님. 1850년대 발견. 1990년대 정신건강 연구에서 재주목.","dosage":"2-4g/일(불안), 4g 미오이노시톨(PCOS)","evidence":"양호","food_sources":"감귤류, 현미, 콩류, 견과류","fun_fact":"다낭성난소증후군(PCOS)에서 미오이노시톨:D-카이로이노시톨 = 40:1 비율이 최적이라는 연구가 있음."},
    "choline": {"desc":"아세틸콜린(신경전달물질), 포스파티딜콜린(세포막), 베타인(메틸 공여체) 합성의 전구체. 간 건강과 태아 뇌 발달에 필수.","origin_type":"현대과학","origin_story":"1998년에야 IOM이 필수 영양소로 공식 인정. 가장 최근에 '필수'로 지정된 영양소 중 하나.","dosage":"425-550mg/일","evidence":"양호","food_sources":"달걀노른자(1개=147mg), 간, 대두, 닭가슴살","fun_fact":"달걀노른자가 콜린의 최고 식품 공급원. 달걀 기피와 함께 현대인의 콜린 섭취가 크게 감소한 것으로 추정."},
    "folate-5mthf": {"desc":"엽산의 체내 활성 형태(5-메틸테트라하이드로폴레이트). MTHFR 변이자도 직접 이용 가능.","origin_type":"현대과학","origin_story":"합성 엽산(folic acid)의 체내 전환 한계를 보완하기 위해 개발. MTHFR 유전자 다형성 연구와 함께 주목.","dosage":"400-800mcg/일","evidence":"양호","food_sources":"보충제 전용 (식품 엽산은 다양한 형태 혼합)","fun_fact":"Quatrefolic, Metafolin 등이 대표 브랜드. MTHFR C677T 변이 보유율은 한국인에서 약 30%."},

    # === AMINO ACIDS (15) ===
    "bcaa": {"desc":"류신·이소류신·발린 세 가지 분지쇄 아미노산. 근육에서 직접 산화되어 에너지원으로 사용. 근단백질 합성 신호(mTOR) 활성화.","origin_type":"현대과학","origin_story":"1818년 프랑스 화학자가 치즈에서 류신을 최초 분리. 1990년대 보디빌딩 커뮤니티에서 보충제로 대중화.","dosage":"5-10g/일","evidence":"양호","food_sources":"닭가슴살, 소고기, 참치, 달걀, 유청","fun_fact":"최근 연구에서 충분한 단백질을 섭취하는 경우 별도 BCAA 보충의 추가 효과가 제한적이라는 의견이 증가."},
    "l-glutamine": {"desc":"체내 가장 풍부한 아미노산. 장 상피세포의 주요 에너지원이며 면역 세포(림프구) 증식에 필수.","origin_type":"현대과학","origin_story":"스트레스·외상·수술 후 체내 글루타민이 급격히 고갈되는 것이 발견되어 '조건부 필수 아미노산'으로 분류.","dosage":"5-15g/일","evidence":"양호","food_sources":"소고기, 닭고기, 생선, 달걀, 두부, 유제품","fun_fact":"장 점막 세포가 48-72시간마다 교체되는데, 이 빠른 세포 분열에 글루타민이 핵심 연료."},
    "l-lysine": {"desc":"필수아미노산. 콜라겐 합성(수산화라이신), 카르니틴 합성, 칼슘 흡수 촉진에 관여.","origin_type":"현대과학","origin_story":"1889년 독일 화학자 Edmund Drechsel이 카세인에서 분리. 곡물 기반 식단에서 제1 제한 아미노산.","dosage":"1-3g/일","evidence":"보통","food_sources":"닭가슴살, 소고기, 참치, 달걀, 치즈, 대두","fun_fact":"헤르페스 바이러스(HSV) 재발 억제에 대한 연구가 있음. 라이신이 아르기닌과 경쟁하여 바이러스 복제를 억제한다는 가설."},
    "l-methionine": {"desc":"필수아미노산이자 황 함유 아미노산. SAMe·시스테인·글루타치온 합성의 출발점. 간 해독에 중요.","origin_type":"현대과학","origin_story":"1922년 카세인에서 분리. 메틸기 공여체로서 DNA 메틸화와 에피제네틱스 연구의 핵심.","dosage":"500-1500mg/일","evidence":"보통","food_sources":"달걀, 생선, 참깨, 브라질너트, 소고기","fun_fact":"아세트아미노펜(타이레놀) 과다 복용 시 NAC(메티오닌 유도체)로 해독하는 것이 표준 치료법."},
    "l-citrulline": {"desc":"수박에서 유래한 비필수 아미노산. 체내에서 아르기닌으로 전환 → 일산화질소(NO) 생성 → 혈관 확장.","origin_type":"식품유래","origin_story":"1930년 일본에서 수박(Citrullus)에서 분리되어 이름 유래. 수박의 흰 부분에 가장 많이 농축.","dosage":"3-6g/일","evidence":"양호","food_sources":"수박(특히 흰 부분), 호박, 오이","fun_fact":"아르기닌을 직접 먹는 것보다 시트룰린을 먹는 것이 혈중 아르기닌을 더 많이 올린다는 역설적 결과."},
    "l-arginine": {"desc":"반필수아미노산. 일산화질소(NO) 합성의 직접 기질. 혈관 확장, 성장호르몬 분비 자극, 면역 세포 기능에 관여.","origin_type":"현대과학","origin_story":"1886년 루핀 씨앗에서 분리. 1998년 NO 발견 연구팀(Furchgott, Ignarro, Murad)이 노벨상 수상.","dosage":"3-6g/일","evidence":"양호","food_sources":"칠면조, 돼지고기, 닭고기, 호박씨, 대두, 땅콩","fun_fact":"비아그라(실데나필)는 NO 경로의 하류를 조절. 아르기닌은 같은 경로의 상류에서 NO 생성을 증가시킴."},
    "l-carnitine": {"desc":"라이신과 메티오닌에서 합성. 장쇄 지방산을 미토콘드리아 내막으로 운반하여 베타산화(지방연소)를 가능하게 하는 운반체.","origin_type":"현대과학","origin_story":"라틴어 carnis(고기)에서 유래. 1905년 고기 추출물에서 발견. 지방 '태우기'의 핵심 운반 분자.","dosage":"1-3g/일","evidence":"보통","food_sources":"양고기, 소고기, 돼지고기, 닭가슴살, 우유","fun_fact":"적색육이 카르니틴의 최고 공급원. 채식주의자는 체내 합성에 의존하므로 카르니틴 수치가 상대적으로 낮음."},
    "l-theanine": {"desc":"녹차 특유의 감칠맛 아미노산. GABA·세로토닌·도파민 경로를 조절하여 '이완하되 졸리지 않은' 상태 유도. 알파파(α-wave) 증가.","origin_type":"식품유래","origin_story":"1949년 일본 과학자가 옥로차(玉露, 차광 재배 녹차)에서 처음 분리. 차(茶)의 학명 thea에서 이름 유래.","dosage":"100-200mg/일","evidence":"양호","food_sources":"녹차(특히 옥로, 말차), 홍차(소량)","fun_fact":"카페인과 함께 섭취하면 카페인의 각성 효과는 유지하면서 불안·떨림은 줄이는 시너지. 커피 대신 녹차가 '부드러운 각성'을 주는 이유."},
    "l-tryptophan": {"desc":"필수아미노산. 세로토닌·멜라토닌 합성 경로의 출발점. 나이아신(비타민B3) 합성에도 관여.","origin_type":"현대과학","origin_story":"1901년 카세인에서 분리. 1989년 일본산 오염 트립토판에 의한 EMS(호산구성 근육통증후군) 사건으로 일시 판매 금지.","dosage":"500-1000mg/일","evidence":"보통","food_sources":"칠면조, 닭고기, 치즈, 두부, 바나나, 귀리","fun_fact":"추수감사절 칠면조를 먹으면 졸리다는 속설이 있지만, 실제로는 과식과 알코올이 주원인. 칠면조의 트립토판 함량은 닭고기와 비슷."},
    "l-tyrosine": {"desc":"도파민·노르에피네프린·에피네프린(카테콜아민)의 전구체. 갑상선 호르몬(T3, T4) 합성에도 필수.","origin_type":"현대과학","origin_story":"그리스어 tyros(치즈)에서 유래. 1846년 치즈의 카세인에서 분리.","dosage":"500-2000mg/일","evidence":"보통","food_sources":"치즈, 닭고기, 달걀, 콩류, 아몬드","fun_fact":"미군에서 극한 스트레스 상황(수면 부족, 추위)에서 인지 능력 유지를 위해 L-티로신 보충을 연구한 군사 연구 존재."},
    "nac": {"desc":"시스테인의 아세틸화 형태. 글루타치온(체내 최강 항산화제) 합성의 속도제한 전구체. 점액 용해 작용도 보유.","origin_type":"현대과학","origin_story":"1960년대 점액 용해제로 개발. 이후 아세트아미노펜 중독 해독제(응급의학)로 표준 채택. 글루타치온 전구체로서 항산화 연구 확장.","dosage":"600-1800mg/일","evidence":"양호","food_sources":"보충제 전용(시스테인은 마늘, 양파, 브로콜리에 풍부)","fun_fact":"전 세계 모든 응급실에 상비되어 있는 필수 해독제. WHO 필수의약품 목록에 등재."},
    "gamma-aminobutyric-acid": {"desc":"뇌의 주요 억제성 신경전달물질. 신경 흥분을 가라앉혀 이완·수면·항불안 작용. 성장호르몬 분비 자극 연구.","origin_type":"현대과학","origin_story":"1950년 뇌에서 발견. 경구 GABA가 혈뇌장벽(BBB)을 통과하는지에 대한 논쟁이 현재도 진행 중.","dosage":"100-750mg/일","evidence":"보통","food_sources":"김치, 된장, 현미, 발아현미, 토마토","fun_fact":"GABA는 뇌에서 합성되므로 경구 투여 시 BBB 통과 여부가 논란. 하지만 장신경계(Enteric NS)를 통한 간접 효과 가설도 존재."},
    "glutathione": {"desc":"글루탐산·시스테인·글리신 세 아미노산의 트리펩타이드. 체내 모든 세포에 존재하는 '마스터 항산화제'. 해독(Phase II 결합 반응)의 핵심.","origin_type":"현대과학","origin_story":"1888년 발견. 오랫동안 경구 섭취 시 위장에서 분해되어 무효하다고 여겨졌으나, 2015년 연구에서 경구 리포좀 글루타치온의 혈중 수치 상승이 확인됨.","dosage":"250-1000mg/일","evidence":"보통","food_sources":"아스파라거스, 아보카도, 시금치, 브로콜리(전구체 공급)","fun_fact":"글루타치온은 미백 주사의 핵심 성분. 멜라닌 합성 효소(티로시나아제)를 억제하여 피부 톤에 영향."},
    "glycine": {"desc":"가장 단순한 아미노산. 콜라겐의 1/3을 구성(Gly-X-Y 반복 구조). 억제성 신경전달, 크레아틴·글루타치온 합성에 관여.","origin_type":"현대과학","origin_story":"1820년 젤라틴에서 분리. '달다'는 뜻의 그리스어 glykys에서 이름 유래 — 실제로 약간 단맛이 남.","dosage":"3-5g/일","evidence":"보통","food_sources":"젤라틴, 콜라겐, 뼈국물, 새우, 돼지 껍데기","fun_fact":"취침 전 3g 글리신이 수면 질을 개선한다는 일본 연구. 체심 온도(core body temperature) 하강을 촉진하여 입면을 도움."},
    "taurine": {"desc":"황 함유 아미노산(비단백질성). 담즙산 결합, 삼투압 조절, 심근 안정화, GABAergic 조절에 관여.","origin_type":"현대과학","origin_story":"1827년 황소(taurus) 담즙에서 분리되어 이름 유래. 에너지 드링크의 주요 성분이나 '흥분'이 아닌 '안정화' 작용.","dosage":"1-3g/일","evidence":"양호","food_sources":"조개·굴, 생선, 닭고기, 소고기","fun_fact":"에너지 드링크의 타우린은 사실 흥분제가 아님. 카페인의 과도한 각성을 완화하는 완충제 역할을 함."},
}

def main():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "ingredients.json")
    path = os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    updated = 0
    for item in data:
        if item["tier"] != 1: continue
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
    print(f"T1 batch 1 updated: {updated}/{len(T1)}")

if __name__ == "__main__":
    main()
