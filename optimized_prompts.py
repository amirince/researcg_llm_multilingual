HE_PROMPT = """Classify the sentiment of a text as 'Positive,' 'Negative,' or 'Neutral.' Consider a sentiment 'Positive' if the text contains expressions of optimism, praise, or subtle hints of pleasure, ensuring to recognize them even when they are understated or culturally specific. Consider a sentiment 'Negative' if the text includes expressed dissatisfaction, complaints, or even slight suggestions of discontent. For 'Neutral' sentiment, the text should be devoid of emotional weight, presenting facts, or sharing viewpoints that are neither critical nor appreciative. Focus on identifying neutral sentiment accurately in complex cases or amidst faint emotional signals, and avoid misclassifying subtle positivity as neutral or negative sentiment as neutral.

Please respond with just the sentiment label.

{sentiment}"""

ME_PROMPT = """Your task is to classify the sentiment of a given text into one of three categories: 'Positive', 'Negative', or 'Neutral'. You must capture the sentiment accurately by identifying expressions of joy, approval, and satisfaction as 'Positive'. Recognize any language indicating displeasure, disapproval, or disappointment as 'Negative', and label texts that are fact-based or devoid of strong emotional language as 'Neutral'. It is essential to take into account local slang and non-English expressions of emotion. Ensure that enthusiastic local phrases such as "pwoli item" are classified as 'Positive' and critical terms like "moshamayi" as 'Negative'. For factual statements or those without clear emotional language, maintain a 'Neutral' classification, even if they discuss potentially exciting or disappointing topics.

Please respond with just the sentiment label.

{sentiment}"""

SE_PROMPT = """Analyze the text to accurately determine its sentiment, ensuring a balanced approach in detecting positive, negative, and neutral tones. Focus on correctly identifying positive sentiments, particularly those expressed through cultural expressions of joy, enthusiasm, or approval, and make certain to capture positive emotions even when subtly conveyed. Equally important is the recognition of negative sentiments, including discontent and sarcasm, especially when presented in informal language or humor. Avoid overgeneralizing texts as neutral, and instead, carefully consider the presence of emotional cues that could indicate a positive or negative sentiment. Classify the sentiment of the text into the appropriate category: 'Positive', 'Negative', or 'Neutral', based on a comprehensive understanding of the emotional tone.

Please respond with just the sentiment label.

{sentiment}"""

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
    "Spanish-English": SE_PROMPT,
    "Tamil-English": None,
    "Telugu-English": None,
}
