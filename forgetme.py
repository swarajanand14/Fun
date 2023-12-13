import streamlit as st
import time

def main():
    st.title("U NEED IT")

    if st.button("Click here to make me Forget U"):
        with st.spinner("Please wait, forgetting in progress..."):
            # Simulate a delay for 5 seconds
            time.sleep(5)
        
        # Display a success message
        st.error("Forgetfulness unsuccessful!")

        # Display an error message with a retry button
        st.error("Error 404: Not Found, The person clicking it cannot pe fogotten by the HOST beacuse u r the most beautiful person he knows, U can retry")
        retry_button = st.button("Retry")

        if retry_button:
            st.experimental_rerun()

if __name__ == "__main__":
    main()