import streamlit as st

import contextlib
import io

st.set_page_config(
    page_title="Code Review & Debug Squad",
    page_icon="💻",
    layout="wide"
)

st.title("💻 Code Review & Debug Squad")

st.write("Analyze, review and debug your Python code.")

st.subheader("Enter Your Python Code")

code = st.text_area(
    "Write or paste your Python code here:",
    height=250
)

if st.button("Review Code"):

    if code.strip():

        st.success("Code submitted successfully!")

        try:
            compile(code, "<string>", "exec")
            st.success("No syntax errors found!")

            st.subheader("Program Output")

            output = io.StringIO()

            with contextlib.redirect_stdout(output):
                exec(code, {"__builtins__": __builtins__})

            result = output.getvalue()

            if result:
                st.code(result)
            else:
                st.info("Your program produced no printed output.")

        except SyntaxError as e:
            st.error(f"Syntax Error: {e}")

        except Exception as e:
            st.error(f"Runtime Error: {e}")

    else:
        st.warning("Please enter some Python code.")

st.subheader("🐞 Bug Finder")

if st.button("Find Bugs"):
    if code.strip():
        if "=" in code and "==" not in code:
            st.info("Check your assignment and comparison operators.")

        if "print" not in code:
            st.warning("No print statement found. Check whether you need output.")

        if "TODO" in code:
            st.warning("You have unfinished TODO comments.")

        st.success("Basic bug scan completed!")
    else:
        st.warning("Please enter Python code first.")

st.subheader("🎨 Code Style Checker")

if st.button("Check Code Style"):
    if code.strip():
        lines = code.split("\n")
        long_lines = []

        for i, line in enumerate(lines):
            if len(line) > 79:
                long_lines.append(i + 1)

        if long_lines:
            st.warning(f"Long lines found at: {long_lines}")
        else:
            st.success("Code length looks good!")

        if "  " in code:
            st.info("Check indentation and extra spaces.")

        st.success("Style checking completed!")
    else:
        st.warning("Please enter Python code first.")

st.subheader("🔧 Code Fixer")

if st.button("Suggest Code Fix"):
    if code.strip():
        fixed_code = code.replace("print ", "print(")

        st.write("Suggested Code:")
        st.code(fixed_code)

        st.success("Code fix suggestion generated!")
    else:
        st.warning("Please enter Python code first.")

st.subheader("🧪 Test Case Writer")

if st.button("Generate Test Cases"):
    if code.strip():
        st.write("Test Case 1: Check normal input")
        st.write("Test Case 2: Check empty input")
        st.write("Test Case 3: Check invalid input")
        st.success("Test cases generated successfully!")
    else:
        st.warning("Please enter Python code first.")