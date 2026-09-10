import streamlit as st

st.set_page_config(
    page_title="CodeMate AI",
    page_icon="💻"
)

st.title("💻 CodeMate")
st.write("Your Coding Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Coding Topics")

    if st.button("🐍 Python"):
        st.session_state.messages.append(
            {"role": "user", "content": "Give me a Python example"}
        )

    if st.button("☕ Java"):
        st.session_state.messages.append(
            {"role": "user", "content": "Give me a Java example"}
        )

    if st.button("🗄️ SQL"):
        st.session_state.messages.append(
            {"role": "user", "content": "Give me an SQL example"}
        )

    if st.button("🔄 Clear"):
        st.session_state.messages = []
        st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.code(message["content"])

question = st.chat_input("Enter your coding question...")

if question:

    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.write(question)

    text = question.lower()

    if "python" in text:
        answer = """Python Example:

name = "Hemamalini"
print("Hello", name)

for i in range(1, 6):
    print(i)"""

    elif "java" in text:
        answer = """Java Example:

public class Main {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}"""

    elif "sql" in text or "database" in text:
        answer = """SQL Example:

CREATE TABLE Student (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

INSERT INTO Student
VALUES (1, 'Anu', 20);

SELECT * FROM Student;"""

    elif "loop" in text:
        answer = """Python For Loop:

for i in range(1, 6):
    print(i)

Output:
1
2
3
4
5"""

    elif "function" in text:
        answer = """Python Function:

def add(a, b):
    return a + b

result = add(10, 20)
print(result)"""

    elif "array" in text:
        answer = """Python List:

numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)"""

    elif "if" in text or "condition" in text:
        answer = """Python If-Else:

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")"""

    else:
        answer = """Coding Topics:

1. Python
2. Java
3. SQL
4. Loops
5. Functions
6. Arrays
7. If-Else

Ask a coding question."""

    with st.chat_message("assistant"):
        st.code(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
