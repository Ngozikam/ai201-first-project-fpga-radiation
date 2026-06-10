# FPGA Radiation RAG System

## Project Overview

This project implements a Retrieval-Augmented Generation (RAG) system focused on FPGA radiation effects, radiation testing, Single Event Upsets (SEUs), Single Event Effects (SEEs), mitigation techniques, and radiation sensing research.

The system ingests technical NASA, AMD/Xilinx, and academic research documents, converts them into searchable chunks, stores semantic embeddings in ChromaDB, and uses a Large Language Model (LLM) to generate grounded answers with source attribution.

The final system ingests 13 FPGA-radiation source documents from NASA, AMD/Xilinx, and peer-reviewed research publications. During document processing, the system generated 1,074 searchable text chunks that were embedded using the all-MiniLM-L6-v2 model and stored in ChromaDB for semantic retrieval.


## Domain

Unofficial Guide to FPGA Radiation Testing, Radiation Effects, Radiation Detection, and Radiation-Tolerant FPGA Design

This system helps students, engineers, and researchers understand FPGA radiation effects, mitigation techniques, and radiation-testing practices. Information on this topic is difficult to find because it is scattered across NASA reports, FPGA vendor documentation, academic papers, and technical presentations.

The system will make this knowledge searchable through a retrieval-augmented question-answering interface. The knowledge base covers radiation-induced faults in FPGAs, mitigation techniques such as TMR and SEM, fault-injection methodologies, radiation-testing procedures, and radiation-sensing materials research.


## Example Questions

- What is a Single Event Upset (SEU) in an FPGA?
- What are Single Event Effects (SEEs)?
- What is Triple Modular Redundancy (TMR)?
- How are FPGA radiation tests conducted?
- What techniques are used to mitigate radiation-induced errors in FPGAs?

## Source Documents
1. NASA FPGA Single Event Effect Radiation Test Guidelines
   URL: https://nepp.nasa.gov/files/23779/FPGA_Radiation_Test_Guidelines_2012.pdf

2. NASA/JPL Assessing and Mitigating Radiation Effects in Xilinx FPGAs
   URL: https://nepp.nasa.gov/DocUploads/08A3733D-6D42-428C-824E76B5B5A92B59/07-113%20Adell_JPL%20Assessing%20and%20Mitigating%20Rad%20effects.pdf

3. NASA Electronic Parts and Packaging FPGA SEE Test Guideline Update (Presentation)
   URL: https://ntrs.nasa.gov/api/citations/20180001945/downloads/20180001945.pdf

4. AMD/Xilinx LogiCORE IP Soft Error Mitigation Controller User Guide (UG764)
   URL: https://docs.amd.com/v/u/1.0-English/sem_ug764

5. Single Event Effects in FPGA Devices: Update 2020
   URL: https://ntrs.nasa.gov/api/citations/20205003879/downloads/2020-561-Berg-Final-Presentation-NEPP-ETW_v3.pdf

6. NASA NEPP FPGA Tasks and Considerations
   URL: https://ntrs.nasa.gov/api/citations/20140017354/downloads/20140017354.pdf

7. Using Classical Reliability Models and Single Event Upset (SEU) Data to Determine Optimum Implementation Schemes for Triple Modular Redundancy (TMR) in SRAM-Based Field Programmable Gate Array (FPGA) Devices
   URL: https://ntrs.nasa.gov/api/citations/20150018112/downloads/20150018112.pdf

8. Single Event Analysis and Fault Injection Techniques Targeting Complex Designs Implemented in Xilinx-Virtex FPGA Devices
   URL: https://ntrs.nasa.gov/api/citations/20140008976/downloads/20140008976.pdf

9. Modernizing Single Event Effect Test and Analysis Methods for Complex FPGA Applications
   URL: https://ntrs.nasa.gov/api/citations/20230005923/downloads/Berg_HEART_2023_v2a.pdf

