#!/usr/bin/env python3
"""
IVC MOCK TEST — 200 Questions
Pattern: UPSC Prelims + TNPSC Group 1 Prelims
Run  : python3 mock_test_ivc.py
"""

import time
import os
import sys
from datetime import timedelta

# ── ANSI Colours ──────────────────────────────────────────────────────────────
R    = "\033[91m"
G    = "\033[92m"
Y    = "\033[93m"
B    = "\033[94m"
C    = "\033[96m"
W    = "\033[97m"
BOLD = "\033[1m"
DIM  = "\033[2m"
RESET= "\033[0m"

def clr(): os.system("cls" if os.name == "nt" else "clear")

# ── Question Bank ─────────────────────────────────────────────────────────────
# Format: [question_text, A, B, C, D, correct_letter, topic, difficulty(1-3)]
# difficulty  1 = TNPSC direct   2 = medium   3 = UPSC-style / tricky

Q = [

# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 1 — BASICS  (Q1–Q15)
# ══════════════════════════════════════════════════════════════════════════════

["The Indus Valley Civilisation belongs to which historical age?",
 "Iron Age","Bronze Age","Copper Age","Neolithic Age","b","Basics",1],

["The Mature Harappan (Integration) phase is dated approximately to:",
 "3300–2600 BCE","2600–1900 BCE","1900–1300 BCE","3000–2300 BCE","b","Basics",1],

["The Indus Valley Civilisation covered an area of approximately:",
 "1 million sq km","1.2 million sq km","1.5 million sq km","2 million sq km","c","Basics",1],

["Who coined the term 'Indus Valley Civilisation'?",
 "Daya Ram Sahni","R.D. Banerji","Sir John Marshall","Mortimer Wheeler","c","Basics",1],

["The IVC is also known as:",
 "Iron Age Civilisation","Harappan Civilisation","Aryan Civilisation","Dravidian Civilisation","b","Basics",1],

["IVC is considered the first what in the Indian subcontinent?",
 "Agricultural settlement","Urban civilisation","Iron-using culture","Temple-building culture","b","Basics",1],

["Which metal was NOT known to the Harappan people?",
 "Copper","Bronze","Iron","Gold","c","Basics",1],

["The IVC was contemporary with which pair of civilisations?",
 "Mesopotamia and Egypt","Roman and Greek","Persian and Babylonian","Chinese and Roman","a","Basics",2],

["In Mesopotamian cuneiform texts, the Indus region is referred to as:",
 "Dilmun","Magan","Meluhha","Akkad","c","Basics",2],

["The IVC is considered the largest Bronze Age civilisation in terms of:",
 "Population","Area","Number of cities","Duration","b","Basics",2],

["The Harappan script is primarily written in which direction?",
 "Left to right","Right to left","Top to bottom","Bottom to top","b","Basics",2],

["The maximum number of Indus Valley sites are concentrated along which river system?",
 "Indus","Ravi","Ghaggar-Hakra","Sabarmati","c","Basics",2],

["The North–South span of the IVC was approximately:",
 "800 km","1,600 km","2,400 km","3,200 km","b","Basics",2],

["Approximately how many IVC sites have been discovered so far?",
 "About 500","About 1,500+","About 3,000","About 800","b","Basics",1],

["The estimated population of IVC at its peak was approximately:",
 "1 million","3 million","5 million","10 million","c","Basics",2],

# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 2 — EXCAVATORS  (Q16–Q30)
# ══════════════════════════════════════════════════════════════════════════════

["Who discovered Harappa in 1921?",
 "R.D. Banerji","Daya Ram Sahni","Sir John Marshall","Mortimer Wheeler","b","Excavators",1],

["Who discovered Mohenjo-Daro in 1922?",
 "Daya Ram Sahni","Sir John Marshall","R.D. Banerji","E.J.H. Mackay","c","Excavators",1],

["Who excavated Lothal (1955–62)?",
 "B.B. Lal","R.S. Bisht","S.R. Rao","J.P. Joshi","c","Excavators",1],

["Who excavated Dholavira (1989–2005)?",
 "S.R. Rao","R.S. Bisht","B.B. Lal","Vasant Shinde","b","Excavators",1],

["Kalibangan was excavated by:",
 "S.R. Rao and J.P. Joshi","B.B. Lal and B.K. Thapar","R.S. Bisht and Daya Ram Sahni","Mortimer Wheeler and E.J.H. Mackay","b","Excavators",1],

["Who excavated Surkotada and identified the (disputed) horse bones?",
 "S.R. Rao","B.B. Lal","J.P. Joshi","R.S. Bisht","c","Excavators",2],

["Chanhu-daro was excavated by:",
 "R.D. Banerji","Mortimer Wheeler","E.J.H. Mackay","Aurel Stein","c","Excavators",2],

["Who led the 2019 Rakhigarhi DNA study?",
 "R.S. Bisht","Vasant Shinde","Asko Parpola","B.B. Lal","b","Excavators",2],

["Asko Parpola, who proposed the Proto-Dravidian theory for IVC script, belongs to:",
 "Sweden","Finland","Denmark","Norway","b","Excavators",2],

["Aurel Stein surveyed which IVC site?",
 "Daimabad","Banawali","Sutkagen-dor","Alamgirpur","c","Excavators",2],

["Who introduced systematic stratigraphic excavation at Harappa in the 1940s?",
 "Sir John Marshall","S.R. Rao","Mortimer Wheeler","R.D. Banerji","c","Excavators",2],

["Banawali was excavated by:",
 "B.B. Lal","J.P. Joshi","R.S. Bisht","Daya Ram Sahni","c","Excavators",2],

["Alamgirpur (easternmost IVC site) was excavated by:",
 "B.B. Lal","J.P. Joshi","Y.D. Sharma","R.S. Bisht","c","Excavators",3],

["Sir John Marshall's title at the Archaeological Survey of India was:",
 "Director","Secretary","Director-General","Commissioner","c","Excavators",2],

["The (discredited) Aryan Invasion Theory to explain IVC decline was proposed by:",
 "Sir John Marshall","Mortimer Wheeler","R.D. Banerji","E.J.H. Mackay","b","Excavators",2],

# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 3 — MAJOR SITES  (Q31–Q70)
# ══════════════════════════════════════════════════════════════════════════════

["The Great Bath is found at:",
 "Harappa","Mohenjo-Daro","Lothal","Dholavira","b","Sites",1],

["The Dancing Girl figurine was found at:",
 "Harappa","Lothal","Mohenjo-Daro","Kalibangan","c","Sites",1],

["The Priest-King sculpture was found at:",
 "Harappa","Kalibangan","Lothal","Mohenjo-Daro","d","Sites",1],

["The world's earliest known dockyard was found at:",
 "Mohenjo-Daro","Harappa","Lothal","Dholavira","c","Sites",1],

["Evidence of the world's first ploughed field was discovered at:",
 "Lothal","Mohenjo-Daro","Dholavira","Kalibangan","d","Sites",1],

["Which IVC site is renowned for its massive water conservation and reservoir system?",
 "Mohenjo-Daro","Harappa","Dholavira","Lothal","c","Sites",1],

["The only major IVC city WITHOUT a citadel is:",
 "Surkotada","Chanhu-daro","Banawali","Alamgirpur","b","Sites",1],

["Horse bones (disputed) were found at which IVC site?",
 "Kalibangan","Dholavira","Surkotada","Lothal","c","Sites",2],

["The largest IVC site located in India is:",
 "Lothal","Dholavira","Kalibangan","Rakhigarhi","d","Sites",1],

["The largest IVC site overall (including Pakistan) is:",
 "Mohenjo-Daro","Harappa","Rakhigarhi","Dholavira","a","Sites",1],

["The westernmost IVC site is:",
 "Dholavira","Sutkagen-dor","Lothal","Shortughai","b","Sites",2],

["The easternmost IVC site is:",
 "Daimabad","Alamgirpur","Kalibangan","Banawali","b","Sites",2],

["The northernmost IVC site is:",
 "Harappa","Sutkagen-dor","Shortughai","Mehrgarh","c","Sites",2],

["The southernmost IVC site is:",
 "Lothal","Rangpur","Dholavira","Daimabad","d","Sites",2],

["Shortughai (Afghanistan) is known for its trade in which commodity?",
 "Carnelian beads","Gold","Lapis lazuli","Cotton","c","Sites",2],

["Which IVC site has a THREE-PART city division (Citadel + Middle Town + Lower Town)?",
 "Mohenjo-Daro","Harappa","Dholavira","Lothal","c","Sites",2],

["Fire altars arranged in rows were found on the CITADEL of which site?",
 "Mohenjo-Daro","Kalibangan","Lothal","Dholavira","b","Sites",2],

["Lothal's fire altars are unique because they were found in the:",
 "Citadel","Cemetery","Lower town","Dockyard area","c","Sites",2],

["The only example of double burial (man + woman together) in IVC was found at:",
 "Harappa","Mohenjo-Daro","Kalibangan","Lothal","d","Sites",2],

["The name 'Kalibangan' means:",
 "Red city","Black bangles","Golden wheat fields","Blue river bank","b","Sites",1],

["Which IVC site yielded evidence of an earthquake in the pre-Harappan layer?",
 "Mohenjo-Daro","Dholavira","Kalibangan","Harappa","c","Sites",2],

["Camel bones have been found ONLY at which IVC site?",
 "Lothal","Surkotada","Kalibangan","Dholavira","c","Sites",3],

["The granary at Harappa was located:",
 "Inside the citadel","Outside the citadel near the river","In the lower town","Below ground level","b","Sites",2],

["The southernmost IVC site Daimabad is located in which Indian state?",
 "Kerala","Karnataka","Maharashtra","Andhra Pradesh","c","Sites",1],

["Alamgirpur is located on which river?",
 "Yamuna","Ganga","Hindon","Gomti","c","Sites",3],

["Major shell-object manufacturing was done at:",
 "Lothal and Dholavira","Nageshwar and Balakot","Chanhu-daro and Harappa","Surkotada and Banawali","b","Sites",2],

["Which pre-Harappan site shows the earliest evidence of farming and cattle domestication in South Asia?",
 "Kot Diji","Amri","Mehrgarh","Harappa","c","Sites",2],

["Dholavira was inscribed as a UNESCO World Heritage Site in:",
 "2017","2019","2021","2023","c","Sites",1],

["The famous bronze chariot, rhinoceros, elephant and buffalo were found at:",
 "Harappa","Mohenjo-Daro","Lothal","Daimabad","d","Sites",2],

["Rakhigarhi is located in which Indian state?",
 "Rajasthan","Gujarat","Haryana","Punjab","c","Sites",1],

["Harappa is located on which river?",
 "Indus","Ravi","Beas","Chenab","b","Sites",1],

["Mohenjo-Daro is located in:",
 "Punjab, Pakistan","Sindh, Pakistan","Gujarat, India","Baluchistan, Pakistan","b","Sites",1],

["Surkotada is located on which river?",
 "Sabarmati","Bhogavo","Mahi","Luni","b","Sites",3],

["Kalibangan is located on which river?",
 "Indus","Ghaggar","Sabarmati","Yamuna","b","Sites",2],

["Inkpot and lip-rouge (lipstick) artefacts were found at:",
 "Harappa","Kalibangan","Chanhu-daro","Mohenjo-Daro","c","Sites",2],

["The red sandstone male torso (headless) was found at:",
 "Harappa","Mohenjo-Daro","Lothal","Kalibangan","a","Sites",2],

["Stone rubble fortification (unique construction) was found at:",
 "Surkotada","Harappa","Dholavira","Chanhu-daro","a","Sites",2],

["Workers' quarters and circular threshing floors were found near the granary at:",
 "Mohenjo-Daro","Harappa","Lothal","Dholavira","b","Sites",2],

["Toy plough (terracotta) was found at:",
 "Kalibangan","Lothal","Banawali","Rakhigarhi","c","Sites",2],

["Dholavira has how many large reservoirs covering approximately 36 acres?",
 "8","12","16","20","c","Sites",3],

# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 4 — TOWN PLANNING  (Q71–Q90)
# ══════════════════════════════════════════════════════════════════════════════

["The standard Harappan brick ratio (Height : Width : Length) is:",
 "1:2:3","1:2:4","1:3:6","2:3:4","b","Town Planning",1],

["Harappan main streets were approximately how wide?",
 "3–5 metres","5–7 metres","9–10 metres","12–15 metres","c","Town Planning",1],

["Harappan city roads followed which layout pattern?",
 "Circular","Radial","Grid-iron (chess-board)","Random organic","c","Town Planning",1],

["The drains in Harappan cities were made of:",
 "Unbaked mud bricks","Stone slabs","Burnt bricks","Wood planks","c","Town Planning",1],

["Which CORRECTLY describes Harappan drainage?",
 "Open drains along streets","Covered drains with inspection holes","Tunnels draining to river","Ceramic pipe drains","b","Town Planning",2],

["In a typical Harappan house, the entrance was through:",
 "The main street","A side lane","The rear of the house","A shared courtyard","b","Town Planning",2],

["Windows in Harappan houses:",
 "Faced the main street","Did NOT face the main street","Were large and ornamental","Were only on upper floors","b","Town Planning",2],

["The Great Bath of Mohenjo-Daro was made watertight using:",
 "Lime mortar","Clay plaster","Bitumen (natural tar)","Gypsum only","c","Town Planning",2],

["The approximate dimensions of the Great Bath are:",
 "5×3×1 m","11.8×7×2.4 m","8×5×3 m","15×10×3 m","b","Town Planning",2],

["The Great Bath was located on the:",
 "Lower town","River bank","Citadel (upper town)","Cemetery area","c","Town Planning",1],

["Private wells were found in:",
 "Only public granary buildings","Larger houses","Every single house","No houses at all","b","Town Planning",2],

["Burnt bricks were specifically used for:",
 "House walls","Roads","Drains and bathroom floors","Citadel platforms","c","Town Planning",2],

["Dholavira's town planning is UNIQUE among all IVC sites because of its:",
 "Circular city layout","Three-part city division","Underground housing","Absence of streets","b","Town Planning",2],

["The Harappan drainage system was superior to which other ancient civilisations?",
 "Mesopotamia and Egypt","China and Japan","Greece and Rome","Persia and Babylonia","a","Town Planning",2],

["What type of mortar was used for the FLOOR of the Great Bath?",
 "Mud mortar","Lime mortar","Gypsum mortar","Bitumen mortar","c","Town Planning",3],

["The Harappan citadel was built on a mud-brick platform of approximately:",
 "1–2 metres","3–4 metres","6–12 metres","20–25 metres","c","Town Planning",2],

["Steps leading INTO the water in the Great Bath were on which ends?",
 "East and West","North and South","All four sides","South end only","b","Town Planning",2],

["The cross-lanes (East–West) in a Harappan city were approximately:",
 "Same as main streets","1.5–3 metres wide","5–6 metres wide","7–8 metres wide","b","Town Planning",2],

["Rubbish disposal in Harappan streets was managed using:",
 "Underground pits","Rubbish jars at street corners","River dumping","Wall chutes","b","Town Planning",2],

["A typical Harappan city was divided into how many main parts?",
 "One (single zone)","Two (Citadel + Lower Town)","Three (all cities)","Four (sectors)","b","Town Planning",2],

# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 5 — ECONOMY, TRADE & CRAFTS  (Q91–Q115)
# ══════════════════════════════════════════════════════════════════════════════

["Which crop did the Harappans cultivate for the FIRST time in world history?",
 "Wheat","Barley","Cotton","Rice","c","Economy",1],

["Harappan weights followed which numerical system?",
 "Decimal","Hexadecimal","Binary (1:2:4:8:16...)","Duodecimal","c","Economy",2],

["The smallest Harappan weight unit weighed approximately:",
 "10 grams","13.63 grams","15 grams","8 grams","b","Economy",3],

["Harappan cubical weights were made of:",
 "Iron","Copper","Chert","Steatite","c","Economy",2],

["The MAIN cereal crop of the Harappans was:",
 "Rice","Wheat","Barley","Millet","c","Economy",2],

["Evidence of rice cultivation in IVC was found at:",
 "Kalibangan","Dholavira","Lothal and Rangpur","Harappa","c","Economy",2],

["Greeks called cotton 'Sindon'. This word is derived from:",
 "Saraswati","Sindhu (Indus)","Sanskrit word Suta","Sumerian Sindoor","b","Economy",2],

["Major shell-object manufacturing centres of IVC were:",
 "Harappa and Mohenjo-Daro","Nageshwar and Balakot","Lothal and Dholavira","Chanhu-daro and Banawali","b","Economy",2],

["IVC trade with Mesopotamia is confirmed by:",
 "Harappan seals found at Ur, Kish and Nippur","Vedic texts mentioning Sindhu traders","Greek accounts of Harappan merchants","Persian inscriptions","a","Economy",2],

["The smallest graduation on the ivory scale found at Lothal was approximately:",
 "5 mm","1.77 mm","10 mm","3 mm","b","Economy",3],

["What did IVC mainly IMPORT from Afghanistan and Central Asia?",
 "Gold and silver","Carnelian and pearls","Tin and lapis lazuli","Cotton and copper","c","Economy",2],

["Carnelian beads manufactured at Lothal were exported to:",
 "Egypt","Mesopotamia (Ur/Sumer)","China","Central Asia only","b","Economy",2],

["In Harappan metallurgy, bronze was made by combining copper with:",
 "Zinc","Lead","Tin","Iron","c","Economy",1],

["The technique used to cast the Dancing Girl figurine was:",
 "Open mould casting","Lost-wax (cire perdue) casting","Sheet metal hammering","Sand casting","b","Economy",2],

["Harappan pottery is characterised by:",
 "White-on-black designs","Black-on-Red ware","Blue-on-white designs","Monochrome red ware","b","Economy",2],

["Which commodity was EXPORTED from IVC to Mesopotamia?",
 "Tin","Silver","Carnelian beads and cotton textiles","Horses","c","Economy",2],

["In ancient Mesopotamian texts, 'Dilmun' refers to:",
 "The Indus region","Oman","Bahrain","Afghanistan","c","Economy",3],

["In ancient Mesopotamian texts, 'Magan' refers to:",
 "The Indus region","Oman","Bahrain","Iran","b","Economy",3],

["The most commonly depicted animal on Harappan seals was:",
 "Humped bull (Zebu)","Elephant","Tiger","Unicorn (single-horned animal)","d","Economy",1],

["Harappan seals were most commonly made of:",
 "Copper","Faience","Steatite (soapstone)","Gold","c","Economy",2],

["Uniform standardised weights across all IVC sites (thousands of km apart) indicates:",
 "Common religious practice","Centralised trade regulation or strong mercantile standards","A common spoken language","Common burial practices","b","Economy",3],

["The world's first ploughed field at Kalibangan belongs to which phase?",
 "Mature Harappan","Late Harappan","Pre-Harappan (Phase I)","Post-Harappan","c","Economy",2],

["Evidence of cotton weaving in IVC comes primarily from:",
 "Bronze tools","Spindle whorls and cloth impressions on pottery","Painted seals showing weavers","Written records","b","Economy",2],

["Harappan tools used for cutting and agriculture were primarily made of:",
 "Iron","Stone only","Copper and bronze","Bone","c","Economy",1],

["Mesopotamian cuneiform references to 'Meluhha' disappear from records around:",
 "2600 BCE","2000 BCE","1800 BCE","1300 BCE","c","Economy",3],

# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 6 — RELIGION, ART & CULTURE  (Q116–Q145)
# ══════════════════════════════════════════════════════════════════════════════

["Which of the following was ABSENT in IVC?",
 "Fire altars","Mother Goddess figurines","Temples","Burial grounds","c","Religion & Art",1],

["The Pashupati Seal shows a figure:",
 "Dancing with animals on a platform","Seated in yoga posture surrounded by four animals","Standing with a weapon over an enemy","Riding a humped bull","b","Religion & Art",1],

["The four animals surrounding the Pashupati figure are:",
 "Lion, tiger, elephant, rhinoceros","Elephant, tiger, rhinoceros, buffalo","Bull, elephant, tiger, crocodile","Elephant, tiger, deer, horse","b","Religion & Art",2],

["The Pashupati Seal is considered the earliest evidence of:",
 "Buddhism","Jainism","Shaivism / Proto-Shiva worship","Vedic fire worship (Yajna)","c","Religion & Art",2],

["The primary Harappan burial practice was:",
 "Cremation","Sea burial","Extended inhumation (body laid flat, head to North)","Excarnation","c","Religion & Art",2],

["In Harappan burials, the body was typically oriented with head toward:",
 "South","East","North","West","c","Religion & Art",2],

["Cemetery H culture at Harappa (Late phase) is characterised by:",
 "Cremation burials only","Fractional burial — skull and limbs placed in urns","Mass graves with grave goods","Stone monument burials","b","Religion & Art",2],

["The Dancing Girl figurine is currently housed at:",
 "British Museum, London","National Museum, New Delhi","Indian Museum, Kolkata","Lahore Museum, Pakistan","b","Religion & Art",1],

["The Priest-King sculpture is made of:",
 "Bronze","Terracotta","Gold","Steatite (soapstone)","d","Religion & Art",1],

["The Dancing Girl figurine is made of:",
 "Gold","Terracotta","Bronze","Steatite","c","Religion & Art",1],

["The red sandstone male torso from Harappa is unique because it has:",
 "The largest size among IVC sculptures","Detachable head and arms (socket holes)","A royal crown carved on it","A bilingual IVC inscription","b","Religion & Art",2],

["Mother Goddess terracotta figurines in IVC most likely represent:",
 "Queens and noblewomen","Fertility / agricultural goddess","Dancing performers","Merchant women","b","Religion & Art",2],

["The pipal tree (Ficus religiosa) is associated with IVC religion because:",
 "It was the main fuel for brick kilns","A deity is depicted inside/beneath it on seals","It was the primary food crop","It was sacred only to Vedic priests","b","Religion & Art",2],

["Ornaments in IVC were worn by:",
 "Only women","Only priests","Only high-status men","Both men and women","d","Religion & Art",2],

["How many bangles was the Dancing Girl wearing on her LEFT upper arm?",
 "10–12","18–20","24–25","30–32","c","Religion & Art",3],

["The trefoil (clover-leaf) pattern is found on which IVC artefact?",
 "Dancing Girl's bangles","Background of Pashupati Seal","Priest-King's shawl/robe","Great Bath wall tiles","c","Religion & Art",2],

["Evidence of systematic fire rituals in IVC comes from fire altars found at:",
 "Mohenjo-Daro only","Kalibangan and Lothal","Harappa only","Dholavira and Harappa only","b","Religion & Art",2],

["The swastika symbol found on IVC seals represents:",
 "A political symbol of authority","An ancient auspicious / good-luck symbol","The symbol of the sun god","A warrior's clan emblem","b","Religion & Art",2],

["Grave goods found in Harappan burials typically include:",
 "Gold coins and iron weapons","War weapons and horse harness","Pottery, ornaments and tools","Written manuscripts and scrolls","c","Religion & Art",2],

["The height of the Dancing Girl figurine is approximately:",
 "5.5 cm","10.5 cm","17.5 cm","25 cm","b","Religion & Art",3],

["The height of the Priest-King sculpture is approximately:",
 "10.5 cm","17.5 cm","25 cm","35 cm","b","Religion & Art",3],

["Two animals at the FEET of the Pashupati figure are:",
 "Two bulls","Two deer","Two tigers","Two elephants","b","Religion & Art",3],

["The Pashupati figure is described as having:",
 "One face and two arms","Three faces (or horned headdress)","Five heads like Brahma","A single face with no headdress","b","Religion & Art",3],

["Evidence of dance / performing arts in IVC comes from:",
 "Pashupati Seal","Dancing Girl bronze figurine","Terracotta Mother Goddess","Fire altar ash deposits","b","Religion & Art",1],

["Harappan terracotta toy animals with wheels indicate:",
 "Ritual sacrifice of animals","Wheeled transport was known","Religious procession wagons","Funerary objects","b","Religion & Art",2],

["IVC terracotta figurines of animals include all EXCEPT:",
 "Zebu bull","Dog","Camel","Bird","c","Religion & Art",3],

["Which of the following designs is NOT associated with Harappan pottery decoration?",
 "Fish-scale pattern","Pipal leaf motif","Battle scene motif","Peacock motif","c","Religion & Art",3],

["The grave goods in IVC burials indicate belief in:",
 "Sun worship","Afterlife","Water worship","Fire god","b","Religion & Art",2],

["Harappan fire altars at Kalibangan had how many altars arranged in a row on the citadel?",
 "3","5","7","10","c","Religion & Art",3],

["The Pashupati Seal was found at:",
 "Harappa","Kalibangan","Mohenjo-Daro","Lothal","c","Religion & Art",2],

# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 7 — SCRIPT & SEALS  (Q146–Q158)
# ══════════════════════════════════════════════════════════════════════════════

["The total number of IVC inscriptions found is approximately:",
 "500","2,000","5,000+","10,000","c","Script & Seals",2],

["The longest known single Harappan inscription contains:",
 "10 signs","15 signs","26 signs","50 signs","c","Script & Seals",2],

["The largest Harappan inscription (on a signboard at the city gate) is found at:",
 "Mohenjo-Daro","Harappa","Lothal","Dholavira","d","Script & Seals",2],

["The Harappan script is believed to be written in which style?",
 "Purely pictographic","Boustrophedon (alternating directions)","Purely syllabic alphabetic","Ideographic like Chinese","b","Script & Seals",3],

["The approximate total number of distinct signs in the Harappan script is:",
 "26","100","400+","1,000+","c","Script & Seals",2],

["The primary reason the Harappan script has NOT been deciphered is:",
 "No tablets with text have been found","No bilingual inscription found; texts are too short","The script was deliberately destroyed","The language has no known relatives","b","Script & Seals",2],

["On average, Harappan seals contain how many signs?",
 "1–2 signs","4–5 signs","10–15 signs","20+ signs","b","Script & Seals",2],

["Which scholar proposed that IVC script is Proto-Dravidian?",
 "S.R. Rao","Mortimer Wheeler","Asko Parpola","Sir John Marshall","c","Script & Seals",2],

["The total number of seals found from IVC is approximately:",
 "500","1,000","2,000","4,000+","d","Script & Seals",2],

["The Persian Gulf seal found at Lothal was DIFFERENT from standard IVC seals because it was:",
 "Square with animal motif","Circular / round button seal","Triangular copper seal","Star-shaped with inscription","b","Script & Seals",2],

["The most common shape of Harappan seals is:",
 "Square with a boss (projection) on back","Circular","Rectangular","Cylindrical","a","Script & Seals",2],

["Harappan seals were primarily used for:",
 "Religious amulets only","Commercial identity marking and trade","Decorating house walls","Military identification","b","Script & Seals",2],

["The Dholavira signboard inscription had how many large signs?",
 "5","10","15","26","b","Script & Seals",2],

# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 8 — DECLINE & POST-IVC  (Q159–Q175)
# ══════════════════════════════════════════════════════════════════════════════

["The decline of the Mature Harappan phase began approximately around:",
 "2600 BCE","2000 BCE","1900 BCE","1300 BCE","c","Decline",2],

["The Aryan Invasion Theory to explain IVC decline is now:",
 "Widely accepted","Under debate","Discredited and rejected","Proven by DNA evidence","c","Decline",2],

["Which river's drying up is considered the MOST important environmental factor in IVC decline?",
 "Indus","Ravi","Ghaggar-Hakra (ancient Saraswati)","Sabarmati","c","Decline",2],

["The 2019 Rakhigarhi DNA study found that IVC people had:",
 "Significant Central Asian steppe ancestry","Close genetic ties to Mesopotamians","NO steppe (R1a/Aryan) ancestry — genetically indigenous South Asians","Genetic links to East African populations","c","Decline",2],

["Ochre Coloured Pottery (OCP) culture is associated with:",
 "Late Harappan eastward migration toward U.P./Haryana","Dravidian southward migration","Aryan invasion from Central Asia","Mesopotamian traders settling in India","a","Decline",3],

["Cemetery H culture at Harappa represents:",
 "Mature Harappan burial practice","Post-mature / Late Harappan phase with different pottery and burial","Vedic Aryan burial practice","Dravidian burial from South India","b","Decline",2],

["The flooding theory for the decline of Mohenjo-Daro was proposed by:",
 "Sir John Marshall","Mortimer Wheeler","R.L. Raikes and Robert Dales","Gwen Robbins Schug","c","Decline",3],

["The Painted Grey Ware (PGW) culture in the Gangetic plains is associated with:",
 "Megalithic South India","Dravidian southward migration","Early / Later Vedic culture","Harappan eastward settlement","c","Decline",2],

["The Black and Red Ware (BRW) culture in South India after IVC is associated with:",
 "Early Vedic culture","Megalithic culture of South India","Harappan migration to Gujarat","Mesopotamian traders","b","Decline",2],

["The deforestation theory for IVC decline argues forests were destroyed to provide:",
 "Farmland expansion","Fuel for brick kilns (millions of bricks)","Timber for shipbuilding","Material for Vedic rituals","b","Decline",2],

["The Jhukar culture found in post-mature Harappan Sindh represents:",
 "Pre-Harappan (Early) phase","Mature Harappan phase","Late / Post-mature Harappan phase","Post-Harappan Vedic phase","c","Decline",3],

["After IVC decline, population movement was primarily toward:",
 "Central Asia (northwest)","Gangetic plains (east) and Deccan (south)","Arabia (west)","Tibet (north)","b","Decline",2],

["Scholarly evidence that IVC trade collapsed comes from:",
 "Absence of pottery after 1900 BCE","Meluhha trade disappearing from Mesopotamian records ~1800 BCE","Vedic hymns mentioning IVC destruction","DNA evidence of population replacement","b","Decline",3],

["The disease / epidemic theory for IVC decline was proposed by:",
 "Mortimer Wheeler","Gwen Robbins Schug","R.L. Raikes","Asko Parpola","b","Decline",3],

["The IVC Rakhigarhi DNA study confirms that IVC people were ancestors of:",
 "Central Asian populations","Mesopotamian populations","Modern South Asian (likely Dravidian-speaking) populations","East Asian populations","c","Decline",2],

["Mortimer Wheeler's claim of a 'massacre' at Mohenjo-Daro (37 skeletons) was refuted because:",
 "No weapons were found at the site","The skeletons were post-IVC deposits with no signs of massacre","DNA showed they died of disease only","The skeletons were of animals, not humans","b","Decline",3],

["The Jhukar phase at Chanhu-daro followed the:",
 "Pre-Harappan Amri phase","Mature Harappan phase","Vedic Aryan intrusion","Megalithic South Indian phase","b","Decline",3],

# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 9 — UPSC STATEMENT-BASED  (Q176–Q193)
# ══════════════════════════════════════════════════════════════════════════════

["Consider the following statements about the Great Bath of Mohenjo-Daro:\n"
 "1. The Great Bath is located on the lower town of Mohenjo-Daro\n"
 "2. Bitumen (natural tar) was used to make the Great Bath watertight\n"
 "Which of the above statements is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","b","UPSC Statements",3],

["Consider the following statements about Lothal:\n"
 "1. Lothal has the world's earliest known dockyard\n"
 "2. Lothal is located on the Bhogavo river\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","a","UPSC Statements",3],

["Consider the following statements about Dholavira:\n"
 "1. Dholavira has a three-part city division (Citadel + Middle Town + Lower Town)\n"
 "2. Dholavira was inscribed as a UNESCO World Heritage Site in 2019\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","a","UPSC Statements",3],

["Consider the following statements about IVC economy:\n"
 "1. IVC was the first civilisation in the world to cultivate cotton\n"
 "2. IVC imported tin from Mesopotamia\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","a","UPSC Statements",3],

["Consider the following statements about IVC religion:\n"
 "1. No temples have been found at any IVC site\n"
 "2. Evidence of fire worship was found ONLY at Kalibangan\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","a","UPSC Statements",3],

["Consider the following statements about the Harappan script:\n"
 "1. The Harappan script has been deciphered by Asko Parpola as Proto-Dravidian\n"
 "2. The Harappan script contains approximately 400+ distinct signs\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","b","UPSC Statements",3],

["Consider the following statements about IVC weights:\n"
 "1. Harappan weights followed a binary system (1:2:4:8:16...)\n"
 "2. The smallest Harappan weight unit was 16.3 grams\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","a","UPSC Statements",3],

["Consider the following statements about IVC art:\n"
 "1. The Dancing Girl is made of terracotta\n"
 "2. The Priest-King is made of steatite (soapstone)\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","b","UPSC Statements",3],

["Consider the following statements about IVC decline:\n"
 "1. The drying of the Ghaggar-Hakra river is considered a major factor in IVC decline\n"
 "2. The Aryan Invasion Theory proposed by Mortimer Wheeler is the currently accepted explanation\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","a","UPSC Statements",3],

["Consider the following statements about the Pashupati Seal:\n"
 "1. The Pashupati Seal shows a three-faced figure seated in yoga posture\n"
 "2. The figure is surrounded by six animals including a horse\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","a","UPSC Statements",3],

["Consider the following statements about Kalibangan:\n"
 "1. Kalibangan is located on the Ghaggar river in Rajasthan\n"
 "2. The world's first ploughed field at Kalibangan belongs to the Mature Harappan phase\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","a","UPSC Statements",3],

["Consider the following statements about Chanhu-daro:\n"
 "1. Chanhu-daro is the only major IVC city without a citadel\n"
 "2. Chanhu-daro yielded evidence of horse riding in IVC\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","a","UPSC Statements",3],

["Consider the following statements about IVC burial:\n"
 "1. Extended inhumation was the primary burial method in IVC\n"
 "2. Cemetery H at Harappa shows fractional burials with body parts in urns\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","c","UPSC Statements",3],

["Consider the following statements about IVC trade:\n"
 "1. Harappan seals have been found at Mesopotamian sites including Ur and Nippur\n"
 "2. The Indus region is referred to as 'Magan' in Mesopotamian cuneiform texts\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","a","UPSC Statements",3],

["Consider the following statements about Rakhigarhi:\n"
 "1. Rakhigarhi is the largest IVC site located in India\n"
 "2. The 2019 DNA study at Rakhigarhi found significant steppe ancestry in IVC people\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","a","UPSC Statements",3],

["Consider the following statements about Mohenjo-Daro:\n"
 "1. Mohenjo-Daro was excavated by R.D. Banerji in 1922\n"
 "2. Mohenjo-Daro was the FIRST IVC site to be discovered\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","a","UPSC Statements",3],

["Consider the following statements comparing IVC with contemporaries:\n"
 "1. IVC had a better drainage system than contemporary Mesopotamia and Egypt\n"
 "2. IVC had the most elaborate temples among contemporary Bronze Age civilisations\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","a","UPSC Statements",3],

["Consider the following statements about Harappan seals:\n"
 "1. The unicorn is the most commonly depicted animal on Harappan seals\n"
 "2. Most Harappan seals are made of copper\n"
 "Which of the above is/are correct?",
 "1 only","2 only","Both 1 and 2","Neither 1 nor 2","a","UPSC Statements",3],

# ══════════════════════════════════════════════════════════════════════════════
#  SECTION 10 — ADVANCED / MATCH / NEGATIVE  (Q194–Q200)
# ══════════════════════════════════════════════════════════════════════════════

["Which of the following is INCORRECTLY matched (Site : Unique Feature)?",
 "Lothal : World's earliest dockyard","Chanhu-daro : Only IVC site without a citadel",
 "Dholavira : World's first ploughed field","Rakhigarhi : Largest IVC site in India",
 "c","Advanced",3],

["Which of the following pairs is CORRECTLY matched (Term : Place in Mesopotamian texts)?",
 "Dilmun = Oman; Magan = Bahrain","Dilmun = Bahrain; Magan = Oman",
 "Dilmun = Indus region; Magan = Bahrain","Meluhha = Bahrain; Dilmun = Indus region",
 "b","Advanced",3],

["Match the following excavators with sites:\n"
 "1. Mohenjo-Daro — R.D. Banerji\n"
 "2. Lothal — S.R. Rao\n"
 "3. Dholavira — B.B. Lal\n"
 "4. Kalibangan — R.S. Bisht\n"
 "Which are CORRECTLY matched?",
 "1 and 2 only","1, 2 and 3","2 and 4 only","3 and 4 only",
 "a","Advanced",3],

["Arrange the following IVC site discoveries in CHRONOLOGICAL ORDER (earliest first):\n"
 "1. Harappa discovered  2. Mohenjo-Daro discovered  3. Lothal excavated  4. Dholavira excavated",
 "1-2-3-4","2-1-3-4","1-3-2-4","2-1-4-3",
 "a","Advanced",3],

["Which of the following statements about IVC are ALL INCORRECT?\n"
 "1. IVC people used iron tools\n"
 "2. IVC had elaborate temples for worship\n"
 "3. IVC had confirmed domesticated horse usage",
 "Only 1 is incorrect","Only 1 and 2 are incorrect","All three (1, 2 and 3) are incorrect","Only 2 and 3 are incorrect",
 "c","Advanced",3],

["The Rakhigarhi DNA study (2019) CORRECTLY concluded that IVC people:",
 "Were of Aryan (Central Asian steppe) origin","Were closely related to present-day Mesopotamians",
 "Were genetically indigenous South Asians with NO steppe ancestry","Migrated from East Africa to India","c","Advanced",3],

["Which of the following CORRECTLY identifies the four geographical extremes of IVC?",
 "West:Sutkagen-dor; East:Daimabad; North:Shortughai; South:Alamgirpur",
 "West:Sutkagen-dor; East:Alamgirpur; North:Shortughai; South:Daimabad",
 "West:Shortughai; East:Alamgirpur; North:Sutkagen-dor; South:Daimabad",
 "West:Daimabad; East:Sutkagen-dor; North:Alamgirpur; South:Shortughai",
 "b","Advanced",3],

]  # END OF QUESTIONS

