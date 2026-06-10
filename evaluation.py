from query import ask

evaluation_questions = [
    "What is a Single Event Upset (SEU) in an FPGA?",
    "What are Single Event Effects (SEEs) in FPGA devices?",
    "What is Triple Modular Redundancy (TMR) and why is it used?",
    "How are FPGA radiation tests conducted?",
    "What techniques are used to mitigate radiation-induced errors in FPGAs?",
    "What is the capital of Texas?"   # failure test
]

for i, question in enumerate(evaluation_questions, start=1):

    print("\n" + "=" * 80)
    print(f"QUESTION {i}")
    print("=" * 80)

    print("\nQuestion:")
    print(question)

    result = ask(question)

    print("\nAnswer:")
    print(result["answer"])

    print("\nSources:")

    for source in result["sources"]:
        print(f"- {source}")

    print("\n")