10. Noise Impact of Single Event Upsets on an FPGA-Based Digital Filter
    URL: https://www.nsf-shrec.org/sites/default/files/2024-03/Noise-impact-of-single-event-upsets-on-an-fpga-based-digital-filter.pdf

11.   X-ray Radiation Effects on SWCNT/PMMA Thin Film Nanocomposites
      Authors: Suman, G., Pulikkathara, M., & Wilkins, R.
      Source: IEEE Transactions on Nanotechnology, Vol. 20, pp. 517–524, 2021.
      DOI: 10.1109/TNANO.2021.3080624

12. Ionizing Radiation Sensing with Functionalized and Copper-Coated SWCNT/PMMA Thin Film Nanocomposites.
    Authors: Suman, G., Pulikkathara, M., Wilkins, R., & Treadwell, L. J.
    Source: Nanomaterials, Vol. 13, Article 2653, 2023.
    DOI: 10.3390/nano13192653

13. X-ray Radiation Effects on Thin Film Nanocomposites of Functionalized and Copper-Coated Multi-Walled Carbon Nanotube and Poly(Methyl Methacrylate)
    Authors: Kyatsandra, S., Pulikkathara, M., & Wilkins, R. 
    Source: Surfaces and Interfaces, Vol. 17, Article 100362, 2019
     https://doi.org/10.1016/j.surfin.2019.100362


## System Architecture
FPGA Radiation Documents
        │
        ▼
Document Ingestion
(PDF Extraction)
        │
        ▼
Chunking
(800 chars, 150 overlap)
        │
        ▼
Embeddings
(all-MiniLM-L6-v2)
        │
        ▼
Vector Store
(ChromaDB)
        │
        ▼
Retrieval
(Top-5 Semantic Search)
        │
        ▼
Grounded Generation
(Groq Llama 3.3 70B)
        │
        ▼
User Answer + Source Attribution

## Chunking Strategy
I will use fixed-size chunks of approximately 800 characters with an overlap of 150 characters.

My document collection consists primarily of NASA radiation-test guidelines, AMD/Xilinx FPGA documentation, fault-injection reports, and academic research papers. These documents contain technical explanations that often span multiple paragraphs and include concepts such as Single Event Upsets (SEUs), Triple Modular Redundancy (TMR), fault injection, radiation testing procedures, and radiation-sensing materials.

An 800-character chunk is large enough to preserve technical context while remaining small enough for precise semantic retrieval. A 150-character overlap helps ensure that important information is not lost when concepts cross chunk boundaries. For example, a discussion of TMR reliability, SEM operation, or FPGA fault injection may begin near the end of one chunk and continue into the next.

If chunks are too small, important technical explanations may be fragmented and retrieved incompletely. If chunks are too large, retrieval may return broad sections of documents containing unrelated information, reducing answer precision.

The overlap improves retrieval quality by ensuring that information located near chunk boundaries remains available in multiple chunks, increasing the likelihood that complete technical concepts can be retrieved.

## Retrieval Approach
I will use the sentence-transformers embedding model **all-MiniLM-L6-v2** together with **ChromaDB** as the vector database for semantic retrieval.

Each document chunk will be stored along with its associated metadata, including the source document name and chunk identifier. This metadata will enable retrieved information to be traced back to its original source and support source attribution during answer generation.

For each user query, the system will retrieve the **top five most relevant chunks (top-k = 5)**. Retrieving too few chunks may exclude important supporting information, while retrieving too many may introduce irrelevant content that can reduce the quality and accuracy of generated responses.

The use of semantic search allows retrieval based on meaning rather than exact keyword matching. For example, a query about *radiation-induced bit flips* may successfully retrieve documents discussing *Single Event Upsets (SEUs)* even when the exact query terms are not present in the text.

If this system were deployed in a production environment, I would investigate larger embedding models that provide stronger retrieval accuracy, improved understanding of technical and scientific terminology, and better support for longer contexts. However, these benefits would need to be balanced against increased computational requirements, memory usage, and response latency.

