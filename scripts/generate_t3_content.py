#!/usr/bin/env python3
"""
Generate Tier 3 content — brief descriptions for 116 additive entries.
Each entry gets: role (역할), one-line description, safety_class.
"""
import json, os

T3_CONTENT = {
    # === 부형제/충전제 ===
    "microcrystalline-cellulose": {"role": "부형제", "brief": "식물 섬유소를 미세 결정화한 것. 정제의 부피를 채우고 형태를 유지하는 가장 흔한 부형제.", "safety": "GRAS"},
    "corn-starch": {"role": "부형제", "brief": "옥수수에서 추출한 전분. 정제 안에서 활성 성분을 고르게 분산시키고 부피를 채움.", "safety": "GRAS"},
    "potato-starch": {"role": "부형제", "brief": "감자에서 추출한 전분. 정제의 부피를 채우고 성형을 도움.", "safety": "GRAS"},
    "rice-starch": {"role": "부형제", "brief": "쌀에서 추출한 전분. 알레르기 위험이 낮아 민감 제형에 선호됨.", "safety": "GRAS"},
    "pregelatinized-starch": {"role": "부형제", "brief": "미리 호화(가열)처리한 전분. 물에 쉽게 녹아 빠른 방출 제형에 사용.", "safety": "GRAS"},
    "dextrin": {"role": "부형제", "brief": "전분을 부분 분해한 탄수화물. 분말 제품의 흐름성과 용해성을 높임.", "safety": "GRAS"},
    "maltodextrin": {"role": "부형제/캡슐화", "brief": "전분에서 유래한 다당류. 분말 보충제의 부피를 만들고 활성 성분을 안정화.", "safety": "GRAS"},
    "lactose": {"role": "부형제", "brief": "우유에서 추출한 유당. 정제의 부피를 채우는 전통적 부형제. 유당불내증이 있다면 확인 필요.", "safety": "GRAS (주의: 유당불내증)"},
    "sucrose": {"role": "부형제/감미", "brief": "사탕수수 또는 사탕무에서 추출한 설탕. 맛을 개선하고 코팅에 사용.", "safety": "GRAS"},
    "mannitol": {"role": "부형제/감미", "brief": "자연계에 존재하는 당알코올. 씹어먹는 정제에서 시원한 감촉과 적당한 단맛을 제공.", "safety": "GRAS"},
    "polydextrose": {"role": "부형제/식이섬유", "brief": "합성 수용성 식이섬유. 부피를 채우면서 칼로리는 낮추는 역할.", "safety": "GRAS"},
    "cyclodextrin": {"role": "캡슐화", "brief": "전분을 환형으로 가공한 올리고당. 난용성 성분을 감싸 흡수율을 높이는 기술.", "safety": "GRAS"},
    "calcium-phosphate": {"role": "부형제", "brief": "칼슘과 인산의 화합물. 정제 부형제이자 칼슘·인 보충 역할을 겸함.", "safety": "GRAS"},
    "dicalcium-phosphate": {"role": "부형제", "brief": "이인산칼슘. 정제의 부피와 경도를 높이며, 소량의 칼슘과 인도 공급.", "safety": "GRAS"},
    "tricalcium-phosphate": {"role": "부형제/활택", "brief": "삼인산칼슘. 부형제 겸 흐름성 개선제. 분말이 뭉치지 않도록 도움.", "safety": "GRAS"},
    "calcium-silicate": {"role": "고결방지", "brief": "분말이 습기를 흡수해 뭉치는 것을 방지하는 고결방지제.", "safety": "GRAS"},
    "calcium-carbonate": {"role": "부형제/중화", "brief": "석회석에서 유래한 탄산칼슘. 정제 부형제, 산도 조절, 칼슘 보충을 겸함.", "safety": "GRAS"},

    # === 코팅제 ===
    "hpmc": {"role": "코팅제/캡슐", "brief": "식물성 셀룰로스 유도체. 정제 코팅과 식물성(비건) 캡슐의 주원료.", "safety": "GRAS"},
    "hydroxypropyl-cellulose": {"role": "코팅제", "brief": "셀룰로스를 화학적으로 변형한 중합체. 정제 표면에 보호막을 형성.", "safety": "GRAS"},
    "ethylcellulose": {"role": "코팅제", "brief": "셀룀로스의 에틸 에테르. 서방형(느리게 녹는) 코팅에 사용.", "safety": "GRAS"},
    "shellac": {"role": "코팅제", "brief": "락충(Lac bug)이 분비하는 천연 수지. 정제 표면에 광택 코팅을 형성.", "safety": "GRAS"},
    "carnauba-wax": {"role": "코팅/광택", "brief": "브라질 야자나무 잎에서 추출한 천연 왁스. 정제에 광택과 방습 효과.", "safety": "GRAS"},
    "beeswax": {"role": "코팅제", "brief": "꿀벌이 만든 천연 왁스. 정제 코팅과 연질 캡슐 제조에 사용.", "safety": "GRAS"},
    "yellow-beeswax": {"role": "코팅제", "brief": "정제하지 않은 자연 상태의 밀랍. 노란색은 프로폴리스 등 천연 성분에서 유래.", "safety": "GRAS"},
    "cellulose-acetate-phthalate": {"role": "장용 코팅", "brief": "위산에서 녹지 않고 장에서만 녹는 코팅제. 위장 자극 성분을 보호.", "safety": "식품첨가물 허가"},
    "methacrylic-acid-copolymer": {"role": "장용 코팅", "brief": "pH에 따라 선택적으로 녹는 합성 고분자. 장용 코팅에 사용.", "safety": "식품첨가물 허가"},
    "low-substituted-hpc": {"role": "붕해제/코팅", "brief": "저치환도 HPC. 물을 흡수하면 팽창하여 정제가 빨리 부서지도록 도움.", "safety": "GRAS"},
    "polyethylene-glycol": {"role": "코팅 가소제", "brief": "코팅막에 유연성을 부여하는 가소제. 코팅이 깨지지 않도록 도움.", "safety": "식품첨가물 허가"},
    "triethyl-citrate": {"role": "코팅 가소제", "brief": "구연산 유도체. 코팅 필름에 유연성을 부여하는 가소제.", "safety": "GRAS"},
    "cetyl-alcohol": {"role": "코팅 보조", "brief": "지방 알코올의 일종. 코팅과 정제 성형 과정에서 윤활 및 결합 역할.", "safety": "GRAS"},

    # === 유화제/안정제 ===
    "lecithin-emulsifier": {"role": "유화제", "brief": "대두 또는 해바라기에서 추출한 인지질. 기름과 물이 섞이도록 돕는 천연 유화제.", "safety": "GRAS"},
    "mono-diglyceride": {"role": "유화제", "brief": "지방산과 글리세롤의 결합체. 제형의 균일한 혼합 상태를 유지.", "safety": "GRAS"},
    "polysorbate-80": {"role": "유화제", "brief": "비이온성 계면활성제. 난용성 성분의 용해와 분산을 돕는 유화제.", "safety": "식품첨가물 허가"},
    "sucrose-ester": {"role": "유화제", "brief": "설탕과 지방산의 에스테르 결합물. 부드러운 질감과 안정적 유화를 제공.", "safety": "GRAS"},
    "fatty-acid-glyceride": {"role": "유화제", "brief": "지방산과 글리세롤의 결합체. 캡슐 내용물의 균질성 유지.", "safety": "GRAS"},
    "sodium-alginate": {"role": "증점/안정", "brief": "갈조류(해조류)에서 추출한 다당류. 액상 제형의 점도를 높이고 안정화.", "safety": "GRAS"},
    "xanthan-gum": {"role": "증점/안정", "brief": "미생물 발효로 생산하는 다당류. 액상 제형의 점도와 안정성을 높임.", "safety": "GRAS"},
    "guar-gum": {"role": "증점/안정", "brief": "구아콩에서 추출한 갈락토만난 다당류. 점도 조절과 안정화 역할.", "safety": "GRAS"},
    "locust-bean-gum": {"role": "증점/안정", "brief": "캐롭콩에서 추출한 갈락토만난. 다른 검류와 함께 사용하면 겔 형성.", "safety": "GRAS"},
    "gellan-gum": {"role": "증점/겔화", "brief": "미생물 발효로 얻는 다당류. 식물성 캡슐, 겔, 젤리 제형에 사용.", "safety": "GRAS"},
    "carrageenan": {"role": "겔화/증점", "brief": "홍조류(해조류)에서 추출한 다당류. 연질 캡슐과 겔 제형의 겔화제.", "safety": "GRAS"},
    "pectin": {"role": "겔화/증점", "brief": "과일 껍질에서 추출한 다당류. 구미(젤리) 보충제의 질감 형성.", "safety": "GRAS"},
    "agar": {"role": "겔화/캡슐", "brief": "우뭇가사리에서 추출한 다당류. 식물성 캡슐과 겔 제형의 원료.", "safety": "GRAS"},
    "gelatin": {"role": "캡슐 원료", "brief": "동물 콜라겐에서 추출한 단백질. 연질·경질 캡슐의 가장 전통적인 원료.", "safety": "GRAS"},
    "arabic-gum": {"role": "안정/유화", "brief": "아카시아 나무의 수액에서 얻는 천연 검. 유화 안정과 코팅 역할.", "safety": "GRAS"},
    "tragacanth": {"role": "증점/안정", "brief": "아스트라갈루스 속 관목의 수액에서 얻는 천연 검. 증점과 현탁 안정.", "safety": "GRAS"},
    "sodium-carboxymethylcellulose": {"role": "증점/안정", "brief": "셀룰로스의 카르복시메틸 유도체. 점성을 높이고 균일한 분산 유지.", "safety": "GRAS"},
    "glycerin": {"role": "보습/용매", "brief": "식물성 또는 합성 글리세롤. 연질 캡슐의 유연성과 수분 유지 역할.", "safety": "GRAS"},

    # === 활택제/흐름제 ===
    "magnesium-stearate": {"role": "활택제", "brief": "스테아린산의 마그네슘 염. 정제가 기계에 달라붙지 않도록 윤활하는 가장 흔한 활택제.", "safety": "GRAS"},
    "stearic-acid": {"role": "활택제", "brief": "코코넛·팜 오일에서 유래한 지방산. 정제 제조 시 윤활과 결합 역할.", "safety": "GRAS"},
    "silicon-dioxide": {"role": "흐름제", "brief": "이산화규소. 분말이 뭉치지 않고 자유롭게 흐르도록 하는 흐름제.", "safety": "GRAS"},
    "silicon-dioxide-flow": {"role": "흐름제", "brief": "이산화규소(흐름 개선 전용). 분말 제형의 균일한 충전을 도움.", "safety": "GRAS"},
    "silicon-dioxide-colloidal": {"role": "흐름제", "brief": "초미세 콜로이드 이산화규소. 표면적이 넓어 소량으로 강한 흐름성 개선.", "safety": "GRAS"},
    "talc": {"role": "활택제", "brief": "규산마그네슘 광물. 정제 제조 시 활택과 고결방지 역할.", "safety": "식품첨가물 허가"},

    # === 붕해제 ===
    "croscarmellose-sodium": {"role": "붕해제", "brief": "가교결합 셀룰로스. 물을 흡수하면 빠르게 팽창하여 정제를 부수는 핵심 붕해제.", "safety": "GRAS"},
    "sodium-croscarmellose": {"role": "붕해제", "brief": "크로스카르멜로스 칼슘 형태. 정제가 위장에서 빠르게 분해되도록 도움.", "safety": "GRAS"},
    "sodium-starch-glycolate": {"role": "붕해제", "brief": "변성 전분 유도체. 물을 만나면 부풀어 정제를 빠르게 부서뜨림.", "safety": "GRAS"},
    "povidone": {"role": "결합제", "brief": "수용성 합성 고분자(PVP). 분말 입자를 서로 결합시켜 정제 형태를 유지.", "safety": "GRAS"},
    "polyvinylpyrrolidone": {"role": "결합제", "brief": "PVP와 동일 성분. 습식 과립 공정에서 결합제로 사용.", "safety": "GRAS"},

    # === 감미료 ===
    "sucralose": {"role": "감미료", "brief": "설탕보다 약 600배 단 인공 감미료. 열량은 0. 씹어먹는 정제와 액상 제형에 사용.", "safety": "식품첨가물 허가"},
    "stevia": {"role": "감미료", "brief": "스테비아 잎에서 추출한 천연 감미료. 설탕 대비 약 200-300배 단맛, 칼로리 0.", "safety": "GRAS"},
    "xylitol": {"role": "감미료", "brief": "자작나무 등에서 추출한 당알코올. 시원한 단맛과 충치 예방 효과.", "safety": "GRAS"},
    "erythritol": {"role": "감미료", "brief": "과일에 자연 존재하는 당알코올. 설탕의 약 70% 단맛에 칼로리는 거의 0.", "safety": "GRAS"},
    "acesulfame-k": {"role": "감미료", "brief": "칼륨을 함유한 인공 감미료. 설탕의 약 200배 단맛. 다른 감미료와 혼합 사용.", "safety": "식품첨가물 허가"},
    "aspartame": {"role": "감미료", "brief": "아미노산 기반 인공 감미료. 설탕의 약 200배 단맛. 페닐케톤뇨증 환자는 주의.", "safety": "식품첨가물 허가 (주의: PKU)"},
    "sorbitol": {"role": "감미료/보습", "brief": "사과, 배 등 과일에서 유래한 당알코올. 시럽형 제형에서 보습과 감미 역할.", "safety": "GRAS"},

    # === 향료 ===
    "strawberry-flavor": {"role": "향료", "brief": "딸기 풍미를 내는 식품 향료. 씹어먹는 정제나 분말 제형의 기호성 향상.", "safety": "식품첨가물 허가"},
    "lemon-flavor": {"role": "향료", "brief": "레몬 풍미를 내는 식품 향료. 발포 정제와 액상 제형에 자주 사용.", "safety": "식품첨가물 허가"},
    "orange-flavor": {"role": "향료", "brief": "오렌지 풍미를 내는 식품 향료. 어린이용 제형에 흔히 사용.", "safety": "식품첨가물 허가"},
    "vanilla-flavor": {"role": "향료", "brief": "바닐라 풍미를 내는 식품 향료. 단백질 보충제와 분말 제형에 자주 사용.", "safety": "식품첨가물 허가"},
    "mint-flavor": {"role": "향료", "brief": "박하 풍미를 내는 식품 향료. 구강용 제형에서 청량감을 제공.", "safety": "식품첨가물 허가"},
    "mixed-fruit-flavor": {"role": "향료", "brief": "여러 과일 풍미를 혼합한 식품 향료. 다양한 제형의 기호성 향상.", "safety": "식품첨가물 허가"},

    # === 색소 ===
    "annatto": {"role": "색소", "brief": "아나토 씨에서 추출한 천연 주황-노랑 색소. 연질 캡슐과 정제의 착색.", "safety": "GRAS"},
    "caramel-color": {"role": "색소", "brief": "설탕을 가열하여 만든 갈색 색소. 액상 및 정제 제형에 갈색 톤을 부여.", "safety": "GRAS"},
    "chlorophyllin": {"role": "색소", "brief": "식물 엽록소에서 유래한 초록색 색소. 녹색 정제와 캡슐 착색에 사용.", "safety": "GRAS"},
    "riboflavin-color": {"role": "색소", "brief": "비타민B2를 색소로 사용. 노란색을 부여하며, 영양소 기능도 겸함.", "safety": "GRAS"},
    "iron-oxide-red": {"role": "색소", "brief": "산화철(적색). 정제 코팅에 붉은색～갈색 톤을 부여하는 무기 색소.", "safety": "식품첨가물 허가"},
    "iron-oxide-yellow": {"role": "색소", "brief": "산화철(황색). 정제 코팅에 노란색 톤을 부여하는 무기 색소.", "safety": "식품첨가물 허가"},
    "iron-oxide-black": {"role": "색소", "brief": "산화철(흑색). 정제 코팅에 검정색 톤을 부여하는 무기 색소.", "safety": "식품첨가물 허가"},
    "titanium-dioxide": {"role": "색소/차단", "brief": "백색 안료. 정제에 흰색을 부여하고 자외선 차단 역할. 일부 국가에서 사용 논란.", "safety": "식품첨가물 허가 (EU 규제 논의 중)"},

    # === 보존제/산화방지 ===
    "potassium-sorbate": {"role": "보존제", "brief": "소르빈산의 칼륨 염. 곰팡이와 효모의 성장을 억제하는 보존제.", "safety": "GRAS"},
    "sodium-benzoate": {"role": "보존제", "brief": "안식향산의 나트륨 염. 세균과 효모의 성장을 억제. 산성 환경에서 효과적.", "safety": "GRAS"},
    "rosemary-extract-preserv": {"role": "산화방지", "brief": "로즈마리에서 추출한 천연 산화방지제. 오일 성분의 산패를 막아 유통기한 연장.", "safety": "GRAS"},
    "mixed-tocopherol": {"role": "산화방지", "brief": "비타민E 혼합물을 산화방지제로 사용. 오일 성분의 산패를 막는 천연 보존제.", "safety": "GRAS"},
    "tocopheryl-acetate": {"role": "산화방지", "brief": "비타민E의 안정화 형태. 산화에 강해 성분 보존과 비타민E 보충을 겸함.", "safety": "GRAS"},
    "d-alpha-tocopherol": {"role": "산화방지", "brief": "천연 비타민E. 산화방지제로 사용되며 동시에 비타민E를 공급.", "safety": "GRAS"},
    "dl-alpha-tocopheryl-acetate": {"role": "산화방지/비타민", "brief": "합성 비타민E 아세테이트. 산화 안정성이 높아 보존제 겸 비타민 보충.", "safety": "GRAS"},
    "ascorbyl-palmitate": {"role": "산화방지", "brief": "비타민C의 지용성 형태. 오일 성분의 산화를 방지하는 천연 산화방지제.", "safety": "GRAS"},

    # === 산도 조절 ===
    "citric-acid": {"role": "산도 조절", "brief": "감귤류에서 유래한 유기산. 산도 조절, 풍미 강화, 보존 효과.", "safety": "GRAS"},
    "malic-acid": {"role": "산도 조절", "brief": "사과에서 유래한 유기산. 상큼한 맛을 더하고 산도를 조절.", "safety": "GRAS"},
    "tartaric-acid": {"role": "산도 조절", "brief": "포도에서 유래한 유기산. 발포 정제의 발포 반응과 산도 조절에 사용.", "safety": "GRAS"},

    # === 오일 ===
    "soybean-oil": {"role": "용매/캡슐", "brief": "대두에서 추출한 식물성 오일. 연질 캡슐의 충전 오일 및 지용성 성분의 용매.", "safety": "GRAS (주의: 대두 알레르기)"},
    "sunflower-oil": {"role": "용매/캡슐", "brief": "해바라기 씨에서 추출한 오일. 연질 캡슐 충전과 비타민E 원료 씨합체.", "safety": "GRAS"},
    "palm-oil": {"role": "부형제/오일", "brief": "팜 열매에서 추출한 식물성 오일. 캡슐 충전과 지용성 성분의 안정화.", "safety": "GRAS"},
    "palm-kernel-oil": {"role": "부형제/오일", "brief": "팜 종자에서 추출한 오일. 팜유 대비 라우르산 함량이 높아 안정성 우수.", "safety": "GRAS"},
    "medium-chain-triglyceride": {"role": "용매/오일", "brief": "코코넛유 유래 중쇄지방산. 지용성 성분의 흡수를 돕는 캡슐 충전제.", "safety": "GRAS"},
    "medium-chain-triglyceride-filler": {"role": "부형제", "brief": "MCT를 부형제로 사용. 캡슐 내부 빈 공간을 채우는 역할.", "safety": "GRAS"},
    "medium-chain-triglyceride-capsule": {"role": "캡슐 충전", "brief": "MCT를 캡슐 충전에 사용. 지용성 활성 성분과 혼합하여 캡슐 내부를 채움.", "safety": "GRAS"},
    "cacao-mass": {"role": "부형제/풍미", "brief": "카카오 열매를 갈아 만든 페이스트. 초콜릿 풍미와 질감을 제공.", "safety": "GRAS"},
    "cocoa-powder": {"role": "부형제/풍미", "brief": "카카오에서 지방을 제거한 분말. 초콜릿 풍미와 색을 부여.", "safety": "GRAS"},

    # === 비타민/미네랄 원료 형태 ===
    "riboflavin-phosphate": {"role": "비타민B2 원료", "brief": "비타민B2의 인산나트륨 형태. 수용성이 높아 액상 제형의 B2 원료로 선호.", "safety": "GRAS"},
    "cyanocobalamin": {"role": "비타민B12 원료", "brief": "비타민B12의 가장 흔한 합성 형태. 정제와 분말 보충제의 B12 원료.", "safety": "GRAS"},
    "thiamine-hcl": {"role": "비타민B1 원료", "brief": "비타민B1의 염산염 형태. 안정성이 높아 정제 제조에 가장 흔히 사용.", "safety": "GRAS"},
    "pyridoxine-hcl": {"role": "비타민B6 원료", "brief": "비타민B6의 염산염 형태. 보충제에서 가장 보편적인 B6 원료.", "safety": "GRAS"},
    "calcium-pantothenate": {"role": "비타민B5 원료", "brief": "판토텐산(비타민B5)의 칼슘 결합 형태. 안정성이 높아 보충제 원료로 사용.", "safety": "GRAS"},
    "folic-acid-synthetic": {"role": "엽산 원료", "brief": "합성 엽산. 체내에서 활성 엽산(5-MTHF)으로 전환되어 세포 분열에 기여.", "safety": "GRAS"},
    "sodium-ascorbate": {"role": "비타민C 원료", "brief": "비타민C의 나트륨 염 형태. 위장 자극이 적어 민감한 위를 위한 비타민C.", "safety": "GRAS"},
    "sodium-selenite": {"role": "셀레늄 원료", "brief": "셀레늄의 무기 형태. 보충제에서 셀레늄을 공급하는 원료.", "safety": "식품첨가물 허가"},
    "potassium-iodide": {"role": "요오드 원료", "brief": "요오드의 칼륨 염 형태. 갑상선 건강에 필수적인 요오드를 공급하는 원료.", "safety": "GRAS"},
    "sodium-molybdate": {"role": "몰리브덴 원료", "brief": "몰리브덴의 나트륨 염. 미량 미네랄 몰리브덴을 공급하는 보충제 원료.", "safety": "식품첨가물 허가"},
    "chromium-picolinate": {"role": "크롬 원료", "brief": "크롬과 피콜린산의 결합체. 혈당 관리 보충제에서 크롬을 공급하는 형태.", "safety": "GRAS"},
    "ferrous-fumarate": {"role": "철분 원료", "brief": "퓨마르산 제일철. 철분 보충제의 원료로, 위장 자극이 비교적 적은 형태.", "safety": "GRAS"},
    "cupric-sulfate": {"role": "구리 원료", "brief": "황산구리. 미량 미네랄 구리를 공급하는 보충제 원료.", "safety": "식품첨가물 허가"},
    "manganese-sulfate": {"role": "망간 원료", "brief": "황산망간. 미량 미네랄 망간을 공급하는 보충제 원료.", "safety": "식품첨가물 허가"},
    "magnesium-oxide": {"role": "마그네슘 원료/부형제", "brief": "산화마그네슘. 마그네슘 함량이 높지만 흡수율은 상대적으로 낮은 형태.", "safety": "GRAS"},
    "zinc-oxide": {"role": "아연 원료", "brief": "산화아연. 아연 보충과 정제 코팅의 백색 안료로 사용.", "safety": "GRAS"},
}


def main():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "ingredients.json")
    path = os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    updated = 0
    missing = []
    for item in data:
        if item["tier"] != 3:
            continue
        if item["id"] in T3_CONTENT:
            c = T3_CONTENT[item["id"]]
            item["content_role"] = c["role"]
            item["content_brief"] = c["brief"]
            item["safety_class"] = c["safety"]
            updated += 1
        else:
            missing.append(item["id"])

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Updated: {updated}/{len([i for i in data if i['tier']==3])}")
    if missing:
        print(f"Missing: {len(missing)}")
        for m in missing:
            print(f"  - {m}")

if __name__ == "__main__":
    main()
