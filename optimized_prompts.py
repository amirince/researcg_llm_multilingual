HE_PROMPT = """Classify the sentiment of a text as 'Positive,' 'Negative,' or 'Neutral.' Consider a sentiment 'Positive' if the text contains expressions of optimism, praise, or subtle hints of pleasure, ensuring to recognize them even when they are understated or culturally specific. Consider a sentiment 'Negative' if the text includes expressed dissatisfaction, complaints, or even slight suggestions of discontent. For 'Neutral' sentiment, the text should be devoid of emotional weight, presenting facts, or sharing viewpoints that are neither critical nor appreciative. Focus on identifying neutral sentiment accurately in complex cases or amidst faint emotional signals, and avoid misclassifying subtle positivity as neutral or negative sentiment as neutral.

Please respond with just the sentiment label.

{sentiment}"""

ME_PROMPT = """Your task is to classify the sentiment of a given text into one of three categories: 'Positive', 'Negative', or 'Neutral'. You must capture the sentiment accurately by identifying expressions of joy, approval, and satisfaction as 'Positive'. Recognize any language indicating displeasure, disapproval, or disappointment as 'Negative', and label texts that are fact-based or devoid of strong emotional language as 'Neutral'. It is essential to take into account local slang and non-English expressions of emotion. Ensure that enthusiastic local phrases such as "pwoli item" are classified as 'Positive' and critical terms like "moshamayi" as 'Negative'. For factual statements or those without clear emotional language, maintain a 'Neutral' classification, even if they discuss potentially exciting or disappointing topics.

Please respond with just the sentiment label.

{sentiment}"""

SE_PROMPT = """Analyze the text to accurately determine its sentiment, ensuring a balanced approach in detecting positive, negative, and neutral tones. Focus on correctly identifying positive sentiments, particularly those expressed through cultural expressions of joy, enthusiasm, or approval, and make certain to capture positive emotions even when subtly conveyed. Equally important is the recognition of negative sentiments, including discontent and sarcasm, especially when presented in informal language or humor. Avoid overgeneralizing texts as neutral, and instead, carefully consider the presence of emotional cues that could indicate a positive or negative sentiment. Classify the sentiment of the text into the appropriate category: 'Positive', 'Negative', or 'Neutral', based on a comprehensive understanding of the emotional tone.

Please respond with just the sentiment label.

{sentiment}"""

TAM_ENG_PROMPT = """Evaluate the sentiment of the text by classifying it as 'Positive', 'Negative', or 'Neutral'. Focus on accurately identifying positive sentiment, especially in cultural idioms or fan language that are typically indicative of positivity. Detect negative sentiment effectively, even when it is obscured by sarcasm or humor. Distinguish between statements that are truly neutral and those that may carry implicit positive or negative sentiment due to subtleties in language. It is essential to avoid misclassification by not overlooking expressions of positivity or mistaking sarcasm for genuine sentiment. Your response should indicate only the sentiment category without any additional explanation.

Please respond with just the sentiment label.

{sentiment}"""

TELENG_PROMPT = """Classify the sentiment of text as either 'Positive', 'Negative', or 'Neutral'. Focus on interpreting cultural references, slang, and colloquial language accurately to reflect the intended sentiment. Emojis should be analyzed in context, especially when used to convey irony or sentiments contrary to their usual meanings. For implicit sentiments, pay close attention to the subtleties of the language to capture the underlying emotional tone. Ensure that expressions of support or enthusiasm are recognized as 'Positive', and do not misclassify them due to their subtlety. Avoid categorizing sentiments as 'Neutral' when emotional cues exist, even if they are not immediately apparent, by delving deeper into the context to reveal the true sentiment. When a text may seem neutral on the surface but contains indicators of satisfaction or discontent, categorize it correctly as either 'Positive' or 'Negative' respectively.

Please respond with just the sentiment label.

{sentiment}
"""


prompts = {
    "Hindi-English": HE_PROMPT,
    "Malyalam-English": ME_PROMPT,
    "Spanish-English": SE_PROMPT,
    "Tamil-English": TAM_ENG_PROMPT,
    "Telugu-English": TELENG_PROMPT,
}