## Sample Chunks

The following examples illustrate representative chunks generated during the document ingestion and chunking stage. Each chunk retains source-document metadata to support retrieval and source attribution during answer generation.

### Sample Chunk 1

**Source Document:** NASA FPGA Single Event Effect Radiation Test Guidelines

```text
Field Programmable Gate Array (FPGA) Single Event Effect (SEE) Radiation Testing

Prepared by: Melanie Berg
MEI Technologies in support of NASA/Goddard Space Flight Center

For: NASA Electronic Parts and Packaging (NEPP) and Defense Threat Reduction Agency

Date: February 2, 2012
```

---

### Sample Chunk 2

**Source Document:** NASA-JPL Assessing and Mitigating Radiation Effects in Xilinx FPGAs

```text
National Aeronautics and Space Administration

Assessing and Mitigating Radiation Effects in Xilinx FPGAs

Philippe Adell
Jet Propulsion Laboratory
California Institute of Technology

Greg Allen
Jet Propulsion Laboratory
California Institute of Technology

JPL Publication 08-9
February 2008
```

---

### Sample Chunk 3

**Source Document:** Using Classical Reliability Models and Single Event Upset (SEU) Data to Determine Optimum Implementation Schemes for Triple Modular Redundancy (TMR) in SRAM-Based FPGA Devices

```text
Abstract:
Space applications are complex systems that require intricate trade analyses for optimum implementations.

This study uses classical reliability theory and Single Event Upset (SEU) data to evaluate appropriate Triple Modular Redundancy (TMR) implementation schemes for SRAM-based FPGA devices.

The study investigates mitigation performance and risk analysis associated with TMR deployment in radiation environments.
```

---

### Sample Chunk 4

**Source Document:** Single Event Effects in Field Programmable Gate Array (FPGA) Devices: Update 2020

```text
Single Event Effects in Field Programmable Gate Array (FPGA) Devices: Update 2020

Presented at the NASA Electronic Parts and Packaging Program (NEPP)
Electronics Technology Workshop

Authors:
Melanie Berg
Michael Campola
Hak Kim
Anthony Phan

NASA Goddard Space Flight Center
June 15–18, 2020
```

---

### Sample Chunk 5

**Source Document:** X-ray Radiation Effects on SWCNT/PMMA Thin Film Nanocomposites

```text
Abstract:
This paper investigates the response of a radiation sensor developed from single-walled carbon nanotube (SWCNT) and poly(methyl methacrylate) (PMMA) nanocomposite thin films.

The effects of X-ray radiation were evaluated through real-time electrical resistance measurements under varying radiation doses and dose rates.

The study demonstrated that ionizing radiation generated charge carriers that reduced the resistance of the nanocomposite material.
```

## Evaluation Results

| Question                                                                | Accuracy                  |
| ----------------------------------------------------------------------- | ------------------------- |
| What is a Single Event Upset (SEU) in an FPGA?                          | Inaccurate                |
| What are Single Event Effects (SEEs) in FPGA devices?                   | Accurate                  |
| What is Triple Modular Redundancy (TMR) and why is it used?             | Accurate                  |
| How are FPGA radiation tests conducted?                                 | Accurate                  |
| What techniques are used to mitigate radiation-induced errors in FPGAs? | Partially Accurate        |
| What is the capital of Texas?                                           | Accurate (Grounding Test) |

### Question 1

**Question:** What is a Single Event Upset (SEU) in an FPGA?

**Expected Answer:** Radiation-induced state change in FPGA memory or logic.

**Actual Result:** The system reported that insufficient information was available.

**Accuracy:** Inaccurate

---

### Question 2

**Question:** What are Single Event Effects (SEEs) in FPGA devices?

**Expected Answer:** Radiation-induced disturbances including SEU, SET, SEFI, SEL, and MBU.

**Actual Result:** The system correctly identified SEE categories and described radiation-induced effects.

