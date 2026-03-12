#!/usr/bin/env python3
"""Expand Tier 1 ingredients to ~150 total."""
import json, os

NEW_T1 = [
    {"id":"vitamin-b-complex","name":"비타민B 복합체","name_en":"Vitamin B Complex","aliases":["비타민B군","B-Complex"],"nickname":"8종 B비타민의 팀 플레이","category":"vitamin","subcategory":"b-complex","tags_purpose":["만성피로"],"tags_function":["에너지 생성"],"tags_bodypart":["전신"],"mfds_functionality":"체내 에너지 생성에 필요"},
    {"id":"choline","name":"콜린","name_en":"Choline","aliases":["Choline"],"nickname":"뇌와 간이 함께 필요로 하는 필수 영양소","category":"vitamin","tags_purpose":["학습-수험생","간건강"],"tags_function":["인지 기능","간 건강"],"tags_bodypart":["뇌","간"],"daily_recommended":"550mg (남성), 425mg (여성)"},
    {"id":"inositol","name":"이노시톨","name_en":"Inositol","aliases":["미오이노시톨","Myo-Inositol"],"nickname":"세포 신호 전달의 2차 메신저","category":"vitamin","tags_purpose":["스트레스","수면"],"tags_function":["신경 안정"],"tags_bodypart":["뇌"]},
    {"id":"paba","name":"PABA","name_en":"Para-Aminobenzoic Acid","aliases":["파라아미노벤조산"],"nickname":"엽산 합성의 출발 물질","category":"vitamin","tags_purpose":["피부","탈모"],"tags_function":["피부 건강"],"tags_bodypart":["피부","모발"]},
    {"id":"phosphorus","name":"인","name_en":"Phosphorus","aliases":["Phosphorus","P"],"nickname":"뼈와 ATP의 필수 구성 원소","category":"mineral","tags_purpose":["뼈-관절"],"tags_function":["뼈 건강","에너지 생성"],"tags_bodypart":["뼈·관절"],"daily_recommended":"700mg"},
    {"id":"fluorine","name":"불소","name_en":"Fluorine","aliases":["Fluoride"],"nickname":"치아 에나멜의 강화제","category":"mineral","tags_purpose":["구강"],"tags_function":["구강 건강"],"tags_bodypart":["구강"]},
    {"id":"silicon","name":"규소","name_en":"Silicon","aliases":["실리카","Silica"],"nickname":"콜라겐 합성에 관여하는 미량 원소","category":"mineral","tags_purpose":["피부","뼈-관절","탈모"],"tags_function":["피부 건강","뼈 건강"],"tags_bodypart":["피부","뼈·관절","모발"]},
    {"id":"boron","name":"붕소","name_en":"Boron","aliases":["Boron"],"nickname":"칼슘과 마그네슘 대사를 돕는 미량 원소","category":"mineral","tags_purpose":["뼈-관절","갱년기"],"tags_function":["뼈 건강"],"tags_bodypart":["뼈·관절"]},
    {"id":"vanadium","name":"바나듐","name_en":"Vanadium","aliases":["Vanadium"],"nickname":"인슐린 유사 작용이 연구되는 미량 원소","category":"mineral","tags_purpose":["혈압-혈당"],"tags_function":["혈당 조절"],"tags_bodypart":["전신"]},
    {"id":"l-carnitine","name":"L-카르니틴","name_en":"L-Carnitine","aliases":["카르니틴","아세틸L카르니틴","L-Carnitine"],"nickname":"지방산을 미토콘드리아로 운반하는 셔틀","category":"amino_acid","tags_purpose":["다이어트","만성피로","운동"],"tags_function":["체지방 감소","에너지 생성"],"tags_bodypart":["근육","전신"]},
    {"id":"l-glutamine","name":"L-글루타민","name_en":"L-Glutamine","aliases":["글루타민","Glutamine"],"nickname":"장 세포와 면역 세포의 주 연료","category":"amino_acid","tags_purpose":["장건강","면역","운동"],"tags_function":["장 건강","면역 기능","근력 향상"],"tags_bodypart":["장","근육"]},
    {"id":"l-lysine","name":"L-라이신","name_en":"L-Lysine","aliases":["라이신","Lysine"],"nickname":"콜라겐 합성의 필수 아미노산","category":"amino_acid","tags_purpose":["피부","면역"],"tags_function":["콜라겐 합성","면역 기능"],"tags_bodypart":["피부","전신"]},
    {"id":"l-methionine","name":"L-메티오닌","name_en":"L-Methionine","aliases":["메티오닌","Methionine"],"nickname":"해독과 항산화의 황 함유 아미노산","category":"amino_acid","tags_purpose":["간건강","탈모"],"tags_function":["간 건강","모발 건강"],"tags_bodypart":["간","모발"]},
    {"id":"l-tyrosine","name":"L-티로신","name_en":"L-Tyrosine","aliases":["티로신","Tyrosine"],"nickname":"도파민과 갑상선 호르몬의 전구체","category":"amino_acid","tags_purpose":["학습-수험생","스트레스","만성피로"],"tags_function":["인지 기능"],"tags_bodypart":["뇌"]},
    {"id":"l-citrulline","name":"L-시트룰린","name_en":"L-Citrulline","aliases":["시트룰린","Citrulline"],"nickname":"수박에서 발견된 혈류 개선 아미노산","category":"amino_acid","tags_purpose":["운동","성기능","혈압-혈당"],"tags_function":["혈행 개선"],"tags_bodypart":["심장·혈관","근육"]},
    {"id":"glycine","name":"글리신","name_en":"Glycine","aliases":["Glycine"],"nickname":"가장 작은 아미노산, 콜라겐의 1/3을 차지","category":"amino_acid","tags_purpose":["수면","피부"],"tags_function":["수면 건강","콜라겐 합성"],"tags_bodypart":["뇌","피부"]},
    {"id":"epa","name":"EPA","name_en":"Eicosapentaenoic Acid","aliases":["에이코사펜타엔산"],"nickname":"혈관 건강에 특화된 오메가3","category":"fatty_acid","subcategory":"omega","tags_purpose":["혈압-혈당","콜레스테롤"],"tags_function":["혈행 개선","혈중 지질 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"dha","name":"DHA","name_en":"Docosahexaenoic Acid","aliases":["도코사헥사엔산"],"nickname":"뇌와 망막의 구조 지방산","category":"fatty_acid","subcategory":"omega","tags_purpose":["학습-수험생","눈건강","임산부"],"tags_function":["인지 기능","눈 건강","태아 발달"],"tags_bodypart":["뇌","눈"]},
    {"id":"alpha-lipoic-acid","name":"알파리포산","name_en":"Alpha-Lipoic Acid","aliases":["ALA","티옥트산","Alpha-Lipoic Acid"],"nickname":"수용성과 지용성 양쪽에서 작동하는 항산화제","category":"other_functional","tags_purpose":["노화방지","혈압-혈당"],"tags_function":["항산화","혈당 조절"],"tags_bodypart":["전신"]},
    {"id":"resveratrol","name":"레스베라트롤","name_en":"Resveratrol","aliases":["Resveratrol"],"nickname":"적포도주의 항노화 폴리페놀","category":"other_functional","tags_purpose":["노화방지","혈압-혈당"],"tags_function":["항산화","세포 보호"],"tags_bodypart":["심장·혈관","전신"]},
    {"id":"quercetin","name":"퀘르세틴","name_en":"Quercetin","aliases":["Quercetin","케르세틴"],"nickname":"양파 껍질에 풍부한 플라보노이드","category":"other_functional","tags_purpose":["면역","노화방지"],"tags_function":["항산화","면역 기능"],"tags_bodypart":["전신"]},
    {"id":"beta-glucan","name":"베타글루칸","name_en":"Beta-Glucan","aliases":["Beta-Glucan","베타-글루칸"],"nickname":"면역 세포를 깨우는 다당류","category":"other_functional","tags_purpose":["면역"],"tags_function":["면역 기능"],"tags_bodypart":["전신"],"mfds_functionality":"면역력 증진에 도움을 줄 수 있음"},
    {"id":"lactoferrin","name":"락토페린","name_en":"Lactoferrin","aliases":["Lactoferrin"],"nickname":"모유에서 발견된 면역 단백질","category":"protein","tags_purpose":["면역","장건강"],"tags_function":["면역 기능","장 건강"],"tags_bodypart":["장","전신"]},
    {"id":"whey-protein","name":"유청단백질","name_en":"Whey Protein","aliases":["유청","Whey Protein","WPC","WPI"],"nickname":"근육 합성 효율이 가장 높은 단백질","category":"protein","tags_purpose":["운동"],"tags_function":["근력 향상"],"tags_bodypart":["근육"]},
    {"id":"digestive-enzyme","name":"소화효소","name_en":"Digestive Enzyme","aliases":["아밀라아제","리파아제","프로테아제","Digestive Enzyme"],"nickname":"음식 분해를 돕는 생체 촉매","category":"enzyme","tags_purpose":["장건강"],"tags_function":["장 건강"],"tags_bodypart":["위","장"]},
    {"id":"nattokinase","name":"나토키나제","name_en":"Nattokinase","aliases":["나토키나아제","Nattokinase"],"nickname":"낫토에서 유래한 혈전 분해 효소","category":"enzyme","tags_purpose":["혈압-혈당","콜레스테롤"],"tags_function":["혈행 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"serrapeptase","name":"세라펩타아제","name_en":"Serrapeptase","aliases":["Serrapeptase"],"nickname":"누에에서 발견된 단백질 분해 효소","category":"enzyme","tags_purpose":["뼈-관절"],"tags_function":["관절 건강"],"tags_bodypart":["뼈·관절"]},
    {"id":"postbiotics","name":"포스트바이오틱스","name_en":"Postbiotics","aliases":["Postbiotics","사균체"],"nickname":"유익균의 대사 산물","category":"probiotic","tags_purpose":["장건강","면역"],"tags_function":["장 건강","면역 기능"],"tags_bodypart":["장"]},
    {"id":"lactobacillus","name":"락토바실러스","name_en":"Lactobacillus","aliases":["유산균","Lactobacillus"],"nickname":"장내 산성 환경을 만드는 대표 유익균","category":"probiotic","tags_purpose":["장건강","면역"],"tags_function":["장 건강"],"tags_bodypart":["장"]},
    {"id":"bifidobacterium","name":"비피도박테리움","name_en":"Bifidobacterium","aliases":["비피더스","Bifidobacterium"],"nickname":"대장에 주로 서식하는 혐기성 유익균","category":"probiotic","tags_purpose":["장건강"],"tags_function":["장 건강","배변 활동"],"tags_bodypart":["장"]},
    {"id":"saccharomyces-boulardii","name":"사카로마이세스 보울라디","name_en":"Saccharomyces boulardii","aliases":["S. boulardii"],"nickname":"효모 기반 프로바이오틱","category":"probiotic","tags_purpose":["장건강"],"tags_function":["장 건강"],"tags_bodypart":["장"]},
    {"id":"red-clover","name":"레드클로버","name_en":"Red Clover","aliases":["붉은토끼풀","Red Clover"],"nickname":"이소플라본이 풍부한 갱년기 허브","category":"extract","tags_purpose":["갱년기"],"tags_function":["여성 건강"],"tags_bodypart":["전신"]},
    {"id":"cranberry-extract","name":"크랜베리추출물","name_en":"Cranberry Extract","aliases":["크랜베리","Cranberry"],"nickname":"요로 건강의 붉은 열매","category":"extract","tags_purpose":["면역"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"pycnogenol","name":"피크노제놀","name_en":"Pycnogenol","aliases":["소나무껍질추출물","Pine Bark Extract"],"nickname":"프랑스 해안 소나무 껍질의 항산화 추출물","category":"extract","tags_purpose":["노화방지","혈압-혈당","피부"],"tags_function":["항산화","혈행 개선"],"tags_bodypart":["심장·혈관","피부"]},
    {"id":"berberine","name":"베르베린","name_en":"Berberine","aliases":["황련추출물","Berberine"],"nickname":"황련에서 추출한 혈당 조절 알칼로이드","category":"extract","tags_purpose":["혈압-혈당","다이어트"],"tags_function":["혈당 조절"],"tags_bodypart":["전신"]},
    {"id":"kudzu-root","name":"칡추출물","name_en":"Kudzu Root","aliases":["칡","갈근","Pueraria","Kudzu"],"nickname":"한방에서 오래 사용된 갈근의 현대적 추출","category":"extract","tags_purpose":["숙취","갱년기"],"tags_function":["간 건강","여성 건강"],"tags_bodypart":["간"]},
    {"id":"artichoke-extract","name":"아티초크추출물","name_en":"Artichoke Extract","aliases":["아티초크","Artichoke","시나린"],"nickname":"담즙 분비를 촉진하는 지중해 원료","category":"extract","tags_purpose":["간건강","콜레스테롤","장건강"],"tags_function":["간 건강","혈중 지질 개선"],"tags_bodypart":["간"]},
    {"id":"olive-leaf-extract","name":"올리브잎추출물","name_en":"Olive Leaf Extract","aliases":["올리브잎","올레유로핀","Oleuropein"],"nickname":"올리브 열매가 아닌 잎의 항산화 성분","category":"extract","tags_purpose":["혈압-혈당","면역"],"tags_function":["항산화","혈압 조절"],"tags_bodypart":["심장·혈관"]},
    {"id":"korean-angelica","name":"당귀추출물","name_en":"Korean Angelica","aliases":["당귀","참당귀","Angelica gigas"],"nickname":"여성 건강의 한방 대표 원료","category":"extract","tags_purpose":["갱년기","만성피로"],"tags_function":["여성 건강","혈행 개선"],"tags_bodypart":["전신"]},
    {"id":"schisandra","name":"오미자추출물","name_en":"Schisandra Extract","aliases":["오미자","Schisandra chinensis"],"nickname":"다섯 가지 맛의 간 보호 열매","category":"extract","tags_purpose":["간건강","만성피로"],"tags_function":["간 건강"],"tags_bodypart":["간"]},
    {"id":"licorice-root","name":"감초추출물","name_en":"Licorice Root","aliases":["감초","글리시리진","Glycyrrhizin"],"nickname":"한방 처방의 조화제이자 위장 보호제","category":"extract","tags_purpose":["장건강","스트레스"],"tags_function":["장 건강"],"tags_bodypart":["위","장"]},
    {"id":"ginger-extract","name":"생강추출물","name_en":"Ginger Extract","aliases":["생강","진저롤","Gingerol"],"nickname":"소화를 돕고 몸을 따뜻하게 하는 뿌리","category":"extract","tags_purpose":["장건강"],"tags_function":["장 건강"],"tags_bodypart":["위","장"]},
    {"id":"cinnamon-extract","name":"계피추출물","name_en":"Cinnamon Extract","aliases":["계피","시나몬","Cinnamon"],"nickname":"혈당 조절에 관한 연구가 활발한 향신료","category":"extract","tags_purpose":["혈압-혈당"],"tags_function":["혈당 조절"],"tags_bodypart":["전신"]},
    {"id":"fenugreek","name":"호로파추출물","name_en":"Fenugreek","aliases":["호로파","Fenugreek","Trigonella"],"nickname":"혈당과 남성 건강 양쪽에 연구되는 씨앗","category":"extract","tags_purpose":["혈압-혈당","성기능"],"tags_function":["혈당 조절","남성 건강"],"tags_bodypart":["전신"]},
    {"id":"tribulus","name":"트리뷸러스","name_en":"Tribulus Terrestris","aliases":["질려자","Tribulus"],"nickname":"남성 활력에 전통적으로 사용된 식물","category":"extract","tags_purpose":["성기능","운동"],"tags_function":["남성 건강"],"tags_bodypart":["전신"]},
    {"id":"panax-ginseng","name":"인삼","name_en":"Panax Ginseng","aliases":["인삼","Ginseng","진세노사이드"],"nickname":"홍삼의 원료 — 가공 전 상태의 삼","category":"extract","tags_purpose":["만성피로","면역"],"tags_function":["면역 기능","에너지 생성"],"tags_bodypart":["전신"]},
    {"id":"cordyceps","name":"동충하초","name_en":"Cordyceps","aliases":["Cordyceps","코디셉스"],"nickname":"곤충에서 자라는 약용 버섯","category":"extract","tags_purpose":["만성피로","운동","면역"],"tags_function":["에너지 생성","면역 기능"],"tags_bodypart":["전신"]},
    {"id":"reishi","name":"영지버섯","name_en":"Reishi","aliases":["Ganoderma","영지","Reishi"],"nickname":"불로초라 불린 면역 조절 버섯","category":"extract","tags_purpose":["면역","스트레스"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"lions-mane","name":"노루궁뎅이버섯","name_en":"Lion's Mane","aliases":["Lion's Mane","Hericium erinaceus"],"nickname":"신경 성장 인자를 자극하는 것으로 연구된 버섯","category":"extract","tags_purpose":["학습-수험생","노화방지"],"tags_function":["인지 기능"],"tags_bodypart":["뇌"]},
    {"id":"chaga","name":"차가버섯","name_en":"Chaga","aliases":["Chaga","Inonotus obliquus"],"nickname":"자작나무에서 자라는 항산화 버섯","category":"extract","tags_purpose":["면역","노화방지"],"tags_function":["항산화","면역 기능"],"tags_bodypart":["전신"]},
    {"id":"turkey-tail","name":"구름버섯","name_en":"Turkey Tail","aliases":["운지버섯","Trametes versicolor","PSK"],"nickname":"면역 조절 다당체 PSK의 원료 버섯","category":"extract","tags_purpose":["면역"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"green-lipped-mussel","name":"초록입홍합","name_en":"Green-Lipped Mussel","aliases":["Green-Lipped Mussel","뉴질랜드초록홍합"],"nickname":"뉴질랜드산 관절 건강 원료","category":"extract","tags_purpose":["뼈-관절"],"tags_function":["관절 건강"],"tags_bodypart":["뼈·관절"]},
    {"id":"type-2-collagen","name":"비변성2형콜라겐","name_en":"UC-II (Undenatured Type II Collagen)","aliases":["UC-II","2형 콜라겐"],"nickname":"면역 관용으로 관절을 보호하는 콜라겐","category":"protein","tags_purpose":["뼈-관절"],"tags_function":["관절 건강"],"tags_bodypart":["뼈·관절"]},
    {"id":"elastin-peptide","name":"엘라스틴 펩타이드","name_en":"Elastin Peptide","aliases":["엘라스틴","Elastin"],"nickname":"피부 탄력을 담당하는 구조 단백질","category":"protein","tags_purpose":["피부"],"tags_function":["피부 건강"],"tags_bodypart":["피부"]},
    {"id":"ceramide","name":"세라마이드","name_en":"Ceramide","aliases":["Ceramide"],"nickname":"피부 장벽의 지질 벽돌","category":"other_functional","tags_purpose":["피부"],"tags_function":["피부 건강"],"tags_bodypart":["피부"]},
    {"id":"gamma-oryzanol","name":"감마오리자놀","name_en":"Gamma-Oryzanol","aliases":["감마오리자놀","Gamma-Oryzanol"],"nickname":"쌀겨에서 추출한 자율신경 안정 성분","category":"other_functional","tags_purpose":["갱년기","스트레스"],"tags_function":["신경 안정"],"tags_bodypart":["뇌"]},
    {"id":"dhea","name":"DHEA","name_en":"Dehydroepiandrosterone","aliases":["디하이드로에피안드로스테론"],"nickname":"체내에서 성호르몬으로 전환되는 전구체","category":"other_functional","tags_purpose":["노화방지","성기능"],"tags_function":["남성 건강"],"tags_bodypart":["전신"]},
    {"id":"methylsulfonylmethane","name":"히알루론산나트륨","name_en":"Sodium Hyaluronate","aliases":["소듐히알루로네이트"],"nickname":"히알루론산의 저분자 형태","category":"other_functional","tags_purpose":["피부","뼈-관절"],"tags_function":["피부 건강","관절 건강"],"tags_bodypart":["피부","뼈·관절"]},
    {"id":"mct-oil","name":"MCT 오일","name_en":"MCT Oil","aliases":["중쇄지방산","Medium Chain Triglycerides"],"nickname":"빠르게 에너지로 전환되는 지방","category":"fatty_acid","tags_purpose":["다이어트","만성피로"],"tags_function":["에너지 생성"],"tags_bodypart":["전신"]},
    {"id":"plant-sterol","name":"식물스테롤","name_en":"Plant Sterols","aliases":["피토스테롤","Phytosterol","Plant Sterol"],"nickname":"콜레스테롤 흡수를 경쟁적으로 차단","category":"other_functional","tags_purpose":["콜레스테롤"],"tags_function":["혈중 지질 개선"],"tags_bodypart":["심장·혈관"],"mfds_functionality":"혈중 콜레스테롤 개선에 도움을 줄 수 있음"},
    {"id":"chitosan","name":"키토산","name_en":"Chitosan","aliases":["키토산","Chitosan"],"nickname":"갑각류 껍데기에서 유래한 지방 흡착 다당류","category":"fiber","tags_purpose":["다이어트","콜레스테롤"],"tags_function":["체지방 감소","혈중 지질 개선"],"tags_bodypart":["장"],"mfds_functionality":"혈중 콜레스테롤 개선에 도움을 줄 수 있음"},
    {"id":"chlorogenic-acid","name":"클로로겐산","name_en":"Chlorogenic Acid","aliases":["클로로겐산","녹색커피빈추출물","Green Coffee Bean"],"nickname":"커피 원두의 체지방 관련 폴리페놀","category":"other_functional","tags_purpose":["다이어트"],"tags_function":["체지방 감소"],"tags_bodypart":["전신"],"mfds_functionality":"체지방 감소에 도움을 줄 수 있음"},
    {"id":"octacosanol","name":"옥타코사놀","name_en":"Octacosanol","aliases":["Octacosanol","폴리코사놀"],"nickname":"사탕수수 왁스에서 추출한 지구력 성분","category":"other_functional","tags_purpose":["콜레스테롤","운동"],"tags_function":["혈중 지질 개선"],"tags_bodypart":["심장·혈관"],"mfds_functionality":"혈중 콜레스테롤 개선에 도움을 줄 수 있음"},
    {"id":"corosolic-acid","name":"코로솔산","name_en":"Corosolic Acid","aliases":["바나바잎추출물","Banaba Leaf","Corosolic Acid"],"nickname":"바나바 잎의 혈당 조절 성분","category":"extract","tags_purpose":["혈압-혈당"],"tags_function":["혈당 조절"],"tags_bodypart":["전신"],"mfds_functionality":"식후 혈당 상승 억제에 도움을 줄 수 있음"},
    {"id":"helianthus-tuberosus","name":"돼지감자추출물","name_en":"Jerusalem Artichoke","aliases":["돼지감자","이눌린","Jerusalem Artichoke"],"nickname":"이눌린이 풍부한 혈당 관리 뿌리채소","category":"extract","tags_purpose":["혈압-혈당","장건강"],"tags_function":["혈당 조절","장 건강"],"tags_bodypart":["장"]},
    {"id":"guggul","name":"구굴","name_en":"Guggul","aliases":["Commiphora mukul","구굴스테론"],"nickname":"인도 전통 콜레스테롤 관리 수지","category":"extract","tags_purpose":["콜레스테롤"],"tags_function":["혈중 지질 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"squalene","name":"스쿠알렌","name_en":"Squalene","aliases":["Squalene","스쿠알란"],"nickname":"상어 간유 또는 올리브에서 추출한 산소 운반체","category":"other_functional","tags_purpose":["면역","피부"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"fucoidan","name":"후코이단","name_en":"Fucoidan","aliases":["Fucoidan"],"nickname":"해조류의 면역 조절 다당류","category":"other_functional","tags_purpose":["면역"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"hesperidin","name":"헤스페리딘","name_en":"Hesperidin","aliases":["Hesperidin"],"nickname":"감귤 속껍질의 혈관 보호 플라보노이드","category":"other_functional","tags_purpose":["혈압-혈당"],"tags_function":["혈행 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"rutin","name":"루틴","name_en":"Rutin","aliases":["Rutin"],"nickname":"메밀에 풍부한 모세혈관 강화 성분","category":"other_functional","tags_purpose":["혈압-혈당"],"tags_function":["혈행 개선"],"tags_bodypart":["심장·혈관"]},
]

def main():
    path = os.path.join(os.path.dirname(__file__), "..", "data", "ingredients.json")
    path = os.path.abspath(path)
    with open(path, "r", encoding="utf-8") as f:
        existing = json.load(f)
    existing_ids = {i["id"] for i in existing}
    added = 0
    for item in NEW_T1:
        if item["id"] in existing_ids:
            continue
        item["tier"] = 1
        item["source_type"] = item.get("source_type", "고시형")
        for k in ["tags_age","tags_gender","aliases","related_ingredients"]:
            item.setdefault(k, ["전연령"] if k=="tags_age" else ["공통"] if k=="tags_gender" else [])
        for k in ["upper_limit","daily_recommended","mfds_functionality","subcategory","nickname","name_en"]:
            item.setdefault(k, "")
        existing.append(item)
        added += 1
    with open(path, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    t1 = sum(1 for i in existing if i["tier"]==1)
    print(f"Added {added} Tier 1 items. Total T1: {t1}, Grand total: {len(existing)}")

if __name__ == "__main__":
    main()
