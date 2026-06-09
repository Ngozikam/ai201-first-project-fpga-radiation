import gradio as gr

from query import ask


def handle_query(question):

    result = ask(question)

    sources = "\n".join(
        f"• {source}"
        for source in result["sources"]
    )

    return (
        result["answer"],
        sources
    )


with gr.Blocks() as demo:

    gr.Markdown("# FPGA Radiation RAG System")

    gr.Markdown(
        "Ask questions about FPGA radiation effects, SEUs, mitigation techniques, TMR, SEM controllers, and radiation sensing research."
    )

    question = gr.Textbox(
        label="Enter Your Question"
    )

    ask_button = gr.Button("Ask")

    answer = gr.Textbox(
        label="Answer",
        lines=10
    )

    sources = gr.Textbox(
        label="Sources Used",
        lines=5
    )

    ask_button.click(
        handle_query,
        inputs=question,
        outputs=[answer, sources]
    )

    question.submit(
        handle_query,
        inputs=question,
        outputs=[answer, sources]
    )

demo.launch()