**Accuracy:** Accurate

---

### Question 3

**Question:** What is Triple Modular Redundancy (TMR) and why is it used?

**Expected Answer:** TMR uses three replicated modules and voting logic to improve fault tolerance.

**Actual Result:** The system correctly explained TMR and its role in mitigating radiation-induced faults.

**Accuracy:** Accurate

---

### Question 4

**Question:** How are FPGA radiation tests conducted?

**Expected Answer:** FPGA devices are exposed to radiation while functionality and errors are monitored.

**Actual Result:** The system correctly described DUT exposure, monitoring, test vehicles, and radiation-testing procedures.

**Accuracy:** Accurate

---

### Question 5

**Question:** What techniques are used to mitigate radiation-induced errors in FPGAs?

**Expected Answer:** TMR, configuration scrubbing, SEM controllers, fault detection, and redundancy.

**Actual Result:** The system identified TMR and configuration scrubbing but omitted some additional techniques.

**Accuracy:** Partially Accurate

---

### Grounding Test

**Question:** What is the capital of Texas?

**Expected Answer:** Not contained in the FPGA-radiation document collection.

**Actual Result:** The system correctly refused to answer and indicated insufficient information.
**Accuracy:** Accurate

## Failure Analysis

The primary failure occurred for the question:

"What is a Single Event Upset (SEU) in an FPGA?"

Although several retrieved documents contained references to SEUs, the system failed to retrieve a chunk containing a clear definition and therefore responded that insufficient information was available. This failure originated in the retrieval stage rather than the generation stage.

The likely cause is that the relevant SEU definitions were embedded within larger discussions of radiation effects and were not ranked highly enough by the embedding model. In addition, chunk boundaries may have separated the SEU definition from surrounding explanatory context. As a result, the retrieved context lacked sufficient information for the language model to generate a grounded answer.

Potential improvements include increasing chunk size, adjusting overlap, using a stronger embedding model optimized for scientific documents, or implementing hybrid retrieval that combines semantic search with keyword matching.

## Spec Reflection

The project specification provided a clear framework for building the Retrieval-Augmented Generation (RAG) system. It helped guide the development process by separating the project into distinct stages, including document ingestion, chunking, embedding generation, retrieval, grounded answer generation, evaluation, and documentation. Following these milestones made it easier to build and test each component independently before integrating the complete system.

One important lesson from the project was that successful answer generation depends heavily on retrieval quality. Although the generation component worked correctly, the evaluation revealed a failure case for the question "What is a Single Event Upset (SEU) in an FPGA?" because the retrieval stage did not return a chunk containing a clear definition. This demonstrated that even a powerful language model cannot generate a correct grounded answer when the relevant context is not retrieved. As a result, I gained a better understanding of the importance of chunking strategy, embedding quality, and retrieval evaluation in RAG systems.

The implementation generally followed the original design specified in the planning document. However, the evaluation process highlighted limitations in retrieval performance that were not fully anticipated during planning. Future improvements would include experimenting with larger embedding models, adjusting chunk size and overlap, and incorporating hybrid retrieval techniques that combine semantic search with keyword-based search.


## AI Usage

### Example 1: Document Ingestion Pipeline

I used Claude to help generate the initial PDF ingestion code using the pypdf library. The generated code extracted text from PDF files and saved the output to text files. I modified the code to match my project directory structure, added chunk generation functionality, verified successful processing of all 13 FPGA-radiation documents, and tested the output files before proceeding to the embedding stage.

### Example 2: Retrieval and Generation Integration

I used Claude to help generate code integrating ChromaDB, sentence-transformers, and the Groq API. The generated code provided an initial implementation of semantic retrieval and grounded generation. I modified the retrieval logic, adjusted chunking parameters, tested retrieval quality using evaluation queries, implemented source attribution, and verified that the system refused to answer questions outside the FPGA-radiation document collection.

## System Components