# ── Scoring configuration ────────────────────────────────────────────────────

PATTERNS = {
    "1": {
        "name": "UPSC Prelims",
        "correct": 2.0,
        "wrong": -0.667,
        "total_marks": 400,
        "desc": "+2 correct | −2/3 wrong | 200 Qs = 400 marks | 2 hrs"
    },
    "2": {
        "name": "TNPSC Group 1 Prelims",
        "correct": 1.5,
        "wrong": -0.5,
        "total_marks": 300,
        "desc": "+1.5 correct | −0.5 wrong | 200 Qs = 300 marks | 3 hrs"
    }
}

# ── Helpers ───────────────────────────────────────────────────────────────────

def fmt_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    if h:
        return f"{h}h {m}m {s}s"
    return f"{m}m {s}s"

def bar(pct, width=30):
    filled = int(width * pct / 100)
    return G + "█" * filled + DIM + "░" * (width - filled) + RESET

def header_box(title):
    w = 64
    print(f"\n{B}{'═'*w}{RESET}")
    print(f"{B}║{RESET}{BOLD}{title.center(w-2)}{RESET}{B}║{RESET}")
    print(f"{B}{'═'*w}{RESET}\n")

# ── Main test runner ──────────────────────────────────────────────────────────

def run_test():
    clr()
    header_box("  IVC MOCK TEST — 200 QUESTIONS  ")
    print(f"{Y}Pattern Options:{RESET}")
    for k, v in PATTERNS.items():
        print(f"  {B}[{k}]{RESET} {v['name']:<25} {DIM}{v['desc']}{RESET}")
    print()
    while True:
        pat_choice = input(f"  {C}Select pattern (1/2): {RESET}").strip()
        if pat_choice in PATTERNS:
            break
        print(f"  {R}Enter 1 or 2.{RESET}")

    pattern = PATTERNS[pat_choice]
    print(f"\n  {G}Pattern selected: {BOLD}{pattern['name']}{RESET}")
    print(f"\n  {Y}Instructions:{RESET}")
    print(f"  • Enter  {G}a / b / c / d{RESET}  to answer")
    print(f"  • Enter  {Y}s{RESET}             to skip (no penalty)")
    print(f"  • Enter  {R}q{RESET}             to quit and see analysis\n")
    input(f"  {C}Press ENTER to start the test...{RESET}")

    # ── State ─────────────────────────────────────────────────────────────────
    answers  = {}   # qnum(0-indexed) → user answer letter or 's'/'q'
    times    = {}   # qnum → seconds taken

    start_total = time.time()

    for i, q in enumerate(Q):
        clr()
        q_text, a, b, c, d, correct, topic, diff = q

        elapsed_total = fmt_time(time.time() - start_total)
        diff_label = ["","Easy","Medium","Hard"][diff]
        diff_colour = [G, G, Y, R][diff]

        print(f"{DIM}Q {i+1}/200  |  {topic}  |  {diff_colour}{diff_label}{RESET}  |  "
              f"Total time: {elapsed_total}\n")
        print(f"{BOLD}{W}{q_text}{RESET}\n")
        print(f"  {G}(a){RESET} {a}")
        print(f"  {G}(b){RESET} {b}")
        print(f"  {G}(c){RESET} {c}")
        print(f"  {G}(d){RESET} {d}")
        print()

        q_start = time.time()
        while True:
            ans = input(f"  {C}Your answer: {RESET}").strip().lower()
            if ans in ("a","b","c","d","s","q"):
                break
            print(f"  {R}Enter a / b / c / d / s (skip) / q (quit){RESET}")

        times[i] = time.time() - q_start
        answers[i] = ans

        if ans == "q":
            break
        if ans == "s":
            print(f"  {Y}Skipped.{RESET}")
        elif ans == correct:
            print(f"  {G}✓ Correct!{RESET}")
        else:
            opts = [a, b, c, d]
            cidx = ord(correct) - ord('a')
            print(f"  {R}✗ Wrong. Correct: ({correct}) {opts[cidx]}{RESET}")
        time.sleep(0.5)

    # ── Analysis ──────────────────────────────────────────────────────────────
    total_time = time.time() - start_total

    attempted  = {k: v for k, v in answers.items() if v not in ("s","q")}
    skipped    = {k: v for k, v in answers.items() if v == "s"}
    unattempted = set(range(len(Q))) - set(answers.keys())

    correct_qs = {k for k, v in attempted.items() if v == Q[k][5]}
    wrong_qs   = {k for k, v in attempted.items() if v != Q[k][5]}

    score = len(correct_qs)*pattern["correct"] + len(wrong_qs)*pattern["wrong"]
    max_marks = pattern["total_marks"]
    pct = (score / max_marks) * 100

    # topic-wise
    topics = {}
    for i, q in enumerate(Q):
        t = q[6]
        if t not in topics:
            topics[t] = {"correct":0,"wrong":0,"skipped":0,"total":0}
        topics[t]["total"] += 1
        if i in correct_qs:
            topics[t]["correct"] += 1
        elif i in wrong_qs:
            topics[t]["wrong"] += 1
        else:
            topics[t]["skipped"] += 1

    # difficulty-wise
    diff_stats = {1:{"c":0,"w":0,"t":0}, 2:{"c":0,"w":0,"t":0}, 3:{"c":0,"w":0,"t":0}}
    for i, q in enumerate(Q):
        d = q[7]
        diff_stats[d]["t"] += 1
        if i in correct_qs: diff_stats[d]["c"] += 1
        elif i in wrong_qs:  diff_stats[d]["w"] += 1

    avg_time = sum(times.values()) / len(times) if times else 0

    # ── Print report ──────────────────────────────────────────────────────────
    clr()
    header_box("  MOCK TEST — DETAILED ANALYSIS  ")

    # Score card
    print(f"{BOLD}{W}  PATTERN  : {Y}{pattern['name']}{RESET}")
    print(f"{BOLD}{W}  SCORE    : {G if score>=0 else R}{score:.2f} / {max_marks}{RESET}")
    print(f"  PERCENTAGE: {bar(max(0,pct))}  {G if pct>=60 else Y if pct>=40 else R}{pct:.1f}%{RESET}")
    print()

    # Time
    print(f"  {C}TIME TAKEN        :{RESET} {fmt_time(total_time)}")
    print(f"  {C}AVG TIME/QUESTION :{RESET} {avg_time:.1f} seconds")
    print()

    # Summary table
    print(f"  {G}✓ Correct   : {len(correct_qs):>3}   (+{len(correct_qs)*pattern['correct']:.2f} marks){RESET}")
    print(f"  {R}✗ Wrong     : {len(wrong_qs):>3}   ({len(wrong_qs)*pattern['wrong']:.2f} marks){RESET}")
    print(f"  {Y}↷ Skipped   : {len(skipped):>3}{RESET}")
    print(f"  {DIM}○ Not reached: {len(unattempted):>3}{RESET}")
    print()

    # Grade
    if pct >= 80:
        grade, remark = "A+", f"{G}Excellent — UPSC/Group 1 ready!{RESET}"
    elif pct >= 65:
        grade, remark = "A",  f"{G}Very Good — strong foundation{RESET}"
    elif pct >= 50:
        grade, remark = "B",  f"{Y}Good — revise tricky topics{RESET}"
    elif pct >= 35:
        grade, remark = "C",  f"{Y}Average — needs focused revision{RESET}"
    else:
        grade, remark = "D",  f"{R}Needs full IVC revision{RESET}"
    print(f"  {BOLD}GRADE: {Y}{grade}{RESET}  |  {remark}")
    print()

    # Topic-wise
    print(f"\n{B}{'─'*64}{RESET}")
    print(f"{BOLD}  TOPIC-WISE PERFORMANCE{RESET}")
    print(f"{B}{'─'*64}{RESET}")
    print(f"  {'Topic':<22} {'Total':>5} {'Correct':>7} {'Wrong':>6} {'%':>6}  Status")
    print(f"  {'─'*22} {'─'*5} {'─'*7} {'─'*6} {'─'*6}  {'─'*20}")
    weak_topics = []
    for t, s in sorted(topics.items(), key=lambda x: (x[1]['correct']/x[1]['total']) if x[1]['total'] else 0):
        tot = s['total']
        cor = s['correct']
        wrg = s['wrong']
        tp  = (cor/tot*100) if tot else 0
        if tp < 50:
            status = f"{R}⚠ WEAK{RESET}"
            weak_topics.append(t)
        elif tp < 70:
            status = f"{Y}○ REVISE{RESET}"
        else:
            status = f"{G}✓ STRONG{RESET}"
        print(f"  {t:<22} {tot:>5} {cor:>7} {wrg:>6} {tp:>5.0f}%  {status}")

    # Difficulty breakdown
    print(f"\n{B}{'─'*64}{RESET}")
    print(f"{BOLD}  DIFFICULTY BREAKDOWN{RESET}")
    print(f"{B}{'─'*64}{RESET}")
    dnames = {1:"Easy (TNPSC)", 2:"Medium", 3:"Hard (UPSC)"}
    for d in [1,2,3]:
        s   = diff_stats[d]
        tp  = (s['c']/s['t']*100) if s['t'] else 0
        clabel = G if tp>=70 else Y if tp>=50 else R
        print(f"  {dnames[d]:<20} {s['c']:>3}/{s['t']:<3}  "
              f"{clabel}{tp:>5.1f}%{RESET}  {bar(tp, 20)}")

    # Weak topics revision plan
    if weak_topics:
        print(f"\n{B}{'─'*64}{RESET}")
        print(f"{BOLD}{R}  WEAK AREAS — PRIORITY REVISION LIST{RESET}")
        print(f"{B}{'─'*64}{RESET}")
        rev_map = {
            "Basics":         "Review IVC Period, Area, Age, River systems, Comparisons",
            "Excavators":     "Memorise: Who excavated WHICH site and WHEN",
            "Sites":          "Use mnemonic MLDKS-R; drill site→feature→state→river table",
            "Town Planning":  "Focus on brick ratio 1:2:4, Great Bath, Dholavira 3-part city",
            "Economy":        "Binary weights, cotton, trade routes, Dilmun/Magan/Meluhha",
            "Religion & Art": "Pashupati seal animals, Dancing Girl material, Cemetery H",
            "Script & Seals": "Undeciphered reasons, Parpola, Dholavira signboard, seal shapes",
            "Decline":        "Ghaggar-Hakra drying, Rakhigarhi DNA, Cemetery H, PGW/BRW",
            "UPSC Statements":"Practice 2-statement format; watch for half-correct traps",
            "Advanced":       "Match the following: sites/rivers/excavators; boundary extremes",
        }
        for i, t in enumerate(weak_topics, 1):
            tip = rev_map.get(t, "Revisit notes for this topic")
            print(f"  {R}{i}.{RESET} {BOLD}{t}{RESET}")
            print(f"     → {DIM}{tip}{RESET}\n")

    # Wrong questions quick review
    if wrong_qs:
        print(f"\n{B}{'─'*64}{RESET}")
        print(f"{BOLD}{R}  WRONG QUESTIONS — QUICK REVIEW{RESET}")
        print(f"{B}{'─'*64}{RESET}")
        for idx in sorted(wrong_qs):
            q     = Q[idx]
            opts  = [q[1], q[2], q[3], q[4]]
            cidx  = ord(q[5]) - ord('a')
            uidx  = ord(answers[idx]) - ord('a')
            qtxt  = q[0].split('\n')[0][:70]
            print(f"\n  {Y}Q{idx+1}:{RESET} {qtxt}{'...' if len(q[0])>70 else ''}")
            print(f"  {R}You answered: ({answers[idx]}) {opts[uidx]}{RESET}")
            print(f"  {G}Correct:      ({q[5]}) {opts[cidx]}{RESET}")

    # Final footer
    print(f"\n{B}{'═'*64}{RESET}")
    print(f"{BOLD}{C}  TEST COMPLETE  |  Pattern: {pattern['name']}  |  Score: {score:.2f}/{max_marks}{RESET}")
    print(f"{B}{'═'*64}{RESET}\n")

    # Auto-save results + wrong answers to my_notes/mistakes/
    script_dir   = os.path.dirname(os.path.abspath(__file__))
    mistakes_dir = os.path.join(script_dir, "..", "my_notes", "mistakes")
    os.makedirs(mistakes_dir, exist_ok=True)
    ts    = time.strftime('%Y%m%d_%H%M%S')
    fname = os.path.join(mistakes_dir, f"ivc_mock_{ts}.md")

    diff_name = {1: "Easy", 2: "Medium", 3: "Hard"}

    with open(fname, "w") as f:
        f.write(f"# IVC Mock Test — Results & Wrong Answers\n\n")
        f.write(f"| | |\n|---|---|\n")
        f.write(f"| **Pattern** | {pattern['name']} |\n")
        f.write(f"| **Date** | {time.strftime('%Y-%m-%d %H:%M:%S')} |\n")
        f.write(f"| **Score** | {score:.2f} / {max_marks} ({pct:.1f}%) — {grade} |\n")
        f.write(f"| **Time** | {fmt_time(total_time)} |\n")
        f.write(f"| **Correct** | {len(correct_qs)} |\n")
        f.write(f"| **Wrong** | {len(wrong_qs)} |\n")
        f.write(f"| **Skipped** | {len(skipped)} |\n\n")

        f.write("## Topic-wise Performance\n\n")
        f.write("| Topic | Score | % |\n|---|---|---|\n")
        for t, s in topics.items():
            tp   = (s['correct'] / s['total'] * 100) if s['total'] else 0
            flag = " ⚠️" if tp < 90 else ""
            f.write(f"| {t} | {s['correct']}/{s['total']} | {tp:.0f}%{flag} |\n")

        if wrong_qs:
            f.write(f"\n## Wrong Answers ({len(wrong_qs)} questions)\n\n")
            for idx in sorted(wrong_qs):
                q    = Q[idx]
                opts = [q[1], q[2], q[3], q[4]]
                cidx = ord(q[5]) - ord('a')
                uidx = ord(answers[idx]) - ord('a')
                f.write(f"---\n\n### Q{idx+1} — {q[6]} | {diff_name.get(q[7], '')}\n\n")
                f.write(f"**{q[0]}**\n\n")
                for li, opt in zip('abcd', opts):
                    if li == q[5]:
                        marker = " ✓"
                    elif li == answers[idx]:
                        marker = " ✗"
                    else:
                        marker = ""
                    f.write(f"- ({li}) {opt}{marker}\n")
                f.write(f"\n> You answered: **({answers[idx]}) {opts[uidx]}**  \n")
                f.write(f"> Correct answer: **({q[5]}) {opts[cidx]}**\n\n")
        else:
            f.write("\n**No wrong answers — Perfect score!**\n")

    print(f"\n  {G}Results auto-saved → {fname}{RESET}\n")

# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    try:
        run_test()
    except KeyboardInterrupt:
        print(f"\n\n  {Y}Test interrupted. Run again to start fresh.{RESET}\n")
