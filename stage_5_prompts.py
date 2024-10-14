HE_PROMPT = """When classifying the sentiment of text that includes a mix of Hindi and English, carefully discern and categorize the sentiment as 'Positive,' 'Negative,' or 'Neutral.' Pay particular attention to any positive elements present, even if they might be subtle or overshadowed by negative contexts. When texts offer a combination of sentiments, prioritize a 'Neutral' classification if no single sentiment overwhelmingly dominates the narrative. Ensure that positive sentiments are not overlooked due to the presence of some negative aspects, and strive to recognize the overall sentiment accurately. Texts that simply relay information without an emotional charge should be classified as 'Neutral.' Your classification should reflect a balanced assessment of the sentiment expressed in the text, capturing both the explicit and implicit emotional cues.

Now, classify the following text. Please respond with only 'positive', 'negative', or 'neutral':

{sentiment}
"""

ME_PROMPT = """For the sentiment analysis of Malayalam-English mixed text, the sentiment should be classified as follows: Label a text as 'Positive' if it contains expressions of happiness, hope, contentment, or any other affirmative emotion, regardless of the presence of minor negative sentiments. Use phrases like "sukhakaram aakumennu pratheekshikkunnu", "karyam nannayi poyi", and "nostalgic aayi" as indicators of positive sentiment. A text should be labeled as 'Negative' if it primarily conveys emotions of dissatisfaction, sorrow, or displeasure. However, texts that provide factual statements, discuss uncertain outcomes, or lack strong sentiment should be classified as 'Neutral'. This includes situations like discussing an interview experience or waiting for an outcome, which should not be misclassified as negative. Be particularly careful not to mislabel subtle expressions of positive sentiments, such as anticipation or satisfaction, as neutral, nor to classify neutral, factual information as positive.

Now, classify the following text. Please respond with only 'positive', 'negative', or 'neutral':

{sentiment}
"""

TAMENG_PROMPT = """Your task is to assess and classify the sentiment of text composed in a mix of Tamil and English, with a focus on addressing previous model inaccuracies. For each piece of text, assign a sentiment of 'Positive', 'Negative', or 'Neutral' with the following guidelines to improve classification:

Firstly, emphasize the identification of positive sentiment, especially in texts where it may be subtle or intertwined with neutral or negative elements. Secondly, accurately discern neutral sentiments when texts present information or facts without a strong emotional charge, even if certain emotionally charged words are present. Lastly, ensure negative sentiments are not underestimated, particularly in texts expressing stress or concern. Prioritize predominant emotions in texts with mixed sentiments, avoiding overclassification of neutral sentiments.

Your classification should reflect the predominant sentiment, taking into account the overall context and emotion conveyed in the text, rather than defaulting to a single emotional element.


Now, classify the following text. Please respond with only 'positive', 'negative', or 'neutral':

{sentiment}
"""

TELENG_PROMPT = """You are an advanced sentiment analysis classifier tasked with assessing the sentiment of Telugu-English bilingual text. Review the text and determine the predominant sentiment. When positive expressions of happiness, approval, or satisfaction are present, they should be considered the dominant sentiment unless there is strong and prevalent negative language that clearly outweighs the positive aspects. In cases where both positive and negative sentiments are expressed, if the positive sentiment is equal to or more prominent than the negative, classify the text as 'Positive'. For texts that are emotionally neutral, containing factual information or descriptions without a strong emotional tone, classify them as 'Neutral'. It is crucial to avoid a negative bias and ensure that texts expressing overall positivity, even with minor negative elements, are correctly identified as 'Positive'. Your response should include only the sentiment label: 'Positive', 'Negative', or 'Neutral'.

Now, classify the following text. Please respond with only 'positive', 'negative', or 'neutral':

{sentiment}
"""

SPANENG_PROMPT = """As a sentiment analysis expert, your task is to classify texts written in a combination of Spanish and English into one of three categories: 'Positive,' 'Neutral,' or 'Negative.' Ensure precise categorization by adhering to the following guidelines:

1. Categorize as 'Positive' any expression of contentment, enthusiasm, or commendation, no matter how subtly presented. This includes texts that may have a neutral tone but incorporate positive phrases or sentiments.

2. Label as 'Neutral' texts that are primarily informational or express mixed sentiments without a clear lean towards positivity or negativity. Avoid classifying inherently uncertain or ambiguous texts as 'Negative.'

3. Designate as 'Negative' only those texts where negative sentiments such as discontent, critique, or despondency are the central focus. Do not classify texts with incidental negative phrases or mixed sentiments that do not overwhelmingly convey negativity as 'Negative.'

These instructions are designed to ensure that texts with even slight positive nuances are classified as 'Positive,' recognize truly neutral statements, and appropriately categorize unmistakably negative sentiments, avoiding errors from previous assessments.


Now, classify the following text. Please respond with only 'positive', 'negative', or 'neutral':

{sentiment}
"""

prompts = {
    "Hindi-English": HE_PROMPT,
    "Malyalam-English": ME_PROMPT,
    "Spanish-English": SPANENG_PROMPT,
    "Tamil-English": TAMENG_PROMPT,
    "Telugu-English": TELENG_PROMPT,
}
