import streamlit as st
from detoxify import Detoxify

# Set the title of the app
st.title("Comment Toxicity Analyzer")

# Create a text area for user input
input_text = st.text_area("Enter your comment here:")

# Button to trigger analysis
if st.button("Analyze"):
    if input_text:
        # Perform toxicity analysis on the input text
        results = Detoxify('original').predict(input_text)

        # Display detailed results
        st.header("Moderation Results:")
        st.write("Toxicity: {:.2f}".format(results['toxicity']))
        st.write("Severe Toxicity: {:.2f}".format(results['severe_toxicity']))
        st.write("Obscene: {:.2f}".format(results['obscene']))
        st.write("Threat: {:.2f}".format(results['threat']))
        st.write("Insult: {:.2f}".format(results['insult']))
        st.write("Identity Attack: {:.2f}".format(results['identity_attack']))

        # Determine the overall toxicity level
        if results['toxicity'] > 0.5:
            toxicity_result = "Toxic"
        elif results['severe_toxicity'] > 0.5:
            toxicity_result = "Severely Toxic"
        elif results['obscene'] > 0.5:
            toxicity_result = "Obscene"
        elif results['threat'] > 0.5:
            toxicity_result = "Threatening"
        elif results['insult'] > 0.5:
            toxicity_result = "Insulting"
        elif results['identity_attack'] > 0.5:
            toxicity_result = "Identity Attack"
        else:
            toxicity_result = "Non-toxic"

        # Display the single-word analysis result
        st.write("Overall Toxicity Level: **{}**".format(toxicity_result))
    else:
        st.warning("Please enter a comment to analyze.")