- `pipeline.py` – Extracts text from PDF documents and generates chunks.
- `embed_retrieval.py` – Creates embeddings and stores them in ChromaDB.
- `query.py` – Retrieves relevant chunks and generates grounded answers using Groq.
- `app.py` – Launches the Gradio web interface.
- `evaluation.py` – Runs the evaluation questions used in Milestone 6.
- `planning.md` – Project planning document covering Milestones 1 and 2.

## Document Processing Statistics

The ingestion pipeline processed 13 FPGA-radiation documents and generated a total of 1,074 chunks.

### Largest Source Documents

| Document                                                                                             | Chunks |
| ---------------------------------------------------------------------------------------------------- | ------ |
| AMD/Xilinx LogiCORE IP Soft Error Mitigation Controller User Guide (UG764)                           | 291    |
| NASA FPGA Single Event Effect Radiation Test Guidelines                                              | 236    |
| Ionizing Radiation Sensing with Functionalized and Copper-Coated SWCNT/PMMA Thin Film Nanocomposites | 101    |
| NASA-JPL Assessing and Mitigating Radiation Effects in Xilinx FPGAs                                  | 95     |

These documents contain the largest amount of technical content and therefore contribute significantly to the retrieval knowledge base. As expected, they frequently appear among retrieved sources for FPGA-radiation-related questions.

## How to Run

### 1. Install Required Packages

```bash
pip install chromadb sentence-transformers groq python-dotenv gradio pypdf
```

### 2. Add Groq API Key

Create a `.env` file in the project root directory and add:

```text
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Extract Text and Create Chunks

Run the ingestion pipeline to extract text from the PDF documents and create document chunks:

```bash
python pipeline.py
```

### 4. Generate Embeddings and Build Vector Store

Create embeddings using the all-MiniLM-L6-v2 model and store them in ChromaDB:

```bash
python embed_retrieval.py
```

### 5. Test Retrieval and Generation

Run the command-line query interface:

```bash
python query.py
```

### 6. Launch the Web Interface

Start the Gradio application:

```bash
python app.py
```

Open the URL displayed in the terminal (typically http://localhost:7860) and enter FPGA-radiation-related questions.

### 7. Run Project Evaluation

Execute the evaluation script to test all evaluation questions:

```bash
python evaluation.py

```

## Demo Video

A 3–5 minute demonstration video was recorded showing:

- Successful retrieval and grounded generation for FPGA-radiation questions.
- Source attribution from retrieved documents.
- A retrieval failure case involving the SEU definition.
- A grounding test where the system correctly refused to answer an out-of-domain question.
- A walkthrough of the evaluation results and failure analysis.


Demo Video Link:

https://drive.google.com/file/d/1MrgOnZn606uqvOoPgV2w3cOmKOSGEhJR/view?usp=sharing

## Future Improvements

Several enhancements could improve the performance and usability of this system:

1. **Improve Retrieval Accuracy**

   * Experiment with larger embedding models designed for scientific and technical literature.
   * Evaluate alternative retrieval strategies and reranking techniques.

2. **Hybrid Search**

   * Combine semantic retrieval with keyword-based retrieval to improve performance on highly technical terms such as SEU, SEE, TMR, and SEM.

3. **Optimize Chunking Strategy**

   * Evaluate different chunk sizes and overlap values to reduce the likelihood of important information being split across chunk boundaries.

4. **Enhanced Source Attribution**

   * Display the exact retrieved chunks and document locations used to generate each answer.

5. **Expanded Document Collection**

   * Add additional NASA, ESA, Xilinx, AMD, and academic FPGA-radiation publications to improve coverage and answer quality.

6. **Advanced Evaluation**

   * Measure retrieval precision, recall, and grounding performance using a larger set of evaluation questions and benchmark datasets.

7. **Domain-Specific Embeddings**

   * Fine-tune or adopt embedding models trained on scientific and engineering literature to improve retrieval quality for FPGA and radiation-related terminology.
