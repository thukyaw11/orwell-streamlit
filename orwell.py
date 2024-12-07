import streamlit as st

# Title of the app
st.title("George Orwell's *1984*")

# Book cover image
image_url = "https://tankmuseumshop.org/cdn/shop/products/1984.jpg?v=1588779384&width=1284"
st.image(image_url, caption="A classic novel by George Orwell", use_container_width=True)

# Introduction
st.subheader("Introduction")
st.write("""
*1984* is a dystopian social science fiction novel by English author George Orwell. 
Published in 1949, the novel is set in a totalitarian society under constant surveillance 
and ruled by the omnipresent Party and its leader, Big Brother.
""")

# Themes and Influence
st.subheader("Themes and Influence")
st.write("""
The book explores themes of:
- Totalitarianism and authoritarianism.
- Surveillance and loss of privacy.
- Censorship and manipulation of truth.
- Resistance, rebellion, and human spirit.

Its influence extends to politics, language (e.g., terms like *Big Brother* and *Orwellian*), 
and cultural discussions about freedom and control.
""")

# Notable Quotes
st.subheader("Notable Quotes")
st.write("""
- *"Big Brother is Watching You."*
- *"War is peace. Freedom is slavery. Ignorance is strength."*
- *"In the face of pain, there are no heroes."*
""")

# Interactive Section: User Thoughts
st.subheader("Your Thoughts on *1984*")
st.write("Have you read *1984*? Share your thoughts below!")

user_input = st.text_area("What did you think of the book?", placeholder="Write your thoughts here...")
if st.button("Submit"):
    if user_input.strip():
        st.success("Thank you for sharing your thoughts!")
        st.write("Here's what you shared:")
        st.write(f"💬 {user_input}")
    else:
        st.error("Please write something before submitting.")

# Additional Resources
st.subheader("Learn More")
st.write("""
If you'd like to dive deeper into the themes and analysis of *1984*, here are some resources:
- [George Orwell's Biography (Wikipedia)](https://en.wikipedia.org/wiki/George_Orwell)
- [Full Text of *1984* (Project Gutenberg Australia)](http://gutenberg.net.au/ebooks01/0100021.txt)
- [Discussion on *1984* Themes (CliffNotes)](https://www.cliffsnotes.com/literature/n/1984/1984-at-a-glance)
""")

# Footer
st.markdown("---")
st.write("Built with ❤️ using [Streamlit](https://streamlit.io) by [Min Thu Kyaw](https://minthukyaw.vercel.app)")
