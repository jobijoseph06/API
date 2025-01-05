import streamlit as st
import requests

from send_email import send_email


# Load the News API key
API_KEY = "bc07434d1e9a420cb0983d8f5ac3b60a"

# Function to fetch news articles
def fetch_news(topic):

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={topic}&"
        f"sortBy=publishedAt&apiKey={API_KEY}&language=en"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("articles", [])
    else:
        st.error(f"Failed to fetch news: {response.status_code} - {response.reason}")
        return []

# Streamlit UI
def main():
    st.title("📰 News Fetcher")
    st.write("Get the latest news articles on any topic of your choice!")

    # User inputs for topic and email
    topic = st.text_input("Enter the topic you are interested in:", placeholder="eg.technology, tesla")
    receiver_email = st.text_input("Enter the receiver's email address:", placeholder="user@gmail.com")

    if st.button("Fetch News and Send Email"):
        if topic.strip() and receiver_email.strip():
            with st.spinner("Fetching news and preparing your email..."):
                articles = fetch_news(topic)

            if articles:
                # Build the email content
                body = f"Subject: Today's News on {topic}\n\n"
                for article in articles[:10]:  # Top 10 articles
                    title = article.get("title", "No title available")
                    description = article.get("description", "No description available")
                    url = article.get("url", "No URL available")
                    body += f"{title}\n{description}\n{url}\n\n"

                # Send the email
                try:
                    send_email(body, receiver_email)
                    st.success(f"News email sent successfully to {receiver_email}!")
                except Exception as e:
                    st.error(f"Failed to send email: {e}")
            else:
                st.warning(f"No news articles found for '{topic}'. Try a different topic!")
        else:
            st.error("Please provide both a valid topic and email address.")

# Run the app
if __name__ == "__main__":
    main()


