HE_PROMPT = """You are a highly skilled classification assistant. Your task is to analyze the provided text and determine its sentiment. Classify the sentiment as one of the following: 'positive', 'negative', or 'neutral'. 

Please respond with just the sentiment label.

Example 1:
Text: Desh perm sab karte hai chaheya wo Hindu ho ya Muslim example military force jaha log mazhab nahi â€¦
Sentiment: positive

Example 2:
Text: Ye hai fasism ka phla stape ... 2022 target ... Hehe .. Ensan bnaya hai eshwar ne ...... Ldo aur mro
Sentiment: negative

Example 3:
Text: Are koi ni apne yaha se terrorist to bhej hi sakte hi
Sentiment: negative

Example 4:
Text: * Tu Baki Ldkio ki trh extra bf Kyu nahi bnati * Me
Sentiment: neutral

Example 5:
Text: Kya karen ye bechare Bagga sir ðŸ¤” Kal Ek congressi worker se baat hui bo â€¦
Sentiment: neutral

Now, classify the following text. Please respond with only 'positive', 'negative', or 'neutral':

{sentiment}
"""

ME_PROMPT = """You are a highly skilled classification assistant. Your task is to analyze the provided text and determine its sentiment. Classify the sentiment as one of the following: 'positive', 'negative', or 'neutral'. 

Please respond with just the sentiment label.

Example 1: 
Text: Trailer kidu mass marana mass.  Ee padam recordukal thoothuvarrum
Sentiment: positive

Example 2: 
Text: ee chengayikk 68 aano alla 28 aano ejjathi enrgy  kandtt kili paariya pole
Sentiment: positive

Example 3: 
Text: Itu polikkum ithu polikkum Eppo polichennu chodicha mathi
Sentiment: positive

Example 4: 
Text: Ittichan Polichuuuu Onam Lalettan eduthu ennu parayan Paranju
Sentiment: positive

Example 5:
Text: Itchy poloru trailer ithuvare kandittillaa ini kanumonnu ariyillaa kinnnaammkaachiii polichuuuu
Sentiment: positive

Now, classify the following text. Please respond with only 'positive', 'negative', or 'neutral':

{sentiment}
"""

TAMENG_PROMPT = """You are a highly skilled classification assistant. Your task is to analyze the provided text and determine its sentiment. Classify the sentiment as one of the following: 'positive', 'negative', or 'neutral'. 

Please respond with just the sentiment label.

Example 1: 
Text: dislike panna terrorist ah adichu kollunga da
Sentiment: negative

Example 2: 
Text: Same to bro  fast a kathkkuvoo
Sentiment: positive

Example 3: 
Text: AIDSPATHY Visai pans Inga vanthu aluguranunga naalaikku school iruku poi thoongungada
Sentiment: negative

Example 4: 
Text: Otha padam vera level ah irukum pola .thala mass
Sentiment: neutral

Example 5: 
Text: Dai pink film remake ah idhu
Sentiment: positive

Now, classify the following text. Please respond with only 'positive', 'negative', or 'neutral':

{sentiment}
"""

TELENG_PROMPT = """You are a highly skilled classification assistant. Your task is to analyze the provided text and determine its sentiment. Classify the sentiment as one of the following: 'positive', 'negative', or 'neutral'. 

Please respond with just the sentiment label.

Example 1: 
Text: Anna yepude show complete ayindi
Sentiment: neutral

Example 2: How to download johaar movie in 4k Click here 👇 👇
Sentiment: neutral

Example 3: 
Text: Anna nee voice vintunte Malli inkosari video chudali anipistundhi .
Sentiment: positive

Example 4: 
Text: @BJP4Andhra @BJP4India @ncbn @YSRCParty @JaiTDP @somuveerraju @PawanKalyan @JanaSenaParty @narendramodi Kukka ni dengunattu dengadu PK mimmalni ... aina siggu leknda vaadi madda cheekuthunnaru .... erri pookas meeku enduku raa ... egastras
Sentiment: negative

Example 5: 
Text: @memer_habibi @OmNamaahShivaya @MeghUpdates Abe Saudi bhi Israel se dosti karna cha raha hai . Tum jaise Chut * ye hi humanity humanity chilla rahe hai . 😂 🤣 🤣 🤣 🤣 Abhi ruko Israel to pattak ke pele ga in katmullo ko . 😝 😝 😝 😝 😝
Sentiment: negative

Now, classify the following text. Please respond with only 'positive', 'negative', or 'neutral':

{sentiment}
"""


prompts = {
    "Hindi-English": HE_PROMPT,
    "Malyalam-English": ME_PROMPT,
    "Spanish-English": None,
    "Tamil-English": TAMENG_PROMPT,
    "Telugu-English": TELENG_PROMPT,
}
