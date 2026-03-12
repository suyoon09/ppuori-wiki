#!/usr/bin/env python3
"""
Massive expansion to make the ingredient database truly exhaustive.
Sources: 식약처 고시형 69종 기능성원료 complete list, 개별인정형 주요 원료,
식품원료 목록, industry ingredient catalogs.
"""
import json, os

# ============================================================
# CONFIRMED 고시형 기능성원료 69종 — MISSING ONES ONLY
# Source: foodpolis.kr/MFDS 건강기능식품 공전
# ============================================================
GOSI_MISSING = [
    # These are the officially gazetted 69 functional ingredients NOT yet in our DB
    {"id":"marigold-lutein","name":"마리골드꽃추출물","name_en":"Marigold Extract","aliases":["마리골드","루테인 원료"],"nickname":"루테인의 원료 — 금잔화에서 추출","category":"extract","tier":1,"source_type":"고시형","tags_purpose":["눈건강"],"tags_function":["눈 건강"],"tags_bodypart":["눈"],"mfds_functionality":"노화로 인해 감소될 수 있는 황반색소밀도를 유지하는 데 도움을 줄 수 있음"},
    {"id":"haematococcus","name":"헤마토코쿠스추출물","name_en":"Haematococcus Extract","aliases":["헤마토코쿠스","아스타잔틴 원료"],"nickname":"아스타잔틴의 원료 — 미세조류에서 추출","category":"extract","tier":1,"source_type":"고시형","tags_purpose":["눈건강","노화방지"],"tags_function":["항산화","눈 건강"],"tags_bodypart":["눈","전신"],"mfds_functionality":"눈의 피로도 개선에 도움을 줄 수 있음"},
    {"id":"coleus-forskohlii","name":"콜레우스포스콜리추출물","name_en":"Coleus Forskohlii Extract","aliases":["포스콜린","Forskolin"],"nickname":"체지방 감소에 연구된 인도 허브","category":"extract","tier":1,"source_type":"고시형","tags_purpose":["다이어트"],"tags_function":["체지방 감소"],"tags_bodypart":["전신"],"mfds_functionality":"과체중인 성인의 체지방 감소에 도움을 줄 수 있음"},
    {"id":"konjac","name":"곤약감자추출물","name_en":"Konjac Extract","aliases":["곤약","글루코만난","Glucomannan"],"nickname":"위에서 팽창하는 수용성 식이섬유","category":"fiber","tier":1,"source_type":"고시형","tags_purpose":["다이어트","장건강","콜레스테롤"],"tags_function":["배변 활동","혈중 지질 개선"],"tags_bodypart":["장"],"mfds_functionality":"배변활동 원활, 혈중 콜레스테롤 개선에 도움을 줄 수 있음"},
    {"id":"sophora-japonica","name":"회화나무열매추출물","name_en":"Sophora Japonica Extract","aliases":["회화나무","루틴 원료"],"nickname":"루틴이 풍부한 한방 열매 추출물","category":"extract","tier":1,"source_type":"고시형","tags_purpose":["혈압-혈당"],"tags_function":["혈행 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"plum-extract","name":"매실추출물","name_en":"Plum Extract","aliases":["매실","매실 농축액"],"nickname":"유기산이 풍부한 한국 전통 건강 과일","category":"extract","tier":1,"source_type":"고시형","tags_purpose":["장건강"],"tags_function":["장 건강"],"tags_bodypart":["장"],"mfds_functionality":"피로 개선에 도움을 줄 수 있음"},
    {"id":"guava-leaf","name":"구아바잎추출물","name_en":"Guava Leaf Extract","aliases":["구아바잎"],"nickname":"혈당 관리에 연구된 열대 잎 추출물","category":"extract","tier":1,"source_type":"고시형","tags_purpose":["혈압-혈당"],"tags_function":["혈당 조절"],"tags_bodypart":["전신"],"mfds_functionality":"식후 혈당 상승 억제에 도움을 줄 수 있음"},
    {"id":"shark-liver-oil","name":"알콕시글리세롤함유상어간유","name_en":"Shark Liver Oil","aliases":["상어간유","AKG"],"nickname":"면역 조절 지질을 함유한 심해 상어 간 오일","category":"fatty_acid","tier":1,"source_type":"고시형","tags_purpose":["면역"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"tomato-extract","name":"토마토추출물","name_en":"Tomato Extract","aliases":["토마토 리코펜"],"nickname":"리코펜 농축 토마토 추출물","category":"extract","tier":1,"source_type":"고시형","tags_purpose":["노화방지"],"tags_function":["항산화"],"tags_bodypart":["전신"],"mfds_functionality":"항산화에 도움을 줄 수 있음"},
    {"id":"sanghwang-mushroom","name":"상황버섯추출물","name_en":"Phellinus linteus Extract","aliases":["상황버섯","장수버섯"],"nickname":"면역 조절 베타글루칸이 풍부한 약용 버섯","category":"extract","tier":1,"source_type":"고시형","tags_purpose":["면역"],"tags_function":["면역 기능"],"tags_bodypart":["전신"],"mfds_functionality":"면역력 증진에 도움을 줄 수 있음"},
    # Additional 고시형 that are nutrition-type
    {"id":"essential-fatty-acid","name":"필수지방산","name_en":"Essential Fatty Acids","aliases":["리놀레산","알파리놀렌산"],"nickname":"체내에서 합성할 수 없어 반드시 섭취해야 하는 지방산","category":"fatty_acid","tier":1,"source_type":"고시형","tags_purpose":["혈압-혈당"],"tags_function":["혈중 지질 개선"],"tags_bodypart":["전신"]},
    {"id":"protein-supplement","name":"단백질","name_en":"Protein","aliases":["대두단백","유청단백","카세인"],"nickname":"근육·효소·호르몬의 원료인 거대분자","category":"protein","tier":1,"source_type":"고시형","tags_purpose":["운동"],"tags_function":["근력 향상"],"tags_bodypart":["근육"],"mfds_functionality":"근육, 결합조직 등 신체조직의 구성성분"},
]

# ============================================================
# 개별인정형 — MAJOR CATEGORIES (there are 675 entries, many duplicates)
# Unique ingredients extracted from known categories
# ============================================================
GAEBYIN_MISSING = [
    # 프로바이오틱스 개별인정 variants
    {"id":"lactobacillus-rhamnosus","name":"락토바실러스 람노서스","name_en":"Lactobacillus rhamnosus","aliases":["L. rhamnosus GG","LGG"],"category":"probiotic","tags_purpose":["장건강","면역"],"tags_function":["장 건강","면역 기능"],"tags_bodypart":["장"]},
    {"id":"lactobacillus-plantarum","name":"락토바실러스 플란타룸","name_en":"Lactobacillus plantarum","aliases":["L. plantarum"],"category":"probiotic","tags_purpose":["장건강"],"tags_function":["장 건강"],"tags_bodypart":["장"]},
    {"id":"lactobacillus-acidophilus","name":"락토바실러스 아시도필러스","name_en":"Lactobacillus acidophilus","aliases":["L. acidophilus"],"category":"probiotic","tags_purpose":["장건강"],"tags_function":["장 건강"],"tags_bodypart":["장"]},
    {"id":"lactobacillus-casei","name":"락토바실러스 카세이","name_en":"Lactobacillus casei","aliases":["L. casei"],"category":"probiotic","tags_purpose":["장건강","면역"],"tags_function":["장 건강"],"tags_bodypart":["장"]},
    {"id":"lactobacillus-reuteri","name":"락토바실러스 루테리","name_en":"Lactobacillus reuteri","aliases":["L. reuteri"],"category":"probiotic","tags_purpose":["장건강","구강"],"tags_function":["장 건강","구강 건강"],"tags_bodypart":["장","구강"]},
    {"id":"lactobacillus-helveticus","name":"락토바실러스 헬베티쿠스","name_en":"Lactobacillus helveticus","aliases":["L. helveticus"],"category":"probiotic","tags_purpose":["장건강","수면"],"tags_function":["장 건강"],"tags_bodypart":["장"]},
    {"id":"bifidobacterium-longum","name":"비피도박테리움 롱검","name_en":"Bifidobacterium longum","aliases":["B. longum"],"category":"probiotic","tags_purpose":["장건강"],"tags_function":["장 건강"],"tags_bodypart":["장"]},
    {"id":"bifidobacterium-breve","name":"비피도박테리움 브레비","name_en":"Bifidobacterium breve","aliases":["B. breve"],"category":"probiotic","tags_purpose":["장건강","면역"],"tags_function":["장 건강"],"tags_bodypart":["장"]},
    {"id":"bifidobacterium-lactis","name":"비피도박테리움 락티스","name_en":"Bifidobacterium lactis","aliases":["B. lactis","BB-12"],"category":"probiotic","tags_purpose":["장건강","면역"],"tags_function":["장 건강","면역 기능"],"tags_bodypart":["장"]},
    {"id":"bifidobacterium-animalis","name":"비피도박테리움 아니말리스","name_en":"Bifidobacterium animalis","aliases":["B. animalis"],"category":"probiotic","tags_purpose":["장건강"],"tags_function":["장 건강","배변 활동"],"tags_bodypart":["장"]},
    {"id":"streptococcus-thermophilus","name":"스트렙토코쿠스 써모필러스","name_en":"Streptococcus thermophilus","aliases":["S. thermophilus"],"category":"probiotic","tags_purpose":["장건강"],"tags_function":["장 건강"],"tags_bodypart":["장"]},
    {"id":"lactococcus-lactis","name":"락토코쿠스 락티스","name_en":"Lactococcus lactis","aliases":["L. lactis"],"category":"probiotic","tags_purpose":["장건강"],"tags_function":["장 건강"],"tags_bodypart":["장"]},
    {"id":"weissella-cibaria","name":"웨이셀라 시바리아","name_en":"Weissella cibaria","aliases":["W. cibaria"],"category":"probiotic","tags_purpose":["구강"],"tags_function":["구강 건강"],"tags_bodypart":["구강"]},
    # 개별인정 기능성 원료 — diverse categories
    {"id":"rg3-ginsenoside","name":"진세노사이드 Rg3","name_en":"Ginsenoside Rg3","aliases":["Rg3","흑삼추출물"],"category":"extract","tags_purpose":["면역"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"fermented-ginseng","name":"발효홍삼추출물","name_en":"Fermented Red Ginseng","aliases":["발효홍삼","Compound K"],"category":"extract","tags_purpose":["면역","만성피로"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"black-ginseng","name":"흑삼추출물","name_en":"Black Ginseng Extract","aliases":["흑삼","9증9포"],"category":"extract","tags_purpose":["면역","만성피로"],"tags_function":["면역 기능","에너지 생성"],"tags_bodypart":["전신"]},
    {"id":"deer-antler","name":"녹용추출물","name_en":"Deer Antler Extract","aliases":["녹용","녹각"],"category":"extract","tags_purpose":["면역","만성피로"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"platycodon","name":"도라지추출물","name_en":"Platycodon Extract","aliases":["도라지","길경"],"category":"extract","tags_purpose":["면역"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"pterostilbene","name":"프테로스틸벤","name_en":"Pterostilbene","aliases":["Pterostilbene"],"category":"other_functional","tags_purpose":["노화방지"],"tags_function":["항산화"],"tags_bodypart":["전신"]},
    {"id":"pine-needle","name":"솔잎추출물","name_en":"Pine Needle Extract","aliases":["솔잎","송엽"],"category":"extract","tags_purpose":["혈압-혈당"],"tags_function":["혈행 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"mugwort","name":"쑥추출물","name_en":"Mugwort Extract","aliases":["쑥","애엽"],"category":"extract","tags_purpose":["장건강","갱년기"],"tags_function":["장 건강"],"tags_bodypart":["장"]},
    {"id":"bamboo-extract","name":"죽엽추출물","name_en":"Bamboo Leaf Extract","aliases":["대나무잎","죽엽"],"category":"extract","tags_purpose":["노화방지"],"tags_function":["항산화"],"tags_bodypart":["전신"]},
    {"id":"persimmon-leaf","name":"감잎추출물","name_en":"Persimmon Leaf Extract","aliases":["감잎"],"category":"extract","tags_purpose":["노화방지"],"tags_function":["항산화"],"tags_bodypart":["전신"]},
    {"id":"mulberry-root-bark","name":"상백피추출물","name_en":"Mulberry Root Bark","aliases":["상백피"],"category":"extract","tags_purpose":["혈압-혈당"],"tags_function":["혈당 조절"],"tags_bodypart":["전신"]},
    {"id":"acanthopanax","name":"오가피추출물","name_en":"Acanthopanax Extract","aliases":["오가피","Acanthopanax senticosus","시베리아 인삼"],"category":"extract","tags_purpose":["면역","만성피로"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"hovenia-dulcis","name":"헛개나무추출물","name_en":"Hovenia dulcis Extract","aliases":["헛개나무","지구자"],"category":"extract","tags_purpose":["숙취","간건강"],"tags_function":["간 건강"],"tags_bodypart":["간"],"mfds_functionality":"알코올성 손상으로부터 간 건강에 도움을 줄 수 있음"},
    {"id":"pueraria-mirifica","name":"백수오추출물","name_en":"Pueraria mirifica Extract","aliases":["백수오"],"category":"extract","tags_purpose":["갱년기"],"tags_function":["여성 건강"],"tags_bodypart":["전신"]},
    {"id":"chrysanthemum","name":"국화추출물","name_en":"Chrysanthemum Extract","aliases":["국화","감국"],"category":"extract","tags_purpose":["눈건강"],"tags_function":["눈 건강"],"tags_bodypart":["눈"]},
    {"id":"cassia-seed","name":"결명자추출물","name_en":"Cassia Seed Extract","aliases":["결명자"],"category":"extract","tags_purpose":["눈건강","장건강"],"tags_function":["눈 건강","배변 활동"],"tags_bodypart":["눈","장"]},
    {"id":"chlorella-extract","name":"클로렐라추출물","name_en":"Chlorella Extract","aliases":["클로렐라 엑기스"],"category":"extract","tags_purpose":["면역"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"fermented-soybean","name":"청국장추출물","name_en":"Fermented Soybean Extract","aliases":["청국장","나토","낫또"],"category":"extract","tags_purpose":["혈압-혈당","콜레스테롤"],"tags_function":["혈행 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"green-mussel-lipid","name":"초록입홍합오일","name_en":"Green-Lipped Mussel Lipid","aliases":["GLME"],"category":"fatty_acid","tags_purpose":["뼈-관절"],"tags_function":["관절 건강"],"tags_bodypart":["뼈·관절"]},
    {"id":"hyaluronic-acid-chicken","name":"닭볏추출물히알루론산","name_en":"Chicken Comb Hyaluronic Acid","aliases":["닭볏 히알루론산"],"category":"other_functional","tags_purpose":["피부","뼈-관절"],"tags_function":["피부 건강","관절 건강"],"tags_bodypart":["피부","뼈·관절"]},
    {"id":"egg-shell-membrane","name":"난각막","name_en":"Egg Shell Membrane","aliases":["ESM","에그쉘멤브레인"],"category":"protein","tags_purpose":["뼈-관절"],"tags_function":["관절 건강"],"tags_bodypart":["뼈·관절"]},
    {"id":"red-algae-calcium","name":"해조칼슘","name_en":"Red Algae Calcium","aliases":["리토탐니온","Aquamin"],"category":"mineral","tags_purpose":["뼈-관절"],"tags_function":["뼈 건강"],"tags_bodypart":["뼈·관절"]},
    {"id":"fermented-red-clover","name":"발효레드클로버추출물","name_en":"Fermented Red Clover","aliases":["발효 이소플라본"],"category":"extract","tags_purpose":["갱년기"],"tags_function":["여성 건강"],"tags_bodypart":["전신"]},
    {"id":"gamma-aminobutyric-acid-rice","name":"현미발효GABA","name_en":"Fermented Rice GABA","aliases":["발효가바"],"category":"amino_acid","tags_purpose":["수면","스트레스","혈압-혈당"],"tags_function":["수면 건강","혈압 조절"],"tags_bodypart":["뇌"]},
    {"id":"yeast-beta-glucan","name":"효모베타글루칸","name_en":"Yeast Beta-Glucan","aliases":["효모 베타-1,3-글루칸"],"category":"other_functional","tags_purpose":["면역"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"oat-beta-glucan","name":"귀리베타글루칸","name_en":"Oat Beta-Glucan","aliases":["귀리 식이섬유"],"category":"fiber","tags_purpose":["콜레스테롤"],"tags_function":["혈중 지질 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"barley-beta-glucan","name":"보리베타글루칸","name_en":"Barley Beta-Glucan","aliases":["보리 식이섬유"],"category":"fiber","tags_purpose":["콜레스테롤"],"tags_function":["혈중 지질 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"apple-polyphenol","name":"사과추출물","name_en":"Apple Polyphenol","aliases":["사과 폴리페놀","프로시아니딘"],"category":"extract","tags_purpose":["다이어트"],"tags_function":["체지방 감소"],"tags_bodypart":["전신"]},
    {"id":"pomegranate-concentrate","name":"석류농축액","name_en":"Pomegranate Concentrate","aliases":["석류 농축"],"category":"extract","tags_purpose":["갱년기"],"tags_function":["여성 건강"],"tags_bodypart":["전신"]},
    {"id":"blueberry-extract","name":"블루베리추출물","name_en":"Blueberry Extract","aliases":["블루베리"],"category":"extract","tags_purpose":["눈건강","노화방지"],"tags_function":["항산화","눈 건강"],"tags_bodypart":["눈"]},
    {"id":"citrus-bioflavonoid","name":"감귤바이오플라보노이드","name_en":"Citrus Bioflavonoid","aliases":["감귤 플라보노이드"],"category":"other_functional","tags_purpose":["혈압-혈당"],"tags_function":["혈행 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"phytosterol-ester","name":"식물스테롤에스테르","name_en":"Phytosterol Ester","aliases":["피토스테롤 에스테르"],"category":"other_functional","tags_purpose":["콜레스테롤"],"tags_function":["혈중 지질 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"red-mold-rice-monacolin","name":"홍국추출물(모나콜린)","name_en":"Red Mold Rice Monacolin","aliases":["모나콜린K"],"category":"other_functional","tags_purpose":["콜레스테롤"],"tags_function":["혈중 지질 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"gamma-linolenic-borage","name":"보라지종자유GLA","name_en":"Borage Seed GLA","aliases":["보라지유"],"category":"fatty_acid","tags_purpose":["피부"],"tags_function":["피부 건강"],"tags_bodypart":["피부"]},
    {"id":"saffron-extract","name":"사프란추출물","name_en":"Saffron Extract","aliases":["사프란","크로신"],"category":"extract","tags_purpose":["수면","스트레스"],"tags_function":["신경 안정"],"tags_bodypart":["뇌"]},
    {"id":"rice-bran-extract","name":"미강추출물","name_en":"Rice Bran Extract","aliases":["미강","쌀겨"],"category":"extract","tags_purpose":["콜레스테롤"],"tags_function":["혈중 지질 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"aged-garlic","name":"숙성마늘추출물","name_en":"Aged Garlic Extract","aliases":["숙성마늘","SAC"],"category":"extract","tags_purpose":["면역","혈압-혈당"],"tags_function":["면역 기능","혈행 개선"],"tags_bodypart":["심장·혈관"]},
    {"id":"laccase","name":"락카아제","name_en":"Laccase","aliases":["Laccase"],"category":"enzyme","tags_purpose":["노화방지"],"tags_function":["항산화"],"tags_bodypart":["전신"]},
    {"id":"superoxide-dismutase","name":"SOD","name_en":"Superoxide Dismutase","aliases":["SOD","초과산화물불균등화효소"],"category":"enzyme","tags_purpose":["노화방지"],"tags_function":["항산화"],"tags_bodypart":["전신"]},
    {"id":"coenzyme-a","name":"코엔자임A","name_en":"Coenzyme A","aliases":["CoA"],"category":"other_functional","tags_purpose":["만성피로"],"tags_function":["에너지 생성"],"tags_bodypart":["전신"]},
    {"id":"betaine","name":"베타인","name_en":"Betaine","aliases":["트리메틸글리신","TMG"],"category":"amino_acid","tags_purpose":["간건강","운동"],"tags_function":["간 건강"],"tags_bodypart":["간"]},
    {"id":"citrulline-malate","name":"시트룰린말레이트","name_en":"Citrulline Malate","aliases":["Citrulline Malate"],"category":"amino_acid","tags_purpose":["운동"],"tags_function":["혈행 개선"],"tags_bodypart":["근육"]},
    {"id":"ornithine","name":"오르니틴","name_en":"L-Ornithine","aliases":["L-오르니틴"],"category":"amino_acid","tags_purpose":["수면","간건강"],"tags_function":["수면 건강","간 건강"],"tags_bodypart":["간","뇌"]},
    {"id":"carnosine","name":"카르노신","name_en":"Carnosine","aliases":["L-카르노신"],"category":"amino_acid","tags_purpose":["운동","노화방지"],"tags_function":["근력 향상","항산화"],"tags_bodypart":["근육"]},
    {"id":"d-ribose","name":"D-리보스","name_en":"D-Ribose","aliases":["리보스"],"category":"other_functional","tags_purpose":["만성피로","운동"],"tags_function":["에너지 생성"],"tags_bodypart":["전신"]},
    {"id":"ip6","name":"IP6","name_en":"Inositol Hexaphosphate","aliases":["이노시톨헥사포스페이트","피틴산"],"category":"other_functional","tags_purpose":["면역"],"tags_function":["면역 기능"],"tags_bodypart":["전신"]},
    {"id":"dmae","name":"DMAE","name_en":"Dimethylaminoethanol","aliases":["디메틸아미노에탄올"],"category":"other_functional","tags_purpose":["학습-수험생"],"tags_function":["인지 기능"],"tags_bodypart":["뇌"]},
    {"id":"r-alpha-lipoic-acid","name":"R-알파리포산","name_en":"R-Alpha Lipoic Acid","aliases":["R-ALA"],"category":"other_functional","tags_purpose":["노화방지","혈압-혈당"],"tags_function":["항산화"],"tags_bodypart":["전신"]},
    {"id":"pyruvate","name":"피루빈산","name_en":"Pyruvate","aliases":["피루베이트"],"category":"other_functional","tags_purpose":["다이어트","운동"],"tags_function":["체지방 감소"],"tags_bodypart":["전신"]},
    {"id":"glucuronolactone","name":"글루쿠로노락톤","name_en":"Glucuronolactone","aliases":["Glucuronolactone"],"category":"other_functional","tags_purpose":["만성피로"],"tags_function":["에너지 생성"],"tags_bodypart":["전신"]},
]

# ============================================================
# MORE PLANT EXTRACTS commonly found in Korean supplements
# ============================================================
MORE_EXTRACTS = [
    {"id":"siberian-ginseng","name":"가시오갈피","name_en":"Siberian Ginseng","aliases":["엘류테로","Eleutherococcus"],"tags_purpose":["만성피로","스트레스"]},
    {"id":"bacillus-coagulans","name":"바실러스 코아귤란스","name_en":"Bacillus coagulans","aliases":["스포어 프로바이오틱"],"category":"probiotic","tags_purpose":["장건강"],"tags_function":["장 건강"],"tags_bodypart":["장"]},
    {"id":"kelp","name":"다시마추출물","name_en":"Kelp","aliases":["다시마","해조류"],"tags_purpose":["면역"]},
    {"id":"wakame","name":"미역추출물","name_en":"Wakame","aliases":["미역"],"tags_purpose":["면역","다이어트"]},
    {"id":"hijiki","name":"톳추출물","name_en":"Hijiki","aliases":["톳"],"tags_purpose":["면역"]},
    {"id":"mozuku","name":"모즈쿠추출물","name_en":"Mozuku","aliases":["모즈쿠","후코이단 원료"],"tags_purpose":["면역"]},
    {"id":"skullcap","name":"황금추출물","name_en":"Scutellaria Extract","aliases":["황금","바이칼린"],"tags_purpose":["스트레스"]},
    {"id":"magnolia-bark","name":"후박추출물","name_en":"Magnolia Bark","aliases":["후박","호노키올"],"tags_purpose":["스트레스","수면"]},
    {"id":"peony-root","name":"작약추출물","name_en":"Peony Root","aliases":["작약","Paeonia"],"tags_purpose":["갱년기"]},
    {"id":"coptis","name":"황련추출물","name_en":"Coptis Extract","aliases":["황련","코프티스"],"tags_purpose":["장건강","혈압-혈당"]},
    {"id":"phellodendron","name":"황백추출물","name_en":"Phellodendron Extract","aliases":["황백","Phellodendron"],"tags_purpose":["장건강"]},
    {"id":"gentian","name":"용담추출물","name_en":"Gentian Extract","aliases":["용담","겐치아나"],"tags_purpose":["장건강"]},
    {"id":"licorice-glycyrrhizin","name":"글리시리진","name_en":"Glycyrrhizin","aliases":["감초 추출 성분"],"tags_purpose":["장건강","스트레스"]},
    {"id":"ginger-gingerol","name":"진저롤","name_en":"Gingerol","aliases":["생강 활성성분"],"tags_purpose":["장건강"]},
    {"id":"turmeric-curcuminoid","name":"커큐미노이드","name_en":"Curcuminoid","aliases":["강황 색소 성분"],"tags_purpose":["노화방지","간건강"]},
    {"id":"wasabi-extract","name":"고추냉이추출물","name_en":"Wasabi Extract","aliases":["와사비"],"tags_purpose":["장건강"]},
    {"id":"perilla-leaf","name":"들깻잎추출물","name_en":"Perilla Leaf","aliases":["들깻잎","로즈마린산"],"tags_purpose":["면역"]},
    {"id":"pine-bark","name":"소나무껍질추출물","name_en":"Pine Bark Extract","aliases":["OPC"],"tags_purpose":["노화방지","혈압-혈당"]},
    {"id":"grape-skin","name":"포도껍질추출물","name_en":"Grape Skin Extract","aliases":["레스베라트롤 원료"],"tags_purpose":["노화방지"]},
    {"id":"schizandra-fruit","name":"오미자열매","name_en":"Schizandra Fruit","aliases":["오미자 열매"],"tags_purpose":["간건강"]},
    {"id":"yam-extract","name":"산약추출물","name_en":"Chinese Yam","aliases":["산약","마"],"tags_purpose":["갱년기","장건강"]},
    {"id":"barley-grass","name":"보리새싹추출물","name_en":"Barley Grass","aliases":["새싹보리"],"tags_purpose":["노화방지"]},
    {"id":"wheat-grass","name":"밀싹추출물","name_en":"Wheat Grass","aliases":["밀싹"],"tags_purpose":["노화방지"]},
    {"id":"broccoli-sprout","name":"브로콜리새싹","name_en":"Broccoli Sprout","aliases":["브로콜리 스프라우트"],"tags_purpose":["노화방지","간건강"]},
    {"id":"kale-extract","name":"케일추출물","name_en":"Kale Extract","aliases":["케일"],"tags_purpose":["노화방지"]},
    {"id":"black-soybean","name":"서리태추출물","name_en":"Black Soybean Extract","aliases":["서리태","검정콩"],"tags_purpose":["탈모","노화방지"]},
    {"id":"adzuki-bean","name":"팥추출물","name_en":"Adzuki Bean Extract","aliases":["팥"],"tags_purpose":["다이어트"]},
    {"id":"mung-bean","name":"녹두추출물","name_en":"Mung Bean Extract","aliases":["녹두"],"tags_purpose":["피부"]},
    {"id":"chestnut-inner-shell","name":"밤속껍질추출물","name_en":"Chestnut Inner Shell","aliases":["밤속껍질"],"tags_purpose":["탈모"]},
    {"id":"black-sesame","name":"흑임자추출물","name_en":"Black Sesame Extract","aliases":["흑임자","검정깨"],"tags_purpose":["탈모","노화방지"]},
    {"id":"walnut-extract","name":"호두추출물","name_en":"Walnut Extract","aliases":["호두"],"tags_purpose":["학습-수험생"]},
    {"id":"almond-extract","name":"아몬드추출물","name_en":"Almond Extract","aliases":["아몬드"],"tags_purpose":["피부"]},
    {"id":"brazil-nut","name":"브라질너트","name_en":"Brazil Nut","aliases":["브라질넛","셀레늄 원료"],"tags_purpose":["노화방지"]},
    {"id":"hemp-seed","name":"햄프시드","name_en":"Hemp Seed","aliases":["대마종자"],"tags_purpose":["면역"]},
    {"id":"chia-seed","name":"치아씨드","name_en":"Chia Seed","aliases":["치아시드"],"tags_purpose":["장건강","다이어트"]},
    {"id":"coconut-oil","name":"코코넛오일","name_en":"Coconut Oil","aliases":["코코넛 오일","라우르산"],"category":"fatty_acid","tags_purpose":["다이어트"],"tags_function":["에너지 생성"]},
    {"id":"avocado-oil","name":"아보카도오일","name_en":"Avocado Oil","aliases":["아보카도 오일"],"category":"fatty_acid","tags_purpose":["피부","콜레스테롤"],"tags_function":["피부 건강"]},
    {"id":"black-cumin-seed","name":"블랙커민씨드오일","name_en":"Black Cumin Seed Oil","aliases":["흑종초","니겔라"],"tags_purpose":["면역"]},
    {"id":"oregano-oil","name":"오레가노오일","name_en":"Oregano Oil","aliases":["카르바크롤"],"tags_purpose":["면역"]},
    {"id":"tea-tree-oil","name":"티트리오일","name_en":"Tea Tree Oil","aliases":["Tea Tree"],"tags_purpose":["면역"]},
    {"id":"rosemary-extract-func","name":"로즈마리추출물(기능)","name_en":"Rosemary Extract (functional)","aliases":["카르노신산","로즈마린산"],"tags_purpose":["학습-수험생","노화방지"]},
    {"id":"cacao-extract","name":"카카오추출물","name_en":"Cacao Extract","aliases":["카카오 폴리페놀","테오브로민"],"tags_purpose":["혈압-혈당","노화방지"]},
    {"id":"coffee-fruit-extract","name":"커피열매추출물","name_en":"Coffee Fruit Extract","aliases":["커피체리"],"tags_purpose":["학습-수험생"]},
    {"id":"matcha-powder","name":"말차분말","name_en":"Matcha Powder","aliases":["말차","말차 파우더"],"tags_purpose":["노화방지","학습-수험생"]},
    {"id":"rooibos-extract","name":"루이보스추출물","name_en":"Rooibos Extract","aliases":["루이보스"],"tags_purpose":["노화방지"]},
    {"id":"hibiscus-extract","name":"히비스커스추출물","name_en":"Hibiscus Extract","aliases":["히비스커스"],"tags_purpose":["혈압-혈당"]},
    {"id":"lemongrass-extract","name":"레몬그라스추출물","name_en":"Lemongrass Extract","aliases":["레몬그라스"],"tags_purpose":["장건강"]},
    {"id":"olive-extract","name":"올리브추출물","name_en":"Olive Extract","aliases":["올리브","하이드록시타이로솔"],"tags_purpose":["노화방지"]},
    {"id":"pomegranate-seed-oil","name":"석류씨오일","name_en":"Pomegranate Seed Oil","aliases":["퓨닉산"],"category":"fatty_acid","tags_purpose":["피부"],"tags_function":["피부 건강"]},
    {"id":"argan-oil","name":"아르간오일","name_en":"Argan Oil","aliases":["아르간 오일"],"category":"fatty_acid","tags_purpose":["피부"],"tags_function":["피부 건강"]},
    {"id":"sacha-inchi","name":"사차인치오일","name_en":"Sacha Inchi Oil","aliases":["사차인치"],"category":"fatty_acid","tags_purpose":["혈압-혈당"],"tags_function":["혈중 지질 개선"]},
    {"id":"camellia-oil","name":"동백오일","name_en":"Camellia Oil","aliases":["동백유"],"category":"fatty_acid","tags_purpose":["피부"],"tags_function":["피부 건강"]},
    {"id":"elderberry-syrup","name":"엘더베리시럽","name_en":"Elderberry Syrup","aliases":["엘더베리 시럽"],"tags_purpose":["면역"]},
    {"id":"tart-cherry","name":"타트체리추출물","name_en":"Tart Cherry Extract","aliases":["몽모랑시체리"],"tags_purpose":["수면","운동"]},
    {"id":"acerola-vitamin-c","name":"아세로라비타민C","name_en":"Acerola Vitamin C","aliases":["자연유래 비타민C"],"tags_purpose":["면역","피부"]},
    {"id":"cactus-extract","name":"백년초추출물","name_en":"Prickly Pear Cactus","aliases":["백년초","선인장"],"tags_purpose":["면역"]},
    {"id":"mistletoe","name":"겨우살이추출물","name_en":"Mistletoe Extract","aliases":["겨우살이"],"tags_purpose":["면역"]},
    {"id":"eucommia-bark","name":"두충나무껍질","name_en":"Eucommia Bark","aliases":["두충피"],"tags_purpose":["뼈-관절","혈압-혈당"]},
    {"id":"cornelian-cherry","name":"산수유추출물","name_en":"Cornelian Cherry","aliases":["산수유"],"tags_purpose":["성기능","만성피로"]},
    {"id":"cnidium-seed","name":"사상자추출물","name_en":"Cnidium Seed","aliases":["사상자"],"tags_purpose":["성기능"]},
    {"id":"horny-goat-weed","name":"음양곽","name_en":"Horny Goat Weed","aliases":["음양곽","이카린","Epimedium"],"tags_purpose":["성기능","뼈-관절"]},
    {"id":"tongkat-ali","name":"통캇알리","name_en":"Tongkat Ali","aliases":["Eurycoma longifolia"],"tags_purpose":["성기능","운동"]},
    {"id":"muira-puama","name":"무이라푸아마","name_en":"Muira Puama","aliases":["Muira Puama"],"tags_purpose":["성기능"]},
    {"id":"damiana","name":"다미아나","name_en":"Damiana","aliases":["Turnera diffusa","다미아나"],"tags_purpose":["성기능"]},
    {"id":"shilajit","name":"실라짓","name_en":"Shilajit","aliases":["Shilajit","풀빅산"],"tags_purpose":["만성피로","성기능"]},
    {"id":"pine-pollen","name":"송화분","name_en":"Pine Pollen","aliases":["소나무 꽃가루"],"tags_purpose":["성기능","만성피로"]},
    {"id":"eurycoma","name":"유리코마","name_en":"Eurycoma","aliases":["롱잭"],"tags_purpose":["성기능"]},
    {"id":"stinging-nettle-root","name":"쐐기풀뿌리","name_en":"Stinging Nettle Root","aliases":["네틀루트"],"tags_purpose":["성기능"]},
    {"id":"pygeum","name":"아프리카자두나무","name_en":"Pygeum","aliases":["피지움","Pygeum africanum"],"tags_purpose":["성기능"]},
    {"id":"palm-extract-beta-sitosterol","name":"베타시토스테롤","name_en":"Beta-Sitosterol","aliases":["베타-시토스테롤","식물 스테롤"],"tags_purpose":["성기능","콜레스테롤"]},
    {"id":"andrographis","name":"안드로그라피스","name_en":"Andrographis","aliases":["안드로그라피스","Andrographis paniculata"],"tags_purpose":["면역"]},
    {"id":"cats-whisker","name":"고양이수염차","name_en":"Cat's Whisker","aliases":["자바티"],"tags_purpose":["혈압-혈당"]},
    {"id":"gymnema-sylvestre","name":"짐네마실베스트레","name_en":"Gymnema Sylvestre","aliases":["짐네마","당을 파괴하는 풀"],"tags_purpose":["혈압-혈당","다이어트"]},
    {"id":"nopal-cactus","name":"노팔선인장","name_en":"Nopal Cactus","aliases":["노팔","Opuntia"],"tags_purpose":["혈압-혈당","다이어트"]},
    {"id":"okra-extract","name":"오크라추출물","name_en":"Okra Extract","aliases":["오크라"],"tags_purpose":["장건강","혈압-혈당"]},
    {"id":"papaya-enzyme","name":"파파야효소","name_en":"Papaya Enzyme","aliases":["청파파야","파파인"],"tags_purpose":["장건강"]},
    {"id":"pineapple-enzyme","name":"파인애플효소","name_en":"Pineapple Enzyme","aliases":["브로멜라인"],"tags_purpose":["장건강"]},
    {"id":"aloe-gel","name":"알로에겔","name_en":"Aloe Gel","aliases":["알로에겔","Aloe vera gel"],"tags_purpose":["피부","장건강"]},
    {"id":"centella-extract","name":"센텔라추출물","name_en":"Centella Extract","aliases":["병풀추출물","CICA"],"tags_purpose":["피부"]},
    {"id":"calendula","name":"카렌듈라추출물","name_en":"Calendula Extract","aliases":["금잔화","Calendula"],"tags_purpose":["피부"]},
    {"id":"licorice-root-extract","name":"감초뿌리추출물","name_en":"Licorice Root Extract","aliases":["글라브리딘"],"tags_purpose":["피부","장건강"]},
    {"id":"houttuynia","name":"어성초추출물","name_en":"Houttuynia Extract","aliases":["어성초","Houttuynia cordata"],"tags_purpose":["피부","면역"]},
    {"id":"sophora-flavescens","name":"고삼추출물","name_en":"Sophora flavescens","aliases":["고삼","쿠라리논"],"tags_purpose":["피부"]},
    {"id":"portulaca","name":"쇠비름추출물","name_en":"Portulaca Extract","aliases":["쇠비름"],"tags_purpose":["피부"]},
    {"id":"gallic-acid","name":"갈릭산","name_en":"Gallic Acid","aliases":["Gallic Acid"],"category":"other_functional","tags_purpose":["노화방지"]},
    {"id":"ellagic-acid","name":"엘라그산","name_en":"Ellagic Acid","aliases":["Ellagic Acid"],"category":"other_functional","tags_purpose":["노화방지"]},
    {"id":"catechin","name":"카테킨","name_en":"Catechin","aliases":["Catechin"],"category":"other_functional","tags_purpose":["다이어트","노화방지"]},
    {"id":"anthocyanin","name":"안토시아닌","name_en":"Anthocyanin","aliases":["Anthocyanin"],"category":"other_functional","tags_purpose":["눈건강","노화방지"]},
    {"id":"proanthocyanidin","name":"프로안토시아니딘","name_en":"Proanthocyanidin","aliases":["OPC","Proanthocyanidin"],"category":"other_functional","tags_purpose":["노화방지","혈압-혈당"]},
    {"id":"curcumin-phytosome","name":"커큐민파이토솜","name_en":"Curcumin Phytosome","aliases":["메리바"],"tags_purpose":["뼈-관절","노화방지"]},
    {"id":"boswellia-serrata","name":"보스웰리아세라타","name_en":"Boswellia Serrata","aliases":["보스웰릭산","AKBA"],"tags_purpose":["뼈-관절"]},
    {"id":"uc-ii-collagen","name":"UC-II","name_en":"UC-II Collagen","aliases":["비변성 2형 콜라겐"],"tags_purpose":["뼈-관절"]},
    {"id":"calcium-hydroxyapatite","name":"미세결정형히드록시아파타이트","name_en":"MCHC","aliases":["MCH 칼슘"],"category":"mineral","tags_purpose":["뼈-관절"],"tags_function":["뼈 건강"]},
    {"id":"bamboo-salt","name":"죽염","name_en":"Bamboo Salt","aliases":["죽염"],"tags_purpose":["구강","면역"]},
    {"id":"xylitol-oral","name":"자일리톨(구강)","name_en":"Xylitol (oral health)","aliases":["자일리톨"],"tags_purpose":["구강"]},
    {"id":"lactoperoxidase","name":"락토퍼옥시다아제","name_en":"Lactoperoxidase","aliases":["LP"],"category":"enzyme","tags_purpose":["구강"],"tags_function":["구강 건강"]},
    {"id":"gum-mastic","name":"매스틱검","name_en":"Mastic Gum","aliases":["매스틱","Pistacia lentiscus"],"tags_purpose":["장건강","구강"]},
    {"id":"licorice-dgl","name":"DGL감초","name_en":"DGL Licorice","aliases":["디글리시라이진감초"],"tags_purpose":["장건강"]},
    {"id":"slippery-elm","name":"슬리퍼리엘름","name_en":"Slippery Elm","aliases":["Ulmus rubra"],"tags_purpose":["장건강"]},
    {"id":"marshmallow-root","name":"마시멜로우루트","name_en":"Marshmallow Root","aliases":["Althaea officinalis"],"tags_purpose":["장건강"]},
    {"id":"zinc-carnosine","name":"아연카르노신","name_en":"Zinc Carnosine","aliases":["Zinc-L-Carnosine","PepZin GI"],"category":"mineral","tags_purpose":["장건강"],"tags_function":["장 건강"]},
    {"id":"tributyrin","name":"트리뷰티린","name_en":"Tributyrin","aliases":["부티르산","뷰티레이트"],"tags_purpose":["장건강"]},
]

def main():
    path = os.path.join(os.path.dirname(__file__),"..","data","ingredients.json")
    path = os.path.abspath(path)
    with open(path,"r",encoding="utf-8") as f:
        existing = json.load(f)
    existing_ids = {i["id"] for i in existing}
    added = {"t1":0,"t2":0}

    all_new = []
    for item in GOSI_MISSING:
        item.setdefault("tier",1)
        all_new.append(item)
    for item in GAEBYIN_MISSING:
        item.setdefault("tier",2)
        item.setdefault("source_type","개별인정형")
        all_new.append(item)
    for item in MORE_EXTRACTS:
        item.setdefault("tier",2)
        item.setdefault("source_type","부원료")
        item.setdefault("category","extract")
        all_new.append(item)

    for item in all_new:
        if item["id"] in existing_ids:
            continue
        t = item["tier"]
        for k in ["tags_age","tags_gender","aliases","related_ingredients"]:
            item.setdefault(k,["전연령"] if k=="tags_age" else ["공통"] if k=="tags_gender" else [])
        for k in ["tags_purpose","tags_function","tags_bodypart"]:
            item.setdefault(k,[])
        for k in ["upper_limit","daily_recommended","mfds_functionality","subcategory","nickname","name_en"]:
            item.setdefault(k,"")
        existing.append(item)
        existing_ids.add(item["id"])
        if t==1: added["t1"]+=1
        else: added["t2"]+=1

    with open(path,"w",encoding="utf-8") as f:
        json.dump(existing,f,ensure_ascii=False,indent=2)

    counts = {}
    for i in existing: counts[i["tier"]]=counts.get(i["tier"],0)+1
    cats = {}
    for i in existing: cats[i["category"]]=cats.get(i["category"],0)+1
    print(f"Added T1:{added['t1']}, T2:{added['t2']}")
    for t in sorted(counts): print(f"  Tier {t}: {counts[t]}")
    print(f"  GRAND TOTAL: {len(existing)}")
    print(f"\nBy category:")
    for c,n in sorted(cats.items(),key=lambda x:-x[1]): print(f"  {c}: {n}")

if __name__=="__main__":
    